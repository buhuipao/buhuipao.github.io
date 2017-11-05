---
title: 意外的笔试以及遇到的意外Java问题
author: 咩
type: post
date: 2016-04-22T14:35:50+00:00
url: /2016/04/22/jvm_terminated-exit_code13/
post_views_count:
  - "37"
flag:
  - .
flashPic:
  - .
categories:
  - 新闻
tags:
  - java
  - JVM

---
邻近毕业，前几天投递一个份优酷土豆的实习生的简历，投递的是运维开发工程实习生，但是意外的是，今天收到了大数据开发的的笔试通知，通知邮件提示我24号将参加java笔试题，当时一阵郁闷，我投的运维开发实习，怎么回了我大数据开发的笔试通知，受宠若惊。

更一下不能理解的是，通知叫我参加java笔试，后来查得大数据开发就是用地JAVA，之前只是听说JAVA能用作服务端，恕我眼界狭窄。实话实说，考java我连java开发环境都不会配置，但是既然通知都来了，那我还是硬着头皮一试把，抓紧这两天看能把java看一个入门，之前又问过一个自学java成才好友，java和php都是OOP，只是语法不同，顿时心里有底了，拼死这两天不吃喝，再背点笔试题库，应该能应付这个笔试；

那么，第一步习惯性搜索怎么搭建运行环境（运维之毒），以前只听说过JAVA虚拟机，还有Eclipse，linux下只需要下载Eclipse,openJDK已经有了，那么直接下载解压，运行发现出错了：
  
VM terminated. Exit code=13
  
/usr/bin/java
  
-Dosgi.requiredJavaVersion=1.7
  
-XX:MaxPermSize=1024m
  
-Xms256m
  
-Xmx1024m
  
-jar /home/buhuipao/eclipse//plugins/org.eclipse.equinox.launcher_1.3.100.v20150511-1540.jar
  
-os linux
  
-ws gtk
  
-arch x86_64
  
-showsplash /home/buhuipao/eclipse//plugins/org.eclipse.platform_4.5.2.v20160212-1500/splash.bmp
  
-launcher /home/buhuipao/eclipse/eclipse
  
-name Eclipse
  
&#8211;launcher.library /home/buhuipao/eclipse//plugins/org.eclipse.equinox.launcher.gtk.linux.x86\_64\_1.1.300.v20150602-1417/eclipse_1612.so
  
-startup /home/buhuipao/eclipse//plugins/org.eclipse.equinox.launcher_1.3.100.v20150511-1540.jar
  
&#8211;launcher.appendVmargs
  
&#8230;
  
无奈百度/googel,得到最多的结果无非两种：
  
1）大肆说你下载的Eclipse和JDK的位数不同，<a href="http://www.jsjtt.com/xitongyingyong/linux/77.html" target="_blank">32!=64</a>，但是一般下载的东西怎么会有错的，也用java   -version 试过，未能解决；
  
2）大量的说，你的权限问题，你必须保证的文件可读可写，但是再次验证，没这回事，
  
3）也有说你的java版本问题，你的版本太高了，没有去试，一般这么说的都可以写在配置文档解决;<span id="transmark"></span>
  
最后实在不想被打败，回到了Eclipse的<a href="http://wiki.eclipse.org/Eclipse.ini#-vm_value:_Linux_Example" target="_blank">wiki官网</a>，跟着修改了eclipse.ini,添加了如下加粗的内容，

<pre>openFile
4 --launcher.appendVmargs
3 <strong>-vm
2 /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.77-1.b03.fc23.x86_64/jre/bin/java</strong>
1 -vmargs
19  -Dosgi.requiredJavaVersion=1.7
1 -XX:MaxPermSize=1024m
2 -Xms256m
3 -Xmx1024m</pre>

于是顺利进入Eclipse,零基础开始学java&#8230;

最后要说一句的是，现在网上信息太杂乱，很多人的复制粘贴回答别人的问题，只会产生更多的互联网垃圾，
  
只想对他们说一句，能不能不害人，并且我们的度娘和骨哥并没有那么聪明，他们只会摘取筛选，将来会不会出现一个人工或者智能筛选的服务，准确提供解决问题的链接，并且实时更新；当然知乎远远不够，他们的定位并不是这个。不久之后定会出现，那我们先叫她&#8221;问题wiki&#8221;吧&#8230;