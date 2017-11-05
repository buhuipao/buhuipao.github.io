---
title: APUE-8-进程控制之Fork
author: 咩
type: post
date: 2017-06-21T03:15:52+00:00
url: /2017/06/21/apue-8-process_fork/
categories:
  - Linux
tags:
  - APUE
  - Fork

---
最近又在回顾进程的Fork知识，然后手头又有APUE，悔恨大学没有看这样的书；在进程Fork时，将会返回两次，返回值为0的为子进程，用getppid()获取的是父进程的pid；返回值为进程id(子进程的）的是父进程，getppid返回的是自己的pid。
  
父子进程共享继承的是：

  * 实际用户ID，实际组ID，有效用户ID，有效组ID，附属组ID
  * 进程组ID
  * 会话ID
  * 文件偏移量
  * 控制终端
  * 目录等环境变量
  * 信号屏蔽和安排
  * 连接的共享存储段
  * 存储镜像、资源限制

父子进程不同的是：

  * fork返回值
  * 进程ID不同
  * 子进程的tms\_utime, tms\_stime, tms\_cutime, tms\_cstime的值为0
  * 子进程不继承父进程的文件锁
  * 子进程的未处理闹钟会被清除
  * 子进程的未处理的信号寄清空

fork之后对于文件描述符有以下两种处理方式：

  1. 父进程等待子进程完成。父进程无需对文件描述符做任何处理，子进程结束后，父进程的文件描述符的偏移量以做相应更新；
  2. 父进程和子进程执行不同程序段。这种情况下，fork之后，父子进程会关闭各自不需要使用的文件描述符（网络服务常用）。

fork用在两种用法：

  1. 父进程希望子进程复制自己，但是去执行不同的代码段，常见于网络服务：父进程负责监听信号，子进程负责处理请求；
  2. 一个进程要执行另一个不同程序，最常见shell：进程fork后立即调用exec执行其他程序。

Linux 之后弄出一个clone， 就是可以在fork时可以自己设定需要共享不共享的数据，然后fork应该是在clone的一个实现（猜）。

附：

<img class="aligncenter wp-image-1154" src="http://www.buhuipao.com/wp-content/uploads/2017/06/A45BF8EE-69A3-4A82-9277-2FBEBCA2FF66.jpg" alt="" width="350" height="564" srcset="http://www.buhuipao.com/wp-content/uploads/2017/06/A45BF8EE-69A3-4A82-9277-2FBEBCA2FF66.jpg 392w, http://www.buhuipao.com/wp-content/uploads/2017/06/A45BF8EE-69A3-4A82-9277-2FBEBCA2FF66-93x150.jpg 93w, http://www.buhuipao.com/wp-content/uploads/2017/06/A45BF8EE-69A3-4A82-9277-2FBEBCA2FF66-186x300.jpg 186w" sizes="(max-width: 350px) 100vw, 350px" />