---
title: LeetCode–Remove-Linked-List-Elements
author: 咩
type: post
date: 2017-05-28T17:26:57+00:00
url: /2017/05/29/leetcode-remove-linked-list-elements/
flag:
  - .
flashPic:
  - .
post_views_count:
  - "8"
categories:
  - Algorithm
  - Python
tags:
  - head
  - python
  - 链表

---
Remove all elements from a linked list of integers that have value val.

Example
  
Given: 1 &#8211;> 2 &#8211;> 6 &#8211;> 3 &#8211;> 4 &#8211;> 5 &#8211;> 6, val = 6
  
Return: 1 &#8211;> 2 &#8211;> 3 &#8211;> 4 &#8211;> 5

<pre class="lang:python decode:1 " ># _*_ coding: utf-8 _*_


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
</pre>