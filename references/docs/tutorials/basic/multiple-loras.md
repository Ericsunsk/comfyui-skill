> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Multiple LoRAs Example

> This guide demonstrates how to apply multiple LoRA models simultaneously in ComfyUI

In our [ComfyUI LoRA Example](/tutorials/basic/lora), we introduced how to load and use a single LoRA model, mentioning the node's chain connection capability.

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=905ee3b2883bf67bd986989f57f62caf" alt="LoRA Node Chaining" data-og-width="1200" width="1200" data-og-height="380" height="380" data-path="images/tutorial/basic/lora/chain_link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=d58794719ae40d147a4de000c8c1c7b3 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=03d1653a50204f3708deaddb5415b072 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aa5a208389e3a0df9c0530685c6dbcb3 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=18b1343ad60feae04be40cef047226c3 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c4d1622631b43b2605038b768c6f079e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=0f9cbc8e9ac1682794e5f3ad07909a77 2500w" />

This tutorial demonstrates chaining multiple `Load LoRA` nodes to apply two LoRA models simultaneously: [blindbox\_V1Mix](https://civitai.com/models/25995?modelVersionId=32988) and [MoXinV1](https://civitai.com/models/12597?modelVersionId=14856).

The comparison below shows individual effects of these LoRAs using identical parameters:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3f26ac1b06c82aa86bf13062a1409131" alt="Single LoRA Effects Comparison" data-og-width="1356" width="1356" data-og-height="678" height="678" data-path="images/tutorial/basic/multiple_loras/compare.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=2c29812bb695bf0ac7edf15d76a72b79 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a2486af00654f43751ef97379ed4f78b 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=eddf667237902ddb6b3d74d063c5c987 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6835d257153bca9cc73aa9ec996cbf35 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f5f9e8f718ae270ee8dbfb998156a78e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3cf3180ecee417189333079029586368 2500w" />

By chaining multiple LoRA models, we achieve a blended style in the final output:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f96d5ad3564a7ce69c8acc643eab0776" alt="Multi-LoRA Application Result" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/basic/multiple_loras/multiple_loras.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=536b5dd5ce9cba96ff07b37a1f33c75a 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=123cc3e5e91e6bbbae18631b7388e9c8 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6248fc473795103b532c72c06d6328a8 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b3192a7e184f81c53bdaf11dc31c15d1 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e7122d3180185bafa0f5ce0ab4941f47 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8a023ec9896266a15c4c5ed2f3f34826 2500w" />

## Model Installation

Download the [dreamshaper\_8.safetensors](https://civitai.com/api/download/models/128713?type=Model\&format=SafeTensor\&size=pruned\&fp=fp16) file and put it in your `ComfyUI/models/checkpoints` folder.

Download the [blindbox\_V1Mix.safetensors](https://civitai.com/api/download/models/32988?type=Model\&format=SafeTensor\&size=full\&fp=fp16) file and put it in your `ComfyUI/models/loras` folder.

Download the [MoXinV1.safetensors](https://civitai.com/api/download/models/14856?type=Model\&format=SafeTensor\&size=full\&fp=fp16) file and put it in your `ComfyUI/models/loras` folder.

## Multi-LoRA Workflow

Download the image below and **drag it into ComfyUI** to load the workflow:
![ComfyUI Workflow - Multiple LoRAs](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/multiple_loras.png)

<Tip>
  Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.
</Tip>

## Complete the Workflow Step by Step

Follow the steps in the diagram below to ensure the workflow runs correctly.

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=daa5ef546221542dfe0b2ec8b408f689" alt="Multi-LoRA Workflow Diagram" data-og-width="2000" width="2000" data-og-height="632" height="632" data-path="images/tutorial/basic/multiple_loras/flow_diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=966d31193e61260c54c8f14e85aa4717 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e750bd33f8db493a6bd4858655b607df 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=24074167ebd91ac8c5b596fc77a984a5 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b17f140123654a59594acda7fcbd7572 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=388e5159a3bb58a446572df3c1ecff29 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=2f8ef1fd667897efd420461df9e68c4e 2500w" />

1. Ensure `Load Checkpoint` loads  **dreamshaper\_8.safetensors**
2. Ensure first `Load LoRA` loads **blindbox\_V1Mix.safetensors**
3. Ensure second `Load LoRA` loads **MoXinV1.safetensors**
4. Click `Queue` or press `Ctrl/Cmd + Enter` to generate

## Try It Yourself

1. Adjust `strength_model` values in both `Load LoRA` nodes to control each LoRA's influence
2. Explore [CivitAI](https://civitai.com/models) for additional LoRAs and create custom combinations
