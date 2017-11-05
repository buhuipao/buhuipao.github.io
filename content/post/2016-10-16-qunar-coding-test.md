---
title: 记一道去哪儿的笔试题
author: 咩
type: post
date: 2016-10-16T03:14:58+00:00
url: /2016/10/16/qunar-coding-test/
post_views_count:
  - "152"
flashPic:
  - .
flag:
  - .
categories:
  - Python
tags:
  - python

---
昨天参加了去哪儿的笔试题，给我分的软件开发卷，两道编程和一个系统设计，两道都不没有完全通过，有一道后来知道自己考虑不周，于是打算重新写一边，可能还有漏洞，希望看到的朋友指出。

题目的意思很简单，就是输入一个自然数，然后叫你输出一个大于它的对称数，例如：
  
input:
  
123
  
999
  
1231
  
output:
  
131
  
1001
  
1331

我笔试的代码:

<pre class="lang:python decode:1 " >#!/bin/env python
# coding:utf-8

import sys

Input = []
while True:
    line = sys.stdin.readline()
    if not line:
      break
    Input.extend(line.split())

In = list(str(int(Input[0])+1))

if len(In) == 1:
    print In[0]
else:
    In = map(int, In)
    if len(In) % 2 == 1:
        count = 0
        Mi = len(In) / 2
        for i in xrange(1, Mi+1):
            if In[Mi+i] &gt; In[Mi-i] and count == 0:
                count += 1
                In[Mi+i-1] += 1
                if i != 1:
                    In[Mi-i+1] += 1
                In[Mi+i] = In[Mi-i]
            else:
                count += 1
                In[Mi+i] = In[Mi-i]
    else:
        count = 1
        Mi = len(In) / 2 - 1
        for i in xrange(1, len(In)/2+1):
            if In[Mi+i] &gt; In[Mi-i] and count == 0:
                count += 1
                if i != 1:
                    In[Mi+i-1] += 1
                    In[Mi-i+1] += 1
                    In[Mi+i] = In[Mi-i]
                else:
                    In[Mi-i] = In[Mi+i]
            else:
                count += 1
                In[Mi+i] = In[Mi-i]
    Out = map(str, In)
    print ''.join(Out)
</pre>

改进后的代码:

<pre class="lang:python decode:1 " >1 #!/bin/env python
  2 # coding:utf-8
  3 
  4 import sys
  5 
  6 Input = []
  7 while True:
  8     line = sys.stdin.readline()
  9     if not line:
 10       break
 11     Input.extend(line.split())
 12 
 13 In = list(str(int(Input[0])+1))
 14 if len(In) % 2 == 1:
 15     Mi = len(In) / 2
 16     for i in xrange(1, Mi+1):
 17         if int(In[Mi+i]) &gt; int(In[Mi-i]):
 18             #前半部分的加一(考虑中位是9),逆序拼接
 19             Mi_int = int(''.join(In[:Mi+1])) + 1
 20             In = list(str(Mi_int))
 21             In.extend(In[:-1][::-1])
 22             break
 23         elif In[Mi+i] &lt; In[Mi-i]:
 24             #直接对半拼接
 25             In = In[:Mi+1]
 26             In.extend(In[:-1][::-1])
 27             break
 28 else:
 29     #组成奇数位，方便比较
 30     In.insert(len(In)/2, '#')
 31     Mi = len(In) / 2
 32     for i in xrange(1,Mi+1):
 33         if In[Mi+i] &gt; In[Mi-i]:
 34             Mi_int = int(''.join(In[:Mi])) + 1
 35             In = list(str(Mi_int))
 36             In.extend(In[::-1])
 37             break
 38         else:
 39             In = In[:Mi]
 40             In.extend(In[::-1])
 41             break
 42
 43 print ''.join(In)
</pre>