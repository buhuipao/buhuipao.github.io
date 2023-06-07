---
title: LeetCode-Binary_Search_Tree_Iterator
author: 咩
type: post
date: 2017-06-30T17:05:57+00:00
url: /2017/07/01/leetcode-binary_search_tree_iterator/
categories:
  - Algorithm
  - Python
tags:
  - BST
  - leetcode
  - 设计

---
一个比较有意思的设计题，需要你设计一个BST的迭代器，不断返回最小值，其实就是中序遍历的过程，然后就是怎么把中序遍历过程用类实现，我给出了两者做法，前一种比较容易实现无需考虑太多，后一种由于加入了hash表所以考虑多一点；原题链接：<a href="https://leetcode.com/problems/binary-search-tree-iterator/" 
target="_blank">https://leetcode.com/problems/binary-search-tree-iterator/</a>

Implement an iterator over a binary search tree (BST).
  
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
  
where h is the height of the tree.

```python
# _*_ coding: utf-8 _*_


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator1(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        典型的BST的中序遍历
        """
        self.cur_node = root.left if root else None
        self.stack = [root] if root else []

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack or self.cur_node

    def next(self):
        """
        :rtype: int
        """
        while self.cur_node:
            self.stack.append(self.cur_node)
            self.cur_node = self.cur_node.left
        self.cur_node = self.stack.pop()
        val = self.cur_node.val
        self.cur_node = self.cur_node.right
        return val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
```

下面是hash表加中序遍历BST的做法，因为考虑到时间复杂为O(1)的做法最常用就是hash表，也确实让next()操作的时间复杂度变成了O(1), 但是由于hash表的存在，内存复杂度一直是O(n);

```python
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        BST的中序遍历, 建立一个hash表
        """
        self.dict = {}
        cur_node = root.left if root else None
        stack = [root] if root else []
        _min = float('-inf')
        while stack or cur_node:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            val = cur_node.val
            self.dict[_min] = val
            _min = val
            cur_node = cur_node.right
        # 考虑stack为空的情形，显然不让进hashNext的循环
        if not self.dict:
            self.max = float('-inf')
        else:
            self.max = val
        self.val = float('-inf')

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.val &lt; self.max

    def next(self):
        """
        :rtype: int
        """
        result = self.dict[self.val]
        self.val = result
        return result
```