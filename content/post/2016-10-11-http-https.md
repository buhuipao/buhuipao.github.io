---
title: '[转载] Http的1.0/1.1/2.0的理解'
author: 咩
type: post
date: 2016-10-11T04:42:16+00:00
url: /2016/10/11/http-https/
post_views_count:
  - "100"
flashPic:
  - .
flag:
  - .
categories:
  - Linux
tags:
  - host
  - HTTPS
  - IP
  - ps

---
先说Http1.0和Http1.1，都是支持Gzip(之前我有误解)的,http 1.0中默认是关闭的，需要在http头加入&#8221;Connection: Keep-Alive&#8221;，才能启用Keep-Alive；http 1.1中默认启用Keep-Alive，如果加入&#8221;Connection: close &#8220;，才关闭。目前大部分浏览器都是用http1.1协议，也就是说默认都会发起Keep-Alive的连接请求了，所以是否能完成一个完整的Keep- Alive连接就看服务器设置情况。

Http1.0没有开启Keep-alive，访问一个网站将是很麻烦的事。服务器规定只能建立短暂连接，打开网页文件后关闭连接，想要加载里面的图片需要从新建立连接。显 然，访问一个包含有许多图像的网页文件的整个过程包含了多次请求和响应，每次请求和响应都需要建立一个单独的连接，每次连接只是传输一个文档和图像，上一次和下一次请求完全分离。即使图像文件都很小，但是客户端和服务器端每次建立和关闭连接却是一个相对比较费时的过程，并且会严重影响客户机和服务器的性能。

为了克服Http1.0的缺点，HTTP 1.1支持持久连接，在一个TCP连接上可以传送多个HTTP请求和响应，减少了建立和关闭连接的消耗和延迟。一个包含有许多图像的网页文件的多个请求和应答可以在一个连接中传输，但每个单独的网页文件的请求和应答仍然需要使用各自的连接。HTTP 1.1还允许客户端不用等待上一次请求结果返回，就可以发出下一次请求，但服务器端必须按照接收到客户端请求的先后顺序依次回送响应结果，以保证客户端能够区分出每次请求的响应内容，这样也显著地减少了整个下载过程所需要的时间。基于HTTP 1.1协议的客户机与服务器的信息交换过程。

HTTP 1.1还通过增加更多的请求头和响应头来改进和扩充HTTP 1.0的功能。例如，由于HTTP 1.0不支持Host请求头字段，WEB浏览器无法使用主机头名来明确表示要访问服务器上的哪个WEB站点，这样就无法使用WEB服务器在同一个IP地址和端口号上配置多个虚拟WEB站点。在HTTP 1.1中增加Host请求头字段后，WEB浏览器可以使用主机头名来明确表示要访问服务器上的哪个WEB站点，这才实现了在一台WEB服务器上可以在同一个IP地址和端口号上使用不同的主机名来创建多个虚拟WEB站点。HTTP 1.1的持续连接，也需要增加新的请求头来帮助实现，例如，Connection请求头的值为Keep-Alive时，客户端通知服务器返回本次请求结果后保持连接；Connection请求头的值为close时，客户端通知服务器返回本次请求结果后关闭连接。HTTP 1.1还提供了与身份认证、状态管理和Cache缓存等机制相关的请求头和响应头。

再说Http1.1和Http2.0的区别，Http1.1是基于TCP，位于TCP之上，而Https(Http2.0)是位于SSL/TSL之上，SSL/TSL位于TCP之上。Https的请求过程基本如下：
  
<img class="aligncenter size-full wp-image-930" src="http://www.buhuipao.com/wp-content/uploads/2016/10/https.png" alt="https" width="400" height="416" srcset="http://www.buhuipao.com/wp-content/uploads/2016/10/https.png 400w, http://www.buhuipao.com/wp-content/uploads/2016/10/https-144x150.png 144w, http://www.buhuipao.com/wp-content/uploads/2016/10/https-288x300.png 288w" sizes="(max-width: 400px) 100vw, 400px" />

1.浏览器将自己支持的一套加密规则发送给网站。

2.网站从中选出一组加密算法与HASH算法，并将自己的身份信息以证书的形式发回给浏览器。证书里面包含了网站地址，加密公钥，以及证书的颁发机构等信息。

3.浏览器获得网站证书之后浏览器要做以下工作：
  
a) 验证证书的合法性（颁发证书的机构是否合法，证书中包含的网站地址是否与正在访问的地址一致等），如果证书受信任，则浏览器栏里面会显示一个小锁头，否则会给出证书不受信的提示。
  
b) 如果证书受信任，或者是用户接受了不受信的证书，浏览器会生成一串随机数的密码，并用证书中提供的公钥加密。
  
c) 使用约定好的HASH算法计算握手消息，并使用生成的随机数对消息进行加密，最后将之前生成的所有信息发送给网站。

4.网站接收浏览器发来的数据之后要做以下的操作：
  
a) 使用自己的私钥将信息解密取出密码，使用密码解密浏览器发来的握手消息，并验证HASH是否与浏览器发来的一致。
  
b) 使用密码加密一段握手消息，发送给浏览器。

5.浏览器解密并计算握手消息的HASH，如果与服务端发来的HASH一致，此时握手过程结束，之后所有的通信数据将由之前浏览器生成的随机密码并利用对称加密算法进行加密。

&#8212;-其实说白了就是：浏览器要请求网站，先告诉网站我支持哪些加密协议你自己选一套吧，网站选好之后把自己的身份证和密码箱(公钥)发过来，浏览器认证身份后，并且用HASH算法计算握手，然后用随机密码加密，然后把装着随机密码的密码箱运给网站，密码在箱子里，网站用私钥打开(非对称加密)，然后解密握手消息验证。之后的通信就都用随机密码加密解密(对称加密)。

非对称加密算法：RSA，DSA/DSS
  
对称加密算法：AES，RC4，3DES
  
HASH算法：MD5，SHA1，SHA256

文章转自：

CSDN博客：<http://blog.csdn.net/clh604/article/details/22179907>

博客园: <http://www.cnblogs.com/ranjiewen/p/5582602.html>

最后附加上阮一峰前辈的的RSA算法原理，感兴趣可以了解下。

１）[http://www.ruanyifeng.com/blog/2013/06/rsa\_algorithm\_part_one.html][1]）

２）[http://www.ruanyifeng.com/blog/2013/07/rsa\_algorithm\_part_two.html][2]

 [1]: http://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html
 [2]: http://www.ruanyifeng.com/blog/2013/07/rsa_algorithm_part_two.html