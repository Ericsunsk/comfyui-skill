> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux 1.1 Pro Ultra Image 合作伙伴节点 ComfyUI 官方示例工作流

> 本文将介绍在 ComfyUI 中使用 Flux 1.1 Pro Ultra Image 合作伙伴节点的相关功能

FLUX 1.1 Pro Ultra 是由 BlackForestLabs 推出的高性能 AI 图像生成工具，主打超高分辨率与高效生成能力。它支持高达 4MP（标准版的 4 倍）的超清画质，同时将单张图像生成时间控制在 10 秒以内，速度比同类高分辨率模型快 2.5 倍。

该工具提供两种核心模式：

* **Ultra 模式**：专为高分辨率需求设计，适合广告、电商等需要细节放大的场景，能精准还原提示词并保持生成速度。
* **Raw 模式**：侧重自然真实感，优化人像肤色、光影及自然景观的细节，减少"AI 味"，适合摄影艺术和真实风格创作。

目前在 ComfyUI 中我们已经支持了 Flux 1.1 Pro Ultra Image 节点，在本篇文档中我们将涉及以下内容：

* Flux 1.1 Pro 文生图
* Flux 1.1 Pro 图生图（Remix）

<Tip>
  使用 API 节点需要保证你已经正常登录，并在受许可的网络环境下使用，请参考[API 节点总览](/zh-CN/tutorials/partner-nodes/overview)部分文档来了解使用 API 节点的具体使用要求。
</Tip>

<Tip>
  <Tabs>
    <Tab title="便携版或手动安装用户">
      请确保你的 ComfyUI 已经更新。

      * [ComfyUI 下载](https://www.comfy.org/download)
      * [ComfyUI 更新教程](/zh-CN/installation/update_comfyui)

      本指南里的工作流可以在 ComfyUI 的[工作流模板](/zh-CN/interface/features/template)中找到。如果找不到，可能是 ComfyUI 没有更新。

      如果加载工作流时有节点缺失，可能原因有：

      1. 你用的不是最新开发版（nightly）。
      2. 你用的是稳定版或桌面版（没有包含最新的更新）。
      3. 启动时有些节点导入失败。
    </Tab>

    <Tab title="桌面版或云端用户">
      * 桌面版是基于 ComfyUI 稳定版本构建的，它会在有新的桌面稳定版本发布时自动更新。
      * [Cloud](https://cloud.comfy.org) 会在 ComfyUI 稳定版本发布后更新，我们会同步更新 Cloud。

      所以，如果你发现本教程中有任何核心节点缺失，那是因为对应的节点支持还在开发中没有发布正式的稳定版，请等待下一个稳定版本发布。
    </Tab>
  </Tabs>
</Tip>

## Flux 1.1 Pro Ultra Image 节点文档

你可查阅下面的文档了解对应节点的详细参数设置

* [Flux 1.1 Pro Ultra Image](/zh-CN/built-in-nodes/partner-node/image/bfl/flux-1-1-pro-ultra-image)

## Flux 1.1 \[pro] 文生图教程

### 1. 工作流文件下载

请下载下面的文件，并拖入 ComfyUI 以加载对应的工作流

![Flux 1.1 pro 文生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_t2i.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b9403dd3baf434686961672addef2a39" alt="工作流步骤" data-og-width="3030" width="3030" data-og-height="1370" height="1370" data-path="images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1dcf01f603e0a9405e06db0f203f6b2b 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=475c7975f874a7fb2bc09755400ac4e0 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2d73cf69387fdf0e83acebf0361a8ceb 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a59ca6310db555c0f8a3be86b7f76f42 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c1790db75c5aaf75635767c055599d12 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=fae50fb73c4fa303b17c6a4ee900bcfd 2500w" />

你可参考图片中的序号来完成最基础的工作流运行

1. (可选)在 `Flux 1.1 [pro] Ultra Image` 节点的 `prompt` 修改工作流的提示词
2. （可选）修改 `raw` 参数为 `false`,可以让输出的图像更真实
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成
4. 等待 API 返回结果后，你可在`Save Image`节点中查看生成的图像, 对应的图像也会被保存至`ComfyUI/output/` 目录下

## Flux 1.1\[pro] 图生图教程

当我们在节点输入中添加了 `image_prompt` 则对应输出结果将会融合输入图片特点进行混合（Remix） ，`image_prompt_strength` 的大小影响混合的比例:数值越大与输入图像越相似.

### 1. 工作流文件下载

请下载下面的文件，并拖入 ComfyUI 以加载对应的工作流，或者在 **文生图工作流**  中紫色的节点上右键设置 `模式（mode）` 为 `总是（always）` 来启用 `image_prompt` 输入

![Flux 1.1 pro 图生图Remix](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_i2i.png)

我们会将下面的图片作为输入：
![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-3/text2image.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0217606be6c3f599e3d6ebd2fb14829a" alt="工作流步骤" data-og-width="2825" width="2825" data-og-height="1076" height="1076" data-path="images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ea1043fe60afb4874f2a0cfa7bfaaf88 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a326c96e4efbd900ad8889d6664465e6 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1583add49f0c0dd731630ddab7564d9c 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=61e7728a9cf17f93396d1af290ae15af 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2dbfbff8d7cb2552ed5daad1e6d1e8c6 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ea4e5fc6ce0dd3dfa287970ed4bc7b29 2500w" />

你可参考图片中的序号来完成最基础的工作流运行

1. 在 `Load Image` 节点上点击 **Upload** 上传输入图像
2. （可选）修改 `Flux 1.1 [pro] Ultra Image` 中的 `image_prompt_strength` 的大小，来改变混合的比例
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成
4. 等待 API 返回结果后，你可在`Save Image`节点中查看生成的图像, 对应的图像也会被保存至`ComfyUI/output/` 目录下

下面是不同 `image_prompt_strength` 的输出结果对比
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=eea7014b92e63f0b8d1bb50d5dae11c3" alt="" data-og-width="3150" width="3150" data-og-height="1173" height="1173" data-path="images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c3fd516ee3fbd72d0d7d5d408a2e3841 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4988d52a69ca1108662a380aabfc3bec 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b85cf288f13cad89155e50242583eb1a 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=24dd19e8afa467fb104b8dd75352afd6 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66c3a578ec5b785123d53d9bfa5b3b29 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4e199e171ba2aaf90d64bc1e911cd2b0 2500w" />
