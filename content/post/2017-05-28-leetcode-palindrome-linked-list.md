---
title: LeetCode–Palindrome-Linked-List
author: 咩
type: post
date: 2017-05-28T15:41:00+00:00
url: /2017/05/28/leetcode-palindrome-linked-list/
flag:
  - .
flashPic:
  - .
post_views_count:
  - "7"
categories:
  - Algorithm
  - Python
tags:
  - head
  - python
  - 链表

---
Given a singly linked list, determine if it is a palindrome.

Follow up:
  
Could you do it in O(n) time and O(1) space?

```python
# _*_ coding: utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        if not head.next.next:
            if head.val == head.next.val:
                return True
            else:
                return False
        slow = head
        fast = head.next
        pre_node = None
        while fast and fast.next:
            fast = fast.next.next
            # 反转链表
            temp = slow.next
            slow.next = pre_node
            pre_node = slow
            slow = temp
            
        # 节点个数为偶数
        if fast:
            l2 = slow.next
            slow.next = pre_node
            l1 = slow
        else:
            l1 = pre_node
            l2 = slow.next
        
        while l1:
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next
        return True
            
```