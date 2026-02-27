> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Flux.1 ControlNet 示例

> 本文将使用 Flux.1 ControlNet 来完成 ControlNet 的工作流示例。

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9796a0a85863c068c836ff7351b21729" alt="Flux.1 Canny Controlnet" data-og-width="1600" width="1600" data-og-height="434" height="434" data-path="images/tutorial/flux/flux-1-canny-controlnet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c8a38bf940731ef4f191acfbc4e7331d 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=57197282f571d9d7fbe9da9afac18d91 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f0e887ea60fdcab432c04e9b9b8cd8be 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9a2e438661c73dba661598d8c85993fa 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7718559f1774a5378b2cce821a00e5db 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=232c092e87b8022fe2e34d113796c18e 2500w" />
<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=34c23b4e92011bb86fe97bc966441d80" alt="Flux.1 Depth Controlnet" data-og-width="1600" width="1600" data-og-height="285" height="285" data-path="images/tutorial/flux/flux-1-depth-controlnet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=65ff60ff81d6db718aaa5d0990150a0f 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5df60b44abf1779409b2531f58c372d7 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=af9afb5910abd39fcdd9fb3a96c728a6 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=471f82a699282e9f0d1ea5e1a5ed8bb1 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8b0b4a5361b74724b97d8984fc34abb6 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=70accae2c7aaa0600b3d99827bd2b634 2500w" />

## FLUX.1 ControlNet 模型介绍

