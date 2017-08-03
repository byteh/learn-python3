 #!/usr/bin/python
 #coding:utf-8

#1.一个简单的迭代器
class SimpleCounter(object):
    def __init__(self, start, end):
        self.start = start
        self.current = start
        self.end = end
        self.operator = ''
    def __iter__(self):
        'Returns itself as an iterator object'
        return  self
    def next(self):
        'Returns the next value till current is lower than end'
        if self.current > self.end:
            raise StopIteration
        else:
            self.operator = '->'
            self.current += 1
            return self.current
    def pre(self):
        'Returns the next value till current is lower than end'
        if self.current <= self.start:
            raise StopIteration
        else:
            self.operator = '<-'
            self.current -= 1
            return self.current

#2.访问这个迭代器
c = SimpleCounter(0,8)
print c.current,c.next(),c.operator,"\n"
print c.current,c.next(),c.operator,"\n"
print c.current, c.pre(),c.operator,"\n"
print c.current, c.pre(),c.operator,"\n"
print c.current,c.next(),c.operator,"\n"
print c.current,c.next(),c.operator,"\n"

#3.另外一种访问方式,将接着迭代器当前的位置继续访问
for entry in iter(c):
    print "-->",entry

print "\n  open file and print"
f = open('test.txt')
for l in iter(f):
    print l
f.close()
