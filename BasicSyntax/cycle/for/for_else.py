#!/usr/bin/env python
# coding=utf-8

print range(10, 20)

for num in range(10, 20):   #num在for循环中定义
    #print num
    for i in range(3, num):
        #print i
        if num % i == 0:    #内层循环体
            j = num / i
            print '%d等于%d * %d' % (num, i, j)
            break
    else:   #外层循环体
        print num, '是一个质数'
