---
title: Docker的centos7内部启动systemctl出现BUG的解决办法
author: 咩
type: post
date: 2016-08-13T04:04:01+00:00
url: /2016/08/13/docker-centos7-systemctl-bug/
post_views_count:
  - "147"
flashPic:
  - .
flag:
  - .
categories:
  - Docker
tags:
  - centos7
  - Docker

---
Failed to get D-Bus connection: Operation not permitted
  
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;
  
距离这个问题一天之后，最后我经过Google，在红帽的一个开发者博客找到了答案，经过测验有效，网址为：

<http://developerblog.redhat.com/2014/05/05/running-systemd-within-docker-container/>，大致意思就是，在你编写自己的Dockerfile时，在ENTRAYPOINT，或者CMD 启动命令设置为[&#8220;/usr/sbin/init&#8221;],它将会启动你的服务。