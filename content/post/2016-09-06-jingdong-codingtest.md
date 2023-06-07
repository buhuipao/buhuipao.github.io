---
title: 记一个京东技术运营的编程题
author: 咩
type: post
date: 2016-09-06T09:50:39+00:00
url: /2016/09/06/jingdong-codingtest/
post_views_count:
  - "47"
flashPic:
  - .
flag:
  - .
categories:
  - Python
tags:
  - HTTPS
  - IP
  - python

---
昨晚参加了京东2016秋招的技术类笔试，无奈自己编程基础不扎实，昨晚一个编程题弄了45来分钟也没完整解决，今天实习比较闲，所以依据记忆终于解决，但不知是否超时。
  
题目是：定义一种数由4，7组成，基本规律为：4，7，44，47，74，77，444，447，&#8230;然后OJ的输入为：

```python
N
k1
k2
..
k(n)
```

第一个N表明要输入多少个数，后面N行就是表示求这个序列里第几个数，例如：

```python
4
5
6
7
10
```

表示一共要输入4个数，然后分别求序列里第5，6，7，10个数，输出要求为：

```python
75
77
444
477
```

然后我经过观察发现这就是个求这个数处在第几个2的n次方的哪个位置，把最后的位置化为二进制，再替换为4，7输出就好了，下面是基于python2.7的代码，有人可能会说思路这么清晰直接用c，只能说c的字符串处理不熟悉很可能越界，所以直接用python。

```python
  0 #coding:utf-8
  1 import sys
  2 import math
  3 
  4 Line = []
  5 while True:
  6     line = sys.stdin.readline()
  7     if not line:
  8         break
  9     Line.extend(line.split()).
 10 count = int(Line[0])
 11 K = []
 12 for i in xrange(1,count+1):
 13     #首先定位到第几个2的n次方
 14     num = math.log(int(Line[i])+2, 2)
 15     #假设整除直接确定是多少个'7'
 16     if num == int(num):
 17         num = int(num) - 1
 18         K.append('7' * num)
 19     #不整除则减去前2的n-1次方的和，再减1(序号从0开始)
 20     else:
 21         num = int(num)
 22         k = int(Line[i]) - (2 ** num - 2) - 1
 23         j = (bin(k)[2:].replace('0', '4').replace('1', '7'))
 24         #位数不足则补0('4')
 25         if len(j) != num:
 26             j = '4' * (num-len(j)) + j
 27         K.append(j)
 28 for k in K:
 29   print("%s" % k)
```

最后记录下京东技术运营的部分附加题，就是叫你写一个脚本取出一个web日志里IP的top10，大概日志格式为：

```bash
45.53.112.237 /app/jd.apk "2016-07-05" "12:13"
```

然后我一时手贱，少写了点东西，写成：

```bash
#!/bin/bash
cat /var/log/nginx/access.log | cut -d -f 1| sort|uniq -c|head -n 10
```

是的没错，写过此类脚本的人都发现了我漏掉了些东西，正确的写法应该是：

```bash
#!/bin/bash
log=$1
awk '{print $1}' $log| sort |uniq -c | sort -nr | head -n 10
```

首先是切割的问题，然后就是uniq之后也不是排好逆序的，还得用sort的-nr参数进行数字逆序排列一下，这个脚本很久前写过放在我[github][1]上，学的东西很久不用等于没学，这是一个教训，对于京东的笔试，只能看自己运气了，实力只有这么多。

 [1]: https://github.com/buhuipao/Script/blob/master/web_count.sh