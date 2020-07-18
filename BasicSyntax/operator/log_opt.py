#!/usr/bin/env python
# coding=utf-8

#逻辑运算符：与，或，非
# and:逻辑与。x and y。会短路运算
# or :逻辑或。x or y。会短路运算
# not:逻辑非。not x

a = 10
b = 20
c = 0

if a and b:
    print '1 a和b的值都为true'
else:
    print '1 a和b有一个不为true'

if a or b:
    print '2 a和b都为true，或者其中一个位true'
else:
    print '2 a,b都不为true'

if a and c:
    print 'a && c = 1'
else:
    print 'a && c = 0'

if a or c:
    print 'a || c = 1'
else:
    print 'a || c = 0'

if not c:
    print '!c = 1'
else:
    print '!c = 0'
