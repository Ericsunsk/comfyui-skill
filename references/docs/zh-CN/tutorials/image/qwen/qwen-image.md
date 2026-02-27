> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen-Image ComfyUI原生工作流示例

> Qwen-Image 是一个拥有 20B 参数的 MMDiT（多模态扩散变换器）模型，基于 Apache 2.0 许可证开源。

**Qwen-Image** 是阿里巴巴通义千问团队发布的首个图像生成基础模型，这是一个拥有 20B 参数的 MMDiT（多模态扩散变换器）模型，基于 Apache 2.0 许可证开源。该模型在**复杂文本渲染**和**精确图像编辑**方面取得了显著进展，无论是英语还是中文等多种语言都能实现高保真输出。

**模型亮点**：

* **卓越的多语言文本渲染**：支持英语、中文、韩语、日语等多种语言的高精度文本生成，保持字体细节和布局一致性
* **多样化艺术风格**：从照片级真实到印象派绘画，从动漫美学到极简设计，流畅适应各种创意提示

*相关链接*\*:

* [GitHub](https://github.com/QwenLM/Qwen-Image)
* [Hugging Face](https://huggingface.co/Qwen/Qwen-Image)
* [ModelScope](https://modelscope.cn/models/qwen/Qwen-Image)

另外目前 Qwen-Image 有多种 ControlNet 支持

* [Qwen-Image-DiffSynth-ControlNets/model\_patches](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/tree/main/split_files/model_patches): 包括 canny、depth、inpaint 三个模型
* [qwen\_image\_union\_diffsynth\_lora.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/blob/main/split_files/loras/qwen_image_union_diffsynth_lora.safetensors): 图像结构控制lora 支持 canny、depth、pose、lineart、softedge、normal、openpose
* instanX ControlNet: 待更新

## ComfyOrg Qwen-Image live stream

**Qwen-Image in ComfyUI - Lightning & LoRAs**

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/WBFHwrpYRtY?si=uREGRhBDryTJBIry" title="Qwen-Image in ComfyUI - Lightning & LoRAs / August 15th, 2025" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**Qwen-Image ControlNet in ComfyUI - DiffSynth**

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/bXMClHfEFn4?si=dcaNdqOMSwvu3t8x" title="Qwen-Image ControlNet in ComfyUI - DiffSynth / August 26th, 2025" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Qwen-Image 原生工作流示例

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

<a href="https://cloud.comfy.org/?template=image_qwen_image&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#7c3aed', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginBottom: '1rem'}}>
  在 Comfy Cloud 上运行
</a>

在本篇文档所附工作流中使用的不同模型有三种

1. Qwen-Image 原版模型 fp8\_e4m3fn
2. 8步加速版： Qwen-Image 原版模型 fp8\_e4m3fn 使用 lightx2v 8步 LoRA,
3. 蒸馏版:Qwen-Image 蒸馏版模型 fp8\_e4m3fn

**显存使用参考**
GPU: RTX4090D 24GB

| 使用模型                            | VRAM Usage | 首次生成  | 第二次生成 |
| ------------------------------- | ---------- | ----- | ----- |
| fp8\_e4m3fn                     | 86%        | ≈ 94s | ≈ 71s |
| fp8\_e4m3fn 使用 lightx2v 8步 LoRA | 86%        | ≈ 55s | ≈ 34s |
| 蒸馏版 fp8\_e4m3fn                 | 86%        | ≈ 69s | ≈ 36s |

### 1. 工作流文件

更新 ComfyUI 后你可以从模板中找到工作流文件，或者将下面的工作流拖入 ComfyUI 中加载
![Qwen-image 文生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/qwen/qwen-image.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载原始版 JSON 格式工作流</p>
</a>

蒸馏版

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/qwen/image_qwen_image_distill.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载蒸馏版JSON 格式工作流</p>
</a>

### 2. 模型下载

**你可以在 ComfyOrg 仓库找到的版本**

* Qwen-Image\_bf16 (40.9 GB)
* Qwen-Image\_fp8 (20.4 GB)
* 蒸馏版本 (非官方，仅需 15 步)

所有模型均可在 [Huggingface](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main) 或者 [魔搭](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI/files) 找到

**Diffusion model**

* [qwen\_image\_fp8\_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors)

Qwen\_image\_distill

* [qwen\_image\_distill\_full\_fp8\_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/non_official/diffusion_models/qwen_image_distill_full_fp8_e4m3fn.safetensors)
* [qwen\_image\_distill\_full\_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/non_official/diffusion_models/qwen_image_distill_full_bf16.safetensors)

<Note>
  - 蒸馏版本原始作者建议在 15 步 cfg 1.0
  - 经测试该蒸馏版本在 10 步 cfg 1.0 下表现良好，根据你想要的图像类型选择 euler 或 res\_multistep
</Note>

**LoRA**

* [Qwen-Image-Lightning-8steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-8steps-V1.0.safetensors)

**Text encoder**

* [qwen\_2.5\_vl\_7b\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**VAE**

* [qwen\_image\_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors)

模型保存位置

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── qwen_image_fp8_e4m3fn.safetensors
│   │   └── qwen_image_distill_full_fp8_e4m3fn.safetensors ## 蒸馏版
│   ├── 📂 loras/
│   │   └── Qwen-Image-Lightning-8steps-V1.0.safetensors   ## 8步加速 LoRA 模型
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

### 3. 工作流使用说明

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=123e11f9be1c31a9e3a3c0ff1df299da" alt="步骤图" data-og-width="3111" width="3111" data-og-height="1829" height="1829" data-path="images/tutorial/image/qwen/image_qwen_image-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fd031c2e037ec5ada7bfc72d5dab4f32 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=890775205ed1e33ad3de3e01136e1c73 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ffb8a3d81da16b3c663cc7d6ca3a1e86 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=807ca8d050cb51f8f4b5057a00d6ad41 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2938f2fc67819563457a78ebea810aae 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2b234cc0550c4157b194d76f8e1066ee 2500w" />

1. 确保 `Load Diffusion Model`节点加载了`qwen_image_fp8_e4m3fn.safetensors`
2. 确保 `Load CLIP`节点中加载了`qwen_2.5_vl_7b_fp8_scaled.safetensors`
3. 确保 `Load VAE`节点中加载了`qwen_image_vae.safetensors`
4. 确保 `EmptySD3LatentImage`节点中设置好了图片的尺寸
5. 在`CLIP Text Encoder`节点中设置好提示词，目前经过测试目前至少支持：英语、中文、韩语、日语、意大利语等
6. 如果需要启用 lightx2v 的 8 步加速 LoRA ，请选中后用 `Ctrl + B` 启用该节点，并按 序号`8` 处的设置参数修改 Ksampler 的设置设置
7. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流
8. 对于不同版本的模型和工作流的对应 KSampler 的参数设置

<Note>
  蒸馏版模型和 lightx2v 的 8 步加速 LoRA 似乎并不兼容，你可以测试具体的组合参数来验证组合使用的方式是否可行
</Note>

## Qwen Image InstantX ControlNet 工作流

这是一个 ControlNet 模型

<a href="https://cloud.comfy.org/?template=image_qwen_image_instantx_controlnet&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#7c3aed', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginBottom: '1rem'}}>
  在 Comfy Cloud 上运行
</a>

### 1. 工作流及输入图片

下载下面的图片并拖入 ComfyUI 以加载工作流
![workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-instantx-controlnet/image_qwen_image_instantx_controlnet.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_instantx_controlnet.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

下载下面的图片作为输入
![input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-instantx-controlnet/input.jpg)

### 2. 模型链接

1. InstantX Controlnet

下载 [Qwen-Image-InstantX-ControlNet-Union.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-InstantX-ControlNets/resolve/main/split_files/controlnet/Qwen-Image-InstantX-ControlNet-Union.safetensors) 并保存到 `ComfyUI/models/controlnet/` 文件夹下

2. **Lotus Depth model**

<Note>
  你也可以使用类似 [comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) 等自定义节点来完成各种类型图像的预处理
</Note>

**Lotus Depth 模型**

我们将使用这个模型来生成图像的深度图，它需要安装以下两个模型：

**Diffusion Model**

* [lotus-depth-d-v1-1.safetensors](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors)

**VAE Model**

* [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors)  或者任意的 SD1.5 的 VAE 都可以使用

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── lotus-depth-d-v1-1.safetensors
│   └── vae/
│       └──  lvae-ft-mse-840000-ema-pruned.safetensors
```

### 3. 工作流说明

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a73a3f375691a80eb87a6cec12c48ad9" alt="流程说明" data-og-width="3800" width="3800" data-og-height="1730" height="1730" data-path="images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d1c3841692bb9868512816925f74ba85 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4633d161d5b014a83c5cf2deec05ea2f 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fbd0674ae9fd596c5975e6c02d235136 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=dae55f9d59a7d33e3bf20ca9a032aabf 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=56b395e407793ea121f6f1497c45316a 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b6eceab00f771c33de88f74f8e498d19 2500w" />

1. 确保 `Load ControlNet Model` 节点正确加载了 `Qwen-Image-InstantX-ControlNet-Union.safetensors`  模型
2. 上传输入图像
3. 这里是一个子图，这里是 ComfyUI 支持的 lotus Depth 模型，你可以在模板中找到 Lotus Depth 或者编辑对应子图了解对应工作流，请确保所有模型都正确加载
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

## Qwen Image ControlNet DiffSynth-ControlNets Model Patches 工作流

<a href="https://cloud.comfy.org/?template=image_qwen_image_controlnet_patch&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#7c3aed', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginBottom: '1rem'}}>
  在 Comfy Cloud 上运行
</a>

这个模型实际上并不是一个 controlnet，而是一个 Model patch， 支持 canny、depth、inpaint 三种不同的控制模式

原始模型地址：[DiffSynth-Studio/Qwen-Image ControlNet](https://www.modelscope.cn/collections/Qwen-Image-ControlNet-6157b44e89d444)
Comfy Org rehost 地址： [Qwen-Image-DiffSynth-ControlNets/model\_patches](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/tree/main/split_files/model_patches)

### 1. 工作流及输入图片

下载下面的图片拖入 ComfyUI 中以加载对应的工作流
![workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-controlnet-model-patch/image_qwen_image_controlnet_patch.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_controlnet_patch.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

下载下面的图片作为输入图片：

![input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-controlnet-model-patch/input.png)

### 2. 模型链接

其它模型与 Qwen-Image 基础工作流一致，你只需下载下面的模型并保存到 `ComfyUI/models/model_patches` 文件夹中

* [qwen\_image\_canny\_diffsynth\_controlnet.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_canny_diffsynth_controlnet.safetensors)
* [qwen\_image\_depth\_diffsynth\_controlnet.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_depth_diffsynth_controlnet.safetensors)
* [qwen\_image\_inpaint\_diffsynth\_controlnet.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_inpaint_diffsynth_controlnet.safetensors)

### 3. 工作流使用说明

目前 diffsynth 有三个 patch 的模型： Canny、Detph、Inpaint 三个模型

如果你是第一次使用 ControlNet 相关的工作流，你需要了解的是，用于控制的图片需要预处理成受支持的图像才可以被模型使用和识别

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3459806aaf59d27e2e1554c4bd2d0de7" alt="输入类型示意" data-og-width="5920" width="5920" data-og-height="2438" height="2438" data-path="images/tutorial/image/qwen/controlnet_input_types.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=98a48facb7eecc0ecf0cb783d620a17c 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=dc05aface8427790488a1db20060354f 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fd4d165a1edd3ce9459f5210155c37b5 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3dc34a088c42b62b73cf344071944115 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ec72ea0b9fa642056de6f6700df2bbf9 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f3a9a233cc4c513b7818b9463fae0ac4 2500w" />

* Canny: 处理后的 canny ， 线稿轮廓
* Detph: 预处理后的深度图，体现空间关系
* Inpaint: 需要用 Mask 标记需要重绘的部分

由于这个 patch 模型分为了三个不同的模型，所以你需要在输入时选择正确的预处理类型来保证图像的正确预处理

**Canny 模型 ControlNet 使用说明**

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ca49f6ba72d3897cb14614314bc0d3c8" alt="Canny 工作流" data-og-width="3800" width="3800" data-og-height="2046" height="2046" data-path="images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1dd6c853b2c2b9cc69877f3f3088a583 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b25f3d2ecff52c8a63ee0b671200b38e 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3a09344131390ad832d0948cac2f5d32 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=48aedbe0e779c62f482183934754ba33 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=bc723145ccca9fa5f4b766d49da10ae8 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6f5f3196d120979c783e841fb2deb82f 2500w" />

1. 确保对应 `qwen_image_canny_diffsynth_controlnet.safetensors` 已被加载
2. 上传输入图片，用于后续处理
3. Canny 节点是原生的预处理节点，它将按照你设置的参数，将输入图像进行预处理，控制生成
4. 如果需要可以修改 `QwenImageDiffsynthControlnet` 节点的 `strength` 强度来控制线稿控制的强度
5. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

> 对于 qwen\_image\_depth\_diffsynth\_controlnet.safetensors 使用，需要将图像预处理成 detph 深度图，替换掉 `image proccessing` 图，对于这部分的使用，请参考本篇文档中 InstantX 的处理方法，其它部分与 Canny 模型的使用类似

**Inpaint 模型 ControlNet 使用说明**
<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c3a3493ab00a11eba1e634624b40a2c1" alt="Inpaint 工作流" data-og-width="3808" width="3808" data-og-height="2046" height="2046" data-path="images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2cd61275d4f008dd88c8f80d79e8abc4 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=85f2dcdc8fce631cc8977a168af9f580 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7d330a90db88bf316006c5f17dba19f0 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=74930608b678ed937bf707bb02341fd6 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3c3e6b0170c96a481cb1a969bc891f4b 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7ec9aeca94135ef2945033492dfbad82 2500w" />

对于 Inpaint 模型，它需要使用 [蒙版编辑器](/zh-CN/interface/maskeditor)，来绘制一个蒙版然后作为输入控制条件

1. 确保 `ModelPatchLoader` 加载的是 `qwen_image_inpaint_diffsynth_controlnet.safetensors` 模型
2. 上传图片，并使用[蒙版编辑器](/zh-CN/interface/maskeditor) 绘制蒙版，你需要将对应 `Load Image`节点的 `mask` 输出连接到 `QwenImageDiffsynthControlnet` 的 `mask` 输入才能保证对应的蒙版被加载
3. 使用 `Ctrl-B` 快捷键，将原本工作流中的 Canny 设置为绕过模式，来使得对应的 Canny 节点处理不生效
4. 在 `CLIP Text Encoder`  输入你需要将蒙版部分修改成样式
5. 如需要可以修改 `QwenImageDiffsynthControlnet` 节点的 `strength` 强度来控制对应的控制强度
6. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

## Qwen Image union ControlNet LoRA 工作流

<a href="https://cloud.comfy.org/?template=image_qwen_image_union_control_lora&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#7c3aed', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginBottom: '1rem'}}>
  在 Comfy Cloud 上运行
</a>

原始模型地址：[DiffSynth-Studio/Qwen-Image-In-Context-Control-Union](https://www.modelscope.cn/models/DiffSynth-Studio/Qwen-Image-In-Context-Control-Union/)
Comfy Org reshot 地址: [qwen\_image\_union\_diffsynth\_lora.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/blob/main/split_files/loras/qwen_image_union_diffsynth_lora.safetensors): 图像结构控制lora 支持 canny、depth、post、lineart、softedge、normal、openpose

### 1. 工作流及输入图片

下载下面的图片并拖入 ComfyUI 以加载工作流
![workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-union-control-lora/image_qwen_image_union_control_lora.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_union_control_lora.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

下载下面的图片作为输入图片

![workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-union-control-lora/input.png)

### 2. 模型链接

下载下面的模型，由于这是一个 LoRA 模型，所以需要保存到 `ComfyUI/models/loras/` 文件夹下

* [qwen\_image\_union\_diffsynth\_lora.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/blob/main/split_files/loras/qwen_image_union_diffsynth_lora.safetensors): 图像结构控制lora 支持 canny、depth、post、lineart、softedge、normal、openpose

### 3. 工作流说明

这个模型是一个统一的控制 LoRA, 支持  canny、depth、pose、lineart、softedge、normal、openpose 等控制, 由于许多的图像预处理原生节点并未完全支持，所以你应该需要类似 [comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) 来完成其它图像的预处理

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=428cafa03e7759a771c9f1e63d759dd0" alt="Union Control LoRA" data-og-width="3800" width="3800" data-og-height="2238" height="2238" data-path="images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e964f8cad5f3b943f677dc4c7d5ef992 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=8ed100d1fc4a43f99736ced29d2d51e3 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5316d6291981443405e65adb048b2f6f 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=58bd2cda362ebf0909786bb5cdb6f7ac 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7e1152f424d5746e13ffeb149b3336ee 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c212ec01f142df185da8ce853571b99f 2500w" />

1. 确保 `LoraLoaderModelOnly` 正确加载了 `qwen_image_union_diffsynth_lora.safetensors`  模型
2. 上传输入图像
3. 如需要你可以调整 `Canny` 节点的参数，由于不同的输入图像需要不同的参数设置来获得更好的图像预处理结果，你可以尝试调整对应的参数值来获得更多/更少细节
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

> 其它类型的类型的控制，也是需要将图像处理的部分替换
