#!/usr/bin/python
#coding:utf-8
# 生成器

#1.生成器推导.得到一个生成器对象
# 创建了名为SimpleCounter的迭代器，用它在for循环中访问数据，没有使用1.8中的inner，重建了SimpleCounter类
SimpleCounter = (x**2 for x in range(1,10))
tot = 0
for val in SimpleCounter:
    print tot,val
    tot += val

print tot

#2.my_gen 是一个生成器
def my_gen(low, high):
    for x in range(low, high):
        yield x**2
tot = 0
for val in my_gen(1,10):
    print tot, val
    tot += val
print tot

#3.验证生成器和可迭代两者才能制造一个迭代器
gen = (x**2 for x in range(1,10))
for val in iter(gen):
    print val
