> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Flux.2 Dev 示例

> 本文将简要介绍 Flux.2 模型，并指导你在 ComfyUI 中使用 Flux.2 Dev 模型进行文生图。

<iframe width="560" height="315" src="https://www.youtube.com/embed/TzTS74Ii23A?si=f2NFmhNbU2VI3PwX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## 关于 FLUX.2

[FLUX.2](https://bfl.ai/blog/flux-2) 是 [Black Forest Labs](https://blackforestlabs.ai/) 推出的下一代图像模型，可生成高达 4MP 的照片级真实输出，在光照、皮肤、织物和手部细节方面有显著提升。它支持可靠的多参考一致性（最多 10 张图像）、改进的编辑精度、更好的视觉理解能力以及专业级的文字渲染。

**主要特点：**

* **多参考一致性：** 在多个输出中可靠地保持身份、产品几何形状、纹理、材质、服装和构图意图
* **高分辨率照片级真实感：** 生成高达 4MP 的图像，具有真实世界的光照行为、空间推理和物理感知细节
* **专业级控制：** 精确的姿势控制、十六进制精确的品牌颜色、任意宽高比以及用于程序化工作流的结构化提示
* **可用的文字渲染：** 在 UI 界面、信息图表和多语言内容中生成清晰、易读的文字

**可用模型：**

* **FLUX.2 Dev：** 开源模型（本教程使用）
* **FLUX.2 Pro：** Black Forest Labs 的 API 版本

<Note>
  本工作流使用量化权重。原始 FLUX.2 仓库可在[此处](https://huggingface.co/black-forest-labs/FLUX.2-dev/)获取。
</Note>

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

## Flux.2 Dev 工作流

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_flux2.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 工作流文件</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_flux2&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>在 Comfy Cloud 上运行</p>
</a>

## 模型链接

**text\_encoders**

* [mistral\_3\_small\_flux2\_bf16.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_bf16.safetensors)

**diffusion\_models**

* [flux2\_dev\_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors)

**vae**

* [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors)

**模型存储位置**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── mistral_3_small_flux2_bf16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── flux2_dev_fp8mixed.safetensors
│   └── 📂 vae/
│          └── flux2-vae.safetensors
```
