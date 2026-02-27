> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux.1 Krea Dev ComfyUI 工作流教程

> Black Forest Labs 与 Krea 合作开发的最佳开源 FLUX 模型，专注于独特美学风格和自然细节，避免 AI 感，提供卓越的真实感和图像质量。

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=79640b1911971da78cf2bedb7b3b75ca" alt="Flux.1 Krea Dev 海报" data-og-width="1080" width="1080" data-og-height="1080" height="1080" data-path="images/tutorial/flux/flux_1_krea_dev_poster.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=390f151f239fedcd7a2e146ca35f51da 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f1a852ee1703607ed39688d813bf3e9b 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=308ab9d5ef0e1f83061eb5d74e531671 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b3cbd4470da7891978a4b8f5439c14ef 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ff33d86c5935c09641c4b708e80c5310 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=4554765c9af26d7e9eb85ed813ab3f57 2500w" />

[Flux.1 Krea Dev](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev) 是由 Black Forest Labs (BFL) 与 Krea 合作开发的先进文本生成图像模型。这是目前最好的开源权重 FLUX 模型，专为文本到图像生成而设计。

**模型特点**

* **独特美学风格**: 专注于生成具有独特美学的图像，避免常见的"AI感"外观
* **自然细节**: 不会产生过曝的高光，保持自然的细节表现
* **卓越的真实感**: 提供出色的真实感和图像质量
* **完全兼容架构**: 与 FLUX.1 \[dev] 完全兼容的架构设计

**模型许可**
该模型采用 [flux-1-dev-non-commercial-license](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/blob/main/LICENSE.md) 许可发布

## Flux.1 Krea Dev ComfyUI 工作流

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

#### 1. 工作流文件

下载下面的图片或JSON，并拖入 ComfyUI 以加载对应工作流
![Flux Krea Dev 工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/krea/flux1_krea_dev.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/flux1_krea_dev.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux1_krea_dev&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>在 Comfy Cloud 上运行</p>
</a>

#### 2. 模型链接

**Diffusion model** 下面两个模型选择其中一个版本即可

* [flux1-krea-dev\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/FLUX.1-Krea-dev_ComfyUI/blob/main/split_files/diffusion_models/flux1-krea-dev_fp8_scaled.safetensors)

下面这个版本是原始权重，如果你追求更高质量有足够的显存，可以尝试这个版本

* [flux1-krea-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/resolve/main/flux1-krea-dev.safetensors)

<Note>
  - `flux1-dev.safetensors` 文件需要同意 [black-forest-labs/FLUX.1-Krea-dev](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/) 的协议后才能使用浏览器进行下载。
</Note>

如果你使用过 Flux 相关的工作流，下面的模型是相同的，不需要重复下载

**Text encoders**

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) 当你的显存大于 32GB 时推荐使用。
* [t5xxl\_fp8\_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors)  For Low VRAM

**VAE**

* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)

文件保存位置：

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └── flux1-krea-dev_fp8_scaled.safetensors 或 flux1-krea-dev.safetensors
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── t5xxl_fp16.safetensors 或 t5xxl_fp8_e4m3fn.safetensors
│   ├── vae/
│   │   └── ae.safetensors

```

#### 3. 按步骤检查确保工作流可以正常运行

<Tip>
  对于低显存用户， 这个模型可能无法在你的设备上顺利运行，你可以等待社区提供 FP8 或 GGUF 版本
</Tip>

请参照下面的图片，确保各个模型文件都已经加载完成

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8475817d518de939bb6c5aabf8c1770e" alt="ComfyUI Flux Krea Dev工作流" data-og-width="2814" width="2814" data-og-height="1612" height="1612" data-path="images/tutorial/flux/flux_1_krea_dev_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f1cd1077597c59efb7e11a44f9219456 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ea811a58031f7fcd99426c1c0b947a30 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=69fffd2a3c686f40d6566e2a70cb4595 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f7b6f4b5fc50d7b92ea8155e2b8949a8 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7c17e7b576636ce9a86483cc6bcf70e7 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f198e11cc581093f11e1ff1ce37e2d11 2500w" />

1. 确保在`Load Diffusion Model`节点加载了`flux1-krea-dev_fp8_scaled.safetensors` 或 `flux1-krea-dev.safetensors`
   * `flux1-krea-dev_fp8_scaled.safetensors` 推荐低显存用户使用
   * `flux1-krea-dev.safetensors` 如果你有足够的显存如 24GB， 你可以尝试这个版本以追求更好的质量
2. 确保在`DualCLIPLoader`节点中下面的模型已加载：
   * clip\_name1: t5xxl\_fp16.safetensors 或 t5xxl\_fp8\_e4m3fn.safetensors
   * clip\_name2: clip\_l.safetensors
3. 确保在`Load VAE`节点中加载了`ae.safetensors`
4. 确保
5. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流
