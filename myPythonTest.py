import dingtalk
from dingtalk_test import dingtalk_test

if __name__ == '__main__':
    access_token = '266a461382aa24505a8720e29b78accf125c1313381f6cdbe8d595cd8eef45ab' # 创建webhook机器人时的access_token
    msgtype = 'markdown'
    dt = dingtalk_test()
    result = dt.DingTalk_Test(access_token,msgtype)
    print(result)