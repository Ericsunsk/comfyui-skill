> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Text to Video 合作伙伴节点 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Luma Text to Video 合作伙伴节点的相关功能

[Luma Text to Video](/zh-CN/built-in-nodes/partner-node/video/luma/luma-text-to-video) 节点允许你使用Luma AI的创新视频生成技术，通过文本描述创建高质量、流畅的视频内容。

本篇指南中，我们将引导你如何使用对应节点来进行文本到视频的工作流设置。

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

## Luma Text to Video 节点文档

你可查阅下面的文档了解对应节点的详细参数设置等

<Card title="Luma Text to Video 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/video/luma/luma-text-to-video">
  Luma Text to Video 合作伙伴节点说明文档
</Card>

<Card title="Luma Concepts 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/video/luma/luma-concepts">
  Luma Concepts 合作伙伴节点说明文档
</Card>

## Luma Text to Video 合作伙伴节点文本到视频工作流

Luma Text to Video 节点需要提供文本提示词来描述生成视频内容。在本篇指南中，我们制作了使用`prompt`和`luma_concepts`的示例，让你体验Luma AI在视频生成上的优秀能力。

### 1. 工作流文件下载

下面的视频的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![Luma 文本到视频工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2v/luma_t2v.mp4)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=96c92693534372a8522603f9c13f088c" alt="Luma 文本到视频工作流步骤图" data-og-width="2097" width="2097" data-og-height="1691" height="1691" data-path="images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7650813bb283f9aabc784d63f2b51547 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ec60e49f9dd61d17f616779b56f785bc 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=de082bf41aef1a9d5464b2971d4f2e2b 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=566048bcd6c3df8e54bb999af0e94715 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7cfc31fc22b5ebd5c567e9f1fecb51bf 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c0c093965f3aa083066ed153937f8dab 2500w" />

你可参考图片中的序号来完成最基础的工作流运行：

1. 在 `Luma Text to Video` 节点中编写提示词，描述你希望生成的视频内容
2. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频的生成
3. 等待 API 返回结果后，你可在 `Save Video` 节点中查看生成的视频，对应的视频也会被保存至 `ComfyUI/output/` 目录下

> (可选)修改 `Luma Concepts` 节点来控制相机运动效果，为视频添加专业的镜头语言

### 3. 补充说明

* **提示词撰写**：尽可能详细地描述场景、主体、动作和氛围，以获得最佳生成效果
* **Luma Concepts**：主要用于控制相机运动，提供更专业的视频镜头效果
* **Seed 参数**：仅用于确定节点是否应重新运行，但实际生成结果与种子值无关
* **模型选择**：不同的视频生成模型有不同的特点，可以通过调整 model 参数来选择
* **分辨率与时长**：可以通过 resolution 和 duration 参数来调整输出视频的分辨率和时长
* **Ray 1.6 模型注意事项**：当使用 Ray 1.6 模型时，duration 和 resolution 参数将不会生效
