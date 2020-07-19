#!/usr/bin/env python
# coding=utf-8

num = 9
if num >= 0 and num <= 10:
    print 'hello'

num = 10
if num <0 or num > 10:
    print 'hello'
else:
    print 'undefine'

num = 8
#当if有多个条件是可以使用括号来区分判断的先后顺序
# 括号中的判断优先执行
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'
