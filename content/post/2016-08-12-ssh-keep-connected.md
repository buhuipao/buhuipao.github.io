---
title: 保持SSH连接不断线（服务端，客户端）
author: 咩
type: post
date: 2016-08-12T04:26:12+00:00
url: /2016/08/12/ssh-keep-connected/
flag:
  - .
flashPic:
  - .
post_views_count:
  - "85"
categories:
  - Linux
  - Shell
tags:
  - Linux
  - SSH

---
最近一直游荡于各个校招群，清早群里有人问到如何保持ssh连接，群内有人提出用screen，和nohup等解决办法，不久前我配置Ganglia监控服务时也遇到这种情况，在这里记录以下防止自己忘掉。
      
如果你有**服务器端**权限（<del datetime="2016-08-12T04:10:34+00:00">一般你是没有的</del>-_-）， 可以让服务器发送“心跳”信号给客户端进行保持连接
  
修改 sshd\_config的配置文件，vim /etc/ssh/sshd\_config，注释掉：
  
[code]ClientAliveInterval 60
  
ClientAliveCountMax 5[/code]
  
意思就是：SSH Server 每 60 秒就会自动发送一个信号给客户端，如果客户端没有回应，会记录下来直到记录数超过5次才会断开连接。
  
如果你没有服务器端管理权限，
      
也在客户端进行设置，新建/etc/ssh/ssh_config文件，添加两行参数就行了

<pre class="lang:shell decode:1 " >TCPKeepAlive yes
ServerAliveInterval 300</pre>

第一行是保持连接，后一行表示每过5分钟“心跳一次”告诉服务器，前提是你在客户端（跳板）有这个权限，如果没有那么直接在连接SSH时加上两个参数，

<pre class="lang:shell decode:1 " >ssh -o TCPKeepAlive=yes -o ServerAliveInterval=180 buhuipao@YourIP -p YouPort</pre>