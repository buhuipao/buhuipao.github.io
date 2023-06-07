---
title: LeetCode－－字典树的添加和搜索单词
author: 咩
type: post
date: 2017-05-18T08:44:26+00:00
url: /2017/05/18/leetcode_trietree/
post_views_count:
  - "9"
flag:
  - .
flashPic:
  - .
categories:
  - Python
tags:
  - python
  - 字典树

---
```python
# _*_ coding: utf-8 _*_

'''
设计一种添加和搜索单词的数据结构
Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)
    search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

    For example:

        addWord("bad")
        addWord("dad")
        addWord("mad")
        search("pad") -&gt; false
        search("bad") -&gt; true
        search(".ad") -&gt; true
        search("b..") -&gt; true
        Note:
            You may assume that all words are consist of lowercase letters a-z.
'''


class TrieNode(object):
    '''
    初始化前缀树（字典树）
    '''
    def __init__(self):
        self.leaves = {}
        # 标记是否为单词的属性, 如果此节点存入了单词，此属性为True
        # 如果是路径，为False
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        like this:
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        # 修改此节点的是否为单词的属性为True
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(word, 0, self.root)

    def _search(self, word, index, cur):
        # 如果对比到单词的末尾(索引为单词长度),
        # 如果此节点不仅为路径还是单词就返回之前存入的True, 否则返回初始化的False
        if index == len(word):
            return cur.is_word

        # 如果此字母在当前节点叶子里, 继续往下一个叶子节点查找
        if word[index] in cur.leaves:
            return self._search(word, index+1, cur.leaves[word[index]])
        # 如果字母是'.'，则跳过当前节点，直接往下搜索所有叶子
        # 只要有一条路径返回True，就最终返回True
        elif word[index] == '.':
            for c in cur.leaves:
                if self._search(word, index+1, cur.leaves[c]):
                    return True
        return False

```