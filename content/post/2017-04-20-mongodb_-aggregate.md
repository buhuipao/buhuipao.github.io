---
title: MongoDB的数据聚合使用实例
author: 咩
type: post
date: 2017-04-20T06:11:23+00:00
url: /2017/04/20/mongodb_-aggregate/
categories:
  - Database
tags:
  - mongodb
  - 聚合

---
由于妹子的毕业设计项目就是用的mongodb，所以对mongodb有初步接触，熟悉了基本用法和特性，但是毕竟毕业设计的项目是个玩具，所以一直没有接触到mongodb的数据聚合，直到有一天领导叫我生成质量的报表时，我开始接触使用；
  
所谓数据聚合就是对一个数据进行多次处理，而每一阶段的处理结果将用管道传到下一阶段，管道的解释为：在Unix和Linux中一般用于将当前命令的输出结果作为下一个命令的参数。而MongoDB的聚合管道将MongoDB文档在一个管道处理完毕后将结果传递给下一个管道处理；且管道操作是可以重复的。
  
这里列举几个常用聚合操作：

    $project：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。
    $match：用于过滤数据，只输出符合条件的文档。$match使用MongoDB的标准查询操作。
    $limit：用来限制MongoDB聚合管道返回的文档数。
    $skip：在聚合管道中跳过指定数量的文档，并返回余下的文档。
    $unwind：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
    $group：将集合中的文档分组，可用于统计结果。
    $sort：将输入文档排序后输出。
    $geoNear：输出接近某一地理位置的有序文档。
    

下面是我的部分代码：

```# _*_ coding: utf-8 _*_


from pymongo import ReturnDocument
from pymongo import MongoClient
from bson import json_util

import time
import sys
import os
# 最终写到csv文件里
import csv

# from pdb import set_trace

client = MongoClient('xxx.xxx.xxx.xxx', 27714)
DB = client.quality


def find_data(role, line, day):
    result = DB.line.aggregate(
    [{'$match': {'line': line, 'role': role}},
    {'$sort': {'time': -1}},
    {'$limit': day},
    {'$group': {'_id': {'role': '$role', 'line': '$line'}, 'time': {'$avg': '$TotalTime'}, 'success': {'$sum': '$Success'}, 'total': {'$sum': '$Total'}}},
    {'$project': {'_id': 0, 'time': 1, 'result': {'$divide': ['$success', '$total']}}}])
    return result
```