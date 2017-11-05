---
title: 不再缘木求鱼，时间如此宝贵，Docker下ubuntu安装QQ失败
author: 咩
type: post
date: 2016-09-07T16:55:16+00:00
url: /2016/09/08/docker-ubuntu-qq-failed/
post_views_count:
  - "149"
flashPic:
  - .
flag:
  - .
categories:
  - Docker
  - Linux
tags:
  - centos7
  - Docker
  - Linux
  - python
  - SSH
  - Ubuntu

---
今下午本来是准备照着国外的一个教程，好好跟着过写一遍如何用python写一个异步web服务端，但是无意中看到一个QQ的新闻，于是想起来很久之前想在linux装好QQ的，接着一下午加一晚上的时间过去了。
  
很久之前在Fedora上试过装QQ但是版本很老，画面惨不忍睹，于是只能转着弯来想办法，自己电脑4G内存跑个Win虚拟机感觉有点吃力，自己有时候文件还是要经过QQ的。突然想起自己很久前的一个小项目，用Docker+NX协议的一个服务端实现了远程登陆控制centos7，因为在Ubuntu下的QQ版本为7.8，基于Win7.5应该可以凑活着用，于是二话不说开始写Dockerfile。
  
首先在wine-qq-7.8的官网[http://www.longene.org/forum/viewtopic.php?f=6&t=30516] 得知他是基于ubuntu12.04开发测试的，所以果断Docker的ubuntu也用了12.04，但是据测试发现，此12.04ubuntu死活无法开启ssh，毕竟之后的远程登陆需要用到ssh，所以放弃了往上一个版本走。于是改用14.04重新构建镜像，等了许久终于成功啦，启动ubuntu-ssh容器，进入容器后尝试用NX的客户端登陆，成功进入桌面。然后继续下载deb包，然后

<pre class="lang:bash decode:1 " >dpkg -i Win-qq-7.8-longene.deb.</pre>

安装成功后，运行

<pre class="lang:bash decode:1 " >/usr/bin/qq</pre>

没错，失败了！说是找不到Wine，于是重新安装Wine，然后再尝试，缺少一个libgbk-3.0.0库，网上找了好久，没有解决办法，最后在一片2年前文章中发现了类似的错误，但是他最后成功了安装了qq2013，但他最后提醒到，**不要缘木求鱼，不要期望在Linux下安装使用QQ，游戏之类的，专注与自己的事，开发写脚本就好了**。
  
今天下午和晚上的时间用掉了，而且还错过了晚上锻炼的时间，最后并没有安装成功，但在这个过程中却构建了一个ubuntu-ssh，ubuntu-remote镜像，只能说不亏不亏。