---
title: LeetCode-Design_Twitter
author: 咩
type: post
date: 2017-06-29T07:36:15+00:00
url: /2017/06/29/leetcode-design_twitter/
categories:
  - Algorithm
  - Python
tags:
  - leetcode
  - 系统设计

---
经典的设计题，以前校招笔试遇到过，题意就是：让你设计一个小的推特系统，能够发推、收到推送、关注和取消关注某人，我的做法是直接采用一个数据表（字典）， 然后写的比较复杂，但是逻辑还算清晰，大量的检查异常情况，多次提交后AC；原题链接：<a href="https://leetcode.com/problems/design-twitter/" target="_blank">https://leetcode.com/problems/design-twitter/</a>

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user
  
and is able to see the 10 most recent tweets in the user&#8217;s news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
  
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user&#8217;s news feed.
  
Each item in the news feed must be posted by users who the user followed or by the user herself.
  
Tweets must be ordered from most recent to least recent.
  
follow(followerId, followeeId): Follower follows a followee.
  
unfollow(followerId, followeeId): Follower unfollows a followee.
  
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
  
twitter.postTweet(1, 5);

// User 1&#8217;s news feed should return a list with 1 tweet id -> [5].
  
twitter.getNewsFeed(1);

// User 1 follows user 2.
  
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
  
twitter.postTweet(2, 6);

// User 1&#8217;s news feed should return a list with 2 tweet ids -> [6, 5].
  
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
  
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
  
twitter.unfollow(1, 2);

// User 1&#8217;s news feed should return a list with 1 tweet id -> [5],
  
// since user 1 is no longer following user 2.
  
twitter.getNewsFeed(1);

```python
# _*_ coding: utf-8 _*_


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        重点设计是被follow
        """
        self.tt = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        import time
        if userId not in self.tt:
            self.tt[userId] = {'followed': set(), 'post': [], 'feed': []}
        _time = time.time()
        self.tt[userId]['post'].append((tweetId, _time))
        self.tt[userId]['feed'].append((userId, tweetId, _time))
        # 去关注自己的人的feed里加文章
        for user in self.tt[userId]['followed']:
            self.tt[user]['feed'].append((userId, tweetId, _time))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user 
        followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.tt or not self.tt[userId]['feed']:
            return []
        feeds = sorted(self.tt[userId]['feed'], key=lambda item: item[2], reverse=True)
        return [i[1] for i in feeds[:10]]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # 需要先建立被关注的人，因为等下需要同步他的post
        if followeeId not in self.tt:
            self.tt[followeeId] = {'followed': set(), 'post': [], 'feed': []}
        # 当前用户不存在则需要建立用户，并且同步他关注人的post
        if followerId not in self.tt:
            self.tt[followerId] = {'followed': set(), 'post': [], 'feed': []}
        # 如果两者是同一个人或者已经关注过直接返回
        if followerId == followeeId or followerId in self.tt[followeeId]['followed']:
            return
        self.tt[followeeId]['followed'].add(followerId)
        for post in self.tt[followeeId]['post']:
            self.tt[followerId]['feed'].append((followeeId, post[0], post[1]))

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # 必须二者都在tt里面
        if followerId not in self.tt or followeeId not in self.tt:
            return
        # 如果两者是同一个人直接返回
        if followerId == followeeId:
            return
        # unfollow之前还需要检查是否之前follow过
        if followerId not in self.tt[followeeId]['followed']:
            return
        self.tt[followeeId]['followed'].remove(followerId)
        self.tt[followerId]['feed'] = filter(
                lambda i: i[0] != followeeId,
                self.tt[followerId]['feed'])
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

这是leetcode的AC结果里的最优解，主要用了一些其他的库，初始化可以看成他是建立了三个数据表，对比我的写法确实简单明了一些，建议采用此解法。

```python
class Twitter1(object):
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)
```