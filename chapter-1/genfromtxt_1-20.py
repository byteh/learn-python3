#!/usr/bin/python
#coding:utf-8

import numpy as np
from StringIO import StringIO

in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
#使用Numpy的genfromtxt来读取数据，并创建一个NumPy数组
data = np.genfromtxt(in_data, dtype=int, delimiter=",")
print data
print
#清除掉不需要的列
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype=int, delimiter=',',usecols=(0,1))
print data
print
#设定列名
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype=int, delimiter=',',names="a,b,c")
print data
print
#使用列名来处理数据
in_data = StringIO("a,b,c\n10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype=int, delimiter=',',names=True)
print data
print