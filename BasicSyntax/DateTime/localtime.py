#!/usr/bin/env python
# coding=utf-8

import time 

#localtime = time.localtime(time.time())
localtime = time.asctime(time.localtime(time.time()))

print '本地时间为：', localtime

while True:
    time.sleep(1)
    print time.strftime('%H:%M:%S', time.localtime())
