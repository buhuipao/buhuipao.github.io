---
title: LeetCode-Partition_List
author: 咩
type: post
date: 2017-06-28T17:08:33+00:00
url: /2017/06/29/leetcode-partition_list/
categories:
  - Algorithm
  - Python
tags:
  - leetcode
  - 算法
  - 链表

---
晚上送妹子回家后做了这个链表的题，怕自己忘了睡前总结下。
  
题目的意思就是：给定一个链表和一个数，把小于这个数的节点放前边，此外的都移到后边，而且保证两部分的节点原有顺序不变；在自己憋了一个来小时后终于AC了，后来对比其他人的提交结果，发现基本都是分成两个链表然后拼接，而我是在原有链表的基础上修改，虽然麻烦点，但也可以实现；对比自己之前对链表的操作，现在已经熟练多了。原题链接：<a href="https://leetcode.com/problems/partition-list/" target="_blank">https://leetcode.com/problems/partition-list/</a>
  
Given a linked list and a value x, partition it such that all
  
nodes less than x come before nodes greater than or equal to x.
  
You should preserve the original relative order of the nodes in each of the two partitions.

For example,
  
Given 1->4->3->2->5->2 and x = 3,
  
return 1->2->2->4->3->5.

```python
# _*_ coding: utf-8 _*_


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node = head
        while node and node.next:
            pre = node
            node = node.next.next
        # 确定老的尾巴
        if node:
            old_tail = node
        else:
            old_tail = pre.next
        # 确定新的头
        pre_head = ListNode(None)
        pre_head.next = head
        node = head
        while node:
            if node.val >= x:
                pre_head.next = node.next
                # 全部大于x
                if node == old_tail:
                    return head
                node = node.next
            else:
                break
        # 开始
        pre = ListNode(None)
        node = head
        tail = old_tail
        while node != old_tail:
            if node.val >= x:
                temp = node.next
                pre.next = temp
                tail.next = node
                node.next = None
                tail = tail.next
                node = temp
            else:
                pre = node
                node = node.next
        # 处理旧的尾巴
        if node.val >= x:
            tail.next = node
            temp = node.next
            pre.next = temp
            node.next = None
        return pre_head.next
```

下面是那种拆分成两个链表然后拼接的方法，确实比上面在原链表的基础上修改的简洁不容易出错。

```python
def partition1(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(None)
        h2 = l2 = ListNode(None)
        while head:
            if head.val &lt; x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l1.next = h2.next
        l2.next = None
        return h1.next
```