---
title: LeetCode－－实现字典树
author: 咩
type: post
date: 2017-05-18T13:34:59+00:00
url: /2017/05/18/leetcode-imp-trietree/
post_views_count:
  - "11"
flashPic:
  - .
flag:
  - .
categories:
  - Algorithm
  - Python
tags:
  - python
  - 字典树
  - 算法

---
<pre class="lang:python decode:1 " >class TrieNode(object):
    def __init__(self):
        self.is_word = False
        # 某个节点是否为单词，一般默认为path（路径）
        # 当有单词录入时，变为True
        self.leaves = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        _cur = self.root
        for c in word:
            # 如果字母不存在于此节点的叶子里，就生成一个新节点
            if c not in _cur.leaves:
                _cur.leaves[c] = TrieNode()
            _cur = _cur.leaves[c]
            
        _cur.is_word = True
        
            def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        _cur = self.root
        for c in word:
            if c not in _cur.leaves:
                return False
            _cur = _cur.leaves[c]
        return True if _cur.is_word else False
        '''
        def _search(word, index, _cur):
            if len(word) == index:
                return _cur.is_word
            if word[index] in _cur.leaves:
                return _search(word, index+1, _cur.leaves[word[index]])
                
            return False
            
        return _search(word, 0, self.root)
        '''
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        '''
        def _search(word, index, _cur):
            if len(word) == index:
                return True
            if word[index] in _cur.leaves:
                return _search(word, index+1, _cur.leaves[word[index]])
                
            return False
            
        return _search(prefix, 0, self.root)
        '''
        _cur = self.root
        for c in prefix:
            if c not in _cur.leaves:
                return False
            _cur = _cur.leaves[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
</pre>

但是LeetCode的评分是73％ 400ms， 回头看看应该是节点类的抽象开销导致，于是改的简单点直接用字典实现：

<pre class="lang:python decode:1 " >class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        _cur = self.root
        for c in word:
            # 如果字母不存在于此节点的叶子里，就生成一个新节点｛｝
            if c not in _cur:
                _cur[c] = {}
            _cur = _cur[c]
            
        _cur['is_word'] = True
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """     
        _cur = self.root
        for c in word:
            if c not in _cur:
                return False
            _cur = _cur[c]
        return True if 'is_word' in _cur else False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        _cur = self.root
        for c in prefix:
            if c not in _cur:
                return False
            _cur = _cur[c]
        return True
</pre>