#!/usr/bin/python
#coding:utf-8

#https://leetcode.com/problems/number-of-digit-one/description/

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0;
        list = []
        for i in range(1,n+1):
            numberStr = str(i)  #类型转换
            hasDigitOne = numberStr.find('1') #字符串查找
            if hasDigitOne >= 0:
                result += 1
                list.append(i)
        print list
        return result

number = int(raw_input('输入一个int类型的数：'))
solution = Solution()
cnt = solution.countDigitOne(number)
print cnt

