---
title: Python—-str,list,dict,set,tuple的互相转换和操作
author: 咩
type: post
date: 2016-07-29T08:08:45+00:00
url: /2016/07/29/python-str-list-dict-set-tuple/
post_views_count:
  - "119"
flashPic:
  - .
flag:
  - .
categories:
  - Python
tags:
  - python

---
Python的字符操作很常用，应此需要熟记于心；
  
将str转换为list以及list转化为str：

```python
>&gt;&gt;s='abcdef'
>&gt;&gt;l=list(s)
>&gt;&gt;l
>&gt;&gt;['a', 'b','c','d','e','f']
>&gt;&gt;''.join(l)
>&gt;&gt;'abcdef'
```