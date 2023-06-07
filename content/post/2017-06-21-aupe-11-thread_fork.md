---
title: AUPE-11-线程同步及线程的Fork
author: 咩
type: post
date: 2017-06-21T04:39:30+00:00
url: /2017/06/21/aupe-11-thread_fork/
categories:
  - Linux
tags:
  - AUPE
  - Fork
  - 线程

---
线程是对进程的一种模仿，而协程（微线程）是对线程的一种模仿；

**线程创建**：

```c
# include "pthread_h"
int pthread_create(pthread_t * restrict tidp,
    const pthread_attr_t *resrict attr,
    void *(*start_rtm) (void), void *restrict arg);
```

**线程同步**：

  * 互斥量（锁），但需要避免死锁；
  * 读写锁（共享锁）；
  * 条件变量；
  * 自旋锁（适应于：a)锁被持有的时间短 ； b)线程不希望被重新调度）
  * 屏障（参考《现代操作系统》，只有多个合作线程都到达同一点时才放行）

**读写锁**又名共享锁，基本特征是：

  1. 当是处于写加锁状态时，在解锁前，其它尝试加锁的线程会被阻塞；
  2. 当处于读加锁时，所有尝试读加锁的进程可以得到访问，但是写加锁的线程会被阻塞直到所有的读加锁线程放锁；
  3. 当处于读加锁时，而这个时候如果有一个线程尝试加写的锁时，之后的其他线程的读加锁都会被阻塞，避免读模式的锁长期锁住（有种优先写模式锁的感觉），参见第二点

**线程加锁**：初始化、销毁锁、加锁、试锁、解锁、定时锁

```c
# include "pthread_h"
int pthread_mutex_init(pthread_mutex_t *restrict mudex,
    const pthread_attr_t *resrict attr);
int pthread_mutex_destroy(pthread_mutex_t *mutex);
int pthread_mutex_lock(pthread_mutex_t *mutex);
int pthread_mutex_trylock(pthread_mutex_t *mutex);  /*失败将会返回EBUSY*/
int pthread_mutex_unlock(pthread_mutex_t *mutex);
int pthread_mutex_timedlock(pthread_mutex_t *mutex, 
    const struct timespace *restrict tsptr);       /*tsptr为绝对时间*/
```

**避免死锁**：

  1. 如果线程对一个互斥量加锁两次将会导致死锁， 应避免；
  2. 如果互相持有一个锁A，B的两个线程，分别对B、A加锁，将会导致死锁，应该顺序加锁A、B，或者在加锁前先释放自己的锁。

**线程的Fork：**

线程fork只会fork当前线程到新的进程中去，如果直接调用exec干其他的活，旧的地址空间被丢弃，不需要关心所得状态，如果不是的话需要在调用exec之前进行相应的清锁工作；主要函数是：

```c
# include "pthread_h"
int pthread_atfork(void (*prepare) (void),   /*在父进程中获取锁*/
           void (*parent) (void),            /*在fork返回前父进程中解锁*/    
           void (*child) (void));            /*在fork返回前子进程中解锁*/
```

参考APUE：因为子进程继承的是父进程的锁的拷贝，所有上述并不是解锁了两次，而是各自独自解锁。可以多次调用pthread_atfork函数从而设置多套fork处理程序，但是使用多个处理程序的时候。处理程序的调用顺序并不相同。parent和child是以它们注册时的顺序调用的，而prepare的调用顺序与注册顺序相反。

一般情况下，不需要清理条件变量，但如果在一些操作系统中，锁被作为条件变量实现的一部分，也需要清理；但如果锁是嵌入到条件变量的数据结构中，那么在调用fork之后就不能使用条件变量，没可移植的法清理这种锁。

**线程I/O**：两个线程如果同一个时间对一个文件描述符进行读写操作，最后会两个会从后一个线程lseek定位的地方开始读，会读取到相同的内容；所以一般采取pread设置偏移量进行读取。