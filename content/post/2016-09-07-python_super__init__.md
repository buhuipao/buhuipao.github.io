---
title: 理解Python中super()和__init__()方法
author: 咩
type: post
date: 2016-09-07T07:20:07+00:00
url: /2016/09/07/python_super__init__/
post_views_count:
  - "55"
flashPic:
  - .
flag:
  - .
categories:
  - Python
tags:
  - python

---
在实用多线程编程时，在[栈溢出网站][1]有看到多种方法，比如直接用函数，有用class继承，代码如下：

```python
class Mon(object):
  def __init__(self):
    print "Mon created"

class Child(Base):
  def __init__(self):
    Mon.__init__(self)

...
```

但也有发现另外一种继承的方法：

```python
class Child(Base):
  def __init__(self):
    super(Child, self).__init__()
  ...
```

然后在python3里面，super(Child, self).**init**()被替换为super().**init**()

 [1]: http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods