---
title: LeetCode–Remove-Linked-List-Elements
author: 咩
type: post
date: 2017-05-28T17:26:57+00:00
url: /2017/05/29/leetcode-remove-linked-list-elements/
categories:
  - 算法
  - Python
tags:
  - Python
  - 链表

---
Remove all elements from a linked list of integers that have value val.

Example
  
Given: 1 –> 2 –> 6 –> 3 –> 4 –> 5 –> 6, val = 6
  
Return: 1 –> 2 –> 3 –> 4 –> 5

```python
# _*_ coding: utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
                
        pre_head = ListNode(None)
        pre_head.next = head
        pre_node = pre_head

        while head:
            if head.val == val:
                pre_node.next = head.next
            else:
                pre_node = head
            head = head.next

        return pre_head.next
```

**复杂度分析：**
- 时间复杂度：O(n)，遍历一次链表
- 空间复杂度：O(1)，只使用了常数额外空间