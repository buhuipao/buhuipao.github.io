---
title: 本站的改造升级，全站https失败
author: 咩
type: post
date: 2016-08-29T15:56:52+00:00
url: /2016/08/29/web-update-https/
post_views_count:
  - "67"
flashPic:
  - .
flag:
  - .
categories:
  - Linux
tags:
  - chromebook
  - HTTPS
  - IP
  - Linux
  - mysql

---
最近的找工作压力很大，我这”洁癖男“在压力下想换个思路转一下注意力，以便下一步高效复习准备接下来的运维开发的笔试面试。于是想起自己的网站如今越来越卡(心li洁癖)，而且阿里云一直提醒我的WP-IMG漏洞，于是一步一步解决这些问题。终于大半天过去了，差不多解决了，除了网站前台的七牛CDN图片没法https。

首先是把一年前的php56-mysql5.5-apache的Web环境换成php70-mysql-nginx，首先把之前的remove，

[code]sudo yum -y remove php-common &#8230;
  
yum install enabelrepo=remi,remi-php70 install php-common &#8230;
  
[/code]

然后就是添加nginx源安装nginx，安装php-fpm，然后配置php支持，把版本号隐藏，开启缓存之类的老套路&#8230;

看到自己的网站是lnmp之后呢，顺便把本站上的一个监控服务配置下，在这：[Ganglia][1],然后因为一个腾讯主机死活开启不了gmond服务，“浪费”了一个多小时时间，现在只有两个主机在上面监控着(可以看到自己的国外主机一直网咯抽风)。

然后就是阿里一直提醒我的WP-IMG漏洞，官方修复要钱，还是自己动手，网上搜了一波，挺简单：<http://www.mr-wu.cn/aliyun-wordpress-wp-image-editor-imagick/>，接着就是全站https的任务了。

很久之前想用[StartSSL][2]的免费证书，但不久前帮基友的[chromebook安装linux][3]是遇到一个问题，没法下载脚本，发现是证书的问题，基友买的chromebook是14年出的，然后原版chrome(2014)不认识后来作者为自己网站添加的[Let&#8217;s Encrypt][4](2015)证书，折腾很久之后未果，之后goole+上直接问了作者怎么修改他的下载脚本不会出错，他第二天直接回复我了一句，你使用curl时增加-k参数就好了，立即试下curl &#8211;help,果然有这个用法。

说了这么多，于是这次给自己的网站做全站https也就用的这个证书，具体如何实现、如何配置Nginx的SSL请给位自行github，google。七牛的CDN导致网站前台部分图片不可以https，后台妥妥的\`。没办法虽有洁癖但没办法，大一大二折腾的wp-cache，和cdn还不想一下取消掉，日后再弄。

 [1]: https://www.buhuipao.com/ganglia/
 [2]: https://www.startssl.com/
 [3]: https://johnlewis.ie/custom-chromebook-firmware/rom-download/
 [4]: https://letsencrypt.org/