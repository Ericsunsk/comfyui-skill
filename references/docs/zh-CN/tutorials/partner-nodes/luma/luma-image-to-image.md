> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Image to Image 合作伙伴节点 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Luma Image to Image 合作伙伴节点的相关功能

[Luma Image to Image](/zh-CN/built-in-nodes/partner-node/image/luma/luma-image-to-image) 节点允许你使用Luma AI的技术根据文本提示词修改现有图像，同时保留原始图像的某些特征和结构。

本篇指南中，我们将引导你如何使用对应节点来进行图生图的工作流设置。

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

## Luma Image to Image 节点文档

你可查阅下面的文档了解对应节点的详细参数设置等

<Card title="Luma Image to Image 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/image/luma/luma-image-to-image">
  Luma Image to Image 合作伙伴节点说明文档
</Card>

## Luma Image to Image 合作伙伴节点图生图工作流

<Tip>
  这个功能在改变物体、形状等方面效果很好。但在改变颜色时,效果可能不太理想。建议使用较低的权重值,大约在0.0到0.1之间。
</Tip>

### 1. 工作流文件下载

下面的图片的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![Luma 图生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2i/luma_i2i.png)

请下载下面的图片，我们将用做输入图：

![Luma 图生图工作流输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2i/input.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0169a042868519a3cd76ef832fdc714a" alt="Luma 图生图工作流步骤图" data-og-width="2577" width="2577" data-og-height="1139" height="1139" data-path="images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d8384233bba5478b0c86cfc9decc214f 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=54c9dad2fe0366b78de2adc1993c1323 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3fd59ee81bfac6a5ecda6aa722f8d102 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d13fff5d7609ac2fa5805b6849635c88 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7b3d318fc1eb089f8ff39b63bf4ff8ee 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0ddc3da1e3aeb0b4c3f9bff7e0407975 2500w" />

你可参考图片中的序号来完成最基础的工作流运行

1. 在 `Load image` 节点中点击 **upload** 按钮上传输入图片
2. （可选）修改工作流的提示词
3. （可选）修改`image_weight` 来修改输入图片的权重（越小越接近原图）
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成
5. 等待 API 返回结果后，你可在`Save Image`节点中查看生成的图像, 对应的图片也会被保存至`ComfyUI/output/` 目录下

### 3. 不同 `image_weight` 参数输入结果

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d6fc32e5bdbf4f1368f73cfac583643d" alt="权重对比" data-og-width="3150" width="3150" data-og-height="1173" height="1173" data-path="images/tutorial/api_nodes/luma/i2i_image_weight.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=084939a3ef759130180a46e36b0b240c 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=359a906ca12d76263eba36a4e55185c0 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=826d2123c3c5f8497e92b3f977bfaac7 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=dcf51db85f394a66dffadbf651eeba7b 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=563736803d4fa3ec5e92d9c0f05ec5cb 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7403afda95b9ca243af876284db65271 2500w" />
