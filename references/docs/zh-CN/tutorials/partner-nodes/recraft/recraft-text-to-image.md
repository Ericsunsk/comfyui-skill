> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Text to Image 合作伙伴节点 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Recraft Text to Image 合作伙伴节点的相关功能

[Recraft Text to Image](/zh-CN/built-in-nodes/partner-node/image/recraft/recraft-text-to-image) 节点允许你使用Recraft AI的图像生成技术，通过文本描述创建高质量、风格多样的图像内容。

本篇指南中，我们将引导你如何使用对应节点来进行文本到图像的工作流设置。

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

## Recraft Text to Image 合作伙伴节点文本到图像工作流

### 1. 工作流文件下载

下面的图片的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![Recraft 文本到图像工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/recraft/t2i/recraft_t2i.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=26e3744a4e7c44a1d72840e8ffef5c3c" alt="Recraft 文本到图像工作流步骤图" data-og-width="2822" width="2822" data-og-height="1505" height="1505" data-path="images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=dc89e07d6e583587d024f85b99626261 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=10cce0cedd135dbfef4efe38ea61eeab 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=46b3c2bbad43ffa402380f256c2e899d 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4617e18965b44fb37f0c6652a1b8961c 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=02b68dffb02846a5793b0487a2a34173 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b341b7afdec336aabccf223c6312f31f 2500w" />

你可参考图片中的序号来完成最基础的工作流运行：

1. (可选) 修改 `Color` 的 `Recraft Color RGB` 的颜色为你想要的颜色
2. (可选) 修改 `Recraft Style` 节点来控制图像的视觉风格，如数字插画、真实照片或Logo设计等，这个分组同时提供了其它的风格节点，你可以按需启用
3. (可选) 修改 `Recraft Text to Image` 节点中的 `prompt` 参数，你也可以通过修改`size`参数来改变
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图像的生成
5. 等待 API 返回结果后，你可在 `Save Image` 节点中查看生成的图像，对应的图像也会被保存至 `ComfyUI/output/` 目录下

> (可选) 我们在工作流中提供了 **Convert to SVG** 的分组，由于该分组中的 `Recraft Vectorize Image` 节点也会额外消耗积分，你可按需启用，将生成的图像转换成 SVG 格式

### 3. 补充说明

* **Recraft Style**：提供多种预设风格，如真实照片、数字插画、Logo栅格等
* **Seed 参数**：仅用于确定节点是否应重新运行，但实际生成结果与种子值无关

## 相关节点详解

你可查阅下面的文档了解对应节点的详细参数设置等

<Card title="Recraft Text to Image 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/image/recraft/recraft-text-to-image">
  Recraft Text to Image 合作伙伴节点说明文档
</Card>

<Card title="Recraft Style 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/image/recraft/recraft-style-realistic-image">
  Recraft Style - Realistic Image 合作伙伴节点说明文档
</Card>

<Card title="Recraft Controls 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/image/recraft/recraft-controls">
  Recraft Controls 合作伙伴节点说明文档
</Card>
