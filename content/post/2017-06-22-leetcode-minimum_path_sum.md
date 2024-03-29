---
title: LeetCode-minimum_path_sum
author: 咩
type: post
date: 2017-06-22T03:27:52+00:00
url: /2017/06/22/leetcode-minimum_path_sum/
categories:
  - Algorithm
  - Network
tags:
  - dp
  - 动态规划
  - 算法

---
经典的动态规划题，三种解法都是动态规划，但是最后一种空间复杂度最小，原题链接：
  
<https://leetcode.com/problems/minimum-path-sum/>
  
Given a m x n grid filled with non-negative numbers,
  
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

```python
# _*_ coding: utd-8 _*_


class Solution(object):
    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[i][j]
        
    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][i]
                elif i != 0 and j == 0:
                    dp[j] = dp[j] + grid[i][j]
                elif i == 0 and j != 0:
                    dp[j] = dp[j-1] + grid[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[j]
        
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        由于走过的项已经无用了，不申请空间直接覆盖原矩阵
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if i != 0 and j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif i == 0 and j != 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif i != 0 and j != 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[i][j]
```