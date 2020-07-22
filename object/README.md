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