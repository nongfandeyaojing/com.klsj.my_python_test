import  time
import datetime



if __name__=="__main__":
    time_stamp = datetime.datetime.now()
    with open('timingprint.txt',mode='a') as f:
        f.write(time_stamp.strftime('%Y.%m.%d-%H:%M:%S')+'\n')
    print(time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))
