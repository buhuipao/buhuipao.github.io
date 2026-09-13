---
title: 最长递增子序列：从动态规划到二分查找
author: 咩
type: post
date: 2017-06-23T10:03:46+00:00
lastmod: 2026-09-13T00:00:00+08:00
url: /2017/06/23/leetcode-longest_increasing_subsequence/
description: 推导 LIS 的两种状态表示，用反例区分最小末尾数组与真实子序列，并通过穷举小输入检查重复值和空输入。
ads: true
categories:
  - 算法
  - Python
tags:
  - LIS
  - 动态规划
  - 算法
---

这篇笔记讨论 [LeetCode 的最长递增子序列问题](https://leetcode.com/problems/longest-increasing-subsequence/)：按原有顺序挑出一些数，使它们严格递增，求最多能挑多少个。子序列可以跳过元素，但不能重新排列它们。

例如 `[4, 7, 2, 3, 6]` 可以选 `[2, 3, 6]`，长度是 3。直接把整个数组排序会改变问题；把相邻递增的连续片段找出来，也会漏掉允许跳跃的解。下面先建立一个容易检查的动态规划，再改变状态表示来减少查找成本。

## 以“在当前位置结束”定义状态

令 `dp[i]` 表示必须使用 `nums[i]` 作为最后一个数时，能得到的最长长度。每个数自己都能形成长度为 1 的子序列。

要把 `nums[i]` 接在一个已有子序列后面，那个子序列的末尾下标 j 必须满足 `j < i`，而且 `nums[j] < nums[i]`。因此更新规则是：对所有符合条件的 j，尝试用 `dp[j] + 1` 更新 `dp[i]`。

最终结果取整个 dp 数组的最大值。不能只返回 `dp[-1]`，因为最长解未必使用输入的最后一个数：`[1, 2, 3, 0]` 的答案是 3，在 0 处结束的答案却只有 1。

## 换成“同样长度，末尾尽量小”

上面的实现会检查当前位置之前的所有元素，时间是 O(n²)。进一步观察：如果两个递增子序列一样长，末尾较小的那个更容易接上后续输入。

因此令 `tails[k]` 表示已处理前缀里，长度为 k+1 的递增子序列能够取得的最小末尾。遇到 x 时，找到第一个大于等于 x 的末尾：如果找到了，就用 x 替换它；如果没找到，就把 x 追加到末尾。

替换保持长度不变，但给相同长度留下更好的延长机会。追加则说明 x 能接在当前最长序列后面，让已知最长长度增加 1。

| 新读入的数 | tails | 这一步的含义 |
| --- | --- | --- |
| 4 | `[4]` | 长度 1 的末尾是 4 |
| 7 | `[4, 7]` | 可以扩展到长度 2 |
| 2 | `[2, 7]` | 改善长度 1 的末尾 |
| 3 | `[2, 3]` | 改善长度 2 的末尾 |
| 6 | `[2, 3, 6]` | 可以扩展到长度 3 |

这些最小末尾保持递增，所以可以用 `bisect_left` 找替换位置。它返回的是插入边界，具体语义可参见 [Python 标准库文档](https://docs.python.org/3/library/bisect.html)。这里执行的是替换或尾部追加，不是在列表中间插入。

## 两个容易混淆的地方

第一，严格递增不允许相等元素延长序列。输入 `[2, 2, 2]` 时，三个 2 都应该替换位置 0，答案是 1。如果使用 `bisect_right`，它们会不断追加，解决的就变成允许相等的最长不下降子序列。

第二，最终的 tails 不一定是输入中的一个合法子序列。对 `[2, 6, 3, 4, 1, 5]`，最终 tails 是 `[1, 3, 4, 5]`，但输入中的 1 出现在 3 和 4 后面。长度 4 是正确的，例如 `[2, 3, 4, 5]`；各个最小末尾却可能来自不同的选择路径。

如果需求是输出具体的子序列，需要额外记录前驱下标并回溯。本文只求长度，因此没有添加这部分状态。

## 可运行实现与交叉检查

下面代码适用于 Python 3.9 及以上版本。输入约定为可重复遍历的整数列表，不修改原列表。

```python
from bisect import bisect_left
from itertools import product


def lis_dp(nums):
    dp = [1] * len(nums)
    for i, value in enumerate(nums):
        for j in range(i):
            if nums[j] < value:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp, default=0)


def lis_length(nums):
    tails = []
    for value in nums:
        i = bisect_left(tails, value)
        if i == len(tails):
            tails.append(value)
        else:
            tails[i] = value
    return len(tails)


cases = [
    ([], 0),
    ([2, 2, 2], 1),
    ([5, 4, 3, 2], 1),
    ([1, 2, 3, 0], 3),
    ([4, 7, 2, 3, 6], 3),
    ([2, 6, 3, 4, 1, 5], 4),
    ([-3, -1, -2, 0], 3),
]
for values, expected in cases:
    original = values.copy()
    assert lis_dp(values) == lis_length(values) == expected
    assert values == original

# 穷举长度 0～6、取值为 0/1/2 的所有输入，共 1093 组。
checked = 0
for size in range(7):
    for values in product(range(3), repeat=size):
        assert lis_length(values) == lis_dp(values), values
        checked += 1
assert checked == 1093
print("LIS checks passed:", checked)
```

保存后用 `python3` 执行，末尾输出 `LIS checks passed: 1093`。固定用例约束题目语义，穷举检查则更容易发现二分边界和重复值处理的不一致；它不能替代上面的状态推导。

`lis_dp` 使用 O(n²) 时间和 O(n) 空间。`lis_length` 每个元素做一次二分定位，替换为常数成本，尾部追加为均摊常数成本，因此整体为 O(n log n) 时间、O(n) 空间。没有使用 `insort`，因为向中间插入既会破坏状态含义，也会带来元素移动成本。
