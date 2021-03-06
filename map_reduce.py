#!/usr/bin/python
#coding:utf-8
from functools import reduce


#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
#map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
#>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#['1', '2', '3', '4', '5', '6', '7', '8', '9']
#只需要一行代码。
def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
lstR = list(r)
print lstR

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def quadraticSum(x, y):
    return x*x + y*y
re = reduce(quadraticSum,[1,2,3])
print re

def fn(x, y):
    return x * 10 + y

re2 = reduce(fn, [1, 3, 5, 7, 9])
print re2

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

re3 = reduce(fn, map(char2num, '13579'))
print re3

#用map，转化首字母大写
def normalize(name):
    return name.capitalize()
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print L1,'=>',(L2)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
#print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
def prod(L):
    return reduce(mul, L)
def mul(x,y):
    return x * y
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
