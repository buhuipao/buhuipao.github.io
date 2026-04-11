---
title: LeetCode–Convert_Sorted_List_to_Binary_Search_Tree
author: 咩
type: post
date: 2017-06-02T04:13:46+00:00
url: /2017/06/02/leetcode-convert_sorted_list_to_binary_search_tree/
categories:
  - 算法
  - Python
tags:
  - 二叉树
  - Python
  - 链表

---
Given a singly linked list where elements are sorted in ascending order,
  
convert it to a height balanced BST.

```python
# _*_ coding: utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        每次找到中位数，然后递归
        """
        if not head or not head.next:
            return TreeNode(head.val) if head else head
        
        slow, fast, pre = head, head, None
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        # 截断链表
        pre.next = None
        root = TreeNode(slow.val)
        # 递归查找中间位置的节点
        root.left, root.right = map(self.sortedListToBST, [head, slow.next])
        
        return root
```

**复杂度分析：**
- 时间复杂度：O(n * logn)，每层递归需 O(n) 找中点，共 logn 层
- 空间复杂度：O(logn)，递归调用栈深度