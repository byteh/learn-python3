 #!/usr/bin/python
 #coding:utf-8
#列表是一种顺序型的容器对象，它和元组很相似，但是它只能保存同类的数据，并且是可变的。列表支持追加操作，可以用来当做堆或者队列。与元组不同，它可以扩展，创建之后可以使用append来追加元素。

#1.快速地创建一个列表
a = range(1,10)
print a
b = ["a","b","c",4]
print b

#2.列表可以通过索引访问，索引起始于0
print a[0]
#3.用负数作为索引，从反方向开始
print a[-1]

#4.使用两个索引参数，切片操作可以访问列表的子集
print a[1:3] # [2,3]
print a[1:] # [2,3,4,5,6,7,8,9]
print a[-1:] # [9]
print a[:-1:] # [1,2,3,4,5,6,7,8]

#5.列表串联
a = [1,2,3]
b = [3,4]
print a+b 

#6.min and max
print min(a), max(a)

#7.包含于和非包含于
if 1 in a:
    print "Element 1 is available in list a"
else:
    print "Element 1 is available in tuple a"

#8.追加和扩展列表
a = range(1,10)
a.append(10)
print a

#9.列表实现堆
a_stack = []
a_stack.append(1)
a_stack.append(2)
a_stack.append(3)
print a_stack.pop()
print a_stack.pop()
print a_stack.pop()

#9.列表实现堆
a_stack = []
a_stack.append(1)
a_stack.append(2)
a_stack.append(3)
print a_stack.pop()
print a_stack.pop()
print a_stack.pop()
print "\n"

#10。列表实现队列
a_queue = []
a_queue.append(1)
a_queue.append(2)
a_queue.append(3)
print "a_queue lenth:",len(a_queue)
print a_queue.pop(0)
print a_queue.pop(0)
print a_queue.pop(0)

#11.列表排序和反转
from random import shuffle
a=range(1,20)
shuffle(a)
print a
a.sort()
print a
a.reverse()
print a

#12.扩展
a=range(1,20)
b=range(11,15)
a.extend(b)
print a
