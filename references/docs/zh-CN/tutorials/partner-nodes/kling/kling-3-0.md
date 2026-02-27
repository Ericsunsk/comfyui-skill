> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling 3.0 视频和图像生成 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Kling 3.0 模型，实现多镜头视频生成、主体一致性、多语言音频和原生文字渲染

Kling 3.0 是目前最先进的多模态生成系统之一，现已通过合作伙伴节点在 ComfyUI 中提供。此版本包括 **Kling Video 3.0**、**Kling Video 3.0 Omni**、**Kling Image 3.0** 和 **Kling Image 3.0 Omni**，将视频、图像、视听和叙事生成能力直接集成到你的节点工作流中。

## 关于 Kling 3.0

**核心功能：**

* **多镜头生成**：在单次生成中创建多个镜头并控制时长
* **锁定主体一致性**：在相机运动和场景演变中保持角色和物体的身份特征
* **原生音频与角色感知**：多语言对话，精确的口型同步和面部表情对齐
* **原生文字渲染**：为广告、UI 场景和品牌内容生成清晰、结构化的屏幕文字

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

## Kling 3.0 工作流

<CardGroup cols={2}>
  <Card title="I2V 工作流" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_v3_i2v.json">
    下载 Kling 3.0 图生视频工作流。
  </Card>

  <Card title="Omni 视频编辑工作流" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_v3_omni_video_edit.json">
    下载 Kling 3.0 Omni 视频编辑工作流。
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="在云端运行 I2V" icon="cloud" href="https://cloud.comfy.org/?template=api_kling_v3_i2v&utm_source=docs">
    在 Comfy Cloud 上即时体验图生视频工作流。
  </Card>

  <Card title="在云端运行 Omni 编辑" icon="cloud" href="https://cloud.comfy.org/?template=api_kling_v3_omni_video_edit&utm_source=docs">
    在 Comfy Cloud 上即时体验 Omni 视频编辑工作流。
  </Card>
</CardGroup>

## 了解更多

有关 Kling 3.0 功能的详细示例、提示词和视频演示，请查看我们的博客文章：

<Card title="Kling 3.0 模型现已上线" icon="newspaper" href="https://blog.comfy.org/p/kling-30-models-are-now-available">
  阅读完整公告，包含视频示例、提示词技巧和功能深度解析。
</Card>

## 可用模型

| 模型                       | 类型 | 描述             |
| ------------------------ | -- | -------------- |
| **Kling Video 3.0**      | 视频 | 支持多镜头的标准视频生成   |
| **Kling Video 3.0 Omni** | 视频 | 具有视听能力的高级视频生成  |
| **Kling Image 3.0**      | 图像 | 高质量图像生成        |
| **Kling Image 3.0 Omni** | 图像 | 具有增强功能的多模态图像生成 |
