#!/usr/bin/python
#coding:utf-8

#https://leetcode.com/problems/number-of-digit-one/description/

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        if n < 1:
            return 0
        # dict = {}
        for i in range(1,n+1):
            numberStr = str(i)  #类型转换
            postion = 0
            iCnt = 0
            while postion >= 0:
                postion = numberStr.find('1',postion) #字符串查找
                if(postion >=0):
                    postion +=1
                    print numberStr,postion
                    iCnt += 1
            if iCnt > 0 :
                result += iCnt
        return result

number = int(raw_input('输入一个int类型的数：'))
solution = Solution()
cnt = solution.countDigitOne(number)
print cnt

