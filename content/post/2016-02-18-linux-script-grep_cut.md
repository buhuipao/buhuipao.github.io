---
title: 'Linux重要命令之—grep&&cut'
author: 咩
type: post
date: 2016-02-18T13:21:17+00:00
url: /2016/02/18/linux-script-grep_cut/
post_views_count:
  - "41"
flag:
  - .
flashPic:
  - .
categories:
  - Shell
tags:
  - grep
  - Linux
  - shell

---
grep 的基本用法，找出字符串所在行：

```bash
[buhuipao@localhost ~]$ echo -e "this is a word \n next line." | grep word
this is a word
```

<span id="transmark"></span>
  
找到字符串所在行，-i 忽略大小写，-n 打印为行号，&#8211;color=auto 颜色标记：

```bash
[buhuipao@localhost ~]$ grep -i -n drupal drupal7/install.php  --color=auto
5: * Initiates a browser-based installation of Drupal.
9: * Defines the root directory of the Drupal installation.
11:define('DRUPAL_ROOT', getcwd());
20:  print 'Your PHP installation is too old. Drupal requires at least PHP 5.2.4. See the &lt;a href="http://drupal.org/requirements"&gt;system requirements&lt;/a&gt; page for more information.';
25:require_once DRUPAL_ROOT . '/includes/install.core.inc';
26:install_drupal();
```

使用正则表达式：

```bash
[buhuipao@localhost ~]$ grep -E "[a-z]+" script/Readme.txt  #使用-E， 利用正则表达式，找出所有小写字符
Here some useful scripts ,you can use it for free!
```

还可以用egrep：

```bash
[buhuipao@localhost ~]$ egrep  "[a-z]+" script/Readme.txt
Here some useful scripts ,you can use it for free!
```

-o 只输出匹配字符串：

```bash
[buhuipao@localhost ~]$ grep -o useful script/Readme.txt 
useful
```

-v 将匹配的结果反转：

```bash
[buhuipao@localhost ~]$ cat test.txt 
NO.1 first line
NO.2 second line 
NO.3 last line
[buhuipao@localhost ~]$ grep -v NO.2 test.txt 
NO.1 first line
NO.3 last line
```

* * *

cut基本用法：

```bash
[buhuipao@localhost 4]$ cat test.data 
NO  name    Mark     Percent 
1   hewen   88   90
2    huazai 34   90
3   cengbu  44   98 
4    pipi   83      78
[buhuipao@localhost 4]$ cut -f 2,4 test.data 
name     Percent 
hewen    90
 huazai  90
cengbu   98 
 pipi   78
 ```

-d 自定义分割符：

```bash
[buhuipao@localhost 4]$ cat test1.data 
NO ;Name ;Mark ; Percent 
1  ;hewen ;88 ; 90
2; huazai;34 ; 90
3 ;cengbu ;44 ; 98 
4; pipi;83  ;78
[buhuipao@localhost 4]$ cut -f 3 -d";" test1.data 
Mark 
88 
34 
44 
83
```

切割一段字符：

```bash
[buhuipao@localhost 4]$ cat test2.data  
fdsfasffdasdsafadsf
fdasfsafdsafdsafdf 
klkliofikfkffklfff
2943040344043444dd
[buhuipao@localhost 4]$ cut -c 1-5 test2.data 
fdsfa
fdasf
klkli
29430
```

cut 补充：

```bash
cut -c -5 test2.data    #切割每一行第一个到第五个字符
cut -c 5- test2.data     #切割每一行第五个到最后一个字符
cut -c1-3,8-11 test2.data --output-delimiter ";"    #切割两段字符串，并且用；隔开
```