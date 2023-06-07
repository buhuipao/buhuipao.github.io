---
title: LeetCode-Edit_Distance
author: 咩
type: post
date: 2017-06-22T14:52:57+00:00
url: /2017/06/22/leetcode-edit_distance/
categories:
  - Algorithm
  - Python
tags:
  - dp
  - 动态规划
  - 算法

---
比较特殊的动态规划过程，原题链接：<https://leetcode.com/problems/edit-distance/>
  
Given two words word1 and word2, find the minimum number of steps
  
required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
  
b) Delete a character
  
c) Replace a character

```python
# _*_ coding: utf-8 _*_


class Solution(object):
    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        "A B G C _ F"
        "_ B _ D E _"
        """
        n = len(word1)
        m = len(word2)
        if not m or not n:
            return m or n
        dp = [[0] * (n+1) for i in xrange(m+1)]
        for i in xrange(m+1):
            dp[i][0] = i
        for j in xrange(n+1):
            dp[0][j] = j
        for i in xrange(m):
            for j in xrange(n):
                if word1[j] != word2[i]:
                    temp = 1
                else:
                    temp = 0
                dp[i+1][j+1] = min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j]+temp)
        return dp[m][n]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        减少了空间复杂度，时间复杂度依然为O(m*n)
        """
        n = len(word1)
        m = len(word2)
        if not m or not n:
            return m or n
        dp1, dp2 = [0] * (m+1), [i for i in xrange(m+1)]
        for i in xrange(n):
            dp1, dp2 = dp2, [i+1] * (m+1)
            for j in xrange(m):
                if word1[i] != word2[j]:
                    diff = 1
                else:
                    diff = 0
                dp2[j+1] = min(dp1[j]+diff, dp1[j+1]+1, dp2[j]+1)
        return dp2[m]
```

**虽然这两种用法我都已经解出，但是回忆起又一次在线笔试题，计算编辑的成本我就细思极恐，比如插入一个字符消耗1个能量，删除一个字符消耗2个能量，替换一个字符消耗3个能量，给定两个字符串求最少的编辑能耗&#8230;待我想出来了再给出解题代码，知道解法的大神也请联系我，已跪！**