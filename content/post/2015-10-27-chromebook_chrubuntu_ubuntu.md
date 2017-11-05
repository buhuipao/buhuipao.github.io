---
title: 搬运墙外Chromebook的Chrubuntu方法安装ubuntu
author: 咩
type: post
date: 2015-10-26T16:03:39+00:00
url: /2015/10/27/chromebook_chrubuntu_ubuntu/
post_views_count:
  - "163"
flag:
  - .
categories:
  - Linux
tags:
  - chromebook
  - Ubuntu

---
<a href="//www.bluehost.com/track/buhuipao/" target="_blank"><br /> <img border="0" src="//bluehost-cdn.com/media/partner/images/buhuipao/760x80/bh-760x80-04-dy.png" /><br /> </a>

<h1 style="text-align: center;">
  <strong><span id="OUTFOX_JTR_TRANS_NODE-3" class="OUTFOX_JTR_TRANS_NODE">使用ChrUbuntu安装Ubuntu到新chrome笔记本</span></strong>
</h1>

<div id="post-body-3234478954455221800" class="post-body entry-content">
  <p>
    <span id="OUTFOX_JTR_TRANS_NODE-4" class="OUTFOX_JTR_TRANS_NODE">自从我开始ChrUbuntu回来 </span><a href="http://chromeos-cr48.blogspot.com/2010/12/easy-way-to-install-ubuntu-on-your-cr.html" target="_blank"><span id="OUTFOX_JTR_TRANS_NODE-5" class="OUTFOX_JTR_TRANS_NODE">2010年12月 </span></a><span id="OUTFOX_JTR_TRANS_NODE-6" class="OUTFOX_JTR_TRANS_NODE">,这一直是必要使用Chrome OS和Ubuntu Linux内核为了解决一些兼容性问题Chromebook架构。 与Chromebook像素的变化和更新Haswell-based chrome笔记本之类的 </span><a href="http://www.amazon.com/gp/product/B00FNPD1OY/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00FNPD1OY&linkCode=as2&tag=chro48-20"><span id="OUTFOX_JTR_TRANS_NODE-7" class="OUTFOX_JTR_TRANS_NODE">宏碁C720 </span></a><span id="OUTFOX_JTR_TRANS_NODE-8" class="OUTFOX_JTR_TRANS_NODE">和 </span><a href="http://www.amazon.com/gp/product/B00FGOTA9M/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00FGOTA9M&linkCode=as2&tag=chro48-20"><span id="OUTFOX_JTR_TRANS_NODE-9" class="OUTFOX_JTR_TRANS_NODE">惠普Chromebook 14 </span></a><span id="OUTFOX_JTR_TRANS_NODE-10" class="OUTFOX_JTR_TRANS_NODE">。 每个这些模型的支持 </span><a href="https://plus.google.com/100479847213284361344/posts/QhmBpn5GNE9" target="_blank"><span id="OUTFOX_JTR_TRANS_NODE-11" class="OUTFOX_JTR_TRANS_NODE">从更传统的PC BIOS启动模式 </span></a><span id="OUTFOX_JTR_TRANS_NODE-12" class="OUTFOX_JTR_TRANS_NODE">这使得它易于使用股票Ubuntu内核。 </span>
  </p>
  
  <p>
    <a href="http://www.buhuipao.com/wp-content/uploads/2015/10/ubuntu.jpg"><img class="aligncenter wp-image-678" src="http://www.buhuipao.com/wp-content/uploads/2015/10/ubuntu-1024x640.jpg" alt="ubuntu" width="680" height="425" srcset="http://www.buhuipao.com/wp-content/uploads/2015/10/ubuntu-1024x640.jpg 1024w, http://www.buhuipao.com/wp-content/uploads/2015/10/ubuntu-150x94.jpg 150w, http://www.buhuipao.com/wp-content/uploads/2015/10/ubuntu-300x188.jpg 300w" sizes="(max-width: 680px) 100vw, 680px" /></a>
  </p>
  
  <div>
  </div>
  
  <div>
    <span id="OUTFOX_JTR_TRANS_NODE-13" class="OUTFOX_JTR_TRANS_NODE"> 这ChrUbuntu释放是一个 </span><u><span id="OUTFOX_JTR_TRANS_NODE-14" class="OUTFOX_JTR_TRANS_NODE">预览 </span></u><span id="OUTFOX_JTR_TRANS_NODE-15" class="OUTFOX_JTR_TRANS_NODE">只 支持基于x86的chrome笔记本,像素和更新(阅读:基于arm的惠普Chromebook 11不支持,也不旧的宏碁C7、三星550,等。这些设备使用旧s9ryd脚本)。 我希望最终将这个脚本在主sr9yd ChrUbuntu安装脚本,但现在,我推荐这个脚本在这些更新的旧设备。 </span>
  </div>
  
  <div>
    <b><span id="OUTFOX_JTR_TRANS_NODE-16" class="OUTFOX_JTR_TRANS_NODE">注意: </span></b><span id="OUTFOX_JTR_TRANS_NODE-17" class="OUTFOX_JTR_TRANS_NODE">触控板仅支持13.10和更高版本。 我正在向12.04补丁触摸板驱动程序。 现在坚持13.10或使用USB鼠标。 </span>
  </div>
  
  <div>
    <span id="OUTFOX_JTR_TRANS_NODE-18" class="OUTFOX_JTR_TRANS_NODE"> 下面的步骤安装ChrUbuntu像素或Haswell-based Chromebook: </span>
  </div>
  
  <div>
    <div>
      <ol>
        <li>
          <span id="OUTFOX_JTR_TRANS_NODE-19" class="OUTFOX_JTR_TRANS_NODE">首先,确保你的Chromebook处于开发模式。 模型相关的指令可以 </span><a href="http://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices"><span id="OUTFOX_JTR_TRANS_NODE-20" class="OUTFOX_JTR_TRANS_NODE">在这里找到 </span></a><span id="OUTFOX_JTR_TRANS_NODE-21" class="OUTFOX_JTR_TRANS_NODE">。 </span>
        </li>
        <li>
          <span id="OUTFOX_JTR_TRANS_NODE-22" class="OUTFOX_JTR_TRANS_NODE">开 始你的铬设备关机。打开但不要登录。 确保你有一个WiFi或以太网连接配置。 不推荐3 g / 4 g。 按CTRL + ALT + = >(= > F2的向前箭头键将PC)。 不要使用正常的CTRL + ALT + T方法来获取一个壳。 使用CTRL + ALT + = >方法虽然没有人登录。 </span>
        </li>
        <li>
          <span id="OUTFOX_JTR_TRANS_NODE-23" class="OUTFOX_JTR_TRANS_NODE">作为用户chronos登录,不需要密码。 </span>
        </li>
        <li>
          <span id="OUTFOX_JTR_TRANS_NODE-24" class="OUTFOX_JTR_TRANS_NODE">作为chronos用户和不改变目录或运行其他命令,运行: </span><span id="OUTFOX_JTR_TRANS_NODE-25" class="OUTFOX_JTR_TRANS_NODE">curl &#8211; l &#8211; o http://goo。 gl / 9 sgchs;sudo bash 9 sgchs </span><span id="OUTFOX_JTR_TRANS_NODE-26" class="OUTFOX_JTR_TRANS_NODE">确保你有正确的命令。 &#8211; o &#8211; l后旋度都是大写字母。 9 sgchs所有小写字母和数字,听起来像“九ess啊看到aich ess”如果你大声说出来。 如果你得到一个“未找到”错误,确保你有互联网连接和你输入正确的命令。 </span>
        </li>
        <li>
          <span id="OUTFOX_JTR_TRANS_NODE-27" class="OUTFOX_JTR_TRANS_NODE">你会被提示一些信息关于你的Chromebook和ChrUbuntu安装的版本。 按回车键继续。 </span>
        </li>
        <li>
          <span id="OUTFOX_JTR_TRANS_NODE-28" class="OUTFOX_JTR_TRANS_NODE">Chrome OS状态分区,数据和设置默认存储只是短11 gb(除了像素有32或64 gb的SSD),脚本收缩状态分区为ChrUbuntu腾出空间。 你可以选择放弃从5 gb ChrUbuntu 10 gb的1 gb的增量(注意:如果你已经安装了一个更大的SSD铬设备,你的最大数量和建议将会更大)。 我建议不会高于9 10留给Chrome OS很少自由空间(小于1 gb)。 </span>
        </li>
        <li>
          <span id="OUTFOX_JTR_TRANS_NODE-29" class="OUTFOX_JTR_TRANS_NODE">一旦你输入一个数字,你的硬盘重新分区。 一段时间后,它将重新启动并初始化状态分区。 这个过程需要男童分钟然后Chromebook再次重新启动,显示欢迎屏幕你得到当你第一次打开你的Chromebook纸箱。 </span><b><span id="OUTFOX_JTR_TRANS_NODE-30" class="OUTFOX_JTR_TRANS_NODE">专家提示: </span></b><span id="OUTFOX_JTR_TRANS_NODE-31" class="OUTFOX_JTR_TRANS_NODE">不喜欢Ubuntu或它的任何变体? 你现在可以停止和填补准备Linux USB引导磁盘 </span><a href="https://fedoraproject.org/wiki/How_to_create_and_use_Live_USB"><span id="OUTFOX_JTR_TRANS_NODE-32" class="OUTFOX_JTR_TRANS_NODE">Fedora </span></a><span id="OUTFOX_JTR_TRANS_NODE-33" class="OUTFOX_JTR_TRANS_NODE">, </span><a href="http://www.debian.org/releases/stable/i386/ch04s03.html.en"><span id="OUTFOX_JTR_TRANS_NODE-34" class="OUTFOX_JTR_TRANS_NODE">Debian </span></a><span id="OUTFOX_JTR_TRANS_NODE-35" class="OUTFOX_JTR_TRANS_NODE">, </span><a href="http://community.linuxmint.com/tutorial/view/744"><span id="OUTFOX_JTR_TRANS_NODE-36" class="OUTFOX_JTR_TRANS_NODE">薄荷 </span></a><span id="OUTFOX_JTR_TRANS_NODE-37" class="OUTFOX_JTR_TRANS_NODE">在开车或者几乎任何其他发行版。 然后点击CTRL + L发起遗留的引导。 格式和操作系统安装到sda和确保安装GRUB的/dev/sda7分区,你应该去好! </span>
        </li>
        <li>
          <span id="OUTFOX_JTR_TRANS_NODE-38" class="OUTFOX_JTR_TRANS_NODE">再通过Chrome OS安装过程,直到你到达谷歌登录页面。 你需要有一个WiFi或以太网连接在这一点上。 现在按照步骤2到5了。 这一次脚本会发现你已经让位给Ubuntu并开始下载ChrUbuntu。 </span><b><span id="OUTFOX_JTR_TRANS_NODE-39" class="OUTFOX_JTR_TRANS_NODE">专家提示: </span></b><span id="OUTFOX_JTR_TRANS_NODE-40" class="OUTFOX_JTR_TRANS_NODE">在这里您可以安装其他版本的Ubuntu ! 看你有什么选项运行: </span><span id="OUTFOX_JTR_TRANS_NODE-41" class="OUTFOX_JTR_TRANS_NODE">curl &#8211; l &#8211; o http://goo。 gl / 9 sgchs;sudo bash 9 sgchs &#8211; h </span><span id="OUTFOX_JTR_TRANS_NODE-42" class="OUTFOX_JTR_TRANS_NODE">自定义安装一个例子是: </span> <p>
            <span id="OUTFOX_JTR_TRANS_NODE-43" class="OUTFOX_JTR_TRANS_NODE">curl &#8211; l &#8211; o http://goo。 gl / 9 sgchs;sudo bash 9 sgchs &#8211; m xubuntu-desktop &#8211; i386 &#8211; u </span>
          </p>
          
          <p>
            <span id="OUTFOX_JTR_TRANS_NODE-44" class="OUTFOX_JTR_TRANS_NODE">这将安装32位版本的Xubuntu和最新LTS版(12.04.3写),而不是一个64位13.10统一桌面(默认)。 一些可能的味道替代统一(- m选项): </span>
          </p>
          
          <p>
            <b><span id="OUTFOX_JTR_TRANS_NODE-45" class="OUTFOX_JTR_TRANS_NODE">默认的 </span></b><span id="OUTFOX_JTR_TRANS_NODE-46" class="OUTFOX_JTR_TRANS_NODE">——ubuntu桌面 </span><br /> <b><span id="OUTFOX_JTR_TRANS_NODE-47" class="OUTFOX_JTR_TRANS_NODE">kubuntu-desktop </span></b><br /> <b><span id="OUTFOX_JTR_TRANS_NODE-48" class="OUTFOX_JTR_TRANS_NODE">lubuntu-desktop </span></b><br /> <b><span id="OUTFOX_JTR_TRANS_NODE-49" class="OUTFOX_JTR_TRANS_NODE">xubuntu-desktop </span></b><br /> <b><span id="OUTFOX_JTR_TRANS_NODE-50" class="OUTFOX_JTR_TRANS_NODE">edubuntu-desktop </span></b><br /> <b><span id="OUTFOX_JTR_TRANS_NODE-51" class="OUTFOX_JTR_TRANS_NODE">ubuntu-standard </span></b><span id="OUTFOX_JTR_TRANS_NODE-52" class="OUTFOX_JTR_TRANS_NODE">——没有GUI安装 </span>
          </p>
          
          <p>
            <span id="OUTFOX_JTR_TRANS_NODE-53" class="OUTFOX_JTR_TRANS_NODE">一些可能的版本(- u选项): </span>
          </p>
          
          <p>
            <b><span id="OUTFOX_JTR_TRANS_NODE-54" class="OUTFOX_JTR_TRANS_NODE">lts </span></b><span id="OUTFOX_JTR_TRANS_NODE-55" class="OUTFOX_JTR_TRANS_NODE">——最新LTS Ubuntu版本,12.04.3在撰写本文时 </span><br /> <b><span id="OUTFOX_JTR_TRANS_NODE-56" class="OUTFOX_JTR_TRANS_NODE">最新的 </span></b><span id="OUTFOX_JTR_TRANS_NODE-57" class="OUTFOX_JTR_TRANS_NODE">——最新官方版本,目前13.10 </span><br /> <b><span id="OUTFOX_JTR_TRANS_NODE-58" class="OUTFOX_JTR_TRANS_NODE">dev </span></b><span id="OUTFOX_JTR_TRANS_NODE-59" class="OUTFOX_JTR_TRANS_NODE">——不稳定的开发Ubuntu发布。 专家! 如果这休息,不要感到惊讶。 </span><br /> <b><span id="OUTFOX_JTR_TRANS_NODE-60" class="OUTFOX_JTR_TRANS_NODE">12.10 </span></b><span id="OUTFOX_JTR_TRANS_NODE-61" class="OUTFOX_JTR_TRANS_NODE">——Ubuntu 12.10版本 </span>
          </p>
          
          <p>
            <span id="OUTFOX_JTR_TRANS_NODE-62" class="OUTFOX_JTR_TRANS_NODE">可能的架构(- a选项): </span>
          </p>
          
          <p>
            <b><span id="OUTFOX_JTR_TRANS_NODE-63" class="OUTFOX_JTR_TRANS_NODE">amd64 </span></b><span id="OUTFOX_JTR_TRANS_NODE-64" class="OUTFOX_JTR_TRANS_NODE">——默认 </span><br /> <b><span id="OUTFOX_JTR_TRANS_NODE-65" class="OUTFOX_JTR_TRANS_NODE">i386 </span></b>
          </p>
          
          <p>
            <span id="OUTFOX_JTR_TRANS_NODE-66" class="OUTFOX_JTR_TRANS_NODE">&#8211; t目标桌子选项是完全未经考验的现在! </span></li> 
            
            <li>
              <span id="OUTFOX_JTR_TRANS_NODE-67" class="OUTFOX_JTR_TRANS_NODE">在安装期间(5 &#8211; 15分钟内)。 你会看到一些提示选择您的编码,语言环境和语言。 对大多数人来说,默认应该没事的,只是按Enter键,如果你想改变它们。 后来,你会被提示来决定应该安装GRUB的地方。 你必须sda复选框旁边的为了引导工作! </span>
            </li>
            <li>
              <span id="OUTFOX_JTR_TRANS_NODE-68" class="OUTFOX_JTR_TRANS_NODE">毕竟Ubuntu的文件已经下载,安装和配置,该脚本将使更多的更新,然后提示你重新启动。 </span>
            </li>
            <li>
              <span id="OUTFOX_JTR_TRANS_NODE-69" class="OUTFOX_JTR_TRANS_NODE">在屏幕可怕的开发模式,点击CTRL + L,而不是按CTRL + D。 你会看到ChrUbuntu启动! 用户名是“用户”和密码“用户”。 </span>
            </li></ol> </div> 
            
            <div>
              <p>
                <span id="OUTFOX_JTR_TRANS_NODE-70" class="OUTFOX_JTR_TRANS_NODE"> 就是这样! 现在你可以按CTRL + L引导ChrUbuntu(L的遗产,传统操作系统)或按CTRL + D启动Chrome OS(D在默认OS磁盘上)。 </span>
              </p>
              
              <p>
                <span id="OUTFOX_JTR_TRANS_NODE-71" class="OUTFOX_JTR_TRANS_NODE"> 最后但重要的是,我想给一个大感谢+ </span><a href="https://plus.google.com/100479847213284361344/posts" target="_blank"><span id="OUTFOX_JTR_TRANS_NODE-72" class="OUTFOX_JTR_TRANS_NODE">比尔·理查森 </span></a><span id="OUTFOX_JTR_TRANS_NODE-73" class="OUTFOX_JTR_TRANS_NODE">,+ </span><a href="https://plus.google.com/102325349472273329333/posts" target="_blank"><span id="OUTFOX_JTR_TRANS_NODE-74" class="OUTFOX_JTR_TRANS_NODE">罗恩Minnich </span></a><span id="OUTFOX_JTR_TRANS_NODE-75" class="OUTFOX_JTR_TRANS_NODE">, </span><span id="OUTFOX_JTR_TRANS_NODE-76" class="OUTFOX_JTR_TRANS_NODE">+ </span><a href="https://plus.google.com/101550095383851162852/posts" target="_blank"><span id="OUTFOX_JTR_TRANS_NODE-77" class="OUTFOX_JTR_TRANS_NODE">Stefan Reinauer </span></a><span id="OUTFOX_JTR_TRANS_NODE-78" class="OUTFOX_JTR_TRANS_NODE">和其他员工工作的低级Chrome OS硬件/软件,使一个真正令人难以置信的强大和开放Chrome OS平台! 伟大作品的家伙! </span>
              </p>
              
              <hr />
            </div></div> 
            
            <div>
              此文为搬运墙外原著的chromebook安装ubuntu的最新教程（Googel翻译），意在帮助墙内的初级chromebook用户，不喜勿喷，也希望原作者理解我们天朝的子民。本人并不是有意抄袭和盗用，请理解理解！向原著致敬！
            </div>
            
            <div>
            </div>
            
            <div>
              <strong><del>以下为原文，上文的机器翻译如若不对，轻自己对照理解操作！</del></strong>
            </div></div> 
            
            <div>
              <hr />
              
              <h3 class="post-title entry-title" style="text-align: center;">
                ChrUbuntu for New Chromebooks: Now with more Ubuntu
              </h3>
              
              <div id="post-body-3234478954455221800" class="post-body entry-content">
                <p>
                  Since I started ChrUbuntu back in<span class="Apple-converted-space"> </span><a href="http://chromeos-cr48.blogspot.com/2010/12/easy-way-to-install-ubuntu-on-your-cr.html" target="_blank">December of 2010</a>, it&#8217;s always been necessary to utilize the Chrome OS Linux kernel with Ubuntu in order to solve some compatibility issues with the Chromebook architecture. That&#8217;s changed with the Chromebook Pixel and the newer Haswell-based Chromebooks like the<span class="Apple-converted-space"> </span><a href="http://www.amazon.com/gp/product/B00FNPD1OY/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00FNPD1OY&linkCode=as2&tag=chro48-20">Acer C720</a><span class="Apple-converted-space"> </span>and<span class="Apple-converted-space"> </span><a href="http://www.amazon.com/gp/product/B00FGOTA9M/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00FGOTA9M&linkCode=as2&tag=chro48-20">HP Chromebook 14</a>. Each of these models supports<span class="Apple-converted-space"> </span><a href="https://plus.google.com/100479847213284361344/posts/QhmBpn5GNE9" target="_blank">booting from a more traditional PC BIOS mode</a><span class="Apple-converted-space"> </span>which makes it simple to use stock Ubuntu kernels on them.
                </p>
                
                <div>
                </div>
                
                <div>
                  This ChrUbuntu release is a<span class="Apple-converted-space"> </span><u>preview</u><span class="Apple-converted-space"> </span>that will only support x86-based Chromebooks, Pixel and newer (read: the ARM-based HP Chromebook 11 is not supported, nor are the older Acer C7, Samsung 550, etc. Use the old s9ryd script for these devices). I hope to eventually wrap this script back in to the main sr9yd ChrUbuntu install script but for now, I recommend this script on these newer devices over the old one.
                </div>
                
                <div>
                  <b>Note:</b><span class="Apple-converted-space"> </span>The trackpad is only supported with 13.10 and higher. I&#8217;m working to backport the trackpad drivers to 12.04. For now stick with 13.10 or use a USB mouse.
                </div>
                
                <div>
                  Here are the steps to install ChrUbuntu on a Pixel or Haswell-based Chromebook:
                </div>
                
                <div>
                  <div>
                    <ol>
                      <li>
                        To get started, make sure your Chromebook is in developer mode. Model-specific instructions can be<span class="Apple-converted-space"> </span><a href="http://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices">found here</a>.
                      </li>
                      <li>
                        Start with your Chrome device turned off. Turn it on but do not login. Make sure you have a WiFi or Ethernet connection configured at this point. 3G/4G is not recommended. Press CTRL+ALT+=> (=> is the forward arrow where the F2 key would be on a PC). Do not use the normal CTRL+ALT+T method to get a shell. Use the CTRL+ALT+=> method while no one is logged in.
                      </li>
                      <li>
                        Login as user chronos, no password is needed.
                      </li>
                      <li>
                        As the chronos user and without having changed directories or run other commands, run:curl -L -O http://goo.gl/9sgchs; sudo bash 9sgchsMake sure you have the command exactly right. The -O and -L after curl are both capital letters. 9sgchs is all lowercase letters and numbers and would sound like &#8220;nine ess gee see aich ess&#8221; if you said it out loud. If you get a &#8220;not found&#8221; error, make sure you have Internet connectivity and you&#8217;re typing the command correctly.
                      </li>
                      <li>
                        You&#8217;ll be prompted with some information about your Chromebook and the version of ChrUbuntu to be installed. Press Enter to continue.
                      </li>
                      <li>
                        The Chrome OS stateful partition where your data and settings are stored is just short of 11gb by default (except for the Pixel which has a 32 or 64gb SSD), the script shrinks the stateful partition to make room for ChrUbuntu. You can choose to give ChrUbuntu from 5gb up to 10gb in 1gb increments (Note: If you&#8217;ve installed a larger SSD in your Chrome device, your max number and recommended max will be larger). I recommend not going higher than 9 as 10 leaves Chrome OS with very little free space (less than 1gb).
                      </li>
                      <li>
                        Once you&#8217;ve entered a number, your hard drive will be repartitioned. After awhile it will reboot and re-initialize the stateful partition. This process takes 2-15 minutes and then the Chromebook reboots again and shows you the Welcome screen you got when you first turned on your Chromebook out of the cardboard box.<b>Pro Tip:<span class="Apple-converted-space"> </span></b>don&#8217;t like Ubuntu or any of it&#8217;s variants? You can stop now and plug a ready to go Linux USB Boot disk for<span class="Apple-converted-space"> </span><a href="https://fedoraproject.org/wiki/How_to_create_and_use_Live_USB">Fedora</a>,<span class="Apple-converted-space"> </span><a href="http://www.debian.org/releases/stable/i386/ch04s03.html.en">Debian</a>,<span class="Apple-converted-space"> </span><a href="http://community.linuxmint.com/tutorial/view/744">Mint</a><span class="Apple-converted-space"> </span>or pretty much any other distro in the drive. Then hit CTRL+L to initiate the legacy boot. Format and install the OS to the /dev/sda7 partition and make sure GRUB is installed to /dev/sda and you should be good to go!
                      </li>
                      <li>
                        Go through the Chrome OS setup process again until you get to the Google login page. You&#8217;ll need to have a WiFi or Ethernet connection again at this point. Now follow steps 2 through 5 again. This time the script will see that you&#8217;ve already made room for Ubuntu and start downloading ChrUbuntu.<b>Pro Tip:</b><span class="Apple-converted-space"> </span>Here&#8217;s where you can install other versions of Ubuntu! To see what options you have run:curl -L -O http://goo.gl/9sgchs; sudo bash 9sgchs -h <p>
                          An example custom installation would be:
                        </p>
                        
                        <p>
                          curl -L -O http://goo.gl/9sgchs; sudo bash 9sgchs -m xubuntu-desktop -u lts -a i386
                        </p>
                        
                        <p>
                          which would install the 32-bit version of Xubuntu and the latest LTS release (12.04.3 as of writing) rather than a 64-bit 13.10 Unity desktop (which is the default). Some possible flavor alternatives to Unity (-m option) are:
                        </p>
                        
                        <p>
                          <b>default</b><span class="Apple-converted-space"> </span> &#8212; ubuntu-desktop<br /> <b>kubuntu-desktop</b><br /> <b>lubuntu-desktop</b><br /> <b>xubuntu-desktop</b><br /> <b>edubuntu-desktop</b><br /> <b>ubuntu-standard</b><span class="Apple-converted-space"> </span> &#8212; no GUI installed
                        </p>
                        
                        <p>
                          some possible versions (-u option) are:
                        </p>
                        
                        <p>
                          <b>lts</b><span class="Apple-converted-space"> </span>&#8212; latest LTS Ubuntu release, 12.04.3 as of this writing<br /> <b>latest</b><span class="Apple-converted-space"> </span>&#8212; latest official release, currently 13.10<br /> <b>dev</b><span class="Apple-converted-space"> </span>&#8212; unstable development Ubuntu release. Experts only! If this breaks, don&#8217;t be surprised.<br /> <b>12.10</b><span class="Apple-converted-space"> </span>&#8212; Ubuntu 12.10 release
                        </p>
                        
                        <p>
                          the possible architectures (-a option) are:
                        </p>
                        
                        <p>
                          <b>amd64<span class="Apple-converted-space"> </span></b> &#8212; default<br /> <b>i386</b>
                        </p>
                        
                        <p>
                          the -t target desk option is completely untested right now!</li> 
                          
                          <li>
                            During the installation (within the first 5-15 minutes). You&#8217;ll see a few prompts to select your encoding, locale and language. For most people, the defaults should be fine, just press Enter but change them if you&#8217;d like. Later on, you&#8217;ll be prompted to decide where GRUB should be installed. YOU MUST CHECK THE BOX NEXT TO /dev/sda in order for boot to work!
                          </li>
                          <li>
                            After all of the Ubuntu files have been downloaded, installed and configured, the script will make a few more updates and then prompt you to reboot.
                          </li>
                          <li>
                            At the scary developer mode screen, hit CTRL+L instead of CTRL+D. You&#8217;ll see ChrUbuntu start up! The username is &#8220;user&#8221; and the password is &#8220;user&#8221;.
                          </li></ol> </div> 
                          
                          <div>
                            <p>
                              That&#8217;s it! Now you can just press CTRL+L to boot ChrUbuntu (L as in Legacy, traditional OS) or CTRL+D to boot Chrome OS (D as in Default OS on Disk).
                            </p>
                            
                            <p>
                              Last but least, I want to give a big thank you to +<a href="https://plus.google.com/100479847213284361344/posts" target="_blank">Bill Richardson</a>, +<a href="https://plus.google.com/102325349472273329333/posts" target="_blank">Ron Minnich</a>,<span class="Apple-converted-space"> </span>+<a href="https://plus.google.com/101550095383851162852/posts" target="_blank">Stefan Reinauer</a> and other Googlers who work on the low-level Chrome OS hardware/software and have made a truly incredible, powerful and open Chrome OS platform! Great work guys!
                            </p>
                          </div></div> </div> </div>