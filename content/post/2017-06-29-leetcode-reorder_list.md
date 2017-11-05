---
title: LeetCode-Reorder_List
author: 咩
type: post
date: 2017-06-29T02:40:50+00:00
url: /2017/06/29/leetcode-reorder_list/
categories:
  - Algorithm
  - Python
tags:
  - leetcode
  - 算法
  - 链表

---
经典的链表题，考查了反转链表和一些细节，题意也很明白，把L0→L1→…→Ln-1→Ln变为L0→Ln→L1→Ln-1→L2→Ln-2→…即可，原题链接：<a href="https://leetcode.com/problems/reorder-list/" target="_blank">https://leetcode.com/problems/reorder-list/</a>
  
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
  
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
  
You must do this in-place without altering the nodes&#8217; values.

For example,
  
Given {1,2,3,4}, reorder it to {1,4,2,3}.

<pre class="lang:python decode:1"># _*_ coding: utf-8 _*_

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            pre = ListNode(None)
            slow = fast = head
            while fast and fast.next:
                pre = slow
                slow, fast = slow.next, fast.next.next
            # 确定l2的头节点，下面是链表长度为奇数时,之后是长度为偶数时
            if fast:
                l2, slow.next = slow.next, None
            else:
                l2, pre.next = slow, None
            pre_l2 = None
            # 反转l2
            while l2 and l2.next:
                temp = l2.next
                l2.next = pre_l2
                pre_l2 = l2
                l2 = temp
            l2.next = pre_l2
            # 合并head，l2
            l1 = head
            while l2:
                temp2 = l2.next
                temp1 = l1.next
                l1.next = l2
                l2.next = temp1
                l1, l2 = temp1, temp2
</pre>