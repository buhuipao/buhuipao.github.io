---
title: LeetCode-Top_K_Frequent_Elements
author: 咩
type: post
date: 2017-06-04T17:29:09+00:00
url: /2017/06/05/leetcode-top_k_frequent_elements/
flag:
  - .
flashPic:
  - .
post_views_count:
  - "6"
categories:
  - Algorithm
  - Python
tags:
  - Algorithm
  - python
  - 堆
  - 排序

---
Given a non-empty array of integers, return the k most frequent elements.

For example,
  
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
  
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
  
Your algorithm&#8217;s time complexity must be better than O(n log n), where n is the array&#8217;s size.

```python
# _*_ coding: utf-8 _*_

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        if len(nums) &lt;= 1:
            return nums
            
        left = lambda i: 2 * i + 1
        right = lambda i: 2 * i + 2
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        _nums = num_dict.items()
        def heap(_nums, i, k):
            while True:
                if left(i) &lt; k and _nums[left(i)][1] &lt; _nums[i][1]:
                    _min = left(i)
                else:
                    _min = i
                if right(i) &lt; k and _nums[right(i)][1] &lt; _nums[_min][1]:
                    _min = right(i)
                if _min == i:
                    break
                _nums[i], _nums[_min] = _nums[_min], _nums[i]
                i = _min
        # 建立调整小根堆
        for i in xrange(k-1, -1, -1):
            heap(_nums, i, k)
        
        for num in _nums[k:]:
            if num[1] &gt; _nums[0][1]:
                _nums[0] = num
                heap(_nums, 0, k)
        return [i for [i, j] in _nums[:k]]
```