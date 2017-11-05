---
title: /etc/hosts.allow和/etc/hosts.deny配置解释
author: 咩
type: post
date: 2016-08-16T03:27:27+00:00
url: /2016/08/16/etchosts-allow-etchosts-deny/
post_views_count:
  - "97"
flashPic:
  - .
flag:
  - .
categories:
  - Linux
tags:
  - Linux
  - SSH

---
/etc/hosts.allow和/etc/hosts.deny两个文件是控制远程访问设置的，
  
修改/etc/hosts.allow文件
  
sshd:210.13.118.*
  
sshd:222.127.15.*
  
两个ip段连接sshd服务，当然:allow完全可以省略的。
  
all:218.24.129.110 他表示接受所有请求！
  
/etc/hosts.deny文件，此文件是拒绝服务列表，文件内容如下：
  
sshd:all:deny
  
注意看：sshd:all:deny表示拒绝了所有sshd远程连接。
  
当hosts.allow和 host.deny相冲突时，以hosts.allow设置为准。
  
/etc/hosts.allow和/etc/hosts.deny这两个文件是tcpd服务器的配置文件
  
tcpd服务器可以控制外部IP对本机服务的访问
  
<a href="http://www.buhuipao.com/category/linux_web/" target="_blank">linux</a> 系统会先检查/etc/hosts.allow，再检查/etc/hosts.deny，和iptables一样，前面的匹配了后面的就不看了
  
禁止所有ip访问linux 的ssh功能:
  
可以在/etc/hosts.deny添加一行 sshd:all:deny
  
禁止局域网内ip（192.168.11.12）访问ssh功能:
  
可以在/etc/hosts.deny添加一行sshd:192.168.11.12