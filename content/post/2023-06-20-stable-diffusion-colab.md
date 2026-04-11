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

### 使用说明

**1. 环境要求**

使用前请确保你的 Google Colab 已经切换到 GPU 运行时（推荐 T4 或更高）：

- 点击菜单栏 `Runtime` -> `Change runtime type`
- 选择 `T4 GPU`（免费版可用）

**2. 各单元说明**

- **Install Stable Diffusion**：首次使用时运行，会自动下载安装 sd-webui 及相关依赖，耗时大约 5-10 分钟；
- **Load And Run Existing Stable Diffusion**：如果之前已经安装过且挂载了 Google Drive，可以直接运行这个单元来加载已有的安装；
- **Just Start Stable Diffusion**：仅启动 sd-webui 服务，适合已经完成安装和模型下载后使用；
- **Open terminal TTY for debug**：打开一个终端，方便调试和查看日志；

**3. 模型管理**

勾选挂载 Google Drive 后，模型文件会保存在 Google Drive 的对应目录中。你可以手动将下载好的模型文件（.safetensors 或 .ckpt）上传到以下目录：

- 基础模型：`/content/drive/MyDrive/sd/models/Stable-diffusion/`
- LoRA 模型：`/content/drive/MyDrive/sd/models/Lora/`
- VAE 模型：`/content/drive/MyDrive/sd/models/VAE/`

**4. 注意事项**

- Colab 免费版有使用时长限制，长时间不操作可能会断开连接；
- 建议将常用的模型和配置保存在 Google Drive 中，避免每次重新下载；
- 如果遇到显存不足（OOM），可以在 sd-ui 设置中启用 `--medvram` 或 `--lowvram` 选项。