> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Depth ControlNet 使用示例

> 本篇将引导了解基础的 Depth ControlNet 概念，并在 ComfyUI 中完成对应的图像生成

## 深度图与 Depth ControlNet 介绍

深度图(Depth Map)是一种特殊的图像，它通过灰度值表示场景中各个物体与观察者或相机的距离。在深度图中，灰度值与距离成反比：​越亮的区域（接近白色）表示距离越近，​越暗的区域（接近黑色）表示距离越远。

![Depth 图像](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth_input.png)

Depth ControlNet 是专门训练用于理解和利用深度图信息的 ControlNet 模型。它能够帮助 AI 正确解读空间关系，使生成的图像符合深度图指定的空间结构，从而实现对三维空间布局的精确控制。

### 深度图结合 ControlNet 应用场景

深度图在多种场景中都有比较多的应用：

1. **人像场景**：控制人物与背景的空间关系，避免面部等关键部位畸变
2. **风景场景**：控制近景、中景、远景的层次关系
3. **建筑场景**：控制建筑物的空间结构和透视关系
4. **产品展示**：控制产品与背景的分离度和空间位置

本篇示例中，我们将使用深度图生成建筑可视化的场景生成。

## ComfyUI ControlNet 工作流示例讲解

### 1. ControlNet 工作流素材

请下载下面的工作流图片,并拖入 ComfyUI 以加载工作流

![Depth 工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth_controlnet.png)

<Tip>
  Metadata 中包含工作流 json 的图片可直接拖入 ComfyUI 或使用菜单 `Workflows` -> `Open（ctrl+o）` 来加载对应的工作流。
  该图片已包含对应模型的下载链接，直接拖入 ComfyUI 将会自动提示下载。
</Tip>

请下载下面的图片，我们将会将它作为输入。

![Depth 图像](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth_input.png)

### 2. 模型安装

<Note>
  如果你网络无法顺利完成对应模型的自动下载，请尝试手动下载下面的模型，并放置到指定目录中
</Note>

* [architecturerealmix\_v11.safetensors](https://civitai.com/api/download/models/431755?type=Model\&format=SafeTensor\&size=full\&fp=fp16)
* [control\_v11f1p\_sd15\_depth\_fp16.safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors?download=true)

```
ComfyUI/
├── models/
│   ├── checkpoints/
│   │   └── architecturerealmix_v11.safetensors
│   └── controlnet/
│       └── control_v11f1p_sd15_depth_fp16.safetensors
```

### 3. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_depth.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7bcb7a518e96e88c6ccb73c1a7eb7087" alt="ComfyUI 工作流 - Depth ControlNet 流程图" data-og-width="2000" width="2000" data-og-height="1080" height="1080" data-path="images/tutorial/controlnet/flow_diagram_depth.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_depth.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=06ebada589ba06f3099c330e8bf59d73 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_depth.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d954e861f557cd6e16512265bfb9ffe5 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_depth.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2d91e0e82d1aae7bd1a9983ca349bf0e 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_depth.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c44b0150592455946dcfa90643a519b6 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_depth.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f7856a9bd50851e5881421ecab512941 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_depth.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=83a078d5ea4ff21e0d17a77c6921a8c6 2500w" />

1. 确保`Load Checkpoint`可以加载 **architecturerealmix\_v11.safetensors**
2. 确保`Load ControlNet`可以加载 **control\_v11f1p\_sd15\_depth\_fp16.safetensors**
3. 在`Load Image`中点击`Upload` 上传之前提供的 Depth 图像
4. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成

## 混合深度控制与其他技术

根据不同创作需求，可以将深度图 ControlNet 与其它类型的 ControlNet 混合使用来达到更好的效果：

1. **Depth + Lineart**：保持空间关系的同时强化轮廓，适用于建筑、产品、角色设计
2. **Depth + Pose**：控制人物姿态的同时维持正确的空间关系，适用于人物场景

关于多个 ControlNet 混合使用，可以参考 [混合 ControlNet](/zh-CN/tutorials/controlnet/mixing-controlnets) 示例。
