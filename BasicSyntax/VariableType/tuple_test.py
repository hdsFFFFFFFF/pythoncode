#!/usr/bin/env python
# coding=utf-8

tuple = ('h', 'd', 's', 'love', 'k', 'c', 'm', 1314, '1314')
#tuple2 = (1314)    元组不能这样写，必须写成'1314'。列表可以
tuple2 = ('1314')
tuple3 = ('love', 1314)

print tuple
print tuple[:]
#print tuple(:) #语法错误
print tuple[3:8]
print tuple[5]
print tuple[3] * 2
print tuple2[:]
print tuple + tuple3    #元组相加，每个元组元素至少两个
print tuple[:]
print tuple[3:]
print tuple[:4]
