---
title: Python三目运算符两种写法及exec的用法
author: 咩
type: post
date: 2017-06-23T05:29:44+00:00
url: /2017/06/23/python三目运算符两种写法及exec的用法/
categories:
  - Python
tags:
  - exec
  - 三目运算符

---
三目运算符第一种写法：
```python
In [302]: a = 1 if 5 > 3 else 0

In [303]: a
Out[303]: 1

In [304]: a = 1 if 2 > 3 else 0

In [305]: a
Out[305]: 0
```

三目运算符的第二种写法：

```python
In [295]: [5, 3][True]
Out[295]: 3

In [296]: [5, 3][False]
Out[296]: 5

In [306]: L
Out[306]: True

In [307]: [5, 3][L]
Out[307]: 3

In [308]: L = False

In [309]: [5, 3][L]
Out[309]: 5

In [311]: [5, 3][eval('5 > 3')]
Out[311]: 3

In [312]: [5, 3][eval('0')]
Out[312]: 5
</pre>

需要指出的是：exec可以执行一段python代码(在Flask的源码中看见用的比较多)，但是只有副作用没有返回值；

```python
In [316]: code = """
     ...: def append_five(_list):
     ...:     _list.append(5)
     ...: append_five(A)
     ...: print('Append Five!')
     ...: """
In [320]: exec 'A=[1,2,3]'

In [321]: A
Out[321]: [1, 2, 3]

In [322]: exec code
Append Five!

In [323]: A
Out[323]: [1, 2, 3, 5]
```

假如你需要得到返回值，那么可以使用python里的eval；

```python
In [324]: eval('5 > 3')
Out[324]: True
```

如果你需要执行一个文件，那么直接：

```python
In [327]: !vim test.py

In [328]: pwd
Out[328]: u'/Users/chenhua/Desktop'

In [329]: execfile('/Users/chenhua/Desktop/test.py')
Hello Python

In [330]: !cat test.py
print('Hello Python')
```

还有一个可以编译好执行的complie，compile前两个参数分别为字符串、代码文，后一个参数指制被编译的类型件, 返回code object, 使用如下：

```python
In [336]: help(compile)

Help on built-in function compile in module __builtin__:

compile(...)
    compile(source, filename, mode[, flags[, dont_inherit]]) -> code object

In [338]: exec_code = compile(str,'', 'exec')

In [339]: exec_code
Out[339]: &lt;code object &lt;module> at 0x110dc69b0, file "", line 1>

In [340]: exec exec_code
Hello Python!

In [341]: str
Out[341]: "print('Hello Python!')"
```