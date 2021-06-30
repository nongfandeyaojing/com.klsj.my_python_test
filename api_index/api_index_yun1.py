from pyecharts.charts import Bar,Line
from snapshot_selenium import snapshot
from pyecharts import options as opts

# 导入输出图片工具
from pyecharts.render import make_snapshot
from pyecharts.commons.utils import JsCode

def aa(x):
    print("xxxxxxxx")
    return(['xxx','xxx','sda','','sasd','dasda',''])

num=[407810,364156,460734,234860]


func = '''
function(params) {
var num=
'''+str(num)+''';
               if (params.data[1]==Math.max.apply(null, num) || params.data[1]==Math.min.apply(null, num)){
                    return ''  
                } 
                else {
                    return params.data[1] + '万'
                    }
            }
'''

def line1( x_data, y_data, title, subtitle, pic_name):

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
    line.render()

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
                name_rotate=60,
                axislabel_opts={"rotate": 10}
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
    bar.overlap(line).render('render3.html')


if __name__ == "__main__":
    # api_api_counts = [
    #     {"api_count_day": "2021-06-01", "api_count": 12.31},
    #     {"api_count_day": "2021-06-02", "api_count": 36.4123},
    #     {"api_count_day": "2021-06-03", "api_count": 13.21},
    #     {"api_count_day": "2021-06-04", "api_count": 26.0},
    #     {"api_count_day": "2021-06-05", "api_count": 32.051},
    #     {"api_count_day": "2021-06-06", "api_count": 39.350},
    #     {"api_count_day": "2021-06-07", "api_count": 63.47},
    # ]
    #
    # line_x_data = [i['api_count_day'] for i in api_api_counts]
    # line_y_data = [i['api_count'] for i in api_api_counts]
    #
    # line_title = "接口近七天调用次数趋势图"
    # line_subtitle = "2021/06/01 - 2021/06/07"
    # pic_name = "my_line_test.html"
    # line1(line_x_data, line_y_data, line_title, line_subtitle, pic_name)

    # app_api_counts = [
    #     {"app_describe":"交通大屏","app_api_count":167.3881,"app_api_ratio": 0.2},
    #     {"app_describe":"城市大脑_政务_椰城市民云","app_api_count":79.1615,"app_api_ratio": 0.9},
    #     {"app_describe":"城市大脑_政务_行政审批系统","app_api_count":2.5647,"app_api_ratio": 10},
    #     {"app_describe":"市政务管理局_房联网签备案系统","app_api_count":2.0870,"app_api_ratio": 10000},
    #     {"app_describe":"市交通局_运政系统","app_api_count":1.9628,"app_api_ratio": 13},
    #     {"app_describe":"城市大脑_政务_信用信息平台","app_api_count":1.7787,"app_api_ratio": 0.2},
    #     {"app_describe":"医疗_旅游_汇集_12345屏","app_api_count":1.6301,"app_api_ratio": 1000},
    # ]
    #
    # bar_line_label_app = [i['app_describe'] for i in app_api_counts]
    # bar_line_data_app = [i['app_api_count'] for i in app_api_counts]
    # bar_line_line_data_app = [i['app_api_ratio'] for i in app_api_counts]
    # bar_line_pic_name_app = "图片二.png"
    # bar_line_title_app = "各业务应用调用次数Top7"
    # bar_line_subtitle = "2021/06/01 - 2021/06/07"
    # bar_line(bar_line_label_app,bar_line_data_app,bar_line_line_data_app,bar_line_title_app,bar_line_subtitle,bar_line_pic_name_app)

    api_counts = [
        {"api_describe":"交通大屏","api_count":548756,"api_ratio": 0.2 },
        {"api_describe":"交通春运大屏_实时","api_count":334091,"api_ratio": 10 },
        {"api_describe":"相位数据接口V6","api_count":236263,"api_ratio": 20 },
        {"api_describe":"(正式)通过areaId、spObjectId查询热门事项,若没有则查询受理量多的事项","api_count":234619,"api_ratio": 0.2 },
        {"api_describe":"相位数据接口v3","api_count":234323 ,"api_ratio": 1000},
        {"api_describe":"（正式）新增预约件列表接口","api_count":146854 ,"api_ratio": 40},
        {"api_describe":"实时交通流量","api_count":128131 ,"api_ratio": 70},
        {"api_describe":"省API实际获取接口的接口","api_count":94901 ,"api_ratio": 44},
        {"api_describe":"行驶证详情","api_count":83694 ,"api_ratio": 0.1},
        {"api_describe":"省人社厅_职工保险社保个人缴费信息_多条","api_count":79321 ,"api_ratio": 0.2},
    ]

    bar_line_label_api = [i['api_describe'] for i in api_counts]
    bar_line_data_api = [i['api_count'] for i in api_counts]
    bar_line_line_data_api = [i['api_ratio'] for i in api_counts]
    bar_line_pic_name_api = "图片三.png"
    bar_line_title_api = "各接口被调用次数Top10"
    bar_line_subtitle_api = "2021/06/01 - 2021/06/07"
    bar_line(bar_line_label_api,bar_line_data_api,bar_line_line_data_api,bar_line_title_api,bar_line_subtitle_api,bar_line_pic_name_api)


