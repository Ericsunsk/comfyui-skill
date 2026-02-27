> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI LoRA 使用示例

> 本篇将引导了解并完成单个 LoRA 模型的使用

**LoRA 模型​（Low-Rank Adaptation）** 是一种用于微调大型生成模型（如 Stable Diffusion）的高效技术。
它通过在预训练模型的基础上引入可训练的低秩矩阵，仅调整部分参数，而非重新训练整个模型，从而以较低的计算成本实现特定任务的优化，相对于类似 SD1.5 这样的大模型，LoRA 模型更小，更容易训练。

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=742213e2c13c5be487ea3e9827630e5a" alt="LoRA 模型与基础模型对比" data-og-width="1356" width="1356" data-og-height="678" height="678" data-path="images/tutorial/basic/lora/compare.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8dd68996e3201f0cbc9c416cafe9d0e2 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=77fa89d09f71e667183c193fedb36cb1 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f1cb5b3500526ccdd89e2b79617c78a8 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=36e4eeeb06a19e39a097b04ee47830a8 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1169f2af3ce625f4ab28d40c3a3c5d76 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=cbcc1878cf286e1554e2909484c4cfb7 2500w" />

上面的图片对比了同样参数下 [dreamshaper\_8](https://civitai.com/models/4384?modelVersionId=128713) 直接生成和使用 [blindbox\_V1Mix](https://civitai.com/models/25995/blindbox) LoRA 模型生成的图片对比，我们可以看到通过使用 LoRA 模型，可以在不调整基础模型的情况下，生成更符合我们需求的图片。

我们将演示如何使用 LoRA 的示例。所有 LoRA 变体：Lycoris, loha, lokr, locon, 等... 都是以这种方式使用。

在本示例中，我们将完成以下内容来学习[ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载并使用 LoRA 模型，将涉及以下内容：

1. 安装 LoRA 模型
2. 使用 LoRA 模型生成图片
3. `Load LoRA` 节点的简单介绍

## 相关模型安装

请下载 [dreamshaper\_8.safetensors](https://civitai.com/api/download/models/128713?type=Model\&format=SafeTensor\&size=pruned\&fp=fp16) 并保存至 `ComfyUI/models/checkpoints` 目录

请下载 [blindbox\_V1Mix.safetensors](https://civitai.com/api/download/models/32988?type=Model\&format=SafeTensor\&size=full\&fp=fp16) 并保存至 `ComfyUI/models/loras` 目录

## LoRA 工作流文件

请下载下面的工作流图片,并拖入 ComfyUI 以加载工作流
![ComfyUI 工作流 - LoRA](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/lora.png)

<Tip>
  Metadata 中包含工作流 json 的图片可直接拖入 ComfyUI 或使用菜单 `Workflows` -> `Open（ctrl+o）` 来加载对应的工作流。
</Tip>

## 按步骤完成工作流的运行

请参照下图步骤，来确保对应的工作流可以正常运行

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/flow_diagram.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ace6d0baf17bc022e55de4fedc631ceb" alt="ComfyUI 工作流 - LoRA 流程图" data-og-width="2000" width="2000" data-og-height="888" height="888" data-path="images/tutorial/basic/lora/flow_diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/flow_diagram.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b588409dfcc8ad6093c7151bc9a01e49 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/flow_diagram.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4fefaf1590b02ec07da43f7360342f2a 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/flow_diagram.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=98447053bf98452e6ab04f8339a25c5f 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/flow_diagram.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=34055641f55b6cf33777611ada18a338 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/flow_diagram.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=cbf959ae05d8989327ae5e7c500a9783 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/flow_diagram.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=af9d73d163ca2e760eb53a496bbaac4b 2500w" />

1. 确保`Load Checkpoint` 加载了 `dreamshaper_8.safetensors`
2. 确保`Load LoRA` 加载了 `blindbox_V1Mix.safetensors`
3. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成

## Load LoRA 节点介绍

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=86dd2ba28327b5c6c182a9fb4f4404bb" alt="Load LoRA 节点" data-og-width="807" width="807" data-og-height="443" height="443" data-path="images/comfy_core/loaders/load_lora.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=eb9fa4352e0ba183d5f066d31a5cbc7b 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d79c7730598eae59e4e426ba148cc305 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3d668b9ec7f28887c32a5258c69e6bce 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1663b82a24c88b4dbfc910e98d3e1705 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cdbe392bf89945708e98a6bbc1dbc7e7 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f43a1ea6e81cb1b59d7ee7694ecf6e34 2500w" />

位于`ComfyUI\models\loras` 的模型会被 ComfyUI 检测到，并在这个节点中加载

### 输入类型

| 参数名称             | 作用                                        |
| ---------------- | ----------------------------------------- |
| `model`          | 连接基础模型                                    |
| `clip`           | 连接 CLIP 模型                                |
| `lora_name`      | 选择要加载使用的 LoRA 模型                          |
| `strength_model` | 影响 LoRA 对 模型权重（model）的影响程度，数值越大 LoRA 风格越强 |
| `strength_clip`  | 影响 LoRA 对 CLIP 词嵌入（clip）的影响程度             |

### 输出类型

| 参数名称    | 作用                     |
| ------- | ---------------------- |
| `model` | 输出应用了 LoRA 调整的模型       |
| `clip`  | 输出应用了 LoRA 调整的 CLIP 模型 |

该节点支持链式连接，可以将多个`Load LoRA` 节点串联来应用多个 LoRA 模型，具体请参考[ComfyUI 应用多个 LoRA 示例](/zh-CN/tutorials/basic/multiple-loras)

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=905ee3b2883bf67bd986989f57f62caf" alt="LoRA 节点链式连接" data-og-width="1200" width="1200" data-og-height="380" height="380" data-path="images/tutorial/basic/lora/chain_link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=d58794719ae40d147a4de000c8c1c7b3 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=03d1653a50204f3708deaddb5415b072 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aa5a208389e3a0df9c0530685c6dbcb3 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=18b1343ad60feae04be40cef047226c3 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c4d1622631b43b2605038b768c6f079e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=0f9cbc8e9ac1682794e5f3ad07909a77 2500w" />

## 开始你的尝试

1. 试着修改提示词，或者调整 `Load LoRA`  节点的不同参数，比如 `strength_model` ，来观察生成图片的变化，熟悉对应节点。
2. 访问 [CivitAI](https://civitai.com/models) 网站，下载其它风格的 LoRA 模型，尝试使用。
