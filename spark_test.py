import sys
from pyspark import SparkContext
from operator import add
import re


if __name__ == "__main__":
    sc = SparkContext(appName="wordsCount")
    lines = sc.textFile('D:/idea_project1/com.klsj.my_python_test/words.txt')
    # counts = lines.flatMap(lambda x: x.split(' ')) \
    #     .map( lambda x: (x, 1)) \
    #     .reduceByKey(add)
    output = lines.collect()
    print(output)
    # for (word, count) in output:
    #     print("%s: %i" %(word, count))
    # print(sys.path)