FLUX.1 Canny 和 Depth 是由 [Black Forest Labs](https://blackforestlabs.ai/) 推出的 ​[FLUX.1 Tools 套件](https://blackforestlabs.ai/flux-1-tools/) 中的两个强大模型。这套工具旨在为 FLUX.1 添加控制和引导能力，使用户能够修改和重新创建真实或生成的图像。

**FLUX.1-Depth-dev** 和 **FLUX.1-Canny-dev** 都是 12B 参数的 Rectified Flow Transformer 模型，能够基于文本描述生成图像，同时保持与输入图像的一致性。其中 Depth 版本通过深度图提取技术来维持源图像的空间结构，而 Canny 版本则利用边缘检测技术来保持源图像的结构特征，使得用户可以根据不同需求选择合适的控制方式。

这两个模型都具有以下特点：

* 顶级的输出质量和细节表现
* 出色的提示遵循能力，同时保持源图像的结构布局
* 使用引导蒸馏技术训练，提高效率
* 开放权重供社区研究使用
* 提供 API 接口（pro 版）和开源权重（dev 版）

此外，Black Forest Labs 还提供了从完整模型中提取的 **FLUX.1-Depth-dev-lora** 和 **FLUX.1-Canny-dev-lora** 适配器版本，它们可以应用于 FLUX.1 \[dev] 基础模型，以较小的文件体积提供类似的功能，特别适合资源受限的环境。

本文将以分别以完整版本的 **FLUX.1-Canny-dev** 和  **FLUX.1-Depth-dev-lora** 为例，完成ComfyUI 中 Flux  ControlNet 的工作流示例。

<Tip>
  Metadata 中包含工作流 json 的图片可直接拖入 ComfyUI 或使用菜单 `Workflows` -> `Open（ctrl+o）` 来加载对应的工作流。
  本篇示例中的图片包含对应模型的下载链接，直接拖入 ComfyUI 将会自动提示下载。

  对于图像预处理器，你可以使用以下自定义节点来完成图像的预处理，在本示例中，我们将提供处理过的图片作为输入。

  * [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
  * [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
</Tip>

## FLUX.1-Canny-dev 完整版工作流

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_canny_model_example&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

### 1. 工作流及相关素材

请下载下面的工作流图片,并拖入 ComfyUI 以加载工作流

![ComfyUI 工作流 - ControlNet](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/controlnet/flux-1-canny-dev.png)

请下载下面的图片，我们将使用它来作为输入图片

![ComfyUI Flux.1 Canny Controlnet input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/controlnet/flux-1-canny-dev-input.png)

### 2. 手动模型下载

<Note>
  如果你之前使用过[完整版本的 Flux 相关工作流](/zh-CN/tutorials/flux/flux-1-text-to-image)，那么你仅需要下载 **flux1-canny-dev.safetensors** 这个模型文件。
  由于你需要先同意 [black-forest-labs/FLUX.1-Canny-dev](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev) 的协议，所以请访问 [black-forest-labs/FLUX.1-Canny-dev](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev) 页面，确保你参照下图同意了对应的协议。
  <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=64b9b0d0d2b8dd332dc1184dde9689be" alt="Flux Agreement" data-og-width="2000" width="2000" data-og-height="1091" height="1091" data-path="images/tutorial/flux/flux1_canny_dev_agreement.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c3aacab6b791cf60520a0b4be1ee988b 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=72cde7f0cde89233c51a28598dcf996c 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8d31cbd9704522774e3363a4174f1c50 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=37052cd503baba8bda5a10f153ad0710 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=656f8dcc4afab76118ed6ed3e7e253cf 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=96568aa34dc2455b23148d6796b480c5 2500w" />
</Note>

完整模型列表：

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true)
* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)
* [flux1-canny-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev/resolve/main/flux1-canny-dev.safetensors?download=true) （请确保你已经同意了对应 repo 的协议）

文件保存位置：

```
ComfyUI/
├── models/
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── t5xxl_fp16.safetensors
│   ├── vae/
│   │   └── ae.safetensors
│   └── diffusion_models/
│       └── flux1-canny-dev.safetensors
```

### 3. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9dfe7fc30106a96d837a93cb27958e42" alt="ComfyUI Flux.1 Canny Controlnet 步骤流程" data-og-width="4000" width="4000" data-og-height="1736" height="1736" data-path="images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=751235f8031159be58c382a114dc43f3 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=1946bcd3dec56bbf062cedb8bcbd8b97 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=bca1ef585a0acbc78fc4d51140ec10b1 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0f4cbe67dcf79a8af597b3d5f8becacd 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a9f35eb1702f847f6b6300918be03393 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=52c23b72214d6382f24f54c603962406 2500w" />

1. 确保在`Load VAE`中加载了`ae.safetensors`
2. 确保在`Load Diffusion Model`加载了`flux1-canny-dev.safetensors`
3. 确保在`DualCLIPLoader`中下面的模型已加载：
   * clip\_name1: t5xxl\_fp16.safetensors
   * clip\_name2: clip\_l.safetensors
4. 在`Load Image`节点中上传了文档中提供的输入图片
5. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

### 4. 开始你的尝试

尝试使用[FLUX.1-Depth-dev](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev) 模型完成 Depth 版本的工作流

你可以使用下面的图片作为输入
![ComfyUI 室内深度图](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth-t2i-adapter_input.png)

或者借助下面自定义节点中完成图像预处理:

* [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
* [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

## FLUX.1-Depth-dev-lora 工作流

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_depth_lora_example&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

LoRA 版本的工作流是在完整版本的基础上，添加了 LoRA 模型,相对于[完整版本的 Flux 工作流](/zh-CN/tutorials/flux/flux-1-text-to-image),增加了对应 LoRA 模型的加载使用节点。

### 1. 工作流及相关素材

请下载下面的工作流图片,并拖入 ComfyUI 以加载工作流

![ComfyUI 工作流 - ControlNet](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/controlnet/flux-1-depth-dev-lora.png)

请下载下面的图片，我们将使用它来作为输入图片

![ComfyUI Flux.1 Depth Controlnet input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/controlnet/flux-1-depth-dev-lora-input.png)

### 2. 手动模型下载

<Tip>
  如果你之前使用过[完整版本的 Flux 相关工作流](/zh-CN/tutorials/flux/flux-1-text-to-image)，那么你仅需要下载 **flux1-depth-dev-lora.safetensors** 这个模型文件。
</Tip>

完整模型列表：

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true)
* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)
* [flux1-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors?download=true)
* [flux1-depth-dev-lora.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev-lora/resolve/main/flux1-depth-dev-lora.safetensors?download=true)

文件保存位置：

```
ComfyUI/
├── models/
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── t5xxl_fp16.safetensors
│   ├── vae/
│   │   └── ae.safetensors
│   ├── diffusion_models/
│   │   └── flux1-dev.safetensors
│   └── loras/
│       └── flux1-depth-dev-lora.safetensors
```

### 3. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ea682a93040eac4c930e05a66e08dd7f" alt="ComfyUI Flux.1 Depth Controlnet 步骤流程" data-og-width="4000" width="4000" data-og-height="1703" height="1703" data-path="images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=19eb4f1db7a87249bac15f18632c01c7 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9f8739c81b7752be484a37383bad0027 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fbe919a88bd28aa323efdad92ece7161 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b0b2d96d4c2bbea7738e5d4a7c377324 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e888396047285644984cc46db06f5922 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=16ae6afd59005c12beb9612a542a4f01 2500w" />

1. 确保在`Load Diffusion Model`加载了`flux1-dev.safetensors`
2. 确保在`LoraLoaderModelOnly`中加载了`flux1-depth-dev-lora.safetensors`
3. 确保在`DualCLIPLoader`中下面的模型已加载：
   * clip\_name1: t5xxl\_fp16.safetensors
   * clip\_name2: clip\_l.safetensors
4. 在`Load Image`节点中上传了文档中提供的输入图片
5. 确保在`Load VAE`中加载了`ae.safetensors`
6. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

### 4. 开始你的尝试

尝试使用[FLUX.1-Canny-dev-lora](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev-lora) 模型完成 Canny 版本的工作流

借助 [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet) 或者 [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux) 完成图像预处理

## 社区版本 Flux Controlnets

XLab 和 InstantX + Shakker Labs 已经为 Flux 发布了 Controlnet。

**InstantX:**

* [FLUX.1-dev-Controlnet-Canny](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Canny/blob/main/diffusion_pytorch_model.safetensors)
* [FLUX.1-dev-ControlNet-Depth](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Depth/blob/main/diffusion_pytorch_model.safetensors)
* [FLUX.1-dev-ControlNet-Union-Pro](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/blob/main/diffusion_pytorch_model.safetensors)

**XLab**: [flux-controlnet-collections](https://huggingface.co/XLabs-AI/flux-controlnet-collections)

将这些文件放在 `ComfyUI/models/controlnet` 目录下。

你可以访问[Flux Controlnet 示例](https://raw.githubusercontent.com/comfyanonymous/ComfyUI_examples/refs/heads/master/flux/flux_controlnet_example.png)来获取对应工作流图片，并使用[这里](https://raw.githubusercontent.com/comfyanonymous/ComfyUI_examples/refs/heads/master/flux/girl_in_field.png)的图片作为输入图片。
