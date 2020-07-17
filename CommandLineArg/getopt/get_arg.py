#!/usr/bin/env python
# coding=utf-8

#getopt.getopt方法的语法格式：
#   getopt.getopt(args, options[,long_options])
# 该方法的返回值由两个元素构成：
#           第一个是(option, value)元组的列表.
#           第二个是参数列表，包含那些没有-或--的元素

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile =", "ofile "])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            print '输入的文件为：', inputfile
            print '输出的文件为：', outputfile

if __name__ == "__main__":
    main(sys.argv[1:])
