---
title: Linux下/etc的hosts,hosts.conf,hostname, resolv.conf,hosts.deny/allow文件解释
author: 咩
type: post
date: 2016-08-16T03:31:21+00:00
url: /2016/08/16/linux-etc-host/
post_views_count:
  - "58"
flashPic:
  - .
flag:
  - .
categories:
  - Linux
tags:
  - host
  - Linux

---
hosts文件： hosts文件的作用相当如DNS，提供IP地址到hostname的对应。
  
说明：
  
早期的互联网计算机少，单机hosts文件里足够存放所有联网计算机。不过随着互联网的发展，这就远远不够了。于是就出现了分布式的DNS系统。由DNS服务器来提供类似的IP地址到域名的对应。Linux系统在向DNS服务器发出域名解析请求之前会查询/etc/hosts文件，如果里面有相应的记录，就会使用hosts里面的记录。
  
127.0.0.1 localhost.localdomain localhost
  
hosts文件格式是一行一条记录，分别是：
  
IP地址 hostname aliases

* * *

hosts.conf: 指定如何解析主机域名。可设置网络安全。默认情况，vim /etc/hosts.conf:
  
order hosts,bind
  
multi on
  
说明：
  
1. order 是解析顺序的参数，order hosts,bind,nis //说明先查询解析/etc/hosts文件，然后DNS，再是NIS
  
2. multi on //表示是否运行/etc/hosts文件允许主机指定多个多个地址 ，on表示运行
  
3. nospoof on //是否允许服务器对ip地址进行其欺骗，这里的on表示不允许
  
4. rccorder //如果被设置为on，那么所有查询将被重新排序。

* * *

hostname: 本机名字，修改后重启生效

* * *

resolv.conf: 指定本机的域名解析服务器(DNS)，一般会是NetWorkManager生成,

1. nameserver //表明DNS服务器的IP地址。可以有很多行的nameserver，每一个带一个IP地址。在查询时就按nameserver在本文件中的顺序进行，且只有当第一个nameserver没有反应时才查询下面的nameserver。
  
2.domain //声明主机的域名。很多程序用到它，如邮件系统；当为没有域名的主机进行DNS查询时，也要用到。如果没有域名，主机名将被使用，删除所有在第一个点( .)前面的内容。

3.search //它的多个参数指明域名查询顺序。当要查询没有域名的主机，主机将在由search声明的域中分别查找。domain和search不能共存；如果同时存在，后面出现的将会被使用。

4. sortlist //允许将得到域名结果进行特定的排序。它的参数为网络/掩码对，允许任意的排列顺序。

* * *

hosts.deny/aloow解释见：[此处][1]

* * *

 [1]: http://www.buhuipao.com/2016/08/16/etchosts-allow-etchosts-deny/