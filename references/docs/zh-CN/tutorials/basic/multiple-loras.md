> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 应用多个 LoRA 示例

> 本篇将引导你了解并完成在 ComfyUI 中同时应用多个 LoRA 模型

在 [ComfyUI LoRA 使用示例](/zh-CN/tutorials/basic/lora) 中，我们介绍了如何在 ComfyUI 中加载并使用 LoRA 模型，也提及了该节点支持链式连接。

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=905ee3b2883bf67bd986989f57f62caf" alt="LoRA 节点链式连接" data-og-width="1200" width="1200" data-og-height="380" height="380" data-path="images/tutorial/basic/lora/chain_link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=d58794719ae40d147a4de000c8c1c7b3 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=03d1653a50204f3708deaddb5415b072 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aa5a208389e3a0df9c0530685c6dbcb3 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=18b1343ad60feae04be40cef047226c3 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c4d1622631b43b2605038b768c6f079e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=0f9cbc8e9ac1682794e5f3ad07909a77 2500w" />

在本篇中我们将使用链式连接`Load LoRA`节点的方式来同时使用多个 LoRA 模型，在本示例中，我们将使用 [blindbox\_V1Mix](https://civitai.com/models/25995?modelVersionId=32988) 和 [MoXinV1](https://civitai.com/models/12597?modelVersionId=14856) 两个 LoRA 模型。

下图是这两个 LoRA 模型在同样参数下单独使用的效果

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3f26ac1b06c82aa86bf13062a1409131" alt="ComfyUI 中 LoRA 模型单独使用效果" data-og-width="1356" width="1356" data-og-height="678" height="678" data-path="images/tutorial/basic/multiple_loras/compare.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=2c29812bb695bf0ac7edf15d76a72b79 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a2486af00654f43751ef97379ed4f78b 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=eddf667237902ddb6b3d74d063c5c987 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6835d257153bca9cc73aa9ec996cbf35 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f5f9e8f718ae270ee8dbfb998156a78e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3cf3180ecee417189333079029586368 2500w" />

但通过多个 LoRA 模型链式连接后，我们可以在最终的效果中看到两种风格融合在一起的效果

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f96d5ad3564a7ce69c8acc643eab0776" alt="ComfyUI 中多 LoRA 模型应用示例结果" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/basic/multiple_loras/multiple_loras.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=536b5dd5ce9cba96ff07b37a1f33c75a 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=123cc3e5e91e6bbbae18631b7388e9c8 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6248fc473795103b532c72c06d6328a8 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b3192a7e184f81c53bdaf11dc31c15d1 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e7122d3180185bafa0f5ce0ab4941f47 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8a023ec9896266a15c4c5ed2f3f34826 2500w" />

## 相关模型安装

请下载 [dreamshaper\_8.safetensors](https://civitai.com/api/download/models/128713?type=Model\&format=SafeTensor\&size=pruned\&fp=fp16) 并保存至 `ComfyUI/models/checkpoints` 目录

请下载 [blindbox\_V1Mix.safetensors](https://civitai.com/api/download/models/32988?type=Model\&format=SafeTensor\&size=full\&fp=fp16) 并保存至 `ComfyUI/models/loras` 目录

请下载 [MoXinV1.safetensors](https://civitai.com/api/download/models/14856?type=Model\&format=SafeTensor\&size=full\&fp=fp16) 并保存至 `ComfyUI/models/loras` 目录

## 多 LoRA 模型应用示例工作流

请下载下面的工作流图片,并拖入 ComfyUI 以加载工作流
![ComfyUI 工作流 - 多 LoRA 模型应用示例](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/multiple_loras.png)

<Tip>
  Metadata 中包含工作流 json 的图片可直接拖入 ComfyUI 或使用菜单 `Workflows` -> `Open（ctrl+o）` 来加载对应的工作流。
</Tip>

## 按步骤完成工作流的运行

请参照下图步骤完成，确保工作流能够正常运行

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=daa5ef546221542dfe0b2ec8b408f689" alt="ComfyUI 工作流 - 多 LoRA 模型应用示例流程图" data-og-width="2000" width="2000" data-og-height="632" height="632" data-path="images/tutorial/basic/multiple_loras/flow_diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=966d31193e61260c54c8f14e85aa4717 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e750bd33f8db493a6bd4858655b607df 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=24074167ebd91ac8c5b596fc77a984a5 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b17f140123654a59594acda7fcbd7572 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=388e5159a3bb58a446572df3c1ecff29 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=2f8ef1fd667897efd420461df9e68c4e 2500w" />

1. 确保`Load Checkpoint`可以加载 **dreamshaper\_8.safetensors**
2. 确保`Load LoRA`可以加载 **blindbox\_V1Mix.safetensors**
3. 确保`Load LoRA`可以加载 **MoXinV1.safetensors**
4. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片的生成

## 开始你的尝试

1. 试着调整两个 `Load LoRA` 的 `strength_model` 参数，来修改不同 LoRA 模型对最终生成图片的影响
2. 访问 [CivitAI](https://civitai.com/models) 网站，下载其它风格的 LoRA 模型，组合出你满意的效果
