> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Hunyuan3D-2 示例

> 本文将使用 Hunyuan3D-2 来完成在 ComfyUI 中 3D 资产生成的工作流示例。

# 混元3D 2.0 简介

![Hunyuan 3D 2](https://raw.githubusercontent.com/Tencent/Hunyuan3D-2/main/assets/images/e2e-1.gif)
![Hunyuan 3D 2](https://raw.githubusercontent.com/Tencent/Hunyuan3D-2/main/assets/images/e2e-2.gif)

[混元3D 2.0](https://github.com/Tencent/Hunyuan3D-2) 是腾讯推出的开源 3D 资产生成模型，可以通过文本、图像或草图生成带有高分辨率纹理贴图的高保真 3D 模型。

混元3D 2.0采用两阶段生成，首先采用生成无纹理的几何模型，再合成高分辨率的纹理贴图，有效分离了形状和纹理生成的复杂性，下面是混元3D 2.0的两个核心组件:

1. **几何生成模型（Hunyuan3D-DiT）**：基于流扩散的Transformer架构，生成无纹理的几何模型，可精准匹配输入条件。
2. **纹理生成模型（Hunyuan3D-Paint）**：结合几何条件和多视图扩散技术，为模型添加高分辨率纹理，支持PBR材质。

**主要优势**

* **高精度生成**：几何结构锐利，纹理色彩丰富，支持PBR材质生成，实现接近真实的光影效果。
* **多样化使用方式**：提供代码调用、Blender插件、Gradio应用及官网在线体验，适合不同用户需求。
* **轻量化与兼容性**：Hunyuan3D-2mini模型仅需5GB显存，标准版本形状生成需6GB显存，完整流程（形状+纹理）仅需12GB显存。

近期（2025 年 3 月 18 日），混元3D 2.0 还提供多视角形状生成模型（Hunyuan3D-2mv），支持从不同视角输入生成更精细的几何结构。

在本示例中包含三个工作流：

* 使用 Hunyuan3D-2mv 配合多个视图输入生成3D模型
* 使用 Hunyuan3D-2mv-turbo 配合多个视图输入生成3D模型
* 使用 Hunyuan3D-2 配合单个视图输入生成3D模型

<Tip>
  目前 ComfyUI 已原生支持 Hunyuan3D-2mv，暂未支持纹理和材质的生成，请在开始之前确保你已升级到最新版本的 [ComfyUI](https://github.com/comfyanonymous/ComfyUI)。

  本示例中工作流部分的输入图片示例 png 格式的图片的 Metadata 中包含工作流 json 的图片

  * 直接拖入 ComfyUI
  * 使用菜单 `Workflows` -> `Open（ctrl+o）`

  可以加载对应的工作流并提示完成模型下载，对应的 `.glb` 格式模型将输出至 `ComfyUI/output/mesh` 文件夹。
</Tip>

## ComfyUI Hunyuan3D-2mv 工作流示例

Hunyuan3D-2mv 工作流中，我们将使用多视角的图片来生成3D模型，另外多个视角的图片在这个工作流中并不是必须的，你可以只输入 `front` 视角的图片来生成3D模型。

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

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=3d_hunyuan3d_multiview_to_model&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

### 1. 工作流

请下载下面的图片，并拖入 ComfyUI 以加载工作流,

![Hunyuan3D-2mv workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/hunyuan-3d-multiview-elf.webp)

下载下面的图片，同时我们将使用这些图片作为图片输入

![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/front.png)
![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/left.png)
![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/back.png)

<Tip>
  在本示例中提供的输入图片都已经过提前处理去除了多余的背景，在实际的使用中，你可以借助类似[ComfyUI\_essentials](https://github.com/cubiq/ComfyUI_essentials) 这样的自定义来完成多余背景的自动去除。
</Tip>

### 2. 手动安装模型

下载下面的模型，并保存到对应的 ComfyUI 文件夹

* hunyuan3d-dit-v2-mv: [model.fp16.safetensors](https://huggingface.co/tencent/Hunyuan3D-2mv/resolve/main/hunyuan3d-dit-v2-mv/model.fp16.safetensors?download=true)  下载后可重命名为 `hunyuan3d-dit-v2-mv.safetensors`

```
ComfyUI/
├── models/
│   ├── checkpoints/
│   │   └── hunyuan3d-dit-v2-mv.safetensors  // 重命名后的文件
```

### 3. 按步骤运行工作流

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=17e6ac738f0e0133536bceb6e3ea1b56" alt="ComfyUI hunyuan3d_2mv" data-og-width="3000" width="3000" data-og-height="1618" height="1618" data-path="images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=9e42b6d0f41ffc9f6ceaa572386dcf3e 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=28c3841fabf7f4e776285bbc05ce7d52 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6bddcac5fe31ed37eec2b0ca80892364 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=123cc678058a9d792a1788ed4e246a2c 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=dbe9c37ce5d6241481b71a1c0965a4bd 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=9dcf8c15d43ca930dbb41af7072acc27 2500w" />

1. 确保 Image Only Checkpoint Loader(img2vid model) 加载了我们下载并重命名的 `hunyuan3d-dit-v2-mv.safetensors` 模型
2. 在 `Load Image` 节点的各个视角中加载了对应视角的图片
3. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

如果你需要增加更多的视角，请确保 `Hunyuan3Dv2ConditioningMultiView` 节点中加载了其它视角的图片，并确保在 `Load Image` 节点中加载了对应视角的图片。

## 使用 Hunyuan3D-2mv-turbo 工作流

Hunyuan3D-2mv-turbo 工作流中，我们将使用 Hunyuan3D-2mv-turbo 模型来生成3D模型，这个模型是 Hunyuan3D-2mv 的分步蒸馏（Step Distillation）版本，可以更快地生成3D模型，在这个版本的工作流中我们设置 `cfg` 为 1.0 并添加 `flux guidance` 节点来控制 `distilled cfg` 的生成。

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=3d_hunyuan3d_multiview_to_model_turbo&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

### 1. 工作流

请下载下面的图片，并拖入 ComfyUI 以加载工作流,

![Hunyuan3D-2mv-turbo workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_turbo/hunyuan-3d-turbo.webp)

我们将使用下面的图片作为多视角的输入

![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_turbo/front.png)
![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_turbo/right.png)

### 2. 手动安装模型

下载下面的模型，并保存到对应的 ComfyUI 文件夹

* hunyuan3d-dit-v2-mv-turbo: [model.fp16.safetensors](https://huggingface.co/tencent/Hunyuan3D-2mv/resolve/main/hunyuan3d-dit-v2-mv-turbo/model.fp16.safetensors?download=true)  下载后可重命名为 `hunyuan3d-dit-v2-mv-turbo.safetensors`

```
ComfyUI/
├── models/
│   ├── checkpoints/
│   │   └── hunyuan3d-dit-v2-mv-turbo.safetensors  // 重命名后的文件
```

### 3. 按步骤运行工作流

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=33bb861fd695fd4b10a53345f004d2cc" alt="ComfyUI hunyuan3d_2mv_turbo" data-og-width="3000" width="3000" data-og-height="1621" height="1621" data-path="images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=4f8fc51054f97a10e0c1d3b55cc3f6a5 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=18b71c565a8ac2fed93fe1357d0f3675 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=b9bcdff38ec468193b8e226fb29f75ae 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=acb764f7ce1b01fb295bc2e4d2c62736 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=dec0c68da4a0cadff5d596b2da3ec85e 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6380467b73bddf75b59a77e76e160273 2500w" />

1. 确保 `Image Only Checkpoint Loader(img2vid model)` 节点加载了我们重命名后的 `hunyuan3d-dit-v2-mv-turbo.safetensors` 模型
2. 在 `Load Image` 节点的各个视角中加载了对应视角的图片
3. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

## 使用 Hunyuan3D-2 单视图工作流

Hunyuan3D-2 工作流中，我们将使用 Hunyuan3D-2 模型来生成3D模型，这个模型不是一个多视角的模型，在这个工作流中，我们使用`Hunyuan3Dv2Conditioning` 节点替换掉 `Hunyuan3Dv2ConditioningMultiView` 节点。

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=3d_hunyuan3d_image_to_model&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

### 1. 工作流

请下载下面的图片，并拖入 ComfyUI 以加载工作流

![Hunyuan3D-2 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d-non-multiview-train.webp)

同时我们将使用这张图片作为图片输入

![ComfyUI Hunyuan 3D 2 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan_3d_v2_non_multiview_train.png)

### 2. 手动安装模型

下载下面的模型，并保存到对应的 ComfyUI 文件夹

* hunyuan3d-dit-v2-0: [model.fp16.safetensors](https://huggingface.co/tencent/Hunyuan3D-2/resolve/main/hunyuan3d-dit-v2-0/model.fp16.safetensors?download=true)  下载后可重命名为 `hunyuan3d-dit-v2.safetensors`

```
ComfyUI/
├── models/
│   ├── checkpoints/
│   │   └── hunyuan3d-dit-v2.safetensors  // 重命名后的文件
```

### 3. 按步骤运行工作流

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=33c158fcfb133560674aa56bfdb5087d" alt="ComfyUI hunyuan3d_2" data-og-width="3000" width="3000" data-og-height="1624" height="1624" data-path="images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c577c3cf599981076e6fbd785564e55c 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ab1a5bdb4aa0691bb7c41d643cf354a1 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=67127b905771176d81f36e7a8e59b38b 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=4648a8e392939372cd68cd10de587e8b 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=84e03ff178ff77a94eb8fb806f6d4234 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=d53501f12fcd700e312fddc1dd12154b 2500w" />

1. 确保 `Image Only Checkpoint Loader(img2vid model)` 节点加载了我们重命名后的 `hunyuan3d-dit-v2.safetensors` 模型
2. 在 `Load Image` 节点中加载了对应视角的图片
3. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

## 社区资源

下面是 Hunyuan3D-2 的相关的 ComfyUI 社区资源

* [ComfyUI-Hunyuan3DWrapper](https://github.com/kijai/ComfyUI-Hunyuan3DWrapper)
* [Kijai/Hunyuan3D-2\_safetensors](https://huggingface.co/Kijai/Hunyuan3D-2_safetensors/tree/main)
* [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack)

## 混元3D 2.0 开源模型系列

目前混元3D 2.0 开源了多个模型，覆盖了完整的3D生成流程，你可以访问 [Hunyuan3D-2](https://github.com/Tencent/Hunyuan3D-2) 了解更多。

**Hunyuan3D-2mini 系列**

| 模型                    | 描述           | 日期         | 参数   | Huggingface                                                                          |
| --------------------- | ------------ | ---------- | ---- | ------------------------------------------------------------------------------------ |
| Hunyuan3D-DiT-v2-mini | Mini 图像到形状模型 | 2025-03-18 | 0.6B | [前往](https://huggingface.co/tencent/Hunyuan3D-2mini/tree/main/hunyuan3d-dit-v2-mini) |

**Hunyuan3D-2mv 系列**

| 模型                       | 描述                              | 日期         | 参数   | Huggingface                                                                           |
| ------------------------ | ------------------------------- | ---------- | ---- | ------------------------------------------------------------------------------------- |
| Hunyuan3D-DiT-v2-mv-Fast | 指导蒸馏版本，可以将 DIT 推理时间减半           | 2025-03-18 | 1.1B | [前往](https://huggingface.co/tencent/Hunyuan3D-2mv/tree/main/hunyuan3d-dit-v2-mv-fast) |
| Hunyuan3D-DiT-v2-mv      | 多视角图像到形状模型，适合需要用多个角度理解场景的 3D 创作 | 2025-03-18 | 1.1B | [前往](https://huggingface.co/tencent/Hunyuan3D-2mv/tree/main/hunyuan3d-dit-v2-mv)      |

**Hunyuan3D-2 系列**

| 模型                      | 描述      | 日期         | 参数   | Huggingface                                                                        |
| ----------------------- | ------- | ---------- | ---- | ---------------------------------------------------------------------------------- |
| Hunyuan3D-DiT-v2-0-Fast | 指导蒸馏模型  | 2025-02-03 | 1.1B | [前往](https://huggingface.co/tencent/Hunyuan3D-2/tree/main/hunyuan3d-dit-v2-0-fast) |
| Hunyuan3D-DiT-v2-0      | 图像到形状模型 | 2025-01-21 | 1.1B | [前往](https://huggingface.co/tencent/Hunyuan3D-2/tree/main/hunyuan3d-dit-v2-0)      |
| Hunyuan3D-Paint-v2-0    | 纹理生成模型  | 2025-01-21 | 1.3B | [前往](https://huggingface.co/tencent/Hunyuan3D-2/tree/main/hunyuan3d-paint-v2-0)    |
| Hunyuan3D-Delight-v2-0  | 图像去光影模型 | 2025-01-21 | 1.3B | [前往](https://huggingface.co/tencent/Hunyuan3D-2/tree/main/hunyuan3d-delight-v2-0)  |
