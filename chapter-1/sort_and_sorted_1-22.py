#!/usr/bin/python
#coding:utf-8

a = [8,0,3,4,5,2,9,6,7,1]
print a
a.sort()
print a
print
a = [8,0,3,4,5,2,9,6,7,1]
print a
a.sort(reverse=True)
print a
print

b = (8,0,3,4,5,2,9,6,7,1)
print b
b_s = sorted(b)
print b_s

# name, id, age
employee_records = [('joe',1,53),('beck',2,26),('ele',6,32),('neo',3,45),('christ',5,32),('ticke',4,29)]
print employee_records
print sorted(employee_records, key=lambda emp : emp[0])
print sorted(employee_records, key=lambda emp : emp[2])
print

#使用python 函数访问键
employee_records = [('joe',1,53),('beck',2,26),('ele',6,32),('neo',3,45),('christ',5,32),('arise',4,29)]
print employee_records
from operator import itemgetter
print sorted(employee_records, key=itemgetter(1))
print

#将雇员记录封装为类对象
class Employee(object):
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    def pretty_print(self):
        print self.name,self.id,self.age
    def random_method(self):
        return self.age / self.id
#将类填入列表
employee_records2 = []
emp1 = Employee('joe',1,53)
emp2 = Employee('beck',2,26)
emp3 = Employee('ele',6,32)
employee_records2.append(emp1)
employee_records2.append(emp2)
employee_records2.append(emp3)
for emp in employee_records2:
    emp.pretty_print()
print
from operator import attrgetter
employee_records_sorted = sorted(employee_records2, key=attrgetter('age'))
for emp in employee_records_sorted:
    emp.pretty_print()
print
from operator import methodcaller
employee_records_sorted2 = sorted(employee_records2, key=methodcaller('random_method'))
for emp in employee_records_sorted2:
    emp.pretty_print()