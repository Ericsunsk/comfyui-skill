> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI ControlNet 混合使用示例

> 我们将在本篇示例中，完成多个 ControlNet 混合使用，学会使用多个 ControlNet 模型来控制图像生成

在 AI 图像生成中，单一的控制条件往往难以满足复杂场景的需求。混合使用多个 ControlNet 可以同时控制图像的不同区域或不同方面，实现更精确的图像生成控制。

在一些场景下，混合使用 ControlNet 可以利用不同控制条件的特性，来达到更精细的条件控制：

1. **场景复杂性**：复杂场景需要多种控制条件共同作用
2. **精细控制**：通过调整每个 ControlNet 的强度参数，可以精确控制各部分的影响程度
3. **互补效果**：不同类型的 ControlNet 可以互相补充，弥补单一控制的局限性
4. **创意表达**：组合不同控制可以产生独特的创意效果

### 混合 ControlNet 的使用方法

当我们混合使用多个 ControlNet 时，每个 ControlNet 会根据其应用的区域对图像生成过程施加影响。ComfyUI 通过 `Apply ControlNet` 节点的链式连接方式，允许多个 ControlNet 条件按顺序叠加应用混合控制条件：

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6fc3e75414f05e6c62062b4b746dc855" alt="apply controlnet chain link" data-og-width="1500" width="1500" data-og-height="1050" height="1050" data-path="images/tutorial/controlnet/apply_controlnet_chain_link.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=da6928840e7317cf4c0cc56cddd3bef9 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=be2b48a1a8c3f852ffbc1e0e7fa06f54 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8488372f56c5d9e7a4f95574094bcd25 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3893bbb66fd156f76713a5d51623cd12 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aab42fb6856dc99be46f00bb333e8a6f 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c8dee2a84c69fc57166788cae6387f17 2500w" />

## ComfyUI ControlNet 区域分治混合示例

在本示例中，我们将使用 **Pose ControlNet** 和 **Scribble ControlNet** 的组合来生成一张包含多个元素的场景：左侧由 Pose ControlNet 控制的人物和右侧由 Scribble ControlNet 控制的猫咪滑板车。

### 1. ControlNet 混合使用工作流素材

请下载下面的工作流图片,并拖入 ComfyUI 以加载工作流
![ComfyUI 工作流 - Mixing ControlNet](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/mixing_controlnets.png)

<Tip>
  该工作流图片包含 Metadata 数据，可直接拖入 ComfyUI 或使用菜单 `Workflows` -> `Open（ctrl+o）` 加载。系统会自动检测并提示下载所需模型。
</Tip>

用于输入的 pose 图片（控制左侧人物姿态）:

![ComfyUI 工作流 - Mixing ControlNet 输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/mixing_controlnets_input.png)

用于输入的 scribble 图片（控制右侧猫咪和滑板车）:

![ComfyUI 工作流 - Mixing ControlNet 输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/mixing_controlnets_input_scribble.png)

### 2. 手动模型安装

<Note>
  如果你网络无法顺利完成对应模型的自动下载，请尝试手动下载下面的模型，并放置到指定目录中
</Note>

* [awpainting\_v14.safetensors](https://civitai.com/api/download/models/624939?type=Model\&format=SafeTensor\&size=full\&fp=fp16)
* [control\_v11p\_sd15\_scribble\_fp16.safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_scribble_fp16.safetensors?download=true)
* [control\_v11p\_sd15\_openpose\_fp16.safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_openpose_fp16.safetensors?download=true)
* [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors?download=true)

```
ComfyUI/
├── models/
│   ├── checkpoints/
│   │   └── awpainting_v14.safetensors
│   ├── controlnet/
│   │   └── control_v11p_sd15_scribble_fp16.safetensors
│   │   └── control_v11p_sd15_openpose_fp16.safetensors
│   ├── vae/
│   │   └── vae-ft-mse-840000-ema-pruned.safetensors
```

### 3. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b839fc78bb316a334a908ff38389a3d0" alt="ComfyUI 工作流 - Mixing ControlNet 流程图" data-og-width="1681" width="1681" data-og-height="1081" height="1081" data-path="images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=27da5acfce3ec4d1907c1ab4afe95905 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3723acd76c10d49c6901565e28b57bf9 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b5b0ec7de5bc6ae4e24f378c5fc0a4ee 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=63546a6d6c61d981bc110e2c1397ab5e 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7674c4309f93a53d6f18734790313eaa 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0e0979fa692936407c1b45930df2645d 2500w" />

按照图片中的数字标记，执行以下步骤：

1. 确保`Load Checkpoint`可以加载 **awpainting\_v14.safetensors**
2. 确保`Load VAE`可以加载 **vae-ft-mse-840000-ema-pruned.safetensors**

第一组 ControlNet 使用 Openpose 模型:
3\. 确保`Load ControlNet Model`加载 **control\_v11p\_sd15\_openpose\_fp16.safetensors**
4\. 在`Load Image`中点击`Upload` 上传之前提供的 pose 图片

第二组 ControlNet 使用 Scribble 模型:
5\. 确保`Load ControlNet Model`加载 **control\_v11p\_sd15\_scribble\_fp16.safetensors**
6\. 在`Load Image`中点击`Upload` 上传之前提供的 scribble 图片
7\. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成

## 工作流讲解

#### 强度平衡

当控制图像不同区域时，强度参数的平衡尤为重要：

* 如果一个区域的 ControlNet 强度明显高于另一个，可能导致该区域的控制效果过强而抑制另一区域
* 推荐为不同区域的 ControlNet 设置相似的强度值，例如都设为 1.0

#### 提示词技巧

在区域分治混合中，提示词需要同时包含两个区域的描述：

```
"A woman in red dress, a cat riding a scooter, detailed background, high quality"
```

这样的提示词同时涵盖了人物和猫咪滑板车，确保模型能够同时关注两个控制区域。

## 同一主体多维控制的混合应用

除了本例展示的区域分治混合外，另一种常见的混合方式是对同一主体进行多维控制。例如：

* **Pose + Depth**：控制人物姿势及空间感
* **Pose + Canny**：控制人物姿势及边缘细节
* **Pose + Reference**：控制人物姿势但参考特定风格

在这种应用中，多个 ControlNet 的参考图应该对准同一主体，并调整各自的强度确保适当平衡。

通过组合不同类型的 ControlNet 并指定其控制区域，你可以对画面元素进行精确控制。
