
import datetime

if __name__ == '__main__':
    time_stamp = datetime.datetime.now()
    with open('windows_cron_test.txt', mode='a',  encoding='utf-8',) as f:
        f.write(time_stamp.strftime('%Y/%m/%d %H:%M:%S')+" 我是你爸爸！\n")
