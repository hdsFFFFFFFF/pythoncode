#!/usr/bin/env python
# coding=utf-8

class JustCounter:
    __secretCount = 0   #私有类变量
    publicCount = 0     #公开变量

    #类的内部
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()

#类的外部
print counter.publicCount
#print counter.__secretCount    #出错，外部不能访问类的私有属性
