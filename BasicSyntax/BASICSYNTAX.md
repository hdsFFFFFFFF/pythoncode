### python基础

#### 标识符

1. 由字母，数字，和下划线组成。不能以数字开头。
2. 不能以数字开头
3. 标识符区分大小写
4. 下划线开头的标识符有特殊意义：
   - 单下划线开头`_foo`代表不能直接访问的类属性，需要通过类提供的接口进行访问，不能用`from xxx import *`导入
   - 双下划线开头的`_ _foo`代表类的私有成员
   - 以双下划线开头和结尾的`_ _ foo _ _`代表Python里特殊方法专用的标识，如`_ _ init _ _()`代表类的构造函数



#### 多行语句

```python
total = item_one +	\
			  item_two +	\
			  item_three
```

语句中有[]，{}或[]括号就不需要使用续行符		 

```python
 days = ['Monday', 'Tuesday', 'Wednesday',
		  		'Thursday', 'Friday']
```



#### python引号：

1. 可以使用单引号('),双引号("),三引号(''')表示字符串

2. 三引号(''')可以由多行组成		 

   ```python
    text = '''
   			first  line
   			second line
   			third  line
   		  '''
   ```

3. 多行注释：使用三个单引号(''')或者三个双引号(""")
   		

   ```python
     textA = '''
   			first  line
   			second line
   		  '''
   ```

   ```python
     testB = """
   	  	first  line
   		second line
   	  """
   ```



#### 代码块(组)：

1. 缩进相同的一组语句构成一个代码块
2. 像`while`,`if`,`def`,`class`这样的复合语句，首行以关键字开始以冒号(:)结束，该行之后的一行或多行代码构成代码组。
3. 将首行及后面的代码组称为一个子句(clause)



#### python命令行参数

1. getopt模块

   - python提供getopt模块来获取命令行参数			

     ```shell
     $ python test.py arg1 arg2 arg3
     ```

   - python也可以使用sys的sys.argv来获取命令行参数：

     - [x] sys.argv是命令行参数列表
     - [x] len(sys.argv)是命令行参数个数
     - [x] sys.argv[0]表示脚本名



#### python导入

1. `from import` 和 `import` 的区别：

   - 例子1：support.py模块

     ```python
     def print_func(par):
         print "hello:", par
         return
     ```

     使用 import 引入并调用 support 模块内函数的正确方法：

     ```python
     #!/usr/bin/env python
     #	coding=utf-8
     
     #导入模块
     import support
     
     #现在可以调用模块里的函数了
     support.print_func("Runoob")
     ```

     因为print_func( )是support里的函数，如果没有导入support模块，不能直接使用print_func( )实现调用，必须将引入的模块名称当作一个对象，调用这个模块对象下的方法print_func( )，才能实现调用。

     

     使用 from import 引入并调用 support 模块内函数的正确方法：

     ```python
     #!/usr/bin/env python
     #	coding=utf-8
     
     #导入模块内的所有函数
     from support import *
     
     #现在可以调用模块里包含的函数了
     print_func("Runboo")
     ```

     from import的方式因为导入了support模块内的所有函数，所以可以直接调用模块内的函数，不需要再引用模块名。

   - 总结：

     import 模块：导入一个模块。相当于导入的是一个文件夹，是个相对路径

     from import 模块：导入一个模块中的一个函数，相当于导入的是一个文件夹，是个绝对路径。

     ```python
     import		//模块.函数
     from … import		//直接使用函数名就可以
     ```

     **import 与 from import 的区别在于：**

     - [x] import 导入模块，每次使用模块中的函数都要确定是哪个模块
     - [x] from import 导入模块，每次使用模块中的函数，直接使用函数名就可以了

   - 例子2

     ```python
     import datetime
     print(datetime.datetime.now())
     ```

     是引入整个datetime包

     ```python
     from datetime import datetime
     print(datetime.now())
     ```

     是只引入datetime包里的datetime类。

     所以前者(imjport)是datetime这个包可见，后者(from import)是datetime.datetime这个类可见。



#### 标准数据类型

python有5个标准的数据类型

1. Numbers(数字)

   python支持4种不同的数字类型

   - int (有符号整型) `10`
   - long (长整型，也可以代表八进制和十六进制) `5192436L` ,python 2.x中
   - float (浮点型) `15.20`
   - complex (复数)  `3.14J`

2. String(字符串)

3. List(列表)

4. Tuple(元组)

5. Dictionary(字典)



#### python字符串

python的字符串列表有2种取值顺序：

- 从左到右索引默认从0开始的，最大范围是字符串长度减少1
- 从右到左的索引是从-1开始的，最大范围是字符串开头。-1表示倒数第一个。
- 下标为空表示从头取到尾

![python-string-slice](/img/python-string-slice.png)

使用`[头下标:尾下标]`来从字符串中截取一段字符串。获取的字符串包含头下标的字符，但不包含尾下标的字符。比如：

```python
>>> s = 'abcdef'
>>> s[1:5]
'bcde'
>>> s[-5:-1]
'bcde'
```

![o99aU](/img/o99aU.png)

python列表截取可以接收第3个参数，参数的作用是截取的步长。[1:4:2]表示在索引1到索引4的位置间，设置步长为2(间隔一个位置)来截取字符串。

![python_list_slice_2](/img/python_list_slice_2.png)



#### python列表

list(列表)是python中最频繁的数据类型。

1. 列表用`[ ]`标识，是python中最通用的复合数据类型
2. 列表可以完成大多数集合类的数据结构的实现
3. 支持字符，数字，字符串，也可以包含列表(即嵌套)

![list_slicing1](/img/list_slicing1.png)

#### python元组

元组是另一个数据类型，类似于List(列表)。

1. 元组用`( )`标识，内部数据元素用逗号隔开。
2. 元组不能二次赋值，相当于只读列表



#### python字典

字典(dictionary)是除列表以外python中最灵活的内置数据结构类型。

1. 字典用"{ }"标识。字典由索引(key)和它对应的值value组成
2. 列表是有序的对象集合，字典是无序的对象的集合
3. 两者之间的区别在于：字典当中的元素是通过键值来存取的，而不是通过偏移存取



#### python数据类型转换

有时候，我们需要对内置的数据类型进行转换。python数据类型的转换，只需要将数据类型作为函数名即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

| 函数                 | 描述                                                 |
| -------------------- | ---------------------------------------------------- |
| int(x[,base])        | 将x转换为一个整数                                    |
| long(x[,base])       | 将x转换为一个长整数                                  |
| float(x)             | 将x转换为一个浮点数                                  |
| complex(real[,imag]) | 创建一个复数                                         |
| str(x)               | 将对象x转换为字符串                                  |
| repr(x)              | 将对象x转换为表达式字符串                            |
| eval(str)            | 用来计算在字符串中的有效python表达式，并返回一个对象 |
| tuple(s)             | 将序列s转换为一个元组                                |
| list(s)              | 将序列s转换为一个列表                                |
| set(s)               | 转换为可变集合                                       |
| dict(d)              | 创建一个字典。d必须是一个序列(key, value)元组        |
| frozenset(s)         | 转换为不可变集合                                     |
| chr(x)               | 将一个整数转换为一个字符                             |
| unichr(x)            | 将一个整数转换为一个Unicode字符                      |
| ord(x)               | 将一个字符转换为它的整数值                           |
| hex(x)               | 将一个整数转换为一个十六进制字符串                   |
| oct(x)               | 将一个整数转换为一个八进制字符串                     |



#### 参数传递

在python中，类型属于对象，变量是没有类型的：

```python
a = [1, 2, 3]
a = "Runoob"
```

以上的代码中，[1,2,3]是list类型，"`Runoob`"是string类型，而变量a是没有类型，它仅仅是一个对象的引用(一个指针)，可以指向list类型对象，也可以指向string类型对象。

##### 可更改(mutable)与不可更改(immutable)对象

在python中，string, tuple和number是不可更改的对象，而list, `dict`是可以修改的对象

- **不可变类型**：变量赋值a=5后在赋值a=10，这里实际是新生成一个int值的对象10，再让a指向它，而5被丢弃，不是改变a的值，相当于重新生成了a。
- **可变类型**：变量赋值a=[1，2，3，4]后再赋值a[2]=5，则是将list a的第三个元素值更改，本身a没有动，只是其内部的一部分值被修改了。

实例：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def ChangeInt( a ):
    a = 10
 
b = 2
ChangeInt(b)
print b # 结果是 2
```

实例中int对象是2，指向它的变量是b。在传递给`ChangeInt`函数时，按传值的方式复制了变量b，a和b都指向了同一个int对象。然后a=10，新生成一个Int值对象10，并让a指向它。



#### python的`bytes`类型和`unicode`类型

`python3`最重要的特性之一是对字符串和二进制数据流做了明确的区分。文本总是`unicode`，由string类型表示，二进制数据则由`bytes`类型表示。

- 编码是什么？

  编码就是把一个`字符`用一个`二进制数`来`表示`。

- ASCII编码

  最早的字符编码规范是ASCII码。**ASCII编码规定用1个字节即8个bit代表一个字符**(实际只使用了7位，最高位没有用到)。ASCII码8个bit位，最多能表示2^8个(256)个字符。

- `unicode`万国码

  随着计算机得到普及，中文，日文，韩文等等国家的文字需要在计算机内表示，ASCII码的256远远不够，于是标准组织制定出了叫做`unicode`的万国码。**`unicode`规定任何一个字符(不管哪国)至少以2个字节表示，可以更多**。其中，**英文字母**就是用**2个字节**，而汉字是3个字节。

  这个编码虽然很好，满足了所有人的要求，但是它不兼容ASCII，同时还占用较多的空间和内存。因为，在计算机世界更多的字符是英文字母，明明可以1个字节就能够表示，非要用2个。于是，`UTF-8`编码应用而生。

- `UTF-8`

  **`UTF-8`规定英文字母系列用1个字节表示，汉字用3个字节表示**等等。因此它兼容ASCII，可以解码早期的文档。`UTF-8`很快就得到了广泛的应用，现在大部分都是`utf-8`。

> 在编码的发展历程中，我国还创造了自己的编码方式，例如`GBK`，`GB2312`，`BIG5`。它们只局限于在国内使用，不被国外认可。在`GBK`编码中，中文汉字占2个字节。



**bytes和string之间的异同**

- `bytes`是一种比特流，它的存在形式是`01010001110`这种。

字符串类`str`里有一个`encode()`方法，它是从字符串向比特流的编码过程。而`bytes`类型恰好有个`decode()`方法，它是从比特流向字符串解码的过程。

1. 在将字符串存入磁盘和从磁盘读取字符串的过程中，python自动地帮你完成了编码和解码的工作，你不需要关心它的过程。
2. 使用bytes类型，实质上是告诉python，不需要它帮你自动地完成编码和解码的工作，而是用户自己手动进行，并指定编码格式。
3. `python3`已经严格区分了`bytes`和`str`两种数据类型，你不能在需要bytes类型参数的时候使用`str`参数，反之亦然。这点在读写磁盘文件时容易碰到。



**`python2`和`python3`中的`str`类型**

`python2`将`str`类型处理为原生的`bytes`类型，而不是`unicode`。

`python3`所有的`str`类型均是`unicode`类型。

- `python2`

  ```python
  >>> s='中文'
  >>> s
  '\xe4\xb8\xad\xe6\x96\x87'	#\x代表是十六进制
  >>> type(s)
  <type 'str'>
  ```

- `python3`

  ```python
  >>> s='中文'
  >>> s
  '中文'
  >>> b=bytes(s,encoding='utf-8')
  >>> b
  b'\xe4\xb8\xad\xe6\x96\x87'	
  >>> type(b)
  <class 'bytes'>
  ```

在`bytes`和`str`的相互转换过程中，实际就是编码和解码的过程，必须显示地指定编码格式。

```python
>>> b
b'\xe4\xb8\xad\xe6\x96\x87'
>>> type(b)
<class 'bytes'>
>>> s1 = str(b)
>>> s1
"b'\\xe4\\xb8\\xad\\xe6\\x96\\x87'"   #解码时没有指定编码格式，变成这样子的串了。
>>> type(s1)
<class 'str'>
>>> s1 = str(b, encoding='utf-8')   #这样是对的，解码时显示地指定编码格式。
>>> s1
'中文'
>>> type(s1)
<class 'str'>
```



**总结**

1. 从`str`到`bytes`是编码，`比特流 = bytes(串，encoding='utf-8')`

   ```python
   >>> a='中文'
   >>> type(a)
   <class 'str'>
   
   #对字符串'中文'进行编码
   >>> b=bytes(a,encoding='utf-8')
   >>> b
   b'\xe4\xb8\xad\xe6\x96\x87'
   >>> type(b)
   <class 'bytes'>
   ```

2. 从`bytes`到`str`，是解码，`串=str(比特流，encoding='utf-8')`

   ```python
   >>> c=str(b,encoding='utf-8')
   >>> c
   '中文'
   >>> type(c)
   <class 'str'>
   ```



`bytes`类型在`pyton2`和`python3`中的表示

- `python2`

  ```python
  >>> s='中文'
  >>> s
  '\xe4\xb8\xad\xe6\x96\x87'		#python2中不需要b前缀
  ```

- `python3`

  ```python
  >>> s='中文'
  >>> s
  '中文'
  >>> b=bytes(s,encoding='utf-8')
  >>> b
  b'\xe4\xb8\xad\xe6\x96\x87'		#python3中需要b前缀标识这是字节流类型
  ```

  





