#!/usr/bin/env python
# coding=utf-8

def sum(arg1, arg2):
    total = arg1 + arg2
    print '函数内', total
    return #不带参数值的return语句返回none

ret = sum(10, 20)

if not ret:
    print 'return null'
