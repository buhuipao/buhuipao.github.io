---
title: LeetCode-Delect_Operation_for_Two_Strings
author: 咩
type: post
date: 2017-06-22T12:26:12+00:00
url: /2017/06/22/leetcode-delect_operation_for_two_strings/
categories:
  - Algorithm
  - Python
tags:
  - LCS
  - 动态规划
  - 算法

---
LCS的变形题目, 只要求出两个字符串的最长公共子序列，那么最终需要进行删除操作的就是m＋n－2*result。
  
Given two words word1 and word2, find the minimum number of steps required
  
to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
  
Input: &#8220;sea&#8221;, &#8220;eat&#8221;
  
Output: 2
  
Explanation: You need one step to make &#8220;sea&#8221; to &#8220;ea&#8221; and another step to make &#8220;eat&#8221; to &#8220;ea&#8221;.
  
Note:
  
The length of given words won&#8217;t exceed 500.
  
Characters in given words can only be lower-case letters.

<pre class="lang:python decode:1"># _*_ coding: utf-8 _*_


class Solution(object):
    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if not m or not n:
            return m or n
        dp = [[0] * (n+1) for i in xrange(m+1)]
        for i in xrange(m):
            for j in xrange(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return m + n - 2 * dp[i+1][j+1]
    
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        节省了空间，时间复杂度没变
        """
        m, n = len(word1), len(word2)
        if not m or not n:
            return m or n
        dp1, dp2 = [0] * (n+1), [0] * (n+1)
        for i in xrange(m):
            # 替换后一个dp
            dp1, dp2 = dp2, [0] * (n+1)
            for j in xrange(n):
                if word1[i] == word2[j]:
                    dp2[j+1] = dp1[j] + 1
                else:
                    dp2[j+1] = max(dp2[j], dp1[j+1])
        return m + n - 2 * dp2[j+1]
</pre>