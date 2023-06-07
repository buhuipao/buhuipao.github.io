---
title: 记一道Google Test
author: 咩
type: post
date: 2016-10-12T10:34:50+00:00
url: /2016/10/12/google-test/
post_views_count:
  - "69"
flashPic:
  - .
flag:
  - .
categories:
  - Python
tags:
  - IP
  - python

---
自己算法太烂太渣，只有慢慢练，一个运维还是得会写代码，看得懂代码。所以最近一边面试一边自己找题目练习。原题是：

### Problem

The Constitution of a certain country states that the leader is the person with the name containing the greatest number of different alphabet letters. (The country uses the uppercase English alphabet from A through Z.) For example, the name GOOGLE has four different alphabet letters: E, G, L, and O. The name APAC CODE JAM　has eight different letters. If the country only consists of these 2 persons, APAC CODE JAM would be the leader.

If there is a tie, the person whose name comes earliest in alphabetical order is the leader.

Given a list of names of the citizens of the country, can you determine who the leader is?

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each test case starts with a line with an interger **N**, the number of people in the country. Then **N** lines follow. The i-th line represents the name of the i-th person. Each name contains at most 20 characters and contains at least one alphabet letter.

### Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the name of the leader.

### Limits

1 ≤ **T** ≤ 100.
  
1 ≤ **N** ≤ 100.

<img class="aligncenter size-full wp-image-935" src="http://www.buhuipao.com/wp-content/uploads/2016/10/Google_test_Leader.png" alt="google_test_leader" width="560" height="281" srcset="http://www.buhuipao.com/wp-content/uploads/2016/10/Google_test_Leader.png 560w, http://www.buhuipao.com/wp-content/uploads/2016/10/Google_test_Leader-150x75.png 150w, http://www.buhuipao.com/wp-content/uploads/2016/10/Google_test_Leader-300x151.png 300w" sizes="(max-width: 560px) 100vw, 560px" />

```python
1 #!/bin/env python
2 # coding:utf-8
3
4 '''
5 import sys
6
7 Input = []
8 while True:
9     line = sys.stdin.readlines()
10    if not line:
11        break
12    Input.extend(line)
13 '''
14 with open('./Input.in', 'r') as f:
15     Input = f.readlines()
16
17 #创建输入字典
18 num = Input.pop(0)
19 Input_dict = {}
20 count = 0
21 for i in xrange(len(Input)):
22 #换行符去掉
23     Input[i] = Input[i][:-1]
24     if Input[i] in map(lambda x: str(x), (x for x in xrange(1,101))):
25         count += 1
26         Input_dict[str(count)] = []
27 else:
28     Input_dict[str(count)].append(Input[i])
29
30 for j in xrange(1,len(Input_dict)+1):
31     max_len = 0
32     for str_i in Input_dict[str(j)]:
33         set_str = set(str_i)
34         #考虑名字有空格，滤去空格
35         if ' ' in set_str:
36              set_str.remove(' ')
37         if len(set_str) &gt; max_len:
38             max_len = len(str_i)
39             max_str = str_i
40         elif len(set_str) == max_len:
41             sorted_str = sorted([max_str, str_i])
42             max_str = sorted_str[0]
43 with open('./Output.in', 'a') as f:
44      f.write("Case #%d: %s\n" % (j, max_str))
```