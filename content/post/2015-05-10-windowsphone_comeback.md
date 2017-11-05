---
title: windows10手机版回滚wp8.1突变QHSUSB_DLOAD模式，非JTAG黑砖修复
author: 咩
type: post
date: 2015-05-10T02:16:52+00:00
url: /2015/05/10/windowsphone_comeback/
post_views_count:
  - "2715"
flashPic:
  - .
flag:
  - .
tc-thumb-fld:
  - 'a:2:{s:9:"_thumb_id";i:291;s:11:"_thumb_type";s:10:"attachment";}'
categories:
  - 新闻
tags:
  - JTAG
  - QHSUSB_DLOAD
  - 黑砖

---
[<img class="aligncenter size-full wp-image-291" src="http://www.buhuipao.com/wp-content/uploads/2015/05/1392197831776.jpg" alt="wp手机" width="500" height="333" srcset="http://www.buhuipao.com/wp-content/uploads/2015/05/1392197831776.jpg 500w, http://www.buhuipao.com/wp-content/uploads/2015/05/1392197831776-150x100.jpg 150w, http://www.buhuipao.com/wp-content/uploads/2015/05/1392197831776-300x200.jpg 300w" sizes="(max-width: 500px) 100vw, 500px" />][1]

许多尝试<a href="http://www.buhuipao.com/2015/01/25/windows10-for-phone/" target="_blank">windows10手机版</a>的朋友们，由于觉得新的系统存在太多的BUG,于是乎准备回滚到wp8.1，但是悲剧发生了，大量的用户的LUMIA手机变成黑砖，出现了**QHSUSB_DLOAD**模式。本人也是众多小白鼠中的一只，在到处寻求救助之后，终于在一个QQ群里找到了方法，有人分享了几个<a href="http://www.wpxap.com/thread-836759-1-1.html" target="_blank">重要链接</a>，晚上便报以最后一点希望进行了尝试，没想到竟然成功，于是不敢私藏，赶紧分享！

_ **  由于不同人的LUMIA手机情况不同，本人也只是用诺基亚925尝试，请谨慎尝试，如若出现恶劣后果，概不负责！**_

操作环境：64位windows10预览版10074；

实验手机：国行联通版白色诺基亚925；

第一步：安装Windows Phone Recovery Tool，下载地址：<a href="http://go.microsoft.com/fwlink/?LinkID=525569" target="_blank">http://go.microsoft.com/fwlink/?LinkID=525569</a>；

第二步：下载刷机固件，这里推荐<a href="http://www.coolxap.com/" target="_blank">酷七</a>的下载工具，下载地址：<a href="http://pan.baidu.com/s/1jGnE4Lo" target="_blank">http://pan.baidu.com/s/1jGnE4Lo</a>（提取密码是：4wkw）；

第三步：<a href="http://nds2.fds-fire.nokia.com/fds_fire/1408/1815/7389472134/NokiaCareSuiteForStore-5.4.119.1432.exe" target="_blank">安装驱动</a>，查看是否安装好就是去设备管理器查看**QHSUSB_DLOAD**的驱动属性，里面出现三个.dll文件；

第四步：在C盘下创建dump文件夹，把刷机固件文件夹复制到C盘下；

第五步：进入Windows Phone Recovery Tool文件夹，管理员运行CMD,输入cd C:\Program Files (x86)\Microsoft Care Suite\Windows PhoneRecovery Tool（32位：cd C:\ProgramFiles\Microsoft Care Suite\Windows Phone Recovery Tool）；

第六步：诺基亚925刷机包是rm-910，于是以管理员身份进入CMD,运行:thor2 -mode ffureader -ffufile &#8220;C:\rm-910\XXX.ffu&#8221; -dump_gpt -filedir C:\dump,修改dump文件夹里gtp0.bin为msimage.mbn。命令窗里将出现两行乱码，对照前40位下载对应的<a href="http://pan.baidu.com/s/1jGGKM0I" target="_blank">bin文件</a>（提取密码：plfg），并重命名为HEX.bin（也有种说法就是修改dump下的gtp1.bin文件为HEX.bin不知是否可以未测）**；**

第七步：下载<a href="http://pan.baidu.com/s/1o6NynUy" target="_blank">bin2hex程序</a>复制到dump文件下，运行cd C:\dump；进入dump文件夹，再执行命令bin2hex HEX.bin HEX.hex生成HEX.hex文件；

第八步：将dump文件夹里的HEX.hex和msimage.mbn复制到 C:\Program Files (x86)\Microsoft Care Suite\Windows PhoneRecovery Tool（32位：C:\ProgramFiles\Microsoft Care Suite\Windows Phone Recovery Tool）文件夹，重复**第五步**进入文件夹，执行：thor2 -mode emergency -hexfile HEX.hex -mbnfile msimage.mbn -orig_gpt；

第九步：拔掉数据线，重新接入电脑，再充电一会之后，你的手机将会出现红屏，再次执行：thor2.exe -mode vpl -maxtransfersizekb 1 -vplfile C:\rm-910\XXX.vpl（注意是固件包你手机对应颜色和版本的vpl文件），执行完之后你的手机会变成绿屏证明你成功刷入固件了；

第十步：执行命令：thor2 -mode rnd -bootnormalmode，你的手机就会重启，完成。<img class="aligncenter wp-image-290 size-full" src="http://www.buhuipao.com/wp-content/uploads/2015/05/925-e1431482847452.jpg" alt="" width="288" height="480" srcset="http://www.buhuipao.com/wp-content/uploads/2015/05/925-e1431482847452.jpg 288w, http://www.buhuipao.com/wp-content/uploads/2015/05/925-e1431482847452-90x150.jpg 90w, http://www.buhuipao.com/wp-content/uploads/2015/05/925-e1431482847452-180x300.jpg 180w" sizes="(max-width: 288px) 100vw, 288px" />

**以上步骤并非原创，参考借鉴了一下三篇文章，自己尝试感觉难懂便修改整理此文，感谢原作！三篇文章地址：**1）<a href="http://forum.xda-developers.com/windows-phone-8/development/help-programmer-unbrick-jtag-t3082592" target="_blank">http://forum.xda-developers.com/windows-phone-8/development/help-programmer-unbrick-jtag-t3082592</a>；2）<a href="http://www.coolxap.com/thread-366064-1-1.html" target="_blank">http://www.coolxap.com/thread-366064-1-1.html</a>；3）<a href="http://www.wpxap.com/thread-836759-1-1.html" target="_blank">http://www.wpxap.com/thread-836759-1-1.html</a>。

 [1]: http://www.buhuipao.com/wp-content/uploads/2015/05/1392197831776.jpg