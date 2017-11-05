---
title: LeetCode-Linked_List_Cycle_II
author: 咩
type: post
date: 2017-06-28T09:55:00+00:00
url: /2017/06/28/leetcode-linked_list_cycle_ii/
categories:
  - Algorithm
  - Python
tags:
  - leetcode
  - 算法
  - 链表

---
判断链表是否存在循环的变形题，需要你找出链表循环的开始节点，解题思路：先用快慢指针便利链表知道快慢指针指向同一个节点，然后让快指针从head重新开始走，这次每个指针一次只走一步，再一次指向相同节电的第一个就是要找的节点；

可以用简单的数学推导验证：设x为链表非循环段的长度，y为循环段长度，a为第一步相遇时的距离循环开始节点的顺时针偏移量，由第一步可以得出数学表达式：2 \* (x + a) = x + n \* Y + a, 其中n为自然数（0，1，3，..) , 然后解开可以得到等式：x = n * y &#8211; a, 也就是第二步的意思，x长度为n圈循环少a，然后又是第二步刚好是a位置开始，那么再一次相遇时肯定是循环的第一个节点。原题链接：<a href="https://leetcode.com/problems/linked-list-cycle-ii/" target="_blank">https://leetcode.com/problems/linked-list-cycle-ii/</a>
  
Given a linked list, return the node where the cycle begins.
  
If there is no cycle, return null.
  
Note: Do not modify the linked list.

Follow up:
  
Can you solve it without using extra space?

<pre class="lang:python decode:1"># _*_ coding: utf-8 _*_


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        找到一个链表的循环开始节点
        """
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast, slow = fast.next, slow.next
                return slow
        return
</pre>