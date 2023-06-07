---
title: LeetCode–reverse_linked_list_II
author: 咩
type: post
date: 2017-06-01T12:50:11+00:00
url: /2017/06/01/leetcode-reverse_linked_list_ii/
flag:
  - .
flashPic:
  - .
post_views_count:
  - "6"
categories:
  - Algorithm
  - Python
tags:
  - head
  - python
  - 链表

---
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
  
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
  
Given m, n satisfy the following condition:
  
1 ≤ m ≤ n ≤ length of list.

```python
# _*_ coding: utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        diff, dummy, cur = n - m + 1, ListNode(None), head
        dummy.next = head
        # 最后未交换的节点
        last_unswapped = dummy
        while cur and m &gt; 1:
            cur, last_unswapped, m = cur.next, cur, m - 1
        
        prev, first_swapped = last_unswapped,  cur
        while cur and diff &gt; 0:
            cur.next, prev, cur, diff = prev, cur, cur.next, diff - 1
        # 最后调转车头    
        last_unswapped.next, first_swapped.next = prev, cur
        
        return dummy.next
```