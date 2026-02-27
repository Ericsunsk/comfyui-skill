> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Z-Image ComfyUI 工作流示例

> Z-Image 是一个拥有 6B 参数的高效图像生成基础模型，采用单流扩散变换器架构，适用于社区驱动的微调和自定义开发。

**Z-Image（造相）** 是阿里巴巴通义实验室开发的一个强大且高效的图像生成模型，拥有 **6B** 参数。它采用 **可扩展单流 DiT**（S3-DiT）架构，将文本、视觉语义 token 和图像 VAE token 在序列级别进行拼接，作为统一的输入流，最大化参数效率。

Z-Image（Base）是非蒸馏基础模型，专为社区驱动的微调和自定义开发而设计。

**模型亮点**：

* **照片级真实质量**：在保持出色美学质量的同时，提供强大的照片级真实图像生成
* **精准的双语文本渲染**：擅长准确渲染复杂的中英文文本
* **提示词增强与推理**：提示词增强器赋予模型推理能力
* **微调就绪**：适合自定义训练和适配的理想基础模型

**相关链接**：

* [GitHub](https://github.com/Tongyi-MAI/Z-Image)
* [Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image)
* [ModelScope](https://modelscope.cn/models/Tongyi-MAI/Z-Image)

## Z-Image 文生图工作流

<CardGroup cols={2}>
  <Card title="下载工作流" icon="download" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_z_image.json">
    下载 Z-Image 文生图工作流 JSON 文件。
  </Card>

  <Card title="在 ComfyUI Cloud 上运行" icon="cloud" href="https://cloud.comfy.org/?template=image_z_image&utm_source=docs&utm_medium=inhouse_social&utm_campaign=z_image_launch">
    在 ComfyUI Cloud 上直接运行此工作流。
  </Card>
</CardGroup>

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

## Z-Image 模型下载

<CardGroup cols={2}>
  <Card title="qwen_3_4b.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors">
    Z-Image 文本编码器。
  </Card>

  <Card title="z_image_bf16.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/z_image/resolve/main/split_files/diffusion_models/z_image_bf16.safetensors">
    Z-Image 扩散模型。
  </Card>

  <Card title="ae.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors">
    Z-Image VAE。
  </Card>
</CardGroup>

**模型存储位置**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_3_4b.safetensors
│   ├── 📂 diffusion_models/
│   │      └── z_image_bf16.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```
