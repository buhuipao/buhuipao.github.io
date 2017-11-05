---
title: LeetCode-Lowest_Common_Ancestor_of_a_Binary_Search_Tree
author: 咩
type: post
date: 2017-06-06T09:15:08+00:00
url: /2017/06/06/leetcode-lowest_common_ancestor_of_a_binary_search_tree/
post_views_count:
  - "11"
flashPic:
  - .
flag:
  - .
categories:
  - Algorithm
  - Python
tags:
  - BST
  - 算法

---
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

<pre class="lang:bash decode:1 " >_______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
</pre>

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
  
BST的最近公共祖先

<pre class="lang:python decode:1 " ># _*_ coding: utf-8 _*_


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        _s, _b = sorted([p.val, q.val])
        # 假如满足条件则表明，两个节点在一侧，左侧或者右侧
        while not _s &lt;= root.val &lt;= _b:
            root = root.left if root.val &gt; _s else root.right
        return root
</pre>