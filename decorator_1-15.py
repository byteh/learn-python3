#!/usr/bin/python
#coding:utf-8
#装饰器能封装一个函数，并且改变它的行为
#没有能够理解下面这个例子

from string import punctuation

def pipeline_wrapper(func):
    def to_lower(x):
        # print 3,x
        return x.lower()

    def remove_punc(x):
        print 2
        for p in punctuation:
            x = x.replace(p,'')
        return x

    def wrapper(*args, **kwargs):
        print 1
        x = to_lower(*args, **kwargs)
        x = remove_punc(x)
        return func(x)
    return wrapper

@pipeline_wrapper  #装饰器 ？？？
def tokenize_whitespace(inText):
    # print inText   #string with punctuation
    # return inText
    return inText.split()

s = "string. With. Punctuation?"
print tokenize_whitespace(s)
