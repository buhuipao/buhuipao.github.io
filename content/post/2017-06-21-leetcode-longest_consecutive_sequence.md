---
title: LeetCode-Longest_Consecutive_Sequence
author: 咩
type: post
date: 2017-06-21T09:46:10+00:00
url: /2017/06/21/leetcode-longest_consecutive_sequence/
categories:
  - Algorithm
  - Python
tags:
  - 算法
  - 连续子序列

---
题目的意思就是求出列表里最长的连续序列, 原题如下：

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
  
Given [100, 4, 200, 1, 3, 2],
  
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

下面采用了三种不同的方法进行求解， 分别是排序统计、并查集、集合，最后一种为最优解也是最巧妙的

<pre class="lang:python decode:1"># _*_ coding: utf-8 _*_


class UnionFind(object):
    def __init__(self, n):
        self.list = range(n)
        self.size = [1] * n
    
    def root(self, i):
        while self.list[i] != i:
            self.list[i] = self.list[self.list[i]]
            i = self.list[i]
        return i
    
    def union(self, q, p):
        q_root, p_root = self.root(q), self.root(p)
        if q_root == p_root:
            return True
        if self.size[q_root] >= self.size[p_root]:
            self.list[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.list[q_root] = p_root
            self.size[p_root] += self.size[q_root]
    
    def find(self, x, y):
        return self.root(x) == self.root(y)


class Solution(object):
    def longestConsecutive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        明显超时(NlogN)
        """
        if len(nums) &lt; 2:
            return len(nums)
        _nums, cnt, result = sorted(nums), 1, 0
        for i in xrange(1, len(_nums)):
            if _nums[i] - _nums[i-1] == 1:
                cnt += 1
            else:
                result = max(cnt, result)
                cnt = 1
        return max(result, cnt)
        
    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        unionfind(N)
        """
        nums = set(nums)
        if len(nums) &lt; 2:
            return len(nums)
        unionfind, record = UnionFind(len(nums)), {}
        for i, num in enumerate(nums):
            if num - 1 in record:
                unionfind.union(i, record[num-1])
            if num + 1 in record:
                unionfind.union(i, record[num+1])
            record[num] = i
        return max(unionfind.size)
    
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        最巧妙的方法，实际操作步骤const * N,时间复杂度为O(N),空间复杂度为O(N)
        """
        result = 0
        nums = set(nums)
        for num in nums:
            # 每次只找到一个连续序列的最小值才进入下面步骤
            if num - 1 not in nums:
                Plus_one = num + 1
                while Plus_one in nums:
                    Plus_one += 1
                result = max(result, Plus_one-num)
        return result
</pre>