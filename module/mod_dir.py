#!/usr/bin/env python
# coding=utf-8

#dir()函数返回一个排好序的字符串列表，内容是一个模块里定义过的名字。
#返回的列表容纳了一个模块里定义的所有模块，变量和函数。
import bcc

content = dir(bcc)

print content

#运行结果
# ['ArgString', 'BPF', 'DEBUG_BPF', 
#  'DEBUG_BPF_REGISTER_STATE', 'DEBUG_BTF', 
#  'DEBUG_LLVM_IR', 'DEBUG_PREPROCESSOR', 
#  'DEBUG_SOURCE', 'Perf', 'PerfEventArray', 
#  'PerfHWConfig', 'PerfSWConfig', 'PerfType', 
#  'SymbolCache', 'TRACEFS', 'Table', 'USDT', 
#  'USDTException', '_SYM_CB_TYPE', '__builtins__', 
#  '__doc__', '__file__', '__name__', '__package__', 
#  '__path__', '__version__', '_assert_is_bytes', 
#  '_get_num_open_probes', '_num_open_probes', 
#  '_probe_limit', 'atexit', 'bcc_stacktrace_build_id', 
#  'bcc_symbol', 'bcc_symbol_option', 'ct', 'decode_map', 
#  'disassemble_prog', 'disassembler', 'errno', 'fcntl', 
#  'get_online_cpus', 'json', 'lib', 'libbcc', 'os', 'perf', 
#  'print_function', 'printb', 're', 'struct', 'sys', 'table',
#  'usdt', 'utils', 'version']
#
#在这里，特殊字符串变量__name__指向模块的名字，__file__指向该
#模块的导入文件名。
