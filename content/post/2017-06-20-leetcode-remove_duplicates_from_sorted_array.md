---
title: LeetCode-Remove_Duplicates_from_Sorted_Array
author: 咩
type: post
date: 2017-06-20T05:13:19+00:00
url: /2017/06/20/leetcode-remove_duplicates_from_sorted_array/
categories:
  - Algorithm
  - Python
tags:
  - 算法

---
题目比较简单，就是需要你找出数组里面不同数字的个数，但是也要求把这些项搬运到nums数组的前面去

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
  
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
  
It doesn&#8217;t matter what you leave beyond the new length.

```python
# _*_ coding: utf-8 _*_


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        题目要求你返回最后不同元素的个数，但是也会检查你的元素nums[:count+1]是否排列正确
        比如INPUT：［1，1，2］，返回2，但是nums[:2]必须为[1, 2], 最终nums为：[1, 2, 2]
        """
        if not nums:
            return 0
        count = 0
        for i in xrange(1, len(nums)):
            if nums[i-1] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count+1
```