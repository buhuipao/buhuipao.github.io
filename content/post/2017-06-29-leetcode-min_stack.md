---
title: 最小栈：重复最小值为什么不能漏记
author: 咩
type: post
date: 2017-06-29T03:08:00+00:00
lastmod: 2026-09-13T00:00:00+08:00
url: /2017/06/29/leetcode-min_stack/
description: 从重复最小值的反例推导双栈不变量，说明空栈行为与均摊复杂度，并给出可直接运行的操作序列检查。
ads: true
categories:
  - 算法
  - Python
tags:
  - LeetCode
  - 栈
  - 数据结构
---

[Min Stack](https://leetcode.com/problems/min-stack/)要求在普通栈的压入、弹出、读取栈顶之外，快速读取当前最小值。每次调用 `min(stack)` 都遍历一遍当然正确，但栈越大，查询成本越高。

最直接的改进是保存一个“当前最小值”。不过仅保存一个数仍然不够：如果当前最小值被弹出，应该恢复到哪个值？问题的关键在于保存最小值变化的历史。

## 用一个反例确定要保存什么

依次压入 4、2、2、3，再依次弹出。设一个辅助栈只记录小于当前最小值的新元素，那么第二个 2 不会被记录。弹出 3 后再弹出一个 2，辅助栈会把唯一记录的 2 删除，错误地报告最小值是 4；实际上数据栈里还剩一个 2。

所以压入条件必须包含相等：`x <= mins[-1]`。每一份重复最小值都要有对应记录，这样一次弹出只撤销一份记录。

| 操作完成后 | 数据栈 | 最小值栈 | 当前最小值 |
| --- | --- | --- | --- |
| 压入 4 | `[4]` | `[4]` | 4 |
| 压入 2 | `[4, 2]` | `[4, 2]` | 2 |
| 再压入 2 | `[4, 2, 2]` | `[4, 2, 2]` | 2 |
| 压入 3 | `[4, 2, 2, 3]` | `[4, 2, 2]` | 2 |
| 弹出 3 | `[4, 2, 2]` | `[4, 2, 2]` | 2 |
| 弹出一个 2 | `[4, 2]` | `[4, 2]` | 2 |
| 再弹出一个 2 | `[4]` | `[4]` | 4 |

## 两个栈共同维护的不变量

数据栈非空时，辅助栈的栈顶总是所有数据的最小值；辅助栈从底部到顶部不递增。压入一个更大的数时，最小值没有变化，不需要增加记录。压入一个更小或相等的数时，记录一次新的最小值状态。

弹出时，如果移除的元素等于当前最小值，就同步弹出辅助栈；否则当前最小值不受影响。这两条规则配对使用，才能在重复值、负数、完全清空后重新压入等情况下继续成立。

## 完整 Python 实现

代码约定输入为整数，不考虑多个线程并发修改同一实例。空栈的 `pop`、`top` 和 `getMin` 都抛出 `IndexError`，保持一致；用正无穷作为初始哨兵容易让空栈查询悄悄返回一个并不存在的值，因此这里直接使用空列表。

```python
from itertools import product


class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x):
        self.stack.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        x = self.stack.pop()
        if x == self.mins[-1]:
            self.mins.pop()
        return x

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mins[-1]


s = MinStack()
for value in [4, 2, 2, 3]:
    s.push(value)
assert s.pop() == 3
assert s.pop() == 2
assert s.getMin() == 2
assert s.pop() == 2
assert s.getMin() == 4
assert s.pop() == 4
for operation in (s.pop, s.top, s.getMin):
    try:
        operation()
    except IndexError:
        pass
    else:
        raise AssertionError("empty stack did not raise IndexError")
s.push(-5)
assert s.top() == s.getMin() == -5

# 用普通列表作为参照，覆盖负数、重复值和不同压入顺序。
for values in product(range(-1, 2), repeat=4):
    s, reference = MinStack(), []
    for value in values:
        s.push(value)
        reference.append(value)
        assert s.top() == reference[-1]
        assert s.getMin() == min(reference)
    while reference:
        assert s.pop() == reference.pop()
        if reference:
            assert s.top() == reference[-1]
            assert s.getMin() == min(reference)
    assert s.stack == s.mins == []
print("min-stack checks passed")
```

代码适用于 Python 3.9 及以上版本，保存后直接执行即可。参照检查故意使用较慢但直接的 `min(reference)`，以便从外部行为验证辅助栈，而不是再写一份相同实现来互相比较。

## 成本与另一种保存方式

`top` 和 `getMin` 只读取末尾元素，时间是 O(1)。Python 列表尾部压入、弹出的成本按一串操作计算为均摊 O(1)，因此这里的 `push`、`pop` 也应表述为均摊 O(1)，不能把一次扩容的成本忽略后宣称每次都严格恒定。

辅助栈的最坏空间是 O(n)。例如输入持续递减，或者全部相等时，每次压入都会保存一条记录。它只是在部分输入上比为每个元素保存最小值节省空间，并没有改变最坏空间复杂度。

另一种实现是每个数据栈元素都存 `(当前值, 此时的最小值)`。这样弹出一个元素就同时撤销一份最小值快照，不需要同步两个列表；代价是每次压入都增加一份记录。两种实现都围绕同一个事实：最小值必须能随栈操作回退，单独保存一个全局最小值做不到这一点。
