> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Ideogram 3.0 合作伙伴节点官方示例

> 本文将介绍在 ComfyUI 中使用 Ideogram 3.0 合作伙伴节点的相关功能

Ideogram 3.0 是由 Ideogram 发布的一款强大的文本到图像生成模型，以其卓越的照片级逼真度、精确的文本渲染和一致的风格控制而著称。

目前[Ideogram V3](/zh-CN/built-in-nodes/partner-node/image/ideogram/ideogram-v3) 节点支持以下两种模式：

* 文生图模式
* 图像编辑模式（当同时提供了图像和遮罩输入时）

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

## Ideogram 3.0 节点文档

你可查阅下面的文档了解对应节点的详细参数设置等

* [Ideogram V3](/zh-CN/built-in-nodes/partner-node/image/ideogram/ideogram-v3)

## Ideogram 3.0 合作伙伴节点文生图模式

当你只使用 [Ideogram V3](/zh-CN/built-in-nodes/partner-node/image/ideogram/ideogram-v3) 而不输入图像和蒙版时，节点将使用文生图模式。

### 1. 工作流文件下载

请下载下面的文件，并拖入 ComfyUI 以加载对应的工作流

![Ideogram 3.0 ComfyUI 工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/ideogram/v3/ideogram_v3_t2i.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3f51da844d34d588570a037c3ef7a264" alt="Ideogram 3.0 工作流执行步骤图" data-og-width="2037" width="2037" data-og-height="1250" height="1250" data-path="images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=fb13382fe73f03cb4c7ce1e863ce4097 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a849b6be7e0a3149ef1ed52c58109eac 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cce20da548057f45ea7ed32691d6e10e 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=48413ebebe11db98eaf9f0858b0ee76c 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b87b10ed4fc43827aa9b213cb48a816d 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=07083fad209c20ec07201c3e7ac45721 2500w" />

你可参考图片中的序号来完成最基础的工作流运行

1. 在 `Ideogram V3` 节点的 `prompt` 中输入你想要生成的图像的描述
2. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成
3. 等待 API 返回结果后，你可在`Save Image`节点中查看生成的图像, 对应的图像也会被保存至`ComfyUI/output/` 目录下

## Ideogram 3.0 合作伙伴节点图像编辑模式

\[待更新]
