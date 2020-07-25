#!/usr/bin/env python
# coding=utf-8

def wrap(f):
    def decorator(*args, **kw):
        print 'Call %s()' % f.__name__
        return f(*args, **kw)
    return decorator

#@符号用作函数修饰符，可以在模块或者类的定义层内对函数进行修饰。
@wrap   #在模块内进行修饰
def func(a, b):
    return a * 10 + b

if __name__ == '__main__':
    print func(1, 2)
