#!/usr/bin/env python
# coding=utf-8

def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print Argument  #Argument保存输出的异常信息

temp_convert('xyz')
