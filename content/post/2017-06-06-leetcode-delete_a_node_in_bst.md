---
title: LeetCode-delete_a_node_in_BST
author: 咩
type: post
date: 2017-06-06T03:48:12+00:00
url: /2017/06/06/leetcode-delete_a_node_in_bst/
flag:
  - .
flashPic:
  - .
post_views_count:
  - "7"
categories:
  - Algorithm
  - Python
tags:
  - BST
  - python
  - 算法

---
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
  
If the node is found, delete the node.
  
Note: Time complexity should be O(height of tree).
  
也就是必须在树上爬着解决问题，不允许先遍历剔除再重新建树，下面是我写的第一个版本，用的迭代方法；

<pre class="lang:python decode:1 " ># _*_ coding: utf-8 _*_


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if not (root.left or root.right) and root.val ==key:
            return None
        cur = root
        # 标记变量
        finded, left, right = False, False, False
        pre = TreeNode(None)
        pre.right = root
        # 找到节点和父节点
        while cur:
            if cur.val &gt; key:
                pre = cur
                left, right = True, False
                cur = cur.left
            elif cur.val &lt; key:
                pre = cur
                left, right = False, True
                cur = cur.right
            else:
                finded = True
                break
        # 是否找到    
        if not finded:
            return root
        # 是否为叶子节点
        if not (cur.left or cur.right):
            if left:
                pre.left = None
            else:
                pre.right = None
            return root
        # 有右孩子，就把右子树的最左的点替换，最后再整理
        elif cur.right:
            node = cur.right
            while node.left:
                pre = node
                node = node.left
            cur.val = node.val
            # 如果右孩子就是最左点，那么沿用（右孩子的右孩子）为右孩子
            # 否则就把父节点的左孩子更新为当前节点的右孩子（用右孩子替换自己）
            if node == cur.right:
                cur.right = cur.right.right
            else:
                pre.left = node.right
            return root
        else:
            node = cur.left
            while node.right:
                pre = node
                node = node.right
            cur.val = node.val
            if node == cur.left:
                cur.left = cur.left.left
            else:
                pre.right = node.left
            return root
</pre>

下面的是看了LeetCode提交记录后，找到的递归方法, 万恶的递归:);

<pre class="lang:python decode:1 " >class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        
        if root == None:
            return root
        
        def findMax(node):
            while node.right:
                node = node.right
            return node
        
        if key &lt; root.val:
            root.left = self.deleteNode(root.left, key)
        elif key &gt; root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 如果左孩子为空，那么直接返回右孩子替换自己
            if root.left == None:
                return root.right
            # 如果右孩子为空，那么直接返回左孩子替换自己
            if root.right == None:
                return root.left
            else:
                # 找到左子树的最大值替换自己，然后在左子树里把它删掉
                node = findMax(root.left)
                root.val = node.val
                root.left = self.deleteNode(root.left, root.val)
        return root               
</pre>