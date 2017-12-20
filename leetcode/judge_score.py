#coding:utf-8

#有10个评委为参赛选手打分，分数0~100.选手最后得分：去掉一个最高和一个最低分后除以8个分数的平均值。
#思路
#1.随机生成n个0~100的分数，放到列表s中
#2、找到最高和最低
#3、累加后减去最高分和最低分，除以 n-2

import random
def averageScore(n):
    s = []
    for i in range(n):
        s.append(random.randint(10,100))
    maxScore = sumScore = 0
    minScore = 100
    for k in s:
        if maxScore < k:
            maxScore = k
        if minScore > k:
            minScore = k
        sumScore += k
    return {'sum':s, 'max':maxScore,'min':minScore,'avg':float(sumScore - maxScore - minScore) / (n -2)}

def avgScore(n):
    s = [random.randint(10,100) for i in range(n)]
    maxScore = max(s)
    minScore = min(s)
    sumScore = sum(s)
    return {'sum': s, 'max': maxScore, 'min': minScore, 'avg': float(sumScore - maxScore - minScore) / (n - 2)}

print(averageScore(10))

print(avgScore(10))

