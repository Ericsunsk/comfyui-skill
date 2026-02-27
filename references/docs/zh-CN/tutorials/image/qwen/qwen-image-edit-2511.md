> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen-Image-Edit-2511 ComfyUI 原生工作流示例

> Qwen-Image-Edit-2511 是 Qwen-Image-Edit 的增强版本，具有改进的角色一致性、多人编辑、集成 LoRA 功能和增强的几何推理能力。

**Qwen-Image-Edit-2511** 是 Qwen-Image-Edit-2509 的增强版本，具有多项改进，包括显著提升的一致性。该模型将 Qwen-Image 独特的文本渲染能力扩展到编辑任务，实现精准的文字编辑，同时具备语义/外观双重编辑能力。

**Qwen-Image-Edit-2511 的主要增强**：

* **减少图像漂移**：编辑操作期间稳定性提升
* **改进角色一致性**：在创意编辑过程中更好地保留身份和视觉特征
* **多人一致性**：将多张人物图像高保真融合为连贯的合照
* **集成 LoRA 功能**：热门社区 LoRA 直接内置于基础模型中
* **增强工业设计生成**：更好地支持批量工业产品设计和材质替换
* **强化几何推理**：直接生成用于设计或标注的辅助构造线

**官方链接**：

* [GitHub 仓库](https://github.com/QwenLM/Qwen-Image)
* [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)
* [ModelScope](https://modelscope.cn/models/Qwen/Qwen-Image-Edit-2511)
* [技术报告](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf)
* [博客](https://qwenlm.github.io/blog/qwen-image-edit-2511/)

## Qwen-Image-Edit-2511 ComfyUI 原生工作流示例

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

### 1. 工作流文件

更新 ComfyUI 后你可以从模板中找到工作流文件，或者将下面的工作流拖入 ComfyUI 中加载。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_edit_2511.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_qwen_image_edit_2511&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>在 ComfyUI Cloud 上运行</p>
</a>

### 2. 模型下载

**Text Encoders（文本编码器）**

* [qwen\_2.5\_vl\_7b\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**LoRA（可选 - 用于 4 步 Lightning 加速）**

* [Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/resolve/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors)

**Diffusion Models（扩散模型）**

* [qwen\_image\_edit\_2511\_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors)

**VAE**

* [qwen\_image\_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors)

**模型存储位置**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 loras/
│   │      └── Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── qwen_image_edit_2511_bf16.safetensors
│   └── 📂 vae/
│          └── qwen_image_vae.safetensors
```
