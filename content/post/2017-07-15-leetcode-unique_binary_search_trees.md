---
title: LeetCode-Unique_Binary_Search_Trees
author: 咩
type: post
date: 2017-07-15T01:13:02+00:00
url: /2017/07/15/leetcode-unique_binary_search_trees/
categories:
  - Algorithm
  - Python
tags:
  - BST
  - leetcode
  - tree

---
题目的意思就是给你1到n个数，你能组成多少种BST，解题思路就是：以每一个数做一次BST的root节点，然后求和所有次数即可，然后每次以i为root时， 左子树有i-1个点，右子树有n-i各点，得到递推式：dp[i] += dp[j-1] * dp[i-j]，最后求和即可，原题链接：<a href="https://leetcode.com/problems/unique-binary-search-trees/" target="_blank">https://leetcode.com/problems/unique-binary-search-trees/</a>
  
Given n, how many structurally unique BST&#8217;s (binary search trees) that store values 1&#8230;n?

For example,
  
Given n = 3, there are a total of 5 unique BST&#8217;s.

<pre class="lang:shell decode:1">1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
</pre>

<pre class="lang:python decode:1"># _*_ coding: utf-8 _*_


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        每次以i为root节点，那么求n就是以1, 2, 3...n为root节点的总和
        但必须先构建n之前节点的树，求出1～(n-1)的结果
        """
        if n &lt; 0:
            return 0
        dp = [0] * (n + 1)
        # 空树和一个节点
        dp[0] = dp[1] = 1
        i = 2
        while i &lt;= n:
            # 构建n之前的树
            for j in xrange(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
            i += 1
        return dp[n]
</pre>