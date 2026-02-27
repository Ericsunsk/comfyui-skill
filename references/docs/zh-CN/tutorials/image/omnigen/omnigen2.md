> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI OmniGen2 原生工作流示例

> ComfyUI OmniGen2 原生工作流示例 - 统一的文生图、图像编辑和多图像合成模型。

## 关于 OmniGen2

OmniGen2 是一个强大且高效的统一多模态生成模型，总参数量约 **7B**（3B 文本模型 + 4B 图像生成模型）。与 OmniGen v1 不同，OmniGen2 采用创新的双路径 Transformer 架构，具有完全独立的文本自回归模型和图像扩散模型，实现参数解耦和专门优化。

### 模型亮点

* **视觉理解**：继承了 Qwen-VL-2.5 基础模型强大的图像内容解释和分析能力
* **文生图生成**：从文本提示创建高保真度和美观的图像
* **指令引导的图像编辑**：执行复杂的、基于指令的图像修改，在开源模型中达到最先进的性能
* **上下文生成**：多功能的能力，可以处理和灵活结合多样化的输入（包括人物、参考对象和场景），产生新颖且连贯的视觉输出

### 技术特性

* **双路径架构**：基于 Qwen 2.5 VL（3B）文本编码器 + 独立扩散 Transformer（4B）
* **Omni-RoPE 位置编码**：支持多图像空间定位和身份区分
* **参数解耦设计**：避免文本生成对图像质量的负面影响
* 支持复杂的文本理解和图像理解
* 可控的图像生成和编辑
* 优秀的细节保持能力
* 统一架构支持多种图像生成任务
* 文字生成能力：可以在图像中生成清晰的文字内容

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

## OmniGen2 模型下载

由于本文涉及不同工作流，对应的模型文件及安装位置如下，对应工作流中也已包含了模型文件下载信息：

**Diffusion Models）**

* [omnigen2\_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/omnigen2_fp16.safetensors)

**VAE**

* [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors)

**Text Encoders）**

* [qwen\_2.5\_vl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_fp16.safetensors)

文件保存位置：

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── omnigen2_fp16.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_fp16.safetensors
```

## ComfyUI OmniGen2 文生图工作流

### 1. 工作流文件下载

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_omnigen2_t2i&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>在 Comfy Cloud 上运行</p>
</a>

![文生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/omnigen2/image_omnigen2_t2i.png)

### 2. 按步骤完成工作流运行

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0811f0f5d6dbe974749752b85fa7e3b9" alt="工作流使用步骤图" data-og-width="4148" width="4148" data-og-height="1576" height="1576" data-path="images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=45ad3f6862e902ee370dae6e6c73a6f8 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=740f03d026f930d75bee360164fc5dac 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=102c411e373d18a82c28e4862bd8c1cd 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ae539c85f4bc00c0a4b637f6e6fddf83 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2ab1b75cafc02f71855e7719baaafd9f 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0b2037bfacdd554dc19b67fa276dd876 2500w" />

请参照图片序号进行逐步确认，来保证对应工作流的顺利运行：

1. **加载主模型**：确保 `Load Diffusion Model` 节点加载了 `omnigen2_fp16.safetensors`
2. **加载文本编码器**：确保 `Load CLIP` 节点加载了 `qwen_2.5_vl_fp16.safetensors`
3. **加载 VAE**：确保 `Load VAE` 节点加载了 `ae.safetensors`
4. **设置图像尺寸**：在 `EmptySD3LatentImage` 节点设置生成图片的尺寸（推荐 1024x1024）
5. **输入提示词**：
   * 在第一个 `CLipTextEncode` 节点中输入正向提示词（想要出现在图像中的内容）
   * 在第二个 `CLipTextEncode` 节点中输入负向提示词（不想要出现在图像中的内容）
6. **开始生成**：点击 `Queue Prompt` 按钮，或使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行文生图
7. **查看结果**：生成完成后对应的图片会自动保存到 `ComfyUI/output/` 目录下，你也可以在 `SaveImage` 节点中预览

## ComfyUI OmniGen2 图片编辑工作流

OmniGen2 有丰富的图像编辑能力，并且支持为图像添加文本

### 1. 工作流文件下载

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_omnigen2_image_edit&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>在 Comfy Cloud 上运行</p>
</a>

![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/omnigen2/image_omnigen2_image_edit.png)
下载下面的图片，我们将使用它作为输入图片。
![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/omnigen2/input_fairy.png)

### 2. 按步骤完成工作流运行

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=09899794b2d041a8c0e0775da557684a" alt="工作流使用步骤图" data-og-width="4056" width="4056" data-og-height="2808" height="2808" data-path="images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6f080c727c50b8152d8b00e92447cb29 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9daf1f956e69bc958427639852c9d1f2 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=abfae5034a336d261b872d0cd18d9b8e 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5a1e3dc977d640a6c15beedcdad9991b 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9a9e59aa4a1b0ade064ad613d8428abf 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2cd7842cc0b4bb00b2416a257fffa06d 2500w" />

1. **加载主模型**：确保 `Load Diffusion Model` 节点加载了 `omnigen2_fp16.safetensors`
2. **加载文本编码器**：确保 `Load CLIP` 节点加载了 `qwen_2.5_vl_fp16.safetensors`
3. **加载 VAE**：确保 `Load VAE` 节点加载了 `ae.safetensors`
4. **上传图像**：在 `Load Image` 节点中上传提供的图片
5. **输入提示词**：
   * 在第一个 `CLipTextEncode` 节点中输入正向提示词（想要出现在图像中的内容）
   * 在第二个 `CLipTextEncode` 节点中输入负向提示词（不想要出现在图像中的内容）
6. **开始生成**：点击 `Queue Prompt` 按钮，或使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行文生图
7. **查看结果**：生成完成后对应的图片会自动保存到 `ComfyUI/output/` 目录下，你也可以在 `SaveImage` 节点中预览

### 3. 工作流补充说明

* 如果你想要启用第二张图像输入 ，你可以将工作流中状态为粉紫色的节点使用快捷键 **Ctrl + B** 来启用对应的节点输入
* 如果你想要自定义尺寸 ，可以删除链接 `EmptySD3LatentImage` 节点的 `Get image size` 节点，并输入自定义尺寸
