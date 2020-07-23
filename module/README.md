### python模块

Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。



#### import语句

模块定义好后，我们可以使用 import 语句来引入模块，语法如下：

```python
import module1[, module2[, ...moduleN]]
```

比如要引用模块 math，就可以在文件最开始的地方用 **import math** 来引入。在调用 math 模块中的函数时，必须这样引用：

```python
模块名.函数名
```

当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。

> 一个模块只会被导入一次，不管你执行了多少次import。



#### from ... import语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：

```python
from modname import name1[, name2[, ...nameN]]
```

例如，要导入模块 fib 的 fibonacci 函数，使用如下语句：

```python
from fib import fibonacci
```

这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。



#### from ... import *语句

把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

```python
from modname import *
```

例如我们想一次性引入 math 模块中所有的东西，语句如下：

```python
from math import *
```



#### 搜索路径

当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

1. 当前目录
2. 如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3. 如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。



#### 命名空间和作用域

变量是拥有匹配对象的名字（标识符）。命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。

一个 Python 表达式可以访问局部命名空间和全局命名空间里的变量。如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。

python会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。

因此，如果要给函数内的全局变量赋值，必须使用`global`语句。

global VarName的表达式会告诉python，VarName是一个全局变量，这样python就不会在局部命名空间里寻找这个变量了。

```python
#!/usr/bin/env python
# coding=utf-8

Money = 2000

def AddMoney():
    global Money
    Money = Money + 1
```



#### dir()函数

dir() 函数返回一个排好序的字符串列表，内容是一个模块里定义过的名字。

返回的列表容纳了在一个模块里定义的所有模块，变量和函数。如下一个简单的实例：

```python
#!/usr/bin/env python
# coding=utf-8

# 导入内置math模块
import math
 
content = dir(math)
 
print content
```

以上实例输出结果：

```python
['__doc__', '__file__', '__name__', 'acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log','log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
```

在这里，特殊字符串变量 `_ _ name _ _` 指向模块的名字，`_ _ name _ _` 指向该模块的导入文件名。



#### python中的包

包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 `_ _ init _ _.py`文件, 该文件的内容可以为空。`_ _ init _ _.py` 用于标识当前文件夹是一个包。

> 当时用from package import item时，item可以是package的子模块或子包，或是其他的定义在包中的名字(比如一个函数，类或者变量)。
>
> 
>
> 首先检查item是否定义在包中，如果没找到，就认为item是一个模块并尝试加载它，失败时会抛出一个ImportError异常。

