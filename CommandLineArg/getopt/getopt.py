#!/usr/bin/env python
# coding=utf-8

#getopt.getopt方法的语法格式：
#   getopt.getopt(args, options[,long_options])

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts.args = getopt.getopt(argv, "hi:o:", ["ifile =", "ofile "])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ()
