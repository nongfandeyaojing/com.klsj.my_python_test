from pipe import *


@Pipe
def add_ele(iterable,qte):
    for i in iterable:
        i=i+qte
        yield i

# https://www.jianshu.com/p/f0ecf265979e?utm_campaign=haruki
if __name__ == '__main__':
    range(5)  | add #使用add求和

    #(2) 条件过滤
    #求偶数和需要使用到where，作用类似于内建函数filter，过滤出符合条件的元素：
    range(5) | where(lambda x: x % 2 == 0) | add

    #(3)需要对元素应用某个函数可以使用select，作用类似于内建函数map；需要得到一个列表，可以使用as_list：
    [1,2,3] | select(lambda x:x**2) | as_list
    #result
    [1, 4, 9]

    #筛选和过滤
    [1, 2, 3, 4] | take_while(lambda x: x < 3) | concat
    [1, 2, 3, 4] | where(lambda x: x < 3) | concat
    #结果：'1, 2'
    [1, 2, 3, 4] | concat("#")  #concat连接
    #结果：'1#2#3#4'

    #take ：提取前几个元素，count：返回生成器的长度
    [1,2,3] | take(2) | as_list | where(lambda  x : x ==2) | as_list | count
    [1,2,3]|count

    #any()，只要存在一个就返回true
    (1, 3, 5, 6, 7) | any(lambda x: x >= 7)  #结果：Ture
    (1, 3, 5, 6, 7) | any(lambda x: x > 7)  #结果：Flase
    #all(),必须全部满足才会返回true
    (1, 3, 5, 6, 7) | all(lambda x: x < 7)
    (1, 3, 5, 6, 7) | all(lambda x: x <= 7)

    #max() 按照key中的指定的函数来排序，然后筛选出max的函数
    ('aa', 'b', 'fosdfdfo', 'qwerty', 'bar', 'zoog') | max(key=len)
    ('aa', 'b', 'foo', 'qwerty', 'bar', 'zoog') | max()  #不填key的时候返回的是 'zoog'，应该是默认按位置排序

    #平均数
    [1, 2, 3, 4, 5, 6] | average

    #封装itertools.chain
    [[1, 2], [3, 4], [5]] | chain | concat
    (1, 2, 3) | chain_with([4, 5], [6]) | concat



    #运用
    [1,2,3] | add_ele(3) | as_list

