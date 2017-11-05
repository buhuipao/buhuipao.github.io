---
title: Linux 常用命令–ps，head/tail， less/more
author: 咩
type: post
date: 2016-09-13T05:09:02+00:00
url: /2016/09/13/linux-ps-head-tail-less-more/
post_views_count:
  - "80"
flashPic:
  - .
flag:
  - .
categories:
  - Shell
tags:
  - head
  - IP
  - ps

---
**PS**
  
ps -ef
  
ps aux
  
按所占用的cpu降序(-pcpu)排序，取top10,注意head会把第一列打印出来，所以取11

<pre class="lang:bash decode:1 " >[buhuipao@bogon ~]$ ps -eo user,pid,ppid,pcpu,pmem,comm --sort=-pcpu | head -n 11| tail -n 10
buhuipao 13704 3176 9.2 3.1 netease-cloud-m
buhuipao 8040 3189 3.9 6.8 chrome
buhuipao 31576 8055 3.4 4.5 chrome
buhuipao 13741 13715 3.2 4.1 netease-cloud-m
root 1292 1275 3.1 1.0 Xorg
buhuipao 8110 8040 2.5 4.2 chrome
buhuipao 15087 8055 1.5 3.7 chrome
buhuipao 16130 8055 1.3 4.5 chrome
buhuipao 27911 8055 0.8 5.6 chrome
buhuipao 2511 8055 0.7 6.2 chrome
</pre>

#假如 ps -eo user,pid,ppid,pcpu,pmem,comm &#8211;sort=+pmem,-pcpu | tail -n 10
  
#则按照sort后第一个排序为准

<pre class="lang:bash decode:1 " >buhuipao@bogon ~]$ ps -eo user,pid,ppid,pcpu,pmem,comm --sort=+pmem,-pcpu | tail -n 10
buhuipao 13741 13715 3.1 4.1 netease-cloud-m
buhuipao 16130 8055 0.6 4.4 chrome
buhuipao 31576 8055 3.4 4.5 chrome
buhuipao 8110 8040 2.5 4.8 chrome
buhuipao 8137 8055 0.2 5.1 chrome
buhuipao 27911 8055 0.9 5.5 chrome
buhuipao 8124 8055 0.2 5.9 chrome
buhuipao 2511 8055 0.7 6.3 chrome
buhuipao 15692 8055 0.6 6.5 chrome
buhuipao 8040 3189 3.9 6.8 chrome
</pre>

#ps -efH 可以看到树形层级结构
  
**head/tail**
  
head -n 10 #取前十项
  
tail -n 10 #后十项
  
head -10 #同head -n 10
  
#head,tail命令里默认输出的开始为正，结尾为负
  
head -n +10 #输出第1行到10行
  
head -n -10 #输出第1行到倒数11行，后面留10行

<pre class="lang:bash decode:1 " >[buhuipao@bogon ~]$ cat -n 1.py | head -n -10
     1  # coding:utf-8
     2  
     3  import sys 
     4  import math
     5  
     6  for line in sys.stdin:
     7      a = line.split()
     8      R = int(a[0])
     9  
    10  r = math.sqrt(R)
    11  # 考虑圆周不落在整点上
    12  if int(r) != r:
    13      r += 1
    14  
[buhuipao@bogon ~]$ cat -n 1.py |tail -n 10
    15  count = 0
    16  for x in xrange(int(r)):
    17      # 求横坐标
    18      y = math.sqrt(R - x*x)    
    19      if int(y) == y:
    20          count += 1
    21  # 四个象限
    22  count = 4 * count
    23  
    24  print "%d" % count
</pre>

#tail -n +10 #输出最后1行到第10行
  
#tail -n -10 #输出最后10行

<pre class="lang:bash decode:1 " >[buhuipao@bogon ~]$ cat -n 1.py |tail -n +10
    10  r = math.sqrt(R)
    11  # 考虑圆周不落在整点上
    12  if int(r) != r:
    13      r += 1
    14  
    15  count = 0
    16  for x in xrange(int(r)):
    17      # 求横坐标
    18      y = math.sqrt(R - x*x)    
    19      if int(y) == y:
    20          count += 1
    21  # 四个象限
    22  count = 4 * count
    23  
    24  print "%d" % count
[buhuipao@bogon ~]$ cat -n 1.py |tail -n -10
    15  count = 0
    16  for x in xrange(int(r)):
    17      # 求横坐标
    18      y = math.sqrt(R - x*x)    
    19      if int(y) == y:
    20          count += 1
    21  # 四个象限
    22  count = 4 * count
    23  
    24  print "%d" % count
</pre>