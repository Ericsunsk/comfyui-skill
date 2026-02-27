> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 工作流

## 节点图

ComfyUI 是一个用于构建和运行生成内容的 ***工作流*** 的环境。在这个上下文中，工作流被定义为一组称为 ***节点*** 的程序对象，它们相互连接，形成一个网络。这个网络也被称为 ***图***。

ComfyUI 工作流可以生成任何类型的媒体：图像、视频、音频、AI 模型、AI 代理等。

## 示例工作流

要开始，请使用内置的[工作流模板](/zh-CN/interface/features/template)。通过菜单 `Workflow` → `Browse Workflow Templates` 打开。这些模板仅使用 ComfyUI 安装中包含的核心节点，并会自动提示您下载所需的模型。一个蓬勃发展的开发者社区创建了丰富的 [生态系统](https://registry.comfy.org) 的自定义节点，以扩展 ComfyUI 的功能。

### 简单示例

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=60028deaf5c13f399515ca2027f680e6" alt="简单工作流" data-og-width="1400" width="1400" data-og-height="637" height="637" data-path="images/simple_workflow.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=44b4c2822d777030f13340f9076c9e41 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=17c74acde982dffc3890f4d4d0781bf8 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6c44653c323146e9578e277dca28d6bd 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=867c4d06c3510d67daeddff1251a47ea 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3fad15ddc2e7c040f2b444fe2b62849a 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a23372305e8c14c8797350f56ef29078 2500w" />

## 可视化编程

像 ComfyUI 这样的基于节点的计算机程序提供了一种传统菜单和按钮驱动应用程序无法实现的强大灵活性。ComfyUI 节点图不受传统计算机应用程序提供的工具的限制。它是一个高级的 ***可视化编程环境***，允许用户设计复杂的系统，而无需编写程序代码或理解高级数学。

许多其他计算机应用程序也使用相同的节点图范式。示例包括合成应用程序 Nuke、3D 程序 Maya 和 Blender、实时图形引擎 Unreal，以及交互媒体创作程序 Max。

### 更复杂的示例

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=72268aab0bf1c70be6388930d50aa983" alt="复杂工作流" data-og-width="1000" width="1000" data-og-height="511" height="511" data-path="images/complex_workflow.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9efef3c1cfc3f6987ee96b766e13e5f3 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c0b199f01cfd67377ee9b38c361764a3 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6a8866c954c07678fc29dbe1748f61cf 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a7c7ec3f73860b7d36c41889b65911cb 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b800e44f63e64f1346cb72b60b51864b 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c5559937ae61c95c9e025977585b8a68 2500w" />

## 过程框架

另一个用于描述基于节点的应用程序的术语是 ***过程框架***。过程意味着生成：某种过程或算法被用来生成内容，例如 3D 模型或音乐作品。

ComfyUI 是所有这些东西：一个节点图、一个可视化编程环境和一个过程框架。使 ComfyUI 不同（并且令人惊叹！）的是，它的开放结构允许我们生成任何类型的媒体资产，例如图片、电影、声音、3D 模型、AI 模型等。

在 ComfyUI 的上下文中，***工作流*** 这个术语是节点网络或图的同义词。它对应于 3D 或多媒体程序中的 ***场景图***：特定磁盘文件中所有节点的网络。3D 程序称之为 ***场景文件***。视频编辑、合成和多媒体程序通常称之为 ***项目文件***。

## 保存工作流

ComfyUI 工作流会自动保存在任何生成图像的元数据中，允许用户打开并使用生成图像的图形。工作流也可以存储在遵循 JSON 数据格式的人类可读文本文件中。这对于不支持元数据的媒体格式是必要的。以 JSON 文件格式存储的 ComfyUI 工作流非常小，便于版本控制、归档和共享图形，而不依赖于任何生成的媒体。
