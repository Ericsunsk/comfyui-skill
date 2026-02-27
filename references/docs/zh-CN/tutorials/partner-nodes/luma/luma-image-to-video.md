> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Image to Video 合作伙伴节点 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Luma Image to Video 合作伙伴节点的相关功能

[Luma Image to Video](/zh-CN/built-in-nodes/partner-node/video/luma/luma-image-to-video) 节点允许你使用Luma AI的先进技术将静态图像转换为流畅、动态的视频内容，为图像赋予生命力和动态特性。

本篇指南中，我们将引导你如何使用对应节点来进行图像到视频的工作流设置。

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

## Luma Image to Video 节点文档

你可查阅下面的文档了解对应节点的详细参数设置等

<Card title="Luma Image to Video 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/video/luma/luma-image-to-video">
  Luma Image to Video 合作伙伴节点说明文档
</Card>

<Card title="Luma Concepts 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/video/luma/luma-concepts">
  Luma Concepts 合作伙伴节点说明文档
</Card>

## Luma Image to Video 合作伙伴节点图像到视频工作流

Luma Image to Video 节点需要至少提供一个图像输入（`first_image`或`last_image`），结合文本提示词来确定视频的动态效果。在本篇指南中，我们制作了使用`first_image`和`luma_concepts`的示例，让你体验Luma AI在视频生成上的优秀能力。

### 1. 工作流文件下载

下面的视频的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![Luma 图像到视频工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2v/luma_i2v.mp4)

请下载下面的图片，我们将会用作输入：

![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2v/input.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f55c824ff729382814a2e86e35b9f309" alt="Luma 图像到视频工作流步骤图" data-og-width="2492" width="2492" data-og-height="1515" height="1515" data-path="images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=87d66e016ff643f5d0d9e260ffe5f2b3 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6f939ce7a2ebb6f25c9c8a9f896282a4 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4c67f8b817722d7d9cbf51c97b755e6f 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3517730a261ab09b09da43b354a4f181 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f4f6e700862bf6483f1c1fe8bfc3cabc 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=eb3983d8bd61e7e960ef16bc385706d5 2500w" />

你可参考图片中的序号来完成最基础的工作流运行：

1. 在 `first_image` 节点中上传你的输入图像
2. (可选)在 Luma Image to Video 节点中编写提示词，描述你希望视频如何动态展示图像
3. (可选)修改 `Luma Concepts` 节点来控制相机运动效果，为视频添加专业的镜头语言
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频的生成
5. 等待 API 返回结果后，你可在 `Save Video` 节点中查看生成的视频，对应的视频也会被保存至 `ComfyUI/output/` 目录下

### 3. 补充说明

* **输入图像要求**：`first_image` 和 `last_image` 至少需要提供一个，每个输入最多只接受1张图片
* **Luma Concepts**：主要用于控制相机运动，提供更专业的视频镜头效果
* **Seed 参数**：仅用于确定节点是否应重新运行，但实际生成结果与种子值无关
* **启用输入节点**：要启用对应的输入请在目前紫色"绕过（Bypass）"模式的节点上右键，设置对应的"模式（mode）"为"总是（always）"
* **模型选择**：不同的视频生成模型有不同的特点，可以通过调整 model 参数来选择
* **分辨率与时长**：可以通过 resolution 和 duration 参数来调整输出视频的分辨率和时长
