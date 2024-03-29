---
title: LeetCode-Longest_Increasing_Subsequence
author: 咩
type: post
date: 2017-06-23T10:03:46+00:00
url: /2017/06/23/leetcode-longest_increasing_subsequence/
categories:
  - Algorithm
  - Python
tags:
  - LIS
  - 动态规划
  - 算法

---
经典的dp题目：最长增长子序列，都是dp的方法但是时间复杂度分别为O(N^2)、O(NlogN);原题链接：<a href="https://leetcode.com/problems/longest-increasing-subsequence/" target="_blank">https://leetcode.com/problems/longest-increasing-subsequence/</a>
  
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
  
Given [10, 9, 2, 5, 3, 7, 101, 18],
  
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
  
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

```python
# _*_ coding: utf-8 _*_


class Solution(object):
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        时间复杂度O(N^2)
        dp状态方程：
            dp[0] = 1
            dp[i] = max(dp[i], dp[j]+biger(nums[i], nums[j]))
        其中0 &lt;= j &lt; i, biger函数返回1／0
        """
        size = len(nums)
        dp = [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y] + 1)
        return max(dp) if dp else 0

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        时间复杂度O(NlogN)
        dp遇到数原则上大于最后的dp[-1]的将会被append，
        小于的会去替换相应位置的数，而dp长度(l)不会缩短一只保持最长
        """
        size = len(nums)
        l = 0
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low &lt;= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
                l += 1
            else:
                dp[low] = nums[x]
        return l
```