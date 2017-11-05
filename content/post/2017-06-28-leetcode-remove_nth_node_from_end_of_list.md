---
title: LeetCode-Remove_Nth_Node_From_End_of_List
author: 咩
type: post
date: 2017-06-28T08:18:03+00:00
url: /2017/06/28/leetcode-remove_nth_node_from_end_of_list/
categories:
  - Algorithm
  - Python
tags:
  - leetcode
  - 链表

---
比较简单的一个题，意思就是删除链表中倒数第几个节点，需要最后考虑下删除的是否恰巧为头节点，原题链接：<a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/" target="_blank">https://leetcode.com/problems/remove-nth-node-from-end-of-list/</a>
  
Given a linked list, remove the nth node from the end of list and return its head.
  
For example,

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
  
Note:
  
Given n will always be valid.
  
Try to do this in one pass.

<pre class="lang:python decode:1"># _*_ coding: utf-8 _*_


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0
        node = head
        while node:
            node = node.next
            i += 1
        count = i - n
        pre = ListNode(None)
        pre.next = head
        node = head
        while count:
            pre = node
            node = node.next
            count -= 1
        pre.next = node.next
        # 检查剔除的节点是否为头节点
        if node == head:
            return pre.next
        return head
</pre>