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
In [248]: import bisect In [249]: dir(bisect) Out[249]: ['\_\_builtins\_\_', '\_\_doc\_\_', '\_\_file\_\_', '\_\_name\_\_', '\_\_package\_\_', 'bisect', 'bisect\_left', 'bisect\_right', 'insort', 'insort\_left', 'insort\_right'] In [250]: a = [2, 4, 6, 9] In [251]: bisect.insort(a, 5) In [252]: a Out[252]: [2, 4, 5, 6, 9] In [253]: bisect.bisect(a, 3) # 只试探并不插入，返回下标 Out[253]: 1 In [254]: a Out[254]: [2, 4, 5, 6, 9] In [255]: bisect.bisect\_left(a, 8) # 遇到重复项将尝试插入左边，同理bisect\_right为右边，只返回下标 Out[255]: 4 In [256]: a Out[256]: [2, 4, 5, 6, 9] In [257]: bisect.bisect\_left(a, 6) Out[257]: 3 In [258]: bisect.bisect\_right(a, 6) Out[258]: 4 In [259]: bisect.insort\_left(a, 8) # 遇到重复项将插入左边，同理bisect\_right为右边 In [260]: a Out[260]: [2, 4, 5, 6, 8, 9] In [261]: bisect.insort_left(a, 8) In [262]: a Out[262]: [2, 4, 5, 6, 8, 8, 9] # 左边的8才是最后插入的 
```