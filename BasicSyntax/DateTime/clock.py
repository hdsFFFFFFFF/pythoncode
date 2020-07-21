#!/usr/bin/env python
# coding=utf-8


#clock()函数以浮点数计算的秒数返回当前CPU的时间
import time

clk = time.clock()
print '当前的CPU时间为：', clk

def procedure():
    time.sleep(3)

t0 = time.clock()
procedure()

print time.clock() - t0
