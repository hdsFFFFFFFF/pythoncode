### python内置函数

#### `staticmethod()`函数

1. @符号

   **@**符号用作**函数的修饰符**，可以在**模块或者类的定义层内**对函数进行修饰，出现在函数定义的前一行。

   一个修饰符就是一个函数，它将**被修饰的函数作为参数**，并返回修饰后的同名函数或其他可调用的东西(如果返回不是一个可调用的对象那么会报错)。

2. `staticmethod()`

   `staticmethod`返回函数的静态方法。该方法不强制要求传递参数，如下声明一个静态方法：

   ```python
   class C(object):
       @staticmethod
       def f(arg1, arg2, ...):
           ...
   ```

   以上实例声明了静态方法f，从而可以实现实例化使用`C().f()`，当让也可以不实例化调用该方法`C.f()`。

   实例：

   ```python
   #!/usr/bin/env python
   # coding=utf-8
   
   class C(object):
       @staticmethod
       def f():
           print('runoob')
           
   C.f()	#静态方法无需实例化
   
   cobj = C()
   cobj.f()	#也可以实例化后调用
   ```

   以上实例输出结果为

   ```python
   runoob
   runoob
   ```

   

#### int()

**用法**：`int(x, base =10)`

- x表示字符串或数字。
- base表示x的进制数，默认是十进制。

**作用**：把一个字符串或数字转换为一个十进制的数。

int()有两个需要注意的地方：

1. int(12)

   int()中如果是纯数字，则不能带参数base，否则编译报错。

2. int('12', 16)

   16指12是一个十六进制数。因为带了base参数，所以12要以字符串的形式输入。



#### float()

**syntax**:float([x])

**arguments**:

- x：整数或字符串

**return**：返回一个浮点数

实例：

```python
>>>float(1)
1.0
>>> float(112)
112.0
>>> float(-123.6)
-123.6
>>> float('123')     # 字符串
123.0
```



#### split()

**syntax**：`str.split(str = ' ', num = string.count(str))`

**arguments**:

1. str：分隔符，默认为所有的空字符，包括空格，换行(\n)，制表符(\t)等。
2. num：分隔次数，默认为-1，即分隔所有。

**return**:

返回分割后的字符串列表。