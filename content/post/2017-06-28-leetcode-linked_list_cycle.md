---
title: LeetCode-Linked_List_Cycle
author: 咩
type: post
date: 2017-06-28T09:30:13+00:00
url: /2017/06/28/leetcode-linked_list_cycle/
categories:
  - Algorithm
  - Python
tags:
  - leetcode
  - 算法
  - 链表

---
经典的链表题，判断一个链表是否存在循环，而且不许使用额外的空间，解题思路：只要分别设定一个快慢指针，当快慢指针重合时就证明有循环，原题链接：<a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank">https://leetcode.com/problems/linked-list-cycle/</a>
  
Given a linked list, determine if it has a cycle in it.

Follow up:
  
Can you solve it without using extra space?

<pre class="lang:python decode:1"># _*_ coding: utf-8 _*_

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        判断一个链表是不是存在循环
        """
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        return False
</pre>