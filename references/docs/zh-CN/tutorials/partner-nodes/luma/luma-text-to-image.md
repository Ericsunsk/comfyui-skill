> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Text to Image 合作伙伴节点 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Luma Text to Image 合作伙伴节点的相关功能

[Luma Text to Image](/zh-CN/built-in-nodes/partner-node/image/luma/luma-text-to-image) 节点允许你使用Luma AI的先进技术根据文本提示词生成高质量的图像，能够创建照片级别的逼真内容和艺术风格图像。

本篇指南中，我们将引导你如何使用对应节点来进行文本生图的工作流设置。

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

## Luma Text to Image 节点文档

你可查阅下面的文档了解对应节点的详细参数设置等

<Card title="Luma Text to Image 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/image/luma/luma-text-to-image">
  Luma Text to Image 合作伙伴节点说明文档
</Card>

<Card title="Luma Reference 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/image/luma/luma-reference">
  Luma Reference 合作伙伴节点说明文档
</Card>

## Luma Text to Image 合作伙伴节点文本生图工作流

在 `Luma Text to Image` 节点没有使用任何的图像输入时，对应的工作流则为文生图工作流，在本篇指南中，我们制作了使用`style_image` 和 `image_luma_ref` 的示例。
能够让你体验到 Luma AI 在相关图像处理上的优秀能力。

### 1. 工作流文件下载

下面的图片的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![Luma 文本生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/luma_t2i.png)

请下载下面的图片，我们将会用作输入：

![输入图片-参考](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/input_ref.png)
![输入图片-风格](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/input_style.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3122c711034e8270d086ae8c139cb64" alt="Luma 文本生图工作流步骤图" data-og-width="2796" width="2796" data-og-height="1694" height="1694" data-path="images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=34ce72b35a6ce916e2a7cf68bf4d7fab 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b76ef973b5623f2575f08f49279a2c96 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9dbd9de85a6331dbc3dcc0c231adc666 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=870888519eeb09fdabafdf4b867be154 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=69acf9a0fa4ce079286baa22ba66be8d 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=82a2b77c63649c49c8ceae305f539915 2500w" />

你可参考图片中的序号来完成最基础的工作流运行  

1. 在 `Load image` 节点中上传参考图像
2. 在 `Load image（已重命名为 styleref）` 节点中上传风格参考图像
3. （可选）修改 `Luma Text to Image` 节点的提示词
4. （可选）修改 `style_image_weight` 的权重，来调整风格参考图像的权重
5. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成
6. 等待 API 返回结果后，你可在`Save Image`节点中查看生成的图像, 对应的图片也会被保存至`ComfyUI/output/` 目录下

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7f47d2d3a6acdde87df046460afa393f" alt="不同 style_image_weight 效果对比" data-og-width="2100" width="2100" data-og-height="1867" height="1867" data-path="images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=155cadfd9a346447a26ece679de9b2b8 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e2b792354983726d5c33e3c69f8273a5 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0bbb226eb88b380096e0a52238f80898 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1889cb637e62fdcc7b2be4b7ee925355 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7d237e41b44d0249359126ae88c8d1c6 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5e6f5eb502e8347dc1267d7bff119215 2500w" />

### 3. 补充说明

* [对应的节点](/zh-CN/built-in-nodes/partner-node/image/luma/luma-text-to-image)同时允许最多同时分别输入 4 张参考图和角色参考。
* 如果要启用多张图像输入参考，请在对应“紫色”的处于`绕过(Bypass)` 的节点上右键，将对应的 `模式（mode）` 设置为 `总是（always）`
