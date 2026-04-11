---
title: Python—-str,list,dict,set,tuple的互相转换和操作
author: 咩
type: post
date: 2016-07-29T08:08:45+00:00
url: /2016/07/29/python-str-list-dict-set-tuple/
categories:
  - Python
tags:
  - Python

---
Python的字符操作很常用，应此需要熟记于心，下面整理了 str, list, dict, set, tuple 之间的互相转换和常用操作。

### str 和 list 互转

```python
# str -> list
>>> s = 'abcdef'
>>> l = list(s)
>>> l
['a', 'b', 'c', 'd', 'e', 'f']

# list -> str
>>> ''.join(l)
'abcdef'

# 按分隔符拆分
>>> s2 = 'a,b,c,d'
>>> s2.split(',')
['a', 'b', 'c', 'd']

# 按分隔符合并
>>> ','.join(['a', 'b', 'c'])
'a,b,c'
```

### str 和 int/float 互转

```python
>>> int('123')
123
>>> float('3.14')
3.14
>>> str(123)
'123'
>>> str(3.14)
'3.14'
```

### list 和 tuple 互转

```python
>>> l = [1, 2, 3]
>>> t = tuple(l)   # list -> tuple
>>> t
(1, 2, 3)
>>> list(t)         # tuple -> list
[1, 2, 3]
```

### list 和 set 互转

set 会自动去重：

```python
>>> l = [1, 2, 2, 3, 3, 3]
>>> s = set(l)      # list -> set，去重
>>> s
{1, 2, 3}
>>> list(s)         # set -> list
[1, 2, 3]

# 利用set去重
>>> l = [1, 1, 2, 3, 3]
>>> list(set(l))
[1, 2, 3]
```

### dict 相关转换

```python
# dict的keys和values转list
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> list(d.keys())
['a', 'b', 'c']
>>> list(d.values())
[1, 2, 3]

# dict的items转list（得到元组列表）
>>> list(d.items())
[('a', 1), ('b', 2), ('c', 3)]

# 两个list组合成dict
>>> keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>> dict(zip(keys, values))
{'a': 1, 'b': 2, 'c': 3}

# 元组列表转dict
>>> pairs = [('a', 1), ('b', 2), ('c', 3)]
>>> dict(pairs)
{'a': 1, 'b': 2, 'c': 3}

# dict转json字符串
>>> import json
>>> json.dumps(d)
'{"a": 1, "b": 2, "c": 3}'
>>> json.loads('{"a": 1, "b": 2}')
{'a': 1, 'b': 2}
```

### set 相关操作

```python
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}

# 交集
>>> s1 & s2
{2, 3}

# 并集
>>> s1 | s2
{1, 2, 3, 4}

# 差集
>>> s1 - s2
{1}

# 对称差集（两个集合中不重复的元素）
>>> s1 ^ s2
{1, 4}
```

### tuple 和 dict 的一些技巧

```python
# 用enumerate获取带下标的元组
>>> l = ['a', 'b', 'c']
>>> list(enumerate(l))
[(0, 'a'), (1, 'b'), (2, 'c')]

# 字典推导式
>>> {k: v * 2 for k, v in d.items()}
{'a': 2, 'b': 4, 'c': 6}

# 列表推导式转set
>>> {x ** 2 for x in [1, 2, 2, 3]}
{1, 4, 9}
```

### 汇总表

| 源类型 | 目标类型 | 方法 |
|--------|----------|------|
| str | list | `list(s)` 或 `s.split(sep)` |
| list | str | `''.join(l)` 或 `sep.join(l)` |
| list | tuple | `tuple(l)` |
| tuple | list | `list(t)` |
| list | set | `set(l)` |
| set | list | `list(s)` |
| list+list | dict | `dict(zip(keys, vals))` |
| dict | list | `list(d.keys())` / `list(d.values())` / `list(d.items())` |
| str | dict | `json.loads(s)` |
| dict | str | `json.dumps(d)` |