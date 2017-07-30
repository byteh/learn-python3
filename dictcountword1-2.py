#!/usr/bin/python
#coding:utf-8
from collections import Counter

sentence="Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked If Peter Piper picked a peck of pickled peppers Wheres the peck of pickled peppers Peter Piper picked"

word_dict = {}
for word in sentence.split():
# 下面的3行可以被 word_dict.setdefault(word, 0) 替换
#    if word not in word_dict:
#        word_dict[word] = 1
#    else:
        word_dict.setdefault(word, 0)
        word_dict[word]+=1
print(word_dict)

for key,value in word_dict.items():
    print key,value

words = sentence.split()
word_count = Counter(words)
print 'Peter : ' , word_count['Peter']
print word_count
