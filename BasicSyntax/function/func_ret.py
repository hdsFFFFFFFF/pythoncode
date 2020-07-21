#!/usr/bin/env python
# coding=utf-8

def sum(arg1, arg2):
    total = arg1 + arg2
    print '函数内', total
    
    #python中没有null，而是None。
    #python中None的含义和其他语言中null是一样的。
    return #不带参数值的return语句返回none

ret = sum(10, 20)

if not ret:
    print 'return null'
