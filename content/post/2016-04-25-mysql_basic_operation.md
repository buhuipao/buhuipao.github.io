---
title: Mysql的基本操作（1）
author: 咩
type: post
date: 2016-04-25T11:57:38+00:00
url: /2016/04/25/mysql_basic_operation/
post_views_count:
  - "48"
flashPic:
  - .
flag:
  - .
categories:
  - Database
tags:
  - IP
  - Linux
  - mysql
  - shell

---
登陆数据库：

<pre class="lang:shell decode:1 " >mysql buhuipao_db -u buhuipao -p123456</pre>

注：buhuipao\_db为登陆后的所用数据库，也可以登陆后在使用：use buhuipao\_db；
  
-p后面接密码，直接登陆，不会询问密码，
  
使用数据库：

<pre class="lang:shell decode:1 " >use buhuipao_db;</pre>

假如你登陆的的是root用户，或着具有创建表的权用户，创建表：

<pre class="lang:shell decode:1 " >create table employes(
       &gt;emid int not null,
       &gt;name varchar(30),
       &gt;sex varchar(10),
       &gt;salary float,
       &gt;primary key (emid)) ; </pre>

注：primary key 定义这个字段唯一；
  
为表插入数据：

<pre class="lang:shell decode:1 " >insert into employees values(1,'jiefu','man',4000.00);</pre>

如果再次插入emid为1的数据，将会出错；
  
修改表名：

<pre class="lang:shell decode:1 " >alter table employee rename employees;</pre>

为表employees再添加一列字段email：

<pre class="lang:shell decode:1 " >alter table employees
       &gt;add email varchar(20) null;</pre>

如果想用excel导入数据，那么先导出为data.csv,它的分割符为“，”用Editplus打开另存为UTF-8的data.txt,

<pre class="lang:shell decode:1 " >load data local infile '/home/buhuipao/data.txt' into table emploees fields terminated by ',';</pre>

注意：terminated 表示分割符为“，”；相应字段和数据对应起来
  
修改某个字段值：UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值

<pre class="lang:shell decode:1 " >update employees set name = 'huazai' where name = 'jiefu'</pre>

删除数据表：

<pre class="lang:shell decode:1 " >drop table buhuipao_db;</pre>

删除字段：

<pre class="lang:shell decode:1 " >alter table drop column sex;</pre>

最后便顺提一下怎么用shell脚本操作数据库：

<pre class="lang:shell decode:1 " >#!/bin/bash
MYSQL=<code>which mysql</code>
$MYSQL buhuipao_db -u buhuipao -p123456 -e 'select * from employees;
insert into employees values(1,'jiefu','man',4000.00,'admin@buhuipao.com');'</pre>

查询结果将会输出到终端，如果这是一个数据库备份脚本，那么在脚本中显示了MYSQL的用户密码，这是不可取的，所以想要避免这个，那么可以:

<pre class="lang:shell decode:1 " >sudo vim /etc/my.cnf 
#
# This group is read both both by the client and the server
# use it for options that affect everything
#
[client-server]
password=123456
...</pre>

在client-server后面添加对应数据库用户的密码即可。