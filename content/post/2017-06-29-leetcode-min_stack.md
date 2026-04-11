---
title: LeetCode-Min_Stack
author: 咩
type: post
date: 2017-06-29T03:08:00+00:00
url: /2017/06/29/leetcode-min_stack/
categories:
  - 算法
  - Python
tags:
  - LeetCode
  - 栈
  - 数据结构

---
经典的stack相关的设计题，实现一个栈要求能够O(1)时间获取当前栈中最小元素，基本思路是：一个数据栈，另一个栈用栈顶存最小元素，如果弹栈弹得是最小元素，那么最小元素栈也弹栈。原题链接：<a href="https://leetcode.com/problems/min-stack/" target="_blank">https://leetcode.com/problems/min-stack/</a>
  
Design a stack that supports push, pop, top,
  
and retrieving the minimum element in constant time.

push(x) — Push element x onto stack.
  
pop() — Removes the element on top of the stack.
  
top() — Get the top element.
  
getMin() — Retrieve the minimum element in the stack.

```
# _*_ coding: utf-8 _*_


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = [float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x &lt;= self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

**复杂度分析：**
- 时间复杂度：O(1)，push/pop/top/getMin 均为常数时间
- 空间复杂度：O(n)，辅助栈存储最小值
