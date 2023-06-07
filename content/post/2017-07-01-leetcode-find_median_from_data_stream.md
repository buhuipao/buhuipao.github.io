---
title: LeetCode-Find_Median_from_Data_Stream
author: 咩
type: post
date: 2017-07-01T04:42:14+00:00
url: /2017/07/01/leetcode-find_median_from_data_stream/
categories:
  - Algorithm
  - Python
tags:
  - heap
  - leetcode
  - 二分法

---
LeetCode的一道设计题，快速找到已添加的数据的中位数，下面给出的方法添加的时间复杂度为max(n/2, logn), 查找的时间复杂度为O(1), 之后会给出添加时间复杂度为O(logn)查找O(1)的解法，其实就是维护两个堆（一个大根堆一个小根堆）；原题链接：<a href="https://leetcode.com/problems/find-median-from-data-stream/" target="_blank">https://leetcode.com/problems/find-median-from-data-stream/</a>

Median is the middle value in an ordered integer list.
  
If the size of the list is even, there is no middle value.
  
So the median is the mean of the two middle value.
  
Examples:
  
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) &#8211; Add a integer number from the data stream to the data structure.
  
double findMedian() &#8211; Return the median of all elements so far.
  
For example:

addNum(1)
  
addNum(2)
  
findMedian() -> 1.5
  
addNum(3)
  
findMedian() -> 2

```python
# _*_ coding: utf-8 _*_ 


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.count = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        二分查找
        """
        l, h = 0, self.count - 1
        mid = 0
        while l &lt;= h:
            mid = (l + h) / 2
            if num &lt;= self.list[mid]:
                h = mid - 1
            else:
                l = mid + 1
        # 我们知道list的插入操作时间复杂度为O(n)
        self.list.insert(l, num)
        self.count += 1

    def findMedian(self):
        """
        :rtype: float
        """
        mid = self.count / 2
        if self.count % 2 == 1:
            return float(self.list[mid])
        else:
            return float(self.list[mid] + self.list[mid-1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```