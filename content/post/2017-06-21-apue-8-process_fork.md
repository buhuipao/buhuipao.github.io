---
title: fork 实验：独立的内存与共享的文件偏移
author: 咩
type: post
date: 2017-06-21T03:15:52+00:00
lastmod: 2026-09-13T00:00:00+08:00
url: /2017/06/21/apue-8-process_fork/
description: 用单线程 Python 实验观察 fork 返回值、字典副本、共享文件偏移和 waitpid 回收，区分进程内存与内核中的打开文件状态。
ads: true
categories:
  - Linux
tags:
  - APUE
  - 进程
---

阅读 APUE 的进程控制章节时，容易把“子进程复制父进程”和“父子进程共享文件偏移”理解成互相矛盾的说法。实际需要区分两层状态：进程自己的内存，以及文件描述符指向的内核对象。

下面用一个实验同时检查这两层。它使用 Python 3.9 及以上版本，在支持 `os.fork` 的 Linux 或 macOS 上以独立、单线程命令行脚本运行；不适用于 Windows，也不要直接放进已有线程的服务或 Notebook 内核执行。

## 先分清三个进程编号

一次成功的 fork 会让父子进程分别从调用处继续执行。父进程收到的是子进程的 PID，子进程收到 0。`getpid()` 始终表示正在执行这段代码的进程自身，而 `getppid()` 表示它的父进程。

因此父进程中的 `getppid()` 并不是它自己的编号；子进程里的 `getppid()` 也只在父进程仍存活时，才等于 fork 前记录的父进程 PID。具体返回规则见 [fork(2)](https://man7.org/linux/man-pages/man2/fork.2.html)。

实验让父进程等待子进程退出，这样既能保证父进程仍在，也能固定观察顺序，避免用 sleep 猜测哪个进程先获得调度。

## 一段同时观察两种状态的代码

临时文件只有两个字节 `AB`。fork 前把文件偏移移回开头，子进程读取一个字节并修改自己的字典。父进程等它完成后，检查字典和下一次读取的结果。

```python
import os
import tempfile


if not hasattr(os, "fork"):
    raise SystemExit("This example requires a Unix system with os.fork")

state = {"count": 1}
parent_pid = os.getpid()
with tempfile.TemporaryFile() as file:
    fd = file.fileno()
    assert os.write(fd, b"AB") == 2
    os.lseek(fd, 0, os.SEEK_SET)

    child_pid = os.fork()
    if child_pid == 0:
        state["count"] = 99
        ok = os.getppid() == parent_pid and os.read(fd, 1) == b"A"
        os._exit(0 if ok else 1)

    waited_pid, status = os.waitpid(child_pid, 0)
    assert waited_pid == child_pid
    assert os.waitstatus_to_exitcode(status) == 0
    assert state["count"] == 1
    assert os.read(fd, 1) == b"B"
    assert os.read(fd, 1) == b""

    try:
        os.waitpid(child_pid, 0)
    except ChildProcessError:
        pass
    else:
        raise AssertionError("the child should already have been reaped")

print("fork checks passed: independent memory, shared file offset")
```

保存为 `fork_state.py`，执行 `python3 fork_state.py`。成功时输出 `fork checks passed: independent memory, shared file offset`。临时文件会在父进程离开 with 语句时关闭并清理，不需要指定或改动已有文件。

这里使用 `os.read` 和 `os.write` 直接操作描述符，避免 Python 文件对象的缓冲区预读干扰观察。子进程用 `os._exit` 结束，不再次刷新从父进程复制过来的用户态输出缓冲；这是为了使这个小实验的退出行为明确，不是所有业务代码的通用退出写法。

## 从两个断言解释结果

`state["count"] == 1` 检查的是普通内存：子进程把自己的字典改成 99，并没有改变父进程的字典。Linux 通常用写时复制实现这类内存继承，但在程序语义上仍是两个独立的地址空间。

`os.read(fd, 1) == b"B"` 检查的是文件位置：父子进程各有自己的描述符表项，但 fork 继承的两个表项指向同一个打开文件描述，其中包括当前偏移。子进程读过 A 后，这个共享偏移已经前进了一字节，所以父进程接着读到 B。这个关系也由 [fork(2) 对文件描述符继承的说明](https://man7.org/linux/man-pages/man2/fork.2.html)规定。

同一个数字 fd 并不能单独证明共享关系。如果父子进程各自重新打开同一个路径，它们可以拥有独立的打开文件描述与偏移。诊断并发读写时，需要追踪描述符是通过 fork 或 dup 继承的，还是分别 open 得到的。

## 退出与回收是两个步骤

子进程退出后，父进程调用 `waitpid` 取得终止状态并完成回收。上面的第二次 wait 会得到 `ChildProcessError`，因为这个子进程已经被回收，不能再取一次状态。

在默认的子进程回收语义下，如果子进程退出而父进程迟迟没有 wait，它会保留用于报告终止状态的内核记录，通常表现为僵尸进程。僵尸不再执行用户代码；仅向它发送终止信号不能替代父进程回收。细节及信号处理方式带来的例外可参阅 [wait(2)](https://man7.org/linux/man-pages/man2/wait.2.html)。

这个实验适合观察 fork 本身，不是并发任务框架。实际只是想启动另一个命令时，优先使用 `subprocess`；如果程序已经有多个线程，fork 后的子进程可能继承由消失线程持有的锁，不能照搬这里的任意 Python 操作。运行边界及平台限制见 [Python os.fork 文档](https://docs.python.org/3/library/os.html#os.fork)。
