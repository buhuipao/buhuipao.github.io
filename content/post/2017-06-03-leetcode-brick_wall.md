---
title: LeetCode–brick_wall
author: 咩
type: post
date: 2017-06-03T04:59:20+00:00
url: /2017/06/03/leetcode-brick_wall/
flag:
  - .
flashPic:
  - .
post_views_count:
  - "7"
categories:
  - Algorithm
  - Python
tags:
  - hashtab
  - HTTPS
  - ps
  - python
  - 算法

---
比较有意思的题， 求最少穿过的砖的块数，原题连接：<https://leetcode.com/problems/brick-wall/>

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks.
  
The bricks have the same height but different width.
  
You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows.
  
Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed.
  
You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall,
  
in which case the line will obviously cross no bricks.

```python
# _*_ coding: utf-8 _*_


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        width_dict = {}
        for row in wall:
            width = 0
            for i in xrange(len(row)-1):
                # 增加宽度
                width += row[i]
                if width not in width_dict:
                    width_dict[width] = 0
                width_dict[width] += 1
        if not width_dict:
            return len(wall)
        return len(wall) - max(width_dict.values())
```