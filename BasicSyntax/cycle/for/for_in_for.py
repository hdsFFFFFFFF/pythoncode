#!/usr/bin/env python
# coding=utf-8

#九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i * j))
    print('')
