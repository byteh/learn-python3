#!/usr/bin/python
#coding:utf-8

#1.16.2 #使用 lambda 创造匿名函数
a = [10,20,30]

def do_list(a_list, func):
    total = 0
    for element in a_list:
        total += func(element)
    return total

print do_list(a, lambda x:x**2)
print do_list(a, lambda x:x+5)

# b = [lambda x: x%3 ==0 for x in a]
# print b


#1.17 使用map映射函数.一个函数和可迭代对象作为参数
a = [10,20,30]
print map(lambda x:x**2,a)
#一行代码实现1.16.2的累加计数
print sum(map(lambda x:x**2, a))
#N个参数
a = [10,20,30]
b = [1,2,3]
print map(pow, a, b)

#1.18 使用过滤器
a = [10,20,30,40,50]
print filter(lambda x:x>10 and x<50, a)