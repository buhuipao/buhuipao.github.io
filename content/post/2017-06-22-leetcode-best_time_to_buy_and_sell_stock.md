---
title: LeetCode-Best_Time_to_Buy_and_Sell_Stock
author: 咩
type: post
date: 2017-06-22T04:21:50+00:00
url: /2017/06/22/leetcode-best_time_to_buy_and_sell_stock/
categories:
  - Algorithm
  - Python
tags:
  - dp
  - 动态规划
  - 算法

---
动态规划的小题目，买卖股票， 原题链接：<a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/" target="_blank">https://leetcode.com/problems/best-time-to-buy-and-sell-stock/</a>

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
  
design an algorithm to find the maximum profit.

Example 1:
  
Input: [7, 1, 5, 3, 6, 4]
  
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
  
Example 2:
  
Input: [7, 6, 4, 3, 1]
  
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

<pre class="lang:python decode:1"># _*_ coding: utf-8 _*_


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        用dp记录最大收益，以及之前的时段的最低价格
        """
        if not prices:
            return 0
        dp = [0, prices[0]]
        for i in xrange(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                dp[0] = max(prices[i] - dp[1], dp[0])
            dp[1] = min(prices[i], dp[1])
        return dp[0]
</pre>