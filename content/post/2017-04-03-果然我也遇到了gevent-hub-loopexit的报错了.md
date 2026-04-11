---
title: 果然我也遇到了gevent.hub.LoopExit的报错了
author: 咩
type: post
date: 2017-04-03T09:18:45+00:00
url: /2017/04/03/果然我也遇到了gevent-hub-loopexit的报错了/
categories:
  - Python
tags:
  - Python
  - gevent

---
报错信息如下：

gevent.hub.LoopExit: (‘This operation would block forever’, <Hub at 0x1076b7e10 select default pending=0 ref=0 resolver=<gevent.resolver_thread.Resolver at 0x1077eec90 pool=<ThreadPool at 0x1077eecd0 0/10/10>> threadpool=<ThreadPool at 0x1077eecd0 0/10/10>>)

### 原因分析

`gevent.hub.LoopExit` 这个异常的含义是：**当前没有任何可以运行的 greenlet，但有操作正在等待完成**。换句话说，所有的 greenlet 都在等待 I/O 或者已经结束了，event loop 中已经没有活跃的事件源（ref=0），此时如果还有代码试图做阻塞操作（比如 `queue.get()`），gevent 就会抛出这个异常，因为它知道这个等待永远不会有结果。

从报错信息中可以看到 `pending=0 ref=0`，说明 event loop 中已经没有任何待处理的事件了。

### 常见触发场景

**1. monkey_patch 不完整**

如果只 patch 了部分模块，可能导致某些 I/O 操作没有被正确协程化，greenlet 直接阻塞了底层线程：

```python
# 错误：只patch了部分
from gevent import monkey
monkey.patch_socket()

# 正确：patch所有模块
from gevent import monkey
monkey.patch_all()
```

**2. 所有 greenlet 结束后仍在等待 Queue**

这是最常见的场景，生产者 greenlet 已经结束了，但消费者还在 `queue.get()` 等待数据：

```python
import gevent
from gevent.queue import Queue

q = Queue()

def producer():
    for i in range(3):
        q.put(i)
    # producer结束了，不再往queue里放数据

def consumer():
    while True:
        item = q.get()  # producer结束后，这里会触发LoopExit
        print(item)

gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(consumer),
])
```

**3. 在主 greenlet 中做阻塞等待**

如果只有主 greenlet 在运行，没有其他活跃的 greenlet，调用阻塞操作也会触发：

```python
from gevent.queue import Queue
q = Queue()
q.get()  # 没有其他greenlet往里放数据，直接LoopExit
```

### 解决方案

**方案一：给 Queue.get() 加超时**

```python
from gevent.queue import Queue, Empty

q = Queue()

def consumer():
    while True:
        try:
            # 设置超时时间，避免永久阻塞
            item = q.get(timeout=5)
            print(item)
        except Empty:
            print(‘队列超时，退出消费者’)
            break
```

**方案二：使用哨兵值通知消费者退出**

```python
import gevent
from gevent.queue import Queue

SENTINEL = None  # 哨兵值，通知消费者退出
q = Queue()

def producer():
    for i in range(3):
        q.put(i)
    q.put(SENTINEL)  # 生产完毕，放入哨兵值

def consumer():
    while True:
        item = q.get()
        if item is SENTINEL:
            break
        print(item)

gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(consumer),
])
```

**方案三：捕获 LoopExit 异常**

```python
import gevent
from gevent.queue import Queue

q = Queue()

def consumer():
    try:
        while True:
            item = q.get()
            print(item)
    except gevent.hub.LoopExit:
        # 所有生产者已结束，正常退出
        print(‘所有任务已完成，退出’)
```

**方案四：确保 monkey_patch 正确且完整**

```python
# 务必在所有import之前执行
from gevent import monkey
monkey.patch_all()

# 然后再import其他模块
import requests
import socket
```

### 参考

<http://xiaorui.cc/2016/08/07/%E5%85%B3%E4%BA%8Egevent-queue%E9%81%AD%E9%81%87hub-loopexit%E9%97%AE%E9%A2%98/>