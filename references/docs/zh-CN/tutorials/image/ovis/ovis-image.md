> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Ovis-Image ComfyUI 工作流示例

> Ovis-Image 是一个 7B 文生图模型，专门针对高质量文本渲染进行优化，旨在严格的计算约束下高效运行。

**Ovis-Image** 是一个基于 [Ovis-U1](https://github.com/AIDC-AI/Ovis-U1) 构建的 7B 文生图模型，专门针对高质量文本渲染进行优化。它能够提供与更大的 20B 级别系统相当的文本渲染质量，同时保持足够紧凑，可在常见硬件上运行。

**模型亮点**：

* **7B 规模下的强大文本渲染**：提供与 Qwen-Image 等更大的 20B 级别系统相当的文本渲染质量，在文本场景中与 GPT4o 等领先的闭源模型具有竞争力
* **文本密集型提示词的高保真度**：擅长处理需要语言内容与渲染排版紧密对齐的提示词（如海报、横幅、标志、UI 模型、信息图表）
* **精准的双语文本渲染**：在各种字体、大小和宽高比下，生成清晰、拼写正确且语义一致的中英文文本
* **高效且易于部署**：可在单个高端 GPU 上运行，内存需求适中，支持低延迟交互使用

**相关链接**：

* [GitHub](https://github.com/AIDC-AI/Ovis-Image)
* [Hugging Face](https://huggingface.co/AIDC-AI/Ovis-Image-7B)

## Ovis-Image 文生图工作流

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_ovis_text_to_image.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 工作流文件</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_ovis_text_to_image&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
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

## 模型链接

**text\_encoders（文本编码器）**

* [ovis\_2.5.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/text_encoders/ovis_2.5.safetensors)

**diffusion\_models（扩散模型）**

* [ovis\_image\_bf16.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/diffusion_models/ovis_image_bf16.safetensors)

**vae**

* [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors)

**模型存储位置**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── ovis_2.5.safetensors
│   ├── 📂 diffusion_models/
│   │      └── ovis_image_bf16.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```
