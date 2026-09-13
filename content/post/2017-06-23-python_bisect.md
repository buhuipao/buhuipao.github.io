---
title: Python bisect：用时间窗口理解左右边界
author: 咩
type: post
date: 2017-06-23T04:52:44+00:00
lastmod: 2026-09-13T00:00:00+08:00
url: /2017/06/23/python_bisect/
description: 用带重复时间戳的事件列表推导半开区间查询，区分插入位置、查找结果与列表插入成本，并提供可运行的边界检查。
ads: true
categories:
  - Python
tags:
  - 二分查找
---

假设一段日志的事件时间已经按升序整理成 `[1000, 1010, 1010, 1020]`，现在要统计从 1010 开始、到 1020 之前发生了几次事件。遍历一次当然能得到答案，但如果同一批日志要回答很多时间窗口查询，就可以利用已经有序这个条件。

本文的例子使用 Python 3.9 及以上版本，只依赖标准库。列表中的时间是为了说明边界而设定的整数，不涉及实际日志数据。

## 先确定时间窗口怎样包含边界

本文采用半开区间 `[start, stop)`：包含开始时刻，不包含结束时刻。这样，连续窗口 `[1000, 1010)` 与 `[1010, 1020)` 不会重复统计恰好发生在 1010 的事件。

`bisect_left(times, start)` 找到第一个不小于 `start` 的位置；对 `stop` 再执行一次同样的查找，就得到第一个不属于当前窗口的位置。两者之差就是事件数量。这里的语义依据 [Python bisect 文档](https://docs.python.org/3/library/bisect.html)，下面用具体数据检查它如何影响查询结果。

| 查询 | 左边界下标 | 右边界下标 | 事件数 |
| --- | --- | --- | --- |
| `[1000, 1010)` | 0 | 1 | 1 |
| `[1010, 1020)` | 1 | 3 | 2 |
| `[1010, 1010)` | 1 | 1 | 0 |
| `[1021, 1030)` | 4 | 4 | 0 |

重复时间戳保留的是两条事件，不能先用 `set` 去重。查找返回 4 也是合法结果，它表示位置在列表末尾之后，并不表示存在下标为 4 的元素。

## 一个可以直接运行的实现

下面的函数约定 `times` 已经升序排列。它不会在每次查询前重新排序，也不会切片复制命中的事件。如果数据来自外部输入，应在导入时先校验时间类型并完成排序。

```python
from bisect import bisect_left, bisect_right


def count_in_window(times, start, stop):
    if stop < start:
        raise ValueError("stop must be greater than or equal to start")
    return bisect_left(times, stop) - bisect_left(times, start)


times = [1000, 1010, 1010, 1020]
assert count_in_window(times, 1000, 1010) == 1
assert count_in_window(times, 1010, 1020) == 2
assert count_in_window(times, 1010, 1010) == 0
assert count_in_window(times, 1021, 1030) == 0
assert count_in_window([], 1000, 1020) == 0
assert count_in_window(times, 0, 2000) == len(times)

# 如果业务改成包含结束时刻，右边界才改用 bisect_right。
assert bisect_right(times, 1020) - bisect_left(times, 1010) == 3

try:
    count_in_window(times, 1020, 1010)
except ValueError:
    pass
else:
    raise AssertionError("reversed window was accepted")

print("time-window checks passed")
```

保存为 `bisect_window.py` 后执行 `python3 bisect_window.py`，所有检查通过时输出 `time-window checks passed`。开始、结束相同的窗口应该为空，而开始晚于结束是输入错误，两者不能都被默默当作零条事件。

## 插入位置不等于“找到了这个元素”

如果想判断事件时间 1015 是否存在，`bisect_left(times, 1015)` 会返回 3；那里实际存放的是 1020。这个结果只说明把 1015 放到下标 3 可以维持顺序。

因此，“判断是否存在”还需要同时检查 `i < len(times)` 和 `times[i] == target`。如果要找不晚于目标时间的最近事件，可以取 `bisect_right(times, target) - 1`，但必须先排除结果为 -1 的情况；Python 的负下标会读取最后一个元素，容易把“没有历史事件”误判为“最后一条事件”。

左右边界的区别在重复值处尤其明显：对 1010，`bisect_left` 返回 1，`bisect_right` 返回 3。它们之间正好夹住所有等于 1010 的事件。

## 二分查找快，不代表列表插入也快

这个计数函数执行两次二分查找，查询时间是 O(log n)，额外空间是 O(1)。如果还要返回窗口内的 k 条事件，切片和输出本身就需要 O(k) 的工作。

`insort` 则分成两步：先定位，再向 Python 列表中间插入。第二步可能移动后面的元素，所以整体仍是 O(n)。一批乱序数据如果逐条插入，最坏会积累到 O(n²)；只需要最后得到有序结果时，一次 `sorted` 更合适。不能仅因为名字里有二分查找，就断言它一定比追加后排序更快。

对于这个日志查询例子，实用的安排是：先整理一批有序时间，再让多个查询复用它。如果多个线程同时修改同一个列表，查询边界可能失效，需要在外层统一同步；本文的函数只处理查询期间保持不变的列表。

[最长递增子序列](/2017/06/23/leetcode-longest_increasing_subsequence/)还有一个不同的用法：利用 `bisect_left` 定位并替换已有元素。替换不会移动后面的列表元素，所以能保住算法整体的 O(n log n) 时间。
