import dingtalk
from datetime import datetime
import time

class dingtalk_test:
    # https://developers.dingtalk.com/document/app/custom-robot-access
    # access_token:创建webhook机器人时的access_token
    def __init__(self):
        pass

    def DingTalk_Test(self,access_token,msgtype='text',):

        dt = dingtalk.DingTalk(access_token)
        response = ''

        if msgtype =='markdown':
            title = 'test '
            text = '#### 数据资源平台日常巡检指标\n' \
                   '> ###### 播报时间: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) \
                   +'\n---'\
                   '\n ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n' \
                    '> ###### 指标情况 [天气](https://www.dingtalk.com) \n'\
                    '---\n' \
                    '> 1. <font color= #F0F8FF>AliceBlue</font>\n' \
                    '> 2. <font color=#FAEBD7>AntiqueWhite</font>\n' \
                    '> 3. <font color=#00FFFF>Aqua</font>\n' \
                    '> 4. <font color=#7FFFD4>Aquamarine</font>\n' \
                    '> 5. <font color=#F0FFFF>Azure</font>\n' \
                    '> 6. <font color=#F5F5DC>Beige</font>\n' \
                    '> 7. <font color=#FFE4C4>Bisque</font>\n' \
                    '> 8. <font color=#000000>Black</font>\n' \
                    '> 9. <font color=#FFEBCD>BlanchedAlmond</font>\n' \
                    '> 10. <font color=#0000FF>Blue</font>\n' \
                    '> 11. <font color=#8A2BE2>BlueViolet</font>\n' \
                    '> 12. <font color=#A52A2A>Brown</font>\n' \
                    '> 13. <font color=#DEB887>BurlyWood</font>\n' \
                    '> 14. <font color=#5F9EA0>CadetBlue</font>\n' \
                    '> 15. <font color=#7FFF00>Chartreuse</font>\n' \
                    '> 16. <font color=#D2691E>Chocolate</font>\n' \
                    '> 17. <font color=#FF7F50>Coral</font>\n' \
                    '> 18. <font color=#6495ED>CornflowerBlue</font>\n' \
                    '> 19. <font color=#FFF8DC>Cornsilk</font>\n' \
                    '> 20. <font color=#DC143C>Crimson</font>\n' \
                    '> 21. <font color=#00FFFF>Cyan</font>\n' \
                    '> 22. <font color=#00008B>DarkBlue</font>\n' \
                    '> 23. <font color=#008B8B>DarkCyan</font>\n' \
                    '> 24. <font color=#B8860B>DarkGoldenRod</font>\n' \
                    '> 25. <font color=#A9A9A9>DarkGray</font>\n' \
                    '> 26. <font color=#006400>DarkGreen</font>\n' \
                    '> 27. <font color=#BDB76B>DarkKhaki</font>\n' \
                    '> 28. <font color=#8B008B>DarkMagenta</font>\n' \
                    '> 29. <font color=#556B2F>DarkOliveGreen</font>\n' \
                    '> 30. <font color=#FF8C00>Darkorange</font>\n' \
                    '> 31. <font color=#9932CC>DarkOrchid</font>\n' \
                    '> 32. <font color=#8B0000>DarkRed</font>\n' \
                    '> 33. <font color=#E9967A>DarkSalmon</font>\n' \
                    '> 34. <font color=#8FBC8F>DarkSeaGreen</font>\n' \
                    '> 35. <font color=#483D8B>DarkSlateBlue</font>\n' \
                    '> 36. <font color=#2F4F4F>DarkSlateGray</font>\n' \
                    '> 37. <font color=#00CED1>DarkTurquoise</font>\n' \
                    '> 38. <font color=#9400D3>DarkViolet</font>\n' \
                    '> 39. <font color=#FF1493>DeepPink</font>\n' \
                    '> 40. <font color=#00BFFF>DeepSkyBlue</font>\n' \
                    '> 41. <font color=#696969>DimGray</font>\n' \
                    '> 42. <font color=#1E90FF>DodgerBlue</font>\n' \
                    '> 43. <font color=#D19275>Feldspar</font>\n' \
                    '> 44. <font color=#B22222>FireBrick</font>\n' \
                    '> 45. <font color=#FFFAF0>FloralWhite</font>\n' \
                    '> 46. <font color=#228B22>ForestGreen</font>\n' \
                    '> 47. <font color=#FF00FF>Fuchsia</font>\n' \
                    '> 48. <font color=#DCDCDC>Gainsboro</font>\n' \
                    '> 49. <font color=#F8F8FF>GhostWhite</font>\n' \
                    '> 50. <font color=#FFD700>Gold</font>\n' \
                    '> 51. <font color=#DAA520>GoldenRod</font>\n' \
                    '> 52. <font color=#808080>Gray</font>\n' \
                    '> 53. <font color=#008000>Green</font>\n' \
                    '> 54. <font color=#ADFF2F>GreenYellow</font>\n' \
                    '> 55. <font color=#F0FFF0>HoneyDew</font>\n' \
                    '> 56. <font color=#FF69B4>HotPink</font>\n' \
                    '> 57. <font color=#CD5C5C>IndianRed</font>\n' \
                    '> 58. <font color=#4B0082>Indigo</font>\n' \
                    '> 59. <font color=#FFFFF0>Ivory</font>\n' \
                    '> 60. <font color=#F0E68C>Khaki</font>\n' \
                    '> 61. <font color=#E6E6FA>Lavender</font>\n' \
                    '> 62. <font color=#FFF0F5>LavenderBlush</font>\n' \
                    '> 63. <font color=#7CFC00>LawnGreen</font>\n' \
                    '> 64. <font color=#FFFACD>LemonChiffon</font>\n' \
                    '> 65. <font color=#ADD8E6>LightBlue</font>\n' \
                    '> 66. <font color=#F08080>LightCoral</font>\n' \
                    '> 67. <font color=#E0FFFF>LightCyan</font>\n' \
                    '> 68. <font color=#FAFAD2>LightGoldenRodYellow</font>\n' \
                    '> 69. <font color=#D3D3D3>LightGrey</font>\n' \
                    '> 70. <font color=#90EE90>LightGreen</font>\n' \
                    '> 71. <font color=#FFB6C1>LightPink</font>\n' \
                    '> 72. <font color=#FFA07A>LightSalmon</font>\n' \
                    '> 73. <font color=#20B2AA>LightSeaGreen</font>\n' \
                    '> 74. <font color=#87CEFA>LightSkyBlue</font>\n' \
                    '> 75. <font color=#8470FF>LightSlateBlue</font>\n' \
                    '> 76. <font color=#778899>LightSlateGray</font>\n' \
                    '> 77. <font color=#B0C4DE>LightSteelBlue</font>\n' \
                    '> 78. <font color=#FFFFE0>LightYellow</font>\n' \
                    '> 79. <font color=#00FF00>Lime</font>\n' \
                    '> 80. <font color=#32CD32>LimeGreen</font>\n' \
                    '> 81. <font color=#FAF0E6>Linen</font>\n' \
                    '> 82. <font color=#FF00FF>Magenta</font>\n' \
                    '> 83. <font color=#800000>Maroon</font>\n' \
                    '> 84. <font color=#66CDAA>MediumAquaMarine</font>\n' \
                    '> 85. <font color=#0000CD>MediumBlue</font>\n' \
                    '> 86. <font color=#BA55D3>MediumOrchid</font>\n' \
                    '> 87. <font color=#9370D8>MediumPurple</font>\n' \
                    '> 88. <font color=#3CB371>MediumSeaGreen</font>\n' \
                    '> 89. <font color=#7B68EE>MediumSlateBlue</font>\n' \
                    '> 90. <font color=#00FA9A>MediumSpringGreen</font>\n' \
                    '> 91. <font color=#48D1CC>MediumTurquoise</font>\n' \
                    '> 92. <font color=#C71585>MediumVioletRed</font>\n' \
                    '> 93. <font color=#191970>MidnightBlue</font>\n' \
                    '> 94. <font color=#F5FFFA>MintCream</font>\n' \
                    '> 95. <font color=#FFE4E1>MistyRose</font>\n' \
                    '> 96. <font color=#FFE4B5>Moccasin</font>\n' \
                    '> 97. <font color=#FFDEAD>NavajoWhite</font>\n' \
                    '> 98. <font color=#000080>Navy</font>\n' \
                    '> 99. <font color=#FDF5E6>OldLace</font>\n' \
                    '> 100. <font color=#808000>Olive</font>\n' \
                    '> 101. <font color=#6B8E23>OliveDrab</font>\n' \
                    '> 102. <font color=#FFA500>Orange</font>\n' \
                    '> 103. <font color=#FF4500>OrangeRed</font>\n' \
                    '> 104. <font color=#DA70D6>Orchid</font>\n' \
                    '> 105. <font color=#EEE8AA>PaleGoldenRod</font>\n' \
                    '> 106. <font color=#98FB98>PaleGreen</font>\n' \
                    '> 107. <font color=#AFEEEE>PaleTurquoise</font>\n' \
                    '> 108. <font color=#D87093>PaleVioletRed</font>\n' \
                    '> 109. <font color=#FFEFD5>PapayaWhip</font>\n' \
                    '> 110. <font color=#FFDAB9>PeachPuff</font>\n' \
                    '> 111. <font color=#CD853F>Peru</font>\n' \
                    '> 112. <font color=#FFC0CB>Pink</font>\n' \
                    '> 113. <font color=#DDA0DD>Plum</font>\n' \
                    '> 114. <font color=#B0E0E6>PowderBlue</font>\n' \
                    '> 115. <font color=#800080>Purple</font>\n' \
                    '> 116. <font color=#FF0000>Red</font>\n' \
                    '> 117. <font color=#BC8F8F>RosyBrown</font>\n' \
                    '> 118. <font color=#4169E1>RoyalBlue</font>\n' \
                    '> 119. <font color=#8B4513>SaddleBrown</font>\n' \
                    '> 120. <font color=#FA8072>Salmon</font>\n' \
                    '> 121. <font color=#F4A460>SandyBrown</font>\n' \
                    '> 122. <font color=#2E8B57>SeaGreen</font>\n' \
                    '> 123. <font color=#FFF5EE>SeaShell</font>\n' \
                    '> 124. <font color=#A0522D>Sienna</font>\n' \
                    '> 125. <font color=#C0C0C0>Silver</font>\n' \
                    '> 126. <font color=#87CEEB>SkyBlue</font>\n' \
                    '> 127. <font color=#6A5ACD>SlateBlue</font>\n' \
                    '> 128. <font color=#708090>SlateGray</font>\n' \
                    '> 129. <font color=#FFFAFA>Snow</font>\n' \
                    '> 130. <font color=#00FF7F>SpringGreen</font>\n' \
                    '> 131. <font color=#4682B4>SteelBlue</font>\n' \
                    '> 132. <font color=#D2B48C>Tan</font>\n' \
                    '> 133. <font color=#008080>Teal</font>\n' \
                    '> 134. <font color=#D8BFD8>Thistle</font>\n' \
                    '> 135. <font color=#FF6347>Tomato</font>\n' \
                    '> 136. <font color=#40E0D0>Turquoise</font>\n' \
                    '> 137. <font color=#EE82EE>Violet</font>\n' \
                    '> 138. <font color=#D02090>VioletRed</font>\n' \
                    '> 139. <font color=#F5DEB3>Wheat</font>\n' \
                    '> 140. <font color=#FFFFFF>White</font>\n' \
                    '> 141. <font color=#F5F5F5>WhiteSmoke</font>\n' \
                    '> 142. <font color=#FFFF00>Yellow</font>\n' \
                    '> 143. <font color=#9ACD32>YellowGreen</font>\n'
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
