> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI ControlNet 使用示例

> 本篇将引导了解基础的 ControlNet 概念，并在 ComfyUI 中完成对应的图像生成

在 AI 图像生成过程中，要精确控制图像生成并不是一键容易的事情，通常需要通过许多次的图像生成才可能生成满意的图像，但随着 **ControlNet** 的出现，这个问题得到了很好的解决。

ControlNet 是一种基于扩散模型（如 Stable Diffusion）的条件控制生成模型，最早由[Lvmin Zhang](https://lllyasviel.github.io/)与 Maneesh Agrawala 等人于 2023 年提出[Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543)

ControlNet 模型通过引入多模态输入条件（如边缘检测图、深度图、姿势关键点等），显著提升了图像生成的可控性和细节还原能力。
使得我们可以进一步开始控制图像的风格、细节、人物姿势、画面结构等等，这些限定条件让图像生成变得更加可控，在绘图过程中也可以同时使用多个 ControlNet 模型，以达到更好的效果。

在没有 ControlNet 之前，我们每次只能让模型生成图像，直到生成我们满意的图像，充满了随机性。

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=81acd50958fd1df511237b3ba90b1b06" alt="ComfyUI 随机种子生成的图片" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/controlnet/generated_with_random_seed.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ecea01007c3a2d375a0ea70846fcefa0 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7225cef825a3c4ff365c741a360ddc0a 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=1bbe42f0369bfa8d9891671b41979534 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=eee86e1fe36b8fe048e43a510e531bcf 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7d1a369b55b8fcfdd9b1b465e3346c53 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5a64bd353fbadff7b85acc589e19f8ed 2500w" />

但随着 ControlNet 的出现，我们可以通过引入额外的条件，来控制图像的生成，比如我们可以使用一张简单的涂鸦，来控制图像的生成，就可以生成差不多类似的图片。

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=36c37d9cadfaabb3690404f8828143a7" alt="ComfyUI 涂鸦控制图像生成" data-og-width="1024" width="1024" data-og-height="512" height="512" data-path="images/tutorial/controlnet/scribble_example.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c442f3baa2efb48d21d7b037ce97acf1 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a024658d6d9270ce18185ccaf6fe820b 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ab4ce66b96385a6f6c07346f39a67f4c 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9a2e79c32dfcdb73342e36682e147520 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c03cc09cfcef43cb12dd0d90d8d57026 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c8ae34966713cae3564c467f7ab5e0fe 2500w" />

在本示例中，我们将引导你完成在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中 ControlNet 模型的安装与使用, 并完成一个涂鸦控制图像生成的示例。

![ComfyUI ControlNet 工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/scribble_controlnet.png)

<Tip>
  ControlNet V1.1 其它类型的 ControlNet 模型的工作流也与都与本篇示例相同，你只需要根据需要选择对应的模型和上传对应的参考图即可。
</Tip>

## ControlNet 图片预处理相关说明

不同类型的 ControlNet 模型，通常需要使用不同类型的参考图：

![参考图](https://github.com/Fannovel16/comfyui_controlnet_aux/blob/main/examples/CNAuxBanner.jpg?raw=true)

> 图源：[ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

由于目前 **Comfy Core** 节点中，不包含所有类型的 **预处理器** 类型，但在本文档的实际示例中，我们都将提供已经经过处理后的图片，
但在实际使用过程中，你可能需要借助一些自定义节点来对图片进行预处理，以满足不同 ControlNet 模型的需求，下面是一些相关的插件

* [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
* [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

## ComfyUI ControlNet 工作流示例讲解

### 1. ControlNet 工作流素材

请下载下面的工作流图片,并拖入 ComfyUI 以加载工作流

![ComfyUI 工作流 - ControlNet](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/scribble_controlnet.png)

<Tip>
  Metadata 中包含工作流 json 的图片可直接拖入 ComfyUI 或使用菜单 `Workflows` -> `Open（ctrl+o）` 来加载对应的工作流。
  该图片已包含对应模型的下载链接，直接拖入 ComfyUI 将会自动提示下载。
</Tip>

请下载下面的图片，我们将会将它作为输入

![ComfyUI 涂鸦图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/scribble_input.png)

### 2.  手动模型安装

<Note>
  如果你网络无法顺利完成对应模型的自动下载，请尝试手动下载下面的模型，并放置到指定目录中
</Note>

* [dreamCreationVirtual3DECommerce\_v10.safetensors](https://civitai.com/api/download/models/731340?type=Model\&format=SafeTensor\&size=full\&fp=fp16)
* [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors?download=true)
* [control\_v11p\_sd15\_scribble\_fp16.safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_scribble_fp16.safetensors?download=true)

```
ComfyUI/
├── models/
│   ├── checkpoints/
│   │   └── dreamCreationVirtual3DECommerce_v10.safetensors
│   ├── vae/
│   │   └── vae-ft-mse-840000-ema-pruned.safetensors
│   └── controlnet/
│       └── control_v11p_sd15_scribble_fp16.safetensors
```

<Note>
  本示例中 vae 模型也可以使用 dreamCreationVirtual3DECommerce\_v10.safetensors 模型中的 vae 模型，这里我们遵循模型作者建议使用单独的 vae 模型。
</Note>

### 3. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d26abbfd1993f28b88efcf6231246945" alt="ComfyUI 工作流 - ControlNet 流程图" data-og-width="2000" width="2000" data-og-height="1086" height="1086" data-path="images/tutorial/controlnet/flow_diagram_scribble.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=08969e36a1eda27b8d60fb77cb41afee 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=94b8fabbcd1f910e52bf9834d3ac5678 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0e809d2f8d501e7e308408d46a6a8588 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6fea2381caed335cac0b7073ef9366e0 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2d8133f58fc8c11cacf2ed11e8c181bd 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a1c8aec6bfe0316295dcf600b09cebe2 2500w" />

1. 确保`Load Checkpoint`可以加载 **dreamCreationVirtual3DECommerce\_v10.safetensors**
2. 确保`Load VAE`可以加载 **vae-ft-mse-840000-ema-pruned.safetensors**
3. 在`Load Image`中点击`Upload` 上传之前提供的输入图片
4. 确保`Load ControlNet`可以加载 **control\_v11p\_sd15\_scribble\_fp16.safetensors**
5. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成

## 相关节点讲解

### Load ControlNet 节点讲解

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c3a99d9bd08baaedb7a4d426cc930880" alt="load controlnet" data-og-width="807" width="807" data-og-height="294" height="294" data-path="images/comfy_core/loaders/load_controlnet_model.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1d65dc81220e679eb2f17860ffe92562 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3d499a7fab5e9656b3043440bb259906 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=54654343fb221fc3ae377467f2c799a6 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e363dc10dfa46d6f2e26e94018ef47ba 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4c90104f34b30cc2e7943bc047639345 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=eaa65efbc295ed4f2bd3a8885acc02d0 2500w" />

位于`ComfyUI\models\controlnet` 的模型会被 ComfyUI 检测到，并在这个节点中识别并加载

### Apply ControlNet 节点讲解

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=de9e90df2dcfe5cc7020a8c9cdb40a65" alt="apply controlnet " data-og-width="778" width="778" data-og-height="547" height="547" data-path="images/comfy_core/conditioning/controlnet/apply_controlnet.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d2589a80afb77a1dd0d7fa12ae34142c 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=25ed3a4735b06b267519ac4313bcbaca 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=0b18dfc1c8fdd26f07a00c4d5e422f16 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=984444ad3f286a57a48cad3e9d30cb59 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=adbb7c39e09866c7c85fc9bbb59c9ebc 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c1257bb2026d9ef99421d5474e1dea23 2500w" />

这个节点接受 `load controlnet` 加载的 ControlNet 模型，并根据输入的图片，生成对应的控制条件。

**输入类型**

| 参数名称            | 作用                                                                |
| --------------- | ----------------------------------------------------------------- |
| `positive`      | 正向条件                                                              |
| `negative`      | 负向条件                                                              |
| `control_net`   | 要应用的controlNet模型                                                  |
| `image`         | 用于 controlNet 应用参考的预处理器处理图片                                       |
| `vae`           | Vae模型输入                                                           |
| `strength`      | 应用 ControlNet 的强度，越大则 ControlNet 对生成图像的影响越大                       |
| `start_percent` | 确定开始应用controlNet的百分比，比如取值0.2，意味着ControlNet的引导将在扩散过程完成20%时开始影响图像生成 |
| `end_percent`   | 确定结束应用controlNet的百分比，比如取值0.8，意味着ControlNet的引导将在扩散过程完成80%时停止影响图像生成 |

**输出类型**

| 参数名称       | 作用                        |
| ---------- | ------------------------- |
| `positive` | 应用了 ControlNet 处理后的正向条件数据 |
| `negative` | 应用了 ControlNet 处理后的负向条件数据 |

你可以使用链式链接来应用多个 ControlNet 模型，如下图所示，你也可以参考 [混合 ControlNet 模型](/zh-CN/tutorials/controlnet/mixing-controlnets) 部分的指南来了解更多关于混合 ControlNet 模型的使用
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6fc3e75414f05e6c62062b4b746dc855" alt="apply controlnet chain link" data-og-width="1500" width="1500" data-og-height="1050" height="1050" data-path="images/tutorial/controlnet/apply_controlnet_chain_link.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=da6928840e7317cf4c0cc56cddd3bef9 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=be2b48a1a8c3f852ffbc1e0e7fa06f54 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8488372f56c5d9e7a4f95574094bcd25 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3893bbb66fd156f76713a5d51623cd12 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aab42fb6856dc99be46f00bb333e8a6f 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c8dee2a84c69fc57166788cae6387f17 2500w" />

<Note>
  你也许会在有些早期的工作流中看到如下的`Apply ControlNet(Old)` 节点，这个节点是早期 ControlNet 的节点，目前已弃用状态，默认在搜索和节点列表不可见
  <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=eaf2f8df7456df845f7408495d19b9e8" alt="apply controlnet old" data-og-width="778" width="778" data-og-height="370" height="370" data-path="images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d1b70261b17b6e3b46c4ed91e1be1fd4 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9f81de62d9574bcb8b0519488cdc4195 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b0878d93dea28563986e3a1e2c77450b 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a5d3fdd9887f00d55fc68161fbed2ca6 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e34942778977bc4a0898c09123123b26 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=11a8f3eb731d988689ce245a0a327d8d 2500w" />
  如需启用，请在**设置**--> **comfy** --> **Node** 中，启用`Show deprecated nodes in search` 选项，推荐使用新节点
</Note>

## 开始你的尝试

1. 试着制作类似的涂鸦图片，甚至自己手绘，并使用 ControlNet 模型生成图像，体验 ControlNet 带来的乐趣
2. 调整 Apply ControlNet 节点的 `Control Strength` 参数，来控制 ControlNet 模型对生成图像的影响
3. 访问 [ControlNet-v1-1\_fp16\_safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/tree/main)  仓库下载其它类型的 ControlNet 模型，并尝试使用它们生成图像
