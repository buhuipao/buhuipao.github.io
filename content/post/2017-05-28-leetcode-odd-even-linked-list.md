---
title: LeetCode–odd-even-linked-list
author: 咩
type: post
date: 2017-05-28T11:43:15+00:00
url: /2017/05/28/leetcode-odd-even-linked-list/
post_views_count:
  - "8"
flashPic:
  - .
flag:
  - .
categories:
  - Algorithm
  - Python
tags:
  - head
  - ps
  - python
  - 链表

---
最近主要练习链表的变换，这个题很经典，特别是容易忽略末尾出现的闭环
  
Given a singly linked list, group all odd nodes together followed by the even nodes.
  
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
  
Given 1->2->3->4->5->NULL,
  
return 1->3->5->2->4->NULL.

Note:
  
The relative order inside both the even and odd groups should remain as it was in the input.
  
The first node is considered odd, the second node even and so on &#8230;

<pre class="lang:python decode:1 " ># _*_ coding: utf-8 _*_

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        解题思路：就是另外申请一个l2链表用于连接不断便利过程中被取出的偶数项目,最后拼接l1,l2
        """
        if not (head and head.next and head.next.next):
            return head
        pre_l2 = ListNode(None)
        l2 = head.next
        pre_l2.next = l2
        node = head.next.next
        head.next = node
        while node and node.next:
            temp = node.next.next
            l2.next = node.next
            l2 = l2.next
            if not temp:
                break
            node.next = temp
            node = node.next
        node.next = pre_l2.next
        # 防止奇数个数节点时最后一个点出现闭环，将出现TLE错误
        l2.next = None
        return head
</pre>