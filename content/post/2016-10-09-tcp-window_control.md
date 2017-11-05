---
title: TCP的滑动窗口和拥塞控制
author: 咩
type: post
date: 2016-10-09T10:32:23+00:00
url: /2016/10/09/tcp-window_control/
post_views_count:
  - "125"
flashPic:
  - .
flag:
  - .
categories:
  - Network
tags:
  - IP
  - 拥塞控制
  - 滑动窗口

---
TCP协议作为一个可靠的面向流的传输协议，其可靠性和流量控制由滑动窗口协议保证，而拥塞控制则由控制窗口结合一系列的控制算法实现。
  
一.滑动窗口
  
所谓滑动窗口:发送窗口中相关的有四个概念：已发送并收到确认的数据（不再发送窗口和发送缓冲区之内）、已发送但未收到确认的数据（位于发送窗口之中）、允许发送但尚未发送的数据以及发送窗口外发送缓冲区内暂时不允许发送的数据；每次成功发送数据之后，发送窗口就会在发送缓冲区中按顺序移动，将新的数据包含到窗口中准备发送；

其中发送端窗口分为两部分，前半部分为已发送但未确认，后半部分为允许发送但未发送；接收端窗口为允许接受。每次发送一段数据后，发送端收到接收端的ＡＣＫ后，窗口左端P1向右移动，右端P3也向右移动，但是原已发送未确认和允许发送未发送的分界点P2暂时不动，这样允许发送尚未发送区变宽，接下来接续发送数据，P2向右朝P3靠近直到重合。这样发送端的发送窗口已满，可用窗口为０，停止发送。数据全部到达接收端。接收端也发出了确认信息。

这个是时候可能接收端没有收到确认信息，于是等着，认为接收端任然没有收到此段数据。在经过一段时间后，超时计数器起作用，发送端将重发数据，指导收到接收端的确认为止。

接收端有时候接收到未按顺利到达的数据，假设发送端发送３１，３２，３３，但是接收端只接收到３２，３３此时接收端发送的确认报文段中的确认号依然是３１，而不能是３２，３３，后面快重传会提到这个。

二.流量控制
  
**　发送方的发送窗口不能超过接收方给出的接收窗口数值。而且，TCP的窗口单位是字节不是报文段。**接收端的窗口大小是建立在接收缓存上的，回复发送端确认号ACK时也回复接收窗大小。

有时候会出现这种情况，接收端发送接收窗为０的报文段后，接收端接收缓存又有一些空间了，于是向发送端发送接收窗大小为２００的报文段，假如此报文段丢失了，发送端一直在等接收端发送非０窗口的报文段，接收端也理所当然以为发送端收到它的２００接收窗报文段，两边都将等下去。这时TCP为解决此问题，为每个链接设置一个持续计时器(persistence timer).只要发送端收到接收端的０窗口报文段，就启动持续计时器，若时间到期，就发送一个０窗口探测报文段（仅携带一字节数据），接收端确认此报文段时就给出此时的接受窗口大小。假如任然是０，重新启动持续计时器。

考虑到传输效率，应用进程把数据传到发送的缓存后,剩下发送任务由TCP控制，TCP有三种控制发送时机，
  
1)TCP设定一个变量（等于最大报文段长度MSS），当缓存大小达到MSS字节数时发送;
  
2)由发送方的应用进程指明要求发送报文段，即TCP支持的推送(push)操作；
  
3)发送方一个计时器到限，发送当前缓存数据(长度不超过MSS).

有时候用户只发送一个字节长度的数据，加上２０字节的TCP首部，再加上20的IP首部就是４１字节，利用率太低，还占带宽。于是在TCP现实中采用Nagle算法，算法如下：应用程序现将数据慢慢送到缓存区，则先发送一个字节，当接收端回复确认报文段后，把缓存区的所有数据组成一个报文段发出去，同时继续缓存数据，只有收到前一个报文段的确认之后才将全部缓存数据组段发出去。Nagle算法还规定，当到达的数据达到发送窗口的一半时或者达到报文段最大长度时，就立即发送一个报文段。

另一种情况就是反过来，假如接收端的应用程序每次只从接收端缓存读取一个字节，这时接收端一空出一个字节缓存空间，就立即给发送端发送接受窗口为１的报文段，这样也是和浪费。所以同理，接收端也采取同之前发送端类似的策略，等接收缓存出现一半空闲空间或者足够容纳一个最初报文段空间时，再通知发送端的此前接收窗口大小。

两种方法配合使用。

三.TCP拥塞控制
  
拥塞控制就是防止过多数据注入网络，避免网络中路由器的过载丢弃报文段，是这整个网络的控制，而流量控制是端对端通信量的控制。拥塞控制方法有四种算法分别是: 1)慢开始；２）拥塞避免；3)快重传；４）快恢复

１）慢开始算法。发送方维持一个叫做拥塞窗口(cwnd)的状态变量，发送方先不知道网络情况，先设置cwnd为一个最大报文段MSS的数值，本来单位是字节方便叙述理解，将cwnd的单位设为段个数，则第一次设置cwnd=1的M1报文段，收到确认报文段确认后加倍，第二次就是cwnd=2的M2的报文段。除此之外还需要设置一个慢开始的门限ssthresh，
  
当cwnd<ssthresh，继续使用慢开始； 　　　当cwnd>ssthresh,换用拥塞避免;
  
