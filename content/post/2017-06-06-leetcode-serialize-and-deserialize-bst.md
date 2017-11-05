---
title: LeetCode-Serialize and Deserialize BST
author: 咩
type: post
date: 2017-06-06T08:09:10+00:00
url: /2017/06/06/leetcode-serialize-and-deserialize-bst/
post_views_count:
  - "12"
flashPic:
  - .
flag:
  - .
categories:
  - Algorithm
  - Python
tags:
  - Algorithm
  - BST
  - IP
  - python
  - 二叉树
  - 序列化
  - 算法

---
序列化和反序列化一个二叉搜索树，题目的意思是想让我利用搜索树的性质来做，但是我还是坚持了使用按层和先序遍历的方法，仅供参考，原题如下：

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
  
先提供简单无脑的按层遍历序列化：

<pre class="lang:python decode:1 " >class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize1(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        _queue = [root]
        result = []
        while _queue:
            node = _queue.pop(0)
            if node:
                result.append(node.val)
                _queue.append(node.left)
                _queue.append(node.right)
            else:
                result.append('#')
        return '$'.join(map(str, result))
        

    def deserialize1(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split('$')
        root = TreeNode(data[0])
        _queue = [root]
        for i in xrange(1, len(data), 2):
            node = _queue.pop(0)
            if data[i] != '#':
                node.left = TreeNode(data[i])
                _queue.append(node.left)
            if data[i+1] != '#':
                node.right = TreeNode(data[i+1])
                _queue.append(node.right)
        return root
</pre>

接下来的是先序遍历的序列化和反序列化， 之前一直报｀空栈错误｀ ，最后单步调试发现是最后的一个叶子节点的问题，会多出两个&#8217;#&#8217;， 所以反序列化只迭代了倒数第三个字符`xrange(1, len(data)-2, 1)`；其实也可以在序列化时｀return &#8216;$&#8217;.join(result).rstrip(&#8216;#&#8217;)\`, 应该是我没真正掌握先序遍历的‘精髓’:P

<pre class="lang:python decode:1 " >def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        先序遍历
        """
        if not root:
            return ''
        _stack = [root]
        node = root
        result = []
        while _stack:
            node = _stack.pop(-1)
            if node:
                result.append(str(node.val))
                _stack.append(node.right)
                _stack.append(node.left)
            else:
                result.append('#')
        return '$'.join(result)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = data.split('$')
        
        root = TreeNode(int(data[0]))
        node = root
        right = False
        _stack = [root]
        for i in xrange(1, len(data)-2, 1):
            if data[i] != '#':
                if not right:
                    node.left = TreeNode(int(data[i]))
                    node = node.left
                else:
                    node.right = TreeNode(int(data[i]))
                    node = node.right
                _stack.append(node)
                right = False
            else:
                # 更新标记点，指导树枝往右生长
                right = True
                node = _stack.pop(-1)
                
        return root
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
</pre>