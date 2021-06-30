

# pyecharts依赖
from pyecharts.render import make_snapshot
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar,Line
from snapshot_selenium import snapshot
from pyecharts import options as opts
# 导入输出图片工具
from pyecharts.render import make_snapshot
from pyecharts.commons.utils import JsCode

# docx模板依赖
from docxtpl import DocxTemplate,RichText,InlineImage
from docx.shared import Mm

# mysql依赖
import pymysql

# 结构数，用来字符串转json
from ast import literal_eval
import json

# 日期
import datetime


def smooth_line( x_data, y_data, title, subtitle, pic_name):

    # 不要问为什么我要这么做，问就自己体会。真心无语自己
    func = '''
    function(params) {
    var num=
    '''+str(y_data)+''';
                   if (params.data[1]==Math.max.apply(null, num) || params.data[1]==Math.min.apply(null, num)){
                        return ''  
                    } 
                    else {
                        return params.data[1] +'万'
                        }
                }
    '''
    line = (
        Line()
            .add_xaxis(x_data)
            .add_yaxis(
            series_name="",  #这里需要调整一下
            y_axis=y_data,
            is_smooth=True,
            markpoint_opts=opts.MarkPointOpts(
                symbol_size=[70,70],

                data=[opts.MarkPointItem( name = '最大值', type_='max',), opts.MarkPointItem(name = '最小值',type_='min',itemstyle_opts=opts.ItemStyleOpts(color='#0076f6'))]
            ),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="平均线", type_="average")]),
            # label_opts=opts.LabelOpts(formatter=JsCode(
            #     "function(x){return(x.data[1]+ '万');}"
            # ))
            label_opts=opts.LabelOpts(is_show=True, formatter=JsCode(func))
        )
            .set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
                             yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}万')),
                             xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 15})
                             )
    )
    make_snapshot(snapshot, line.render(), pic_name)


def bar_line( bar_label, bar_data, line_data, title, subtitle, pic_name):

    bar = (
        Bar().add_xaxis(xaxis_data= bar_label)
            .add_yaxis(
            series_name="调用次数",
            y_axis=bar_data,
            itemstyle_opts=opts.ItemStyleOpts(color="#003472", opacity=0.7),  # 柱形图颜色及透# 明度
            label_opts=opts.LabelOpts(is_show=True, position='top', formatter="{c}",)  # 显示数据标签
        )
            .extend_axis(
            yaxis=opts.AxisOpts(
                name="增长率",
                type_="value",
                # min_=0,
                # max_=10000,
                # interval=0.5,
                axisline_opts=opts.AxisLineOpts(is_show=True,# y轴线不显示
                                                linestyle_opts=opts.LineStyleOpts(color='#d53a35')), # 设置线颜色, 字体颜色也变
                axistick_opts=opts.AxisTickOpts(is_show=True),   # 刻度线不显示
                axislabel_opts=opts.LabelOpts(formatter="{value}%"), # 次坐标轴数据显示格式
            )
        )
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="cross"
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
                name_rotate=15,
                axislabel_opts={"rotate": 15}
            ),
            yaxis_opts=opts.AxisOpts(
                # name="调用量",
                type_="value",
                # min_=1000,
                # max_=1000000,
                # interval=500000,
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                # splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            title_opts=opts.TitleOpts(title=title, subtitle=subtitle)
        )
    )

    line = (
        Line().add_xaxis(xaxis_data=bar_label)
            .add_yaxis(
            series_name="增长率",
            yaxis_index=1,
            y_axis=line_data,
            color='#003472',
            label_opts=opts.LabelOpts(is_show=True, position='right', formatter=JsCode(
                "function(x){return(x.data[1]+ '%');}"
            )
                                      ),
            linestyle_opts=opts.LineStyleOpts(),
            is_smooth=True,
        )
    )
    bar.overlap(line).render()
    make_snapshot(snapshot, bar.overlap(line).render(), pic_name)

class MysqlUtil:
    def __init__(self, host, port, user, password, db):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, use_unicode=True, charset="utf8")

    def get_data(self, sql_content):
        cursor = self.conn.cursor()
        cursor.execute(sql_content)
        datas = cursor.fetchall()
        title = cursor.description
        cursor.close()
        if len(datas)==0:
            datas = (('',),)
        return(datas)

