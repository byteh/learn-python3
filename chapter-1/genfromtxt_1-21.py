#!/usr/bin/python
#coding:utf-8

import numpy as np
from StringIO import StringIO

in_data = StringIO("30kg,inr2000,31.11,56.33,1\n52kg,inr8000.35,12,16.7,2")
#1使用lambda函数来定义两个数据预处理函数
strip_func_1 = lambda x : float(x.rstrip("kg"))
strip_func_2 = lambda x : float(x.lstrip("inr"))
#2创建一个函数的字典
convert_funcs = {0:strip_func_1, 1:strip_func_2}
#3将这个函数的字典传递给genfromtxt
data = np.genfromtxt(in_data, delimiter=',', converters=convert_funcs)
print data
print
#4使用 lambda 函数来处理转换过程
in_data = StringIO("10,20,30\n56,,90\n33,46,89")
miss_func = lambda x : float(x.strip() or -999)
data = np.genfromtxt(in_data, delimiter=',',converters={1:miss_func})
print data
print