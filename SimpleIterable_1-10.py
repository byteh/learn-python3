#!/usr/bin/python
#coding:utf-8
# 生成器

#1.创建一个简单的带有 iter 方法的类
class SimpleIterable(object):
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        for x in range(self.start, self.end):
            yield x**2

#2.现在调用这个类，并且迭代它的值两次
c = SimpleIterable(1,10)

#3.第一次迭代
tot = 0
for val in iter(c):
    print tot, val
    tot += val
print tot

print "\n"
#4.第二次迭代
tot = 0
for val in iter(c):
    print tot, val
    tot += val
print tot
