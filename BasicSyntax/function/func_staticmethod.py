#!/usr/bin/env python
# coding=utf-8

class C(object):
    @staticmethod
    def f():
        print 'hello world'

C.f()   #静态方法无需实例化
b = C()
b.f()   #也可以实例化后调用