if __name__ == "__main__":

    # mysql配置信息
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = 'aptx4869'
    db = 'mybatis'
    sql_content = 'select index_value from sjzypt_monitor_index_tb where index_id = %s'
    mysqlUtil = MysqlUtil(host, port, user, password, db)

    # 基本信息
    c_day = mysqlUtil.get_data( sql_content%('100104'))[0][0]

    # 文件路径
    templa_doc_file = '海口城市大脑项目 -数据资源平台版块-个人周报模板.docx'  #模板路径
    day_doc_path = '海口城市大脑项目-数据资源平台版块-个人周报' + mysqlUtil.get_data( sql_content%('100104'))[0][0] + '.docx' #每日监测文档存放路径
    # day_excel_path = 'resourse/日常监测每日excel/'  #每日监测excel存放路径


    '''
        绘制图
    '''
    # 绘制日期圆滑折线图
    smooth_line_x_data = [i['day'] for i in literal_eval(mysqlUtil.get_data( sql_content%('100305'))[0][0])]
    smooth_line_y_data = [i['api_call_count'] for i in literal_eval(mysqlUtil.get_data( sql_content%('100305'))[0][0])]
    smooth_line_title = "接口近七天调用次数趋势图"
    smooth_line_subtitle = c_day + "至" +(datetime.datetime.strptime(c_day, "%Y-%m-%d") + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
    smooth_line_pic_name = "接口近七天调用次数趋势图"+smooth_line_subtitle+".png"
    smooth_line(smooth_line_x_data, smooth_line_y_data, smooth_line_title, smooth_line_subtitle, smooth_line_pic_name)

    # 绘制各业务应用调用次数Top7图
    bar_line_label_app = [i['app_name'] for i in literal_eval(mysqlUtil.get_data( sql_content%('100303'))[0][0])]
    bar_line_data_app = [i['api_call_count'] for i in literal_eval(mysqlUtil.get_data( sql_content%('100303'))[0][0])]
    bar_line_line_data_app = [i['api_ratio'] for i in literal_eval(mysqlUtil.get_data( sql_content%('100303'))[0][0])]
    bar_line_title_app = "各业务应用调用次数Top7"
    bar_line_subtitle = c_day + "至" +(datetime.datetime.strptime(c_day, "%Y-%m-%d") + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
    bar_line_pic_name_app = "各业务应用调用次数Top7"+bar_line_subtitle+".png"
    # bar_line(bar_line_label_app,bar_line_data_app,bar_line_line_data_app,bar_line_title_app,bar_line_subtitle,bar_line_pic_name_app)

    # 绘制各接口被调用次数Top10图
    bar_line_label_api = [i['api_describe'][0:10] for i in literal_eval(mysqlUtil.get_data( sql_content%('100304'))[0][0])]
    bar_line_data_api = [i['api_call_count'] for i in literal_eval(mysqlUtil.get_data( sql_content%('100304'))[0][0])]
    bar_line_line_data_api = [i['api_ratio'] for i in literal_eval(mysqlUtil.get_data( sql_content%('100304'))[0][0])]
    bar_line_title_api = "各接口被调用次数Top10"
    bar_line_subtitle_api = c_day + "至" +(datetime.datetime.strptime(c_day, "%Y-%m-%d") + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
    bar_line_pic_name_api = "各接口被调用次数Top10"+bar_line_subtitle_api+".png"
    bar_line(bar_line_label_api,bar_line_data_api,bar_line_line_data_api,bar_line_title_api,bar_line_subtitle_api,bar_line_pic_name_api)

    '''
        结果写入到word
    '''
    tpl = DocxTemplate(templa_doc_file)
    # docx 富文本插入、样式设计
    context = {
        "syzyptgrzb_1002": mysqlUtil.get_data( sql_content%('100101'))[0][0],
        "syzyptgrzb_1003": mysqlUtil.get_data( sql_content%('100102'))[0][0],
        "syzyptgrzb_1004": mysqlUtil.get_data( sql_content%('100103'))[0][0],
        "syzyptgrzb_1001": mysqlUtil.get_data( sql_content%('100104'))[0][0],
        "syzyptgrzb_1016": mysqlUtil.get_data( sql_content%('100301'))[0][0],
        "syzyptgrzb_1017": mysqlUtil.get_data( sql_content%('100302'))[0][0],
        "syzyptgrzb_1019": literal_eval(mysqlUtil.get_data( sql_content%('100303'))[0][0]),
        "syzyptgrzb_1020": literal_eval(mysqlUtil.get_data( sql_content%('100304'))[0][0]),
        "syzyptgrzb_1018": literal_eval(mysqlUtil.get_data( sql_content%('100305'))[0][0]),
        "syzyptgrzb_1005": mysqlUtil.get_data( sql_content%('100306'))[0][0],
        "syzyptgrzb_1006": mysqlUtil.get_data( sql_content%('100307'))[0][0],
        "syzyptgrzb_1007": mysqlUtil.get_data( sql_content%('100308'))[0][0],
        "syzyptgrzb_1008": mysqlUtil.get_data( sql_content%('100309'))[0][0],
        "syzyptgrzb_1009": mysqlUtil.get_data( sql_content%('100310'))[0][0],
        "syzyptgrzb_1010": mysqlUtil.get_data( sql_content%('100311'))[0][0],
        "syzyptgrzb_1011": mysqlUtil.get_data( sql_content%('100312'))[0][0],
        "syzyptgrzb_1012": mysqlUtil.get_data( sql_content%('100313'))[0][0],
        "syzyptgrzb_1013": mysqlUtil.get_data( sql_content%('100314'))[0][0],
        "syzyptgrzb_1014": mysqlUtil.get_data( sql_content%('100315'))[0][0],
        "syzyptgrzb_1015": mysqlUtil.get_data( sql_content%('100316'))[0][0],
        'image0': InlineImage(tpl, smooth_line_pic_name, width=Mm(150)),
        'image1': InlineImage(tpl, bar_line_pic_name_app, width=Mm(150)),
        'image2': InlineImage(tpl, bar_line_pic_name_api, width=Mm(150)),
    }

    tpl.render(context)
    tpl.save(day_doc_path)


