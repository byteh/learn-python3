#!/usr/bin/python
#coding:utf-8
# 1-11 函数作为变量传递,函数式编程

#1.11.2
#1.定义一个简单的函数
def square_input(x):
    return x*x
#2.把它分配给一个变量
square_me = square_input
#3.调用这个变量
print square_me(5)
print "\n"

#1.12.2 函数式编程的了一个概念：在一个函数中定义另一个函数
#1.定义一个函数，返回给定输入数值得平方和
def sum_square(x):
    def square_input(x):
        return x*x
    return sum([square_input(x1) for x1 in x])
#2.输出结果来检查是否正确
print sum_square([1,2,4,5])

#1.13.2 高阶函数功能：将一个函数作为另外一个函数的参数传递
from math import log
def square_input(x):
    return x*x
#1.定义一个函数，它将另外一个函数作为输入，并将它应用到给定的输入序列上
def apply_func(func_x, input_x):
    return map(func_x, input_x)
#2.使用apply_func()函数，并检验结果
a = [1,2,3,4]
print apply_func(square_input, a)
print apply_func(log, a)

#1.14.2 在函数中返回函数
#1 计算圆柱体的体积
def cylinder_vol(r):
    pi = 3.141
    def get_vol(h):
        return pi * r**2 * h
    return get_vol
#2 固定的半径，用一个函数来求出体积
radius = 10
find_volume = cylinder_vol(radius)
#3 给出不同的高度，求解圆柱体的体积
height = 10
print "Volume of cylinder of radius %d and height %d = %.2f cubic units" %(radius, height,find_volume(height))
height = 20
print "Volume of cylinder of radius %d and height %d = %.2f cubic units" %(radius, height,find_volume(height))