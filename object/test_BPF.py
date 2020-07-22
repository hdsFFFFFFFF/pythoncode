#!/usr/bin/env python
# coding=utf-8

from bcc import BPF

#b代表的是当前类的实例，代表当前对象的地址。
b = BPF(text = '''
        int kprobe__sys_clone(void *ctx) {
            bpf_trace_printk("hello\\n");

        return 0;
        }
        ''')
print b
print b.__doc__     #查看类的帮助信息
print b.__class__   #查看对象所属的类
print BPF.__name__
print b.__module__
print b.__dict__

#运行结果
#   <bcc.BPF object at 0x7f18b8e6b350>
#   None
#   <class 'bcc.BPF'>
