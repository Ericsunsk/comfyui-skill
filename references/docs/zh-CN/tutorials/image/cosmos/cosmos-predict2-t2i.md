> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Cosmos Predict2 文生图 ComfyUI 官方示例

> 本文介绍了如何在 ComfyUI 中完成 Cosmos-Predict2 文生图的工作流

Cosmos-Predict2 是由 NVIDIA 推出的新一代物理世界基础模型，专为物理 AI 场景下的高质量视觉生成与预测任务设计。
该模型具备极高的物理准确性、环境交互性和细节还原能力，能够真实模拟复杂的物理现象与动态场景。
Cosmos-Predict2 支持文本到图像（Text2Image）和视频到世界（Video2World）等多种生成方式，广泛应用于工业仿真、自动驾驶、城市规划、科学研究等领域，是推动智能视觉与物理世界深度融合的重要基础工具。

GitHub:[Cosmos-predict2](https://github.com/nvidia-cosmos/cosmos-predict2)
huggingface: [Cosmos-Predict2](https://huggingface.co/collections/nvidia/cosmos-predict2-68028efc052239369a0f2959)

本篇指南将引导你完成在 ComfyUI 中  **文生图** 工作流程。

对于视频生成部分，请参考下面的部分

<Card title="Cosmos Predict2 视频生成" icon="book" href="/zh-CN/tutorials/video/cosmos/cosmos-predict2-video2world">
  使用 Cosmos-Predict2 的进行视频生成
</Card>

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
