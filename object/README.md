### python面向对象

Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。

如果你以前没有接触过面向对象的编程语言，那你可能需要先了解一些面向对象语言的一些基本特征，在头脑里头形成一个基本的面向对象的概念，这样有助于你更容易的学习Python的面向对象编程。

接下来我们先来简单的了解下面向对象的一些基本特征。

#### 面向对象技术简介

- 类(class)：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象就是类的实例。
- 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- 数据成员：类变量或者实例变量，用于处理类及其实例对象的相关的数据。
- 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖(override)，也称为方法的重写。
- 局部变量：定义在方法中的变量，只作用于当前实例的类。
- 实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
- 继承：即一个派生类(derived class)继承基类(base class)的字段和方法。继承也允许把一个派生类对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个(is - a)"关系(例如，Dog是一个Animal)。
- 实例化：创建一个类的实例，类的具体对象。
- 方法：类中定义的函数。
- 对象：通过类定义的数据结构实例。对象包括两个数据成员(类变量和实例变量)和方法。

> 一些函数概念：
>
> - 构造函数：相当于初始化一个对象
> - 析构函数：相当于删除一个对象



#### 创建类

使用class语句来创建一个新类，class之后为类的名称并以冒号结尾：

```python
class ClassName:
    '类的帮助信息'	#类文档字符
    class_suite #类体
```

类的帮助信息可以通过`ClassName._ _doc _ _` 查看

class_suite由类成员，方法，数据属性组成。



#### 实例

以下是一个简单的python类的例子：

```python
#!/usr/bin/env python
# coding=utf-8

class Employee:
    '所有员工的基类'
    empCount = 0	#类变量
    
    def __init__(self, name, salary):	#构造函数
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print 'Total Employee %d' % Employee.empCount
        
    def displayEmployee(self):
        print 'Name:', self.name. 'Salary:', self.salary   
    
```

- `empCount`变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用`Employee.empCount`访问。
- 第一种方法`_ _ init _ _()`方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法。
- self代表类的实例，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。



#### self代表类的实例，而非类

类的方法与普通函数只有一个特别的区别——它们必须有一个额外的第一个参数名称，按照**惯例**它的名称是**self**。

```python
class Test:
    '这是Test类的帮助信息'
    def prt(self):
        print(self)
        print(self.__class__)
        
t = Test()
t.prt()
```

以上实例执行结果为：

```python
<__main__.Test instance at 0x10d066878>
__main__.Test
```

从执行结果可以明显的看出，self代表的是类的实例，代表当前对象的地址，而`self._ _ class _ _`则指向类。



#### 创建实例对象

实例化类在其他编程语言中一般用关键字new，但是在python中并没有这个关键字，类的实例化类似函数调用方式。

以下使用类的名称Employee来实例化，并通过`_ _ init _ _`方法接收参数。

```python
'创建Employee类的第一个对象'
emp1 = Employee('Zara', 2000)

'创建Employee类的第二个参数'
emp2 = Employee('Manni', 5000)
```



#### 访问属性

您可以使用`.`来访问对象的属性。使用如下类的名称访问类变量：

```python
emp1.displayEmployee()
emp2.displayEmployee()
print 'Total Employee %d' % Employee.empCount
```



#### python对象销毁(垃圾回收)

python使用了引用计数这一简单技术来跟踪和回收垃圾。在python内部记录着所有使用中的对象各有多少引用。一个内部跟踪变量，称为一个引用技术器。当对象被创建时，就创建了一个引用计数，当这个对象不再需要时，也就是说，这个对象的引用计数变为0时，它被垃圾回收。但是回收不是立即的，由解释器在适当的时机，将垃圾对象占用的内存空间回收。

```python
a = 40     # 创建对象  <40>
b = a       # 增加引用， <40> 的计数
c = [b]     # 增加引用.  <40> 的计数

del a          # 减少引用 <40> 的计数
b = 100     # 减少引用 <40> 的计数
c[0] = -1   # 减少引用 <40> 的计数
```



#### 类的继承

面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。通过继承创建的新类称为**子类**或**派生类**，被继承的类称为**基类**，**父类**或**超类**。

继承语法

```python
class 派生类名(基类名):
    ...
```

也可以继承多各类：

```python
class A:        # 定义类 A
.....

class B:         # 定义类 B
.....

class C(A, B):   # 继承类 A 和 B
.....
```



#### 方法重写

如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：

```python
#!/usr/bin/env python
# coding=utf-8

class Parent:
    def myMethod(self):
        print '调用父类方法'
        
class Child(Parent):
    def myMethod(self):	#子类重写父类的方法
        print '调用子类方法'
        
c = Child()
c.myMethod()	#子类调用重写方法
```

执行以上代码输出结果如下：

```python
调用子类方法
```



#### 类属性与方法

- **类的私有属性**

  `_ _ private_attrs`：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时用`self._ _ private_attrs`。

- **类的方法**

  在类的内部，使用`def`关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数`self`，且为第一个参数。

- **类的私有方法**

  `_ _ private_method`：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用方式为`self._ _ private_methods`。

python不允许实例化的类访问私有数据，但你可以使用`object._ className _ _ attrName`

(对象名._类名 _ _ 私有属性名)访问属性，参考以下实例;

```python
#!/usr/bin/env python
# coding = utf-8

class Hacker:
    __name = 'hds'
    
people = Hacker()
print people._Hacker__name
```

执行以上代码，结果如下：

```python
hds
```





#### 单下划线，双下划线，头尾双下划线说明

- `_ _ foo _ _`：定义的是特殊方法，一般是**系统定义名字**，类似`_ _ init _ _()`之类的。
- `_ foo`：以单下划线开头的表示的是`protected`类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于`from module import *`。
- `_ _ foo`：双下划线表示的是私有类型(private)的变量，只能是允许这个类本身进行访问。