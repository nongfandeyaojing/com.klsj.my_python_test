from docxtpl import DocxTemplate,RichText,InlineImage
from docx.shared import Mm
import time
from pyecharts.charts import Bar,Line
from snapshot_selenium import snapshot
from pyecharts import options as opts
from pyecharts.faker import Faker
# 导入输出图片工具
from pyecharts.render import make_snapshot
import re
from pyecharts.commons.utils import JsCode
import pandas as pd
from api_index.My_Pyecharts import My_Pyecharts


if __name__ == "__main__":
    pass
    api_api_counts = [
        {"api_count_day": "2021-06-01", "api_count": 460734},
        {"api_count_day": "2021-06-02", "api_count": 364156},
        {"api_count_day": "2021-06-03", "api_count": 407810},
        {"api_count_day": "2021-06-04", "api_count": 234860},
        {"api_count_day": "2021-06-05", "api_count": 321051},
        {"api_count_day": "2021-06-06", "api_count": 394450},
        {"api_count_day": "2021-06-07", "api_count": 426347},
    ]
    app_api_counts = [
                    {"app_describe":"交通大屏","app_api_count":1673881,"app_api_ratio": 0.2},
                    {"app_describe":"城市大脑_政务_椰城市民云","app_api_count":791615,"app_api_ratio": 0.9},
                    {"app_describe":"城市大脑_政务_行政审批系统","app_api_count":25647,"app_api_ratio": 10},
                    {"app_describe":"市政务管理局_房联网签备案系统","app_api_count":20870,"app_api_ratio": 10000},
                    {"app_describe":"市交通局_运政系统","app_api_count":19628,"app_api_ratio": 13},
                    {"app_describe":"城市大脑_政务_信用信息平台","app_api_count":17787,"app_api_ratio": 0.2},
                    {"app_describe":"医疗_旅游_汇集_12345屏","app_api_count":16301,"app_api_ratio": 1000},
                ]
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

    line_x_data = [i['api_count_day'] for i in api_api_counts]
    line_y_data = [i['api_count'] for i in api_api_counts]
    line_title = "接口近七天调用次数趋势图"
    line_subtitle = "2021/06/01 - 2021/06/07"
    pic_name = "图片一.png"
    mp = My_Pyecharts()
    mp.line(line_x_data, line_y_data, line_title, line_subtitle, pic_name)


    bar_line_label_app = [i['app_describe'] for i in app_api_counts]
    bar_line_data_app = [i['app_api_count'] for i in app_api_counts]
    bar_line_line_data_app = [i['app_api_ratio'] for i in app_api_counts]
    bar_line_pic_name_app = "图片二.png"
    bar_line_title_app = "各业务应用调用次数Top7"
    bar_line_subtitle = "2021/06/01 - 2021/06/07"
    mp.bar_line(bar_line_label_app,bar_line_data_app,bar_line_line_data_app,bar_line_title_app,bar_line_subtitle,bar_line_pic_name_app)

    bar_line_label_api = [i['api_describe'] for i in api_counts]
    bar_line_data_api = [i['api_count'] for i in api_counts]
    bar_line_line_data_api = [i['api_ratio'] for i in api_counts]
    bar_line_pic_name_api = "图片三.png"
    bar_line_title_api = "各接口被调用次数Top10"
    bar_line_subtitle_api = "2021/06/01 - 2021/06/07"
    mp.bar_line(bar_line_label_api,bar_line_data_api,bar_line_line_data_api,bar_line_title_api,bar_line_subtitle_api,bar_line_pic_name_api)

    # # 时间
    today = time.strftime("%Y-%m-%d", time.localtime())
    today_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #
    # 文件路径
    templa_doc_file = '海口城市大脑项目 -数据资源平台版块-个人周报模板.docx'  #模板路径
    day_doc_path = '海口城市大脑项目 -数据资源平台版块-个人周报' + today + '.docx' #每日监测文档存放路径
    # day_excel_path = 'resourse/日常监测每日excel/'  #每日监测excel存放路径
    # '''
    #         结果写入到word
    #     '''
    tpl=DocxTemplate(templa_doc_file)
    # docx 富文本插入、样式设计
    context = {
        'today': today,
        'year': time.strftime("%Y", time.localtime()),
        'month': time.strftime("%m", time.localtime()),
        'day': time.strftime("%d", time.localtime()),
        'access_city': 29,
        'access_province': 30,
        'access_social': 14,
        'cloud_count': 8.9,
        'exchange_count': 4039,
        'business_app_count': 2705,
        'data_storage': 96,
        'all_data_storage': 596,
        'provincial_sharing_api': 460,
        'open_api_count': 1062,
        'api_count_7': 2602131,
        'image0': InlineImage(tpl, '图片一.png', width=Mm(150)),
        'image1': InlineImage(tpl, '图片二.png', width=Mm(150)),
        'image2': InlineImage(tpl, '图片三.png', width=Mm(150)),
        'app_api_counts': app_api_counts,
        'api_counts': api_counts,
    }

    tpl.render(context)
    tpl.save(day_doc_path)

    # x, y = Faker.choose(), Faker.values()
    # line = (
    #     Line()
    #         .add_xaxis(x)
    #         .add_yaxis(
    #         "商家A",
    #         y,
    #         is_smooth=True,
    #         markpoint_opts=opts.MarkPointOpts(
    #             data=[opts.MarkPointItem(name="xxx", type_="max"), opts.MarkPointItem(name="xxx", type_="min")]
    #         ),
    #         markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="xxx", type_="average")]),
    #         label_opts=opts.LabelOpts(formatter='{c}万')
    #     )
    #         .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint（自定义）", subtitle="2021/04/01-2021/05/01")
    #      , yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}万'))
    #      , xaxis_opts=opts.AxisOpts(name_rotate=60,
    #                                 axislabel_opts={"rotate": 15})                    )
    #         # .render("line_markpoint_custom.html")
    # )
    # make_snapshot(snapshot, line.render(), "图片一.png")
    #
    # y.sort(reverse=True)
    # bar = (
    #     Bar()
    #         .add_xaxis(x)
    #         .add_yaxis(
    #         "商家A",
    #         y,
    #
    #     )
    #         .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint（自定义）", subtitle="2021/04/01-2021/05/01")
    #                          , yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}万'))
    #                          , xaxis_opts=opts.AxisOpts(name_rotate=60,
    #                                                     axislabel_opts={"rotate": 15})                    )
    # )
    # make_snapshot(snapshot, bar.render(), "图片二.png")





