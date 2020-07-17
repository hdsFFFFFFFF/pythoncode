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

