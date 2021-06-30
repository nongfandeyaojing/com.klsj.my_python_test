from docx.shared import Mm
from docxtpl import DocxTemplate,RichText,InlineImage
from datetime import datetime



tpl=DocxTemplate('日常监测模板.docx')

# docx 富文本插入、样式设计
context = {
    'alerts' : [
        {'date' : '2015-03-10', 'desc' : RichText('Very critical alert',color='FF0000', bold=True), 'type' : 'CRITICAL', 'bg': 'FF0000' },
        {'date' : '2015-03-11', 'desc' : RichText('Just a warning'), 'type' : 'WARNING', 'bg': 'FFDD00' },
        {'date' : '2015-03-12', 'desc' : RichText('Information'), 'type' : 'INFO', 'bg': '8888FF' },
        {'date' : '2015-03-13', 'desc' : RichText('Debug trace'), 'type' : 'DEBUG', 'bg': 'FF00FF' },
    ],
}

tpl.render(context)
tpl.save('python模板测试3.docx')


tpl=DocxTemplate('日常监测模板.docx')

context = {
    'col_labels' : ['fruit', 'vegetable', 'stone', 'thing'],
    'tbl_contents': [
        {'label': 'yellow', 'cols': ['banana', 'capsicum', 'pyrite', 'taxi']},
        {'label': 'red', 'cols': ['apple', 'tomato', 'cinnabar', 'doubledecker']},
        {'label': 'green', 'cols': ['guava', 'cucumber', 'aventurine', 'card']},
    ]
}

tpl.render(context)
tpl.save('python模板测试4.docx')

# 垂直合并表格单元格 {％vm％}垂直合并单元格
tpl=DocxTemplate('日常监测模板.docx')

context = {
    'items' : [
        {'desc' : 'Python interpreters', 'qty' : 2, 'price' : 'FREE' },
        {'desc' : 'Django projects', 'qty' : 5403, 'price' : 'FREE' },
        {'desc' : 'Guido', 'qty' : 1, 'price' : '100,000,000.00' },
    ],
    'total_price' : '100,000,000.00',
    'category' : 'Book'
}

tpl.render(context)
tpl.save('python模板测试5.docx')

# 动态垂直合并表格单元格（表格堆叠用于）
tpl = DocxTemplate('日常监测模板.docx')

data = {
    "data":[
        {"name_0":"pkl",
         "area":[{
             "name_1":"smart",
             "name_2":"beautiful",
             "name_3":"pretty",
             "name_4":"big eyes",
             "name_5":"gentle"
         },{
             "name_1":"smart_2",
             "name_2":"beautiful_2",
             "name_3":"pretty_2",
             "name_4":"big eyes_2",
             "name_5":"gentle_2"
         }

         ]
         },
        {"name_0":"lilicat",
         "area":[{
             "name_1":"stupid",
             "name_2":"beautiful",
             "name_3":"pretty",
             "name_4":"big eyes",
             "name_5":"gentle"
         },{
             "name_1":"stupid_2",
             "name_2":"beautiful_2",
             "name_3":"pretty_2",
             "name_4":"big eyes_2",
             "name_5":"gentle_2"
         }

         ]
         },
        {"name_0":"lilicat1",
         "area":[{
             "name_1":"stupid",
             "name_2":"beautiful",
             "name_3":"pretty",
             "name_4":"big eyes",
             "name_5":"gentle"
         },{
             "name_1":"stupid_2",
             "name_2":"beautiful_2",
             "name_3":"pretty_2",
             "name_4":"big eyes_2",
             "name_5":"gentle_2"
         }

         ]
         }
    ]
}
tpl.render(data)
tpl.save('python模板测试6.docx')

# 内嵌图片
# 本来很简单的被我搞的很复杂
tpl = DocxTemplate('日常监测模板.docx')
data = {
    'image':InlineImage(tpl,'测试花1.jpg',width=Mm(30))
}
tpl.render(data)
tpl.save('python模板测试7.docx')