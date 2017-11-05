---
title: LeetCode–longest_substring_without_repeating_char
author: 咩
type: post
date: 2017-06-03T03:46:40+00:00
url: /2017/06/03/leetcode-longest_substring_without_repeating_char/
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
  - BST
  - hashtab
  - python
  - 算法

---
这是一个面试的经典题，明显是个送分题：）
  
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given &#8220;abcabcbb&#8221;, the answer is &#8220;abc&#8221;, which the length is 3.

Given &#8220;bbbbb&#8221;, the answer is &#8220;b&#8221;, with the length of 1.

Given &#8220;pwwkew&#8221;, the answer is &#8220;wke&#8221;, with the length of 3. Note that the answer must be a substring,
  
&#8220;pwke&#8221; is a subsequence and not a substring.

<pre class="lang:python decode:1 " ># _*_ coding: utf-8 _*_


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        result = 1
        index = {}
        pw_index = -1
        temp = 0
        for i in xrange(len(s)):
            if s[i] not in index:
                index[s[i]] = i
                # 防止全是不重复的字符，必须用temp记录经过的次数
                temp += 0
            else:
                # 更新前一个不重复子字串的索引位置
                if index[s[i]] &gt; pw_index:
                    pw_index = index[s[i]]
                # 重置temp
                temp = 0
                # 记录字符前一次出现位置
                index[s[i]] = i
            result = max(result, temp, i-pw_index)
        return result
</pre>