当cwnd=ssthresh，两种皆可。

２）拥塞避免算法。它让cwnd不再增长那么快，缓慢加１，于是cwnd就呈线性。

<img class="aligncenter size-large wp-image-919" src="http://www.buhuipao.com/wp-content/uploads/2016/10/1176887572-1024x522.jpg" alt="慢开始" width="640" height="326" srcset="http://www.buhuipao.com/wp-content/uploads/2016/10/1176887572-1024x522.jpg 1024w, http://www.buhuipao.com/wp-content/uploads/2016/10/1176887572-150x77.jpg 150w, http://www.buhuipao.com/wp-content/uploads/2016/10/1176887572-300x153.jpg 300w, http://www.buhuipao.com/wp-content/uploads/2016/10/1176887572-768x392.jpg 768w, http://www.buhuipao.com/wp-content/uploads/2016/10/1176887572.jpg 1280w" sizes="(max-width: 640px) 100vw, 640px" />
  
无论在哪个阶段，只要出现拥塞，就**把ssthresh设置为拥塞时发送窗口cwnd的一半，并接着重新设置cwnd为１**。

３）快重传；
  
４）快恢复。快重传算法要求接收方收到一个失序的报文段时立即出现重复确认，目的是为了让发送方及早知道有报文未达到对方。假设接收方接收到M1,M2,M４,M５，M6，没有收到M３,根据快重传算法，接受方在接收到M4,M5,M6时都会回复确认M2,算法规定党收到三个重复确认时就重传M3,不必等为M3设置的重传计数器到期。接下来和之前一样，**把cwnd减半并设置新ssthresh＝cwnd，接着开始执行拥塞避免算法，cwnd缓慢加１。
  
<img class="aligncenter size-large wp-image-922" src="http://www.buhuipao.com/wp-content/uploads/2016/10/1142449014-1024x519.jpg" alt="拥塞" width="640" height="324" srcset="http://www.buhuipao.com/wp-content/uploads/2016/10/1142449014-1024x519.jpg 1024w, http://www.buhuipao.com/wp-content/uploads/2016/10/1142449014-150x76.jpg 150w, http://www.buhuipao.com/wp-content/uploads/2016/10/1142449014-300x152.jpg 300w, http://www.buhuipao.com/wp-content/uploads/2016/10/1142449014-768x389.jpg 768w, http://www.buhuipao.com/wp-content/uploads/2016/10/1142449014.jpg 1280w" sizes="(max-width: 640px) 100vw, 640px" />
  
** 。
  
<img class="aligncenter size-large wp-image-920" src="http://www.buhuipao.com/wp-content/uploads/2016/10/1868362269-1024x420.jpg" alt="kuaihuifu" width="640" height="263" srcset="http://www.buhuipao.com/wp-content/uploads/2016/10/1868362269-1024x420.jpg 1024w, http://www.buhuipao.com/wp-content/uploads/2016/10/1868362269-150x62.jpg 150w, http://www.buhuipao.com/wp-content/uploads/2016/10/1868362269-300x123.jpg 300w, http://www.buhuipao.com/wp-content/uploads/2016/10/1868362269-768x315.jpg 768w, http://www.buhuipao.com/wp-content/uploads/2016/10/1868362269.jpg 1280w" sizes="(max-width: 640px) 100vw, 640px" />

请注意，**有的快速重传是把cwnd继续加三个，理由是你既然有三个后续的报文端到达，可能M3不是拥塞丢失，cwnd还是可以继续增大，那么就增大３个。**

最后，虽然cwnd可以在不拥塞的情况下一直增大，但是这是在假定接收端的缓存空间足够大。接收端会根据自己的情况设置一个接受窗口rwnd,所以，最终发送端发送窗口的上限值由Min(cwnd,rwnd)决定。

最后附加三次握手，四次挥手的图片。

 <img class="aligncenter size-large wp-image-925" src="http://www.buhuipao.com/wp-content/uploads/2016/10/799254799-1024x520.jpg" alt="TCP_3_connect" width="640" height="325" srcset="http://www.buhuipao.com/wp-content/uploads/2016/10/799254799-1024x520.jpg 1024w, http://www.buhuipao.com/wp-content/uploads/2016/10/799254799-150x76.jpg 150w, http://www.buhuipao.com/wp-content/uploads/2016/10/799254799-300x152.jpg 300w, http://www.buhuipao.com/wp-content/uploads/2016/10/799254799-768x390.jpg 768w, http://www.buhuipao.com/wp-content/uploads/2016/10/799254799.jpg 1280w" sizes="(max-width: 640px) 100vw, 640px" /><img class="aligncenter size-large wp-image-926" src="http://www.buhuipao.com/wp-content/uploads/2016/10/1012281139-1024x706.jpg" alt="TCP_4_close" width="640" height="441" srcset="http://www.buhuipao.com/wp-content/uploads/2016/10/1012281139-1024x706.jpg 1024w, http://www.buhuipao.com/wp-content/uploads/2016/10/1012281139-150x103.jpg 150w, http://www.buhuipao.com/wp-content/uploads/2016/10/1012281139-300x207.jpg 300w, http://www.buhuipao.com/wp-content/uploads/2016/10/1012281139-768x530.jpg 768w, http://www.buhuipao.com/wp-content/uploads/2016/10/1012281139.jpg 1280w" sizes="(max-width: 640px) 100vw, 640px" />