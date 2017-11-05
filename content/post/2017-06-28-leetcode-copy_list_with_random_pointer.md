---
title: LeetCode-Copy_List_with_Random_Pointer
author: 咩
type: post
date: 2017-06-28T08:31:03+00:00
url: /2017/06/28/leetcode-copy_list_with_random_pointer/
categories:
  - Algorithm
  - Python
tags:
  - leetcode
  - 算法
  - 链表

---
一个比较经典的链表操作题，深度复制一个链表，链表包含一个next指针和一个random的指针，目前比较多的方法是hash表和自我复制法（在自己后面加一个自己），我写的是第二种方法需要注意的细节比较多，后面加了别人的hash表方法，原题链接：<a href="https://leetcode.com/problems/copy-list-with-random-pointer/" target="_blank">https://leetcode.com/problems/copy-list-with-random-pointer/</a>
  
A linked list is given such that each node contains an additional
  
random pointer which could point to any node in the list or null.

Return a deep copy of the list.

<pre class="lang:python decode:1"># _*_ coding: utf-8 _*_


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        node = head
        while node:
            temp = node.next
            node.next = RandomListNode(node.label)
            node.next.next = temp
            node = temp
        # 新的头节点
        n_head = head.next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            else:
                node.next.random = None
            node = node.next.next
        node = head
        while node:
            temp = node.next
            node.next = temp.next
            # 判定是否为最后的节点
            if node.next:
                temp.next = node.next.next
            else:
                temp.next = None
            node = node.next
        return n_head
</pre>

hash表方法：

<pre class="lang:python decode:1">class Solution(object):
    def Clone(self, pHead):
        # write code here
         
        head = pHead
        p_head = None
        new_head = None
         
        random_dic = {}
        old_new_dic = {}
         
        while head:
            node = RandomListNode(head.label)
            node.random = head.random
            old_new_dic[id(head)] = id(node)
            random_dic[id(node)] = node
            head = head.next
             
            if new_head:
                new_head.next = node
                new_head = new_head.next
            else:
                new_head = node
                p_head = node
                 
        new_head = p_head
        while new_head:
            if new_head.random != None:
                new_head.random = random_dic[old_new_dic[id(new_head.random)]]
            new_head = new_head.next
        return p_head
</pre>