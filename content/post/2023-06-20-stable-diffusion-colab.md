---
title: Stable diffusion UI colab
author: 咩
type: post
date: 2023-06-20T20:31:47+00:00
url: /2023/06/20/stable-diffusion-ui-colab/
categories:
  - AIGC 
tags:
  - sd-ui
  - colab
  - Stable-diffusion

---
利用空闲时间，整理了一个基于colab快速启动一套sd-ui的ipython notebook，具体链接：[https://github.com/buhuipao/sd-webui-colab](https://github.com/buhuipao/sd-webui-colab)。整个notebook包含以下几个单元：
* Install Stable Diffusion
* Load And Run Existing Stable Diffusion
* Just Start Stable Diffusion
* Open terminal TTY for debug
![image.png](/img/sd-ui-ipynb.jpg)
在运行之后，你便可以在里colab的标准输出里找到sd-ui的登录地址，默认用户名和密码是：admin/123456。

需要特殊说明的是，这个notebook里有一个选项：「挂载Google Driver」，建议勾选。勾选之后你就可以将你的sd模型放到相应的目录，避免每次都进行下载了。
![google-driver-sd-dir](/img/google-driver-sd.jpg)