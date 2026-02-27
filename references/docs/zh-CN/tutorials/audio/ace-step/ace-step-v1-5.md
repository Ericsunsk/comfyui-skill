> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI ACE-Step 1.5 AI 音乐生成指南

> 学习如何在 ComfyUI 中使用 ACE-Step 1.5 进行 AI 音乐生成。包含 ComfyUI 工作流、模型下载和设置说明的完整指南。

## 关于 ComfyUI 中的 ACE-Step 1.5

ACE-Step 1.5 是开源音乐生成模型的重大更新，现已在 ComfyUI 中原生支持。它将商业级质量带到你的本地机器上，采用新颖的混合架构，其中语言模型作为全能规划器，将简单的用户查询转换为完整的歌曲蓝图。

**ACE-Step 1.5 模型亮点：**

* **商业级质量**：在音乐连贯性方面达到 4.72 分，超越大多数商业音乐模型
* **极速生成**：使用 ComfyUI 在 RTX 5090 上约 1 秒生成完整的 4 分钟歌曲，在 RTX 3090 上不到 10 秒
* **50+ 语言支持**：对英语、中文、日语、韩语、西班牙语、德语、法语、葡萄牙语、意大利语和俄语有强大支持
* **LoRA 微调**：支持在 ComfyUI 中通过 LoRA 训练进行轻量级个性化定制

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

## 选项 1：一体化 Checkpoint（推荐）

AIO 版本将所有模型打包成单个 checkpoint 文件，更易于下载和管理。

### AIO 工作流

<CardGroup cols={2}>
  <Card title="在 Comfy Cloud 运行" icon="cloud" href="https://cloud.comfy.org/?template=audio_ace_step_1_5_checkpoint&utm_source=docs">
    直接在 Comfy Cloud 上运行 AIO 工作流。
  </Card>

  <Card title="下载工作流" icon="download" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/audio_ace_step_1_5_checkpoint.json">
    下载一体化 checkpoint 工作流用于本地使用。
  </Card>
</CardGroup>

### AIO 模型下载

<CardGroup cols={1}>
  <Card title="ace_step_1.5_turbo_aio.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/checkpoints/ace_step_1.5_turbo_aio.safetensors">
    一体化 checkpoint 文件（推荐大多数用户使用）。
  </Card>
</CardGroup>

**AIO 模型存储位置**

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 checkpoints/
│       └── ace_step_1.5_turbo_aio.safetensors
```

## 选项 2：分离模型文件

分离版本允许你单独下载各个模型组件。

### 分离模型工作流

<CardGroup cols={2}>
  <Card title="在 Comfy Cloud 运行" icon="cloud" href="https://cloud.comfy.org/?template=audio_ace_step_1_5_split&utm_source=docs">
    直接在 Comfy Cloud 上运行分离模型工作流。
  </Card>

  <Card title="下载工作流" icon="download" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/audio_ace_step_1_5_split.json">
    下载分离模型工作流用于本地使用。
  </Card>
</CardGroup>

### 分离模型下载

<CardGroup cols={2}>
  <Card title="acestep_v1.5_turbo.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_turbo.safetensors">
    扩散模型。
  </Card>

  <Card title="qwen_0.6b_ace15.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors">
    文本编码器 (0.6B)。
  </Card>

  <Card title="qwen_1.7b_ace15.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_1.7b_ace15.safetensors">
    文本编码器 (1.7B)。
  </Card>

  <Card title="ace_1.5_vae.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/vae/ace_1.5_vae.safetensors">
    VAE 模型。
  </Card>
</CardGroup>

**分离模型存储位置**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── acestep_v1.5_turbo.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen_0.6b_ace15.safetensors
│   │   └── qwen_1.7b_ace15.safetensors
│   └── 📂 vae/
│       └── ace_1.5_vae.safetensors
```

## ACE-Step 1.5 在 ComfyUI 中的主要特性

### 思维链规划

ACE-Step 1.5 模型通过思维链推理综合元数据、歌词和描述来指导扩散过程，从而产生更连贯的长篇作品。

### 混合 LM + DiT 架构

ACE-Step 1.5 结合了规划歌曲结构的语言模型和处理音频合成的扩散 Transformer (DiT)，全部在 ComfyUI 中原生运行。

### 在 ComfyUI 中进行 LoRA 微调

只需几首歌曲，你就可以训练一个捕捉特定风格的 LoRA。因为你在 ComfyUI 中本地运行 ACE-Step 1.5，所以你拥有 LoRA 的所有权，不必担心数据泄露。

## 即将在 ComfyUI 中推出

这些功能在 ACE-Step 1.5 中可用，但尚未在 ComfyUI 中支持：

* **翻唱 (Cover)**：将任何歌曲作为输入，配合新的提示词和歌词，模型将以完全不同的风格重新演绎曲目
* **重绘 (Repaint)**：选择一个片段，仅重新生成该部分，模型会将其拼接回去，同时保持其他部分不变

## ACE-Step 1.5 ComfyUI 相关资源

* [项目主页](https://ace-step.github.io/)
* [Hugging Face 模型](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files)
* [GitHub 仓库](https://github.com/ace-step/ACE-Step)
* [博客文章](https://blog.comfy.org/p/ace-step-15-is-now-available-in-comfyui)
