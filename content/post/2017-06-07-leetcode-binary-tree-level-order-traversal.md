---
title: LeetCode-binary-tree-level-order-traversal
author: 咩
type: post
date: 2017-06-07T07:30:11+00:00
url: /2017/06/07/leetcode-binary-tree-level-order-traversal/
post_views_count:
  - "9"
flashPic:
  - .
flag:
  - .
categories:
  - Algorithm
  - Python
tags:
  - BFS
  - python
  - 算法

---
Given a binary tree, return the level order traversal of its nodes&#8217; values. (ie, from left to right, level by level).

For example:
  
Given binary tree [3,9,20,null,null,15,7],

```bash
    3
   / \
  9  20
    /  \
   15   7
```

return its level order traversal as:

```bash
[
  [3],
  [9,20],
  [15,7]
]
```

```python
# _*_ coding: utf-8 _*_


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        n_last = last = root
        _queue = [root]
        result, temp = [], []
        while _queue:
            node = _queue.pop(0)
            temp.append(node.val)
            if node.left:
                _queue.append(node.left)
                n_last = node.left
            if node.right:
                _queue.append(node.right)
                n_last = node.right
            if node == last:
                result.append(temp)
                last = n_last
                temp = []
        return result

    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, level = [], [root]
        while root and level:
            # 先倒出所有不为空的叶子
            res.append([n.val for n in level if n])
            # 用之前的叶子找到下一层不为空的叶子
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return res
```