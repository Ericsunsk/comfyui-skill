> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen-Image-Layered ComfyUI 工作流示例

> Qwen-Image-Layered 是一个能够将图像分解为多个 RGBA 图层的模型，通过图层分解实现固有的可编辑性。

**Qwen-Image-Layered** 是阿里巴巴通义千问团队开发的模型，能够将图像分解为多个 RGBA 图层。这种分层表示解锁了固有的可编辑性：每个图层都可以独立操作而不影响其他内容。

**主要特性**：

* **固有可编辑性**：每个图层都可以独立操作而不影响其他内容
* **高保真基础操作**：支持调整大小、重新定位和重新着色，语义组件物理隔离
* **可变图层分解**：不限于固定数量的图层 - 可根据需要分解为 3、4、8 或更多图层
* **递归分解**：任何图层都可以进一步分解，实现无限分解深度

**相关链接**：

* [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Layered)
* [研究论文](https://arxiv.org/abs/2512.15603)
* [博客](https://qwenlm.github.io/blog/qwen-image-layered/)

## Qwen-Image-Layered 工作流

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_layered.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_qwen_image_layered&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>在 ComfyUI Cloud 上运行</p>
</a>

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

## 模型下载

**text\_encoders**

* [qwen\_2.5\_vl\_7b\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**diffusion\_models**

* [qwen\_image\_layered\_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_layered_bf16.safetensors)

**vae**

* [qwen\_image\_layered\_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/main/split_files/vae/qwen_image_layered_vae.safetensors)

**模型保存位置**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 diffusion_models/
│   │      └── qwen_image_layered_bf16.safetensors
│   └── 📂 vae/
│          └── qwen_image_layered_vae.safetensors
```

## FP8 版本

默认使用 bf16，需要较高显存。如需降低显存使用，可以使用 fp8 版本：

* [qwen\_image\_layered\_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_layered_fp8mixed.safetensors)

然后更新[子图](/zh-CN/interface/features/subgraph)中的 **Load Diffusion model** 节点来使用它。

## 工作流设置

### 采样器设置

该模型运行较慢。原始采样设置为 steps: 50 和 CFG: 4.0，这将至少使生成时间翻倍。

### 输入尺寸

输入尺寸建议使用 640px。如需高分辨率输出，请使用 1024px。

### 提示词（可选）

文本提示词用于描述输入图像的整体内容——包括可能被部分遮挡的元素（例如，你可以指定隐藏在前景物体后面的文字）。它不是用来明确控制各个图层的语义内容的。
