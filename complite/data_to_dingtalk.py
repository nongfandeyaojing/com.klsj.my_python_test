import dingtalk

class dingtalk_test:
    # https://developers.dingtalk.com/document/app/custom-robot-access
    # access_token:创建webhook机器人时的access_token
    def __init__(self):
        pass

    def DingTalk_Test(self,access_token,msgtype='text',):

        dt = dingtalk.DingTalk(access_token)
        response = ''

        if msgtype =='markdown':
            title = '数据源检测test'
            text = '# 数据源检测test \n  - '
            at_mobiles = ['18844058377']
            at_all = False
            response = dt.send_markdown(title, text, at_mobiles, at_all)

        elif msgtype == "text":
            text = 'test,我就是我, @刘宝盛 是不一样的烟火'
            at_mobiles = ['18844058377']
            at_all = False
            response = dt.send_text(text, at_mobiles, at_all)

        elif msgtype == "link":
            title = 'link test'
            text = '这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是红树林'
            message_url = 'https://jingyan.baidu.com/article/0964eca20a02d08285f53601.html'
            picture_url='https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2334462635,4058253196&fm=26&gp=0.jpg'
            response = dt.send_link(title, text, message_url, picture_url)

        elif msgtype == "actionCard":
            """
           发送独立跳转的action card
           :param title: 首屏会话展示的标题内容
           :param text: markdown格式的文本内容
           :param hide_avatar: 0 显示发送消息者头像, 1 隐藏发送消息者头像
           :param button_orientation: 0 按钮竖直排列, 1 按钮水平排列
           :param buttons: list。每个列表的元素都是一个dict，单个按钮的跳转，需要传递title和actionURL字段。
           :return:
           """
            title = 'actionCard test乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身'
            text = '''![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)
            ### 乔布斯 20 年前想打造的苹果咖啡厅
    Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划'''
            buttons = [{'title':'xxx','actionURL':'https://developers.dingtalk.com/document/app/custom-robot-access'},
                       {'title':'xxx','actionURL':'https://developers.dingtalk.com/document/app/custom-robot-access'}]
            hide_avatar=0
            button_orientation=1
            response = dt.send_action_card(title, text, buttons, hide_avatar, button_orientation)

        elif msgtype == "feedCard":
            """
            发送feed card消息
            :param links: 列表。列表中的每个元素为dict，每个dict需要包含title、messageURL以及picURL字段。
            :return:
            """
            links = [ {
                "title": "test时代的火车向前开1",
                "messageURL": "https://www.dingtalk.com/",
                "picURL": "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"
            },
                {
                    "title": "时代的火车向前开2",
                    "messageURL": "https://www.dingtalk.com/",
                    "picURL": "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"
                }]
            response = dt.send_feed_card(links)

        else:
            print('请正确输入msgtype类型')

        # 直接返回response对象
        return (response)
