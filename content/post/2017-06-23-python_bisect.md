---
title: Python二分查找的一个库–bisect
author: 咩
type: post
date: 2017-06-23T04:52:44+00:00
url: /2017/06/23/python_bisect/
categories:
  - Python
tags:
  - 二分查找

---
今天在刷Leetcode的动态规划LIS题时，在提交页发现了一个返回即将插入列表的元素的下标的库bisect，下面应该是用二分查找做的，库的用法如下：

```python
In [248]: import bisect

In [249]: dir(bisect)
Out[249]: ['bisect', 'bisect_left', 'bisect_right', 'insort', 'insort_left', 'insort_right']

In [250]: a = [2, 4, 6, 9]

In [251]: bisect.insort(a, 5)

In [252]: a
Out[252]: [2, 4, 5, 6, 9]

In [253]: bisect.bisect(a, 3)  # 只试探并不插入，返回下标
Out[253]: 1

In [254]: a
Out[254]: [2, 4, 5, 6, 9]
```

### bisect_left 和 bisect_right 的区别

这两个函数都是返回元素应该插入的位置索引，区别在于遇到重复元素时的处理：

- `bisect_left`：返回重复元素的**左边**位置；
- `bisect_right`（等价于 `bisect`）：返回重复元素的**右边**位置；

```python
In [255]: a = [2, 4, 5, 6, 9]

In [256]: bisect.bisect_left(a, 6)   # 重复项的左边
Out[256]: 3

In [257]: bisect.bisect_right(a, 6)  # 重复项的右边
Out[257]: 4

In [258]: bisect.bisect_left(a, 8)   # 不存在的元素，返回应该插入的位置
Out[258]: 4

In [259]: bisect.bisect_right(a, 8)  # 不存在时两者结果一样
Out[259]: 4
```

### insort_left 和 insort_right 的用法

`insort` 系列函数会真正将元素插入到列表中，保持列表有序：

```python
In [260]: a = [2, 4, 5, 6, 9]

In [261]: bisect.insort_left(a, 8)  # 插入8到合适位置
In [262]: a
Out[262]: [2, 4, 5, 6, 8, 9]

In [263]: bisect.insort_left(a, 8)  # 再插入一个8，放在已有8的左边
In [264]: a
Out[264]: [2, 4, 5, 6, 8, 8, 9]    # 左边的8才是最后插入的

In [265]: bisect.insort_right(a, 8) # 放在已有8的右边
In [266]: a
Out[266]: [2, 4, 5, 6, 8, 8, 8, 9]
```

### 实际应用场景

**1. 维护有序列表**

需要频繁插入元素并保持有序时，`insort` 比先 append 再 sort 更高效：

```python
import bisect

# 维护一个有序的成绩列表
scores = []
for score in [85, 92, 78, 95, 88]:
    bisect.insort(scores, score)
print(scores)  # [78, 85, 88, 92, 95]
```

**2. 查找分数等级**

官方文档里的经典例子，根据分数查找对应等级：

```python
import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """根据分数返回等级"""
    i = bisect.bisect(breakpoints, score)
    return grades[i]

# 测试
print([grade(score) for score in [33, 60, 77, 85, 92, 100]])
# 输出: ['F', 'D', 'C', 'B', 'A', 'A']
```

**3. 在有序列表中查找元素**

利用 bisect 做二分查找，比线性查找快：

```python
import bisect

def binary_search(sorted_list, target):
    """在有序列表中查找target，找到返回索引，否则返回-1"""
    i = bisect.bisect_left(sorted_list, target)
    if i < len(sorted_list) and sorted_list[i] == target:
        return i
    return -1

a = [1, 3, 5, 7, 9, 11]
print(binary_search(a, 7))   # 3
print(binary_search(a, 6))   # -1
```

### 小结

bisect 模块底层用的是二分查找，查找插入位置的时间复杂度为 O(logN)，但实际插入操作（insort）由于涉及列表元素的移动，时间复杂度为 O(N)。在刷题和日常开发中用起来都很方便，尤其适合需要维护有序列表的场景。