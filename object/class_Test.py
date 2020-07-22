#!/usr/bin/env python
# coding=utf-8

class Test:
    '这是类的帮助信息'
    def prt(self):
        print(self) #与下面的写法效果相同
        print self  #与上面的写法效果相同
        print self.__doc__  #打印class Test下面那句字符串
        print(self.__class__)

t = Test()
t.prt()
