> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan 3D API 节点模型生成 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Hunyuan 3D 节点的 API 进行 3D 模型生成

Hunyuan 3D 3.0 是腾讯推出的最先进的 3D 生成模型，可在几分钟内完成 3D 内容创建。它可以通过文本提示、图像或草图生成可用于生产的 3D 资产，大大降低了传统 3D 建模流程的门槛。

ComfyUI 现已原生集成了相应的 Hunyuan 3D API，让您可以方便地在 ComfyUI 中使用相关节点进行模型生成。

目前，ComfyUI 的合作伙伴节点支持以下 Hunyuan 3D 模型生成功能：

* 文本到 3D 生成
* 图像到 3D 生成
* 多视图到 3D 生成

<Tip>
  To use the API nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [API Nodes Overview](/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the API nodes.
</Tip>

<Tip>
  <Tabs>
    <Tab title="Portable or self deployed users">
      Make sure your ComfyUI is updated.

      * [Download ComfyUI](https://www.comfy.org/download)
      * [Update Guide](/installation/update_comfyui)

      Workflows in this guide can be found in the [Workflow Templates](/interface/features/template).
      If you can't find them in the template, your ComfyUI may be outdated. (Desktop version's update will delay sometime)

      If nodes are missing when loading a workflow, possible reasons:

      1. You are not using the latest ComfyUI version (Nightly version)
      2. Some nodes failed to import at startup
    </Tab>

    <Tab title="Desktop or Cloud users">
      * The Desktop is base on ComfyUI stable release, it will auto-update when there is a new Desktop stable release available.
      * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

      So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.
    </Tab>
  </Tabs>
</Tip>

## 使用场景

* **游戏开发创意**：快速生成角色、道具和环境，具有优化的拓扑结构，适用于绑定和实时渲染
* **产品与电商**：将产品照片转换为交互式 3D 模型，用于在线展示
* **工业设计**：草图到 3D 原型制作和 3D 打印就绪的零件分解
* **视觉特效与动画**：具有专业 UV 和 PBR 材质的高分辨率资产

## 开始使用

### 1. 访问工作流模板

1. 打开侧边栏中的模板库
2. 导航到 **3D** → **Hunyuan 3D**
3. 选择 Hunyuan 3D 的工作流模板

### 2. 运行工作流

1. 根据工作流类型输入文本提示、图像或草图
2. 点击 `Run` 按钮，或使用快捷键 `Ctrl(cmd) + Enter` 执行模型生成
3. 工作流完成后，预览并导出您的 3D 模型

## 文本到 3D 工作流

输入文本描述即可一键生成 3D 模型。模型能够准确遵循风格、形状和材质细节，确保结果一致。

**示例提示词**："带齿轮的机械海豚，蒸汽朋克风格"

<Card title="Hunyuan 3D 文本到 3D 工作流" icon="cloud" href="https://cloud.comfy.org/?template=api_hunyuan3d_text_to_model&utm_source=docs&utm_medium=inhouse_social&utm_campaign=inhouse_feature_launches&utm_content=post&utm_niche=workflow_engineering&utm_creator=purz">
  在 Comfy Cloud 上运行
</Card>

## 图像到 3D 工作流

上传一张或多张图像以生成高质量的 3D 模型。支持 2-4 张多视图图像可提高几何和材质的保真度。

<Card title="Hunyuan 3D 图像到 3D 工作流" icon="cloud" href="https://cloud.comfy.org/?template=api_hunyuan3d_image_to_model&utm_source=docs&utm_medium=inhouse_social&utm_campaign=inhouse_feature_launches&utm_content=post&utm_niche=workflow_engineering&utm_creator=purz">
  在 Comfy Cloud 上运行
</Card>

## 多视图到 3D 工作流

提供多个视角的图像（正面、背面、侧面）以生成精度和细节更高的 3D 模型。此功能与图像到 3D 使用相同的工作流——只需上传 2-4 张不同角度的图像即可。

<Card title="Hunyuan 3D 图像到 3D 工作流" icon="cloud" href="https://cloud.comfy.org/?template=api_hunyuan3d_image_to_model&utm_source=docs&utm_medium=inhouse_social&utm_campaign=inhouse_feature_launches&utm_content=post&utm_niche=workflow_engineering&utm_creator=purz">
  在 Comfy Cloud 上运行
</Card>
