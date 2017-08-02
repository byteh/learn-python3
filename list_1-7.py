 #!/usr/bin/python
 #coding:utf-8
# 2017-08-02
#列表推导是从一个序列创建另一个序列的操作
# 推导是不是就是迭代呢？

#1.定义一个有一些正整数和负整数构成的简单列表
a=[1,2,-1,-2,3,4,-3,-4,-5]
#2.列表推导
# pow()是幂函数，第一个参数是底数，第二个是指数
# 输入列表是a，输出列表是b
# x表示列表中的每个元素
# pow(x,2) 是输出表达式，使用输入列表中的元素来计算产生输出列表
# "if x<0" 是谓词表达式，负责选择输入列表中的元素
b = [pow(x,2) for x in a if x<0]
print b

#3.字典也可以推导 k->key v->value
a = {'a':1,'b':2,'c':3}
b = {k:pow(v,2) for k,v in a.items()}
print b

def process(x):
    if isinstance(x,str):
        return x.lower()
    elif isinstance(x,int):
        return x*x*2
    else:
        return -9

a = (1,2,-1,-2,'D',3,4,-3,'A',3.14,'a')
print "a=",a
b = tuple(process(x) for x in a)
c = {tuple(process(x) for x in a)}  # 一个大set 注意len
print b,len(b)
print c,len(c)
print "a=",a
d = {process(x) for x in a}  # set会去掉重复的值，注意len
print d,len(d)