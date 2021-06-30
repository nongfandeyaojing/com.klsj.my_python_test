from pyecharts.charts import Bar,Line
from snapshot_selenium import snapshot
from pyecharts import options as opts

# 导入输出图片工具
from pyecharts.render import make_snapshot
from pyecharts.commons.utils import JsCode

class My_Pyecharts:

    def __init__(self):
        pass

    def line(self, x_data, y_data, title, subtitle, pic_name):
        line = (
            Line()
                .add_xaxis(x_data)
                .add_yaxis(
                    series_name="",  #这里需要调整一下
                    y_axis=y_data,
                    is_smooth=True,
                    markpoint_opts=opts.MarkPointOpts(
                        data=[opts.MarkPointItem(name="xxx", type_="max"), opts.MarkPointItem(name="xxx", type_="min")]
                    ),
                    markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="xxx", type_="average")]),
                    label_opts=opts.LabelOpts(formatter=JsCode(
                        "function(x){return(x.data[1]+ '万');}"
                    ))
                )
                .set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
                                 yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}万')),
                                 xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 15})
                                 )
        )
        make_snapshot(snapshot, line.render(), pic_name)

    def bar_line(self, bar_label, bar_data, line_data, title, subtitle, pic_name):

        bar = (
            Bar().add_xaxis(xaxis_data= bar_label)
                .add_yaxis(
                series_name="调用次数",
                y_axis=bar_data,
                itemstyle_opts=opts.ItemStyleOpts(color="#c23531", opacity=0.6),  # 柱形图颜色及透# 明度
                label_opts=opts.LabelOpts(is_show=True, position='top', formatter="{c}",)  # 显示数据标签
                )
                .extend_axis(
                    yaxis=opts.AxisOpts(
                        name="增长率",
                        type_="value",
                        # min_=0,
                        # max_=10000,
                        # interval=0.5,
                        axisline_opts=opts.AxisLineOpts(is_show=False,# y轴线不显示
                                                        linestyle_opts=opts.LineStyleOpts(color='#c23531')), # 设置线颜色, 字体颜色也变
                        axistick_opts=opts.AxisTickOpts(is_show=False),   # 刻度线不显示
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
                        interval=500000,
                        axislabel_opts=opts.LabelOpts(formatter="{value}"),
                        axistick_opts=opts.AxisTickOpts(is_show=True),
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                    ),
                    title_opts=opts.TitleOpts(title=title, subtitle=subtitle)
                )
        )

        line = (
            Line().add_xaxis(xaxis_data=bar_label)
                .add_yaxis(
                series_name="xxx增长率",
                yaxis_index=1,
                y_axis=line_data,
                label_opts=opts.LabelOpts(is_show=True, formatter=JsCode(
                    "function(x){return(x.data[1]+ '%');}"
                )
                                          ),
                linestyle_opts=opts.LineStyleOpts(width=3, color ='#c23531'),
                is_smooth=True,
            )
        )
        make_snapshot(snapshot, bar.overlap(line).render(), pic_name)
        # bar1.overlap(line1).render("mixed_bar_and_line.html")
