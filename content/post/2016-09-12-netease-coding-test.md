---
title: 记网易笔试两道编程题
author: 咩
type: post
date: 2016-09-12T14:28:47+00:00
url: /2016/09/12/netease-coding-test/
post_views_count:
  - "81"
flashPic:
  - .
flag:
  - .
categories:
  - Python
tags:
  - python

---
第一道是给你一个圆半径的平方，然后问你x,y坐标均为整数(可正负)的点落在圆上的个数:

```python
  1 # coding:utf-8
  2 
  3 import sys
  4 import math
  5 
  6 for line in sys.stdin:
  7     a = line.split()
  8     R = int(a[0])
  9 
 10 r = math.sqrt(R)
 11 # 考虑圆周不落在整点上
 12 if int(r) != r:
 13     r += 1
 14 
 15 count = 0
 16 for x in xrange(int(r)):
 17     # 求横坐标
 18     y = math.sqrt(R - x*x)
 19     if int(y) == y:
 20         count += 1
 21 # 四个象限
 22 count = 4 * count
 23 
 24 print "%d" % count
```

第二道是给你一个N正整数，求1,2,3&#8230;N 的各项最大奇约数的和，考试的时候脑子笨没转过弯来运行超时了，刚才又改了一下，然后又去[牛客][1]讨论了一下，得出第二段代码，应该不超时了:

```python
#第一段代码：
  1 # coding:utf-8
  2 
  3 import sys
  4 import math
  5 
  6 for line in sys.stdin:
  7     a = line.split()
  8     N = int(a[0])
  9 S = []
 10 
 11 for n in xrange(1,N+1):
 12     i = math.log(n,2)
 13     while i &gt;= 0:
 14         #奇数直接加
 15         if n % 2 == 1:
 16             S.append(n)
 17             break
 18         else: 
 19             n = n / 2
 20         i = i - 1
 21 print "%d" % sum(S)
```

```python
# 第二段代码:
  1 # conding:utf-8
  2 
  3 import sys
  4 for line in sys.stdin:
  5     a = line.split()
  6     N = int(a[0])
  7 S = []
  8 
  9 # 直到N为1
 10 while  N &gt;= 1:
 11     #N为偶数时,抽取列中奇数项求和,自除二
 12     if N % 2 == 0:
 13         s = (N * N/2) / 2
 14         S.append(s)
 15         N = N / 2
 16     else:
 17         #N为奇数时,抽取列中奇求和,列中最大偶数除二
 18         s = (1+N) * (N+1)/2 / 2
 19         S.append(s)
 20         N = (N-1) / 2
 21 
 22 print "%d" % sum(S)
```

 [1]: http://www.nowcoder.com/discuss/9620?toCommentId=227350