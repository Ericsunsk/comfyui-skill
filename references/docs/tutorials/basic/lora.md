> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI LoRA Example

> This guide will help you understand and use a single LoRA model

**LoRA (Low-Rank Adaptation)** is an efficient technique for fine-tuning large generative models like Stable Diffusion.
It introduces trainable low-rank matrices to the pre-trained model, adjusting only a portion of parameters rather than retraining the entire model,
thus achieving optimization for specific tasks at a lower computational cost.
Compared to base models like SD1.5, LoRA models are smaller and easier to train.

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=742213e2c13c5be487ea3e9827630e5a" alt="LoRA Model vs Base Model Comparison" data-og-width="1356" width="1356" data-og-height="678" height="678" data-path="images/tutorial/basic/lora/compare.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8dd68996e3201f0cbc9c416cafe9d0e2 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=77fa89d09f71e667183c193fedb36cb1 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f1cb5b3500526ccdd89e2b79617c78a8 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=36e4eeeb06a19e39a097b04ee47830a8 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1169f2af3ce625f4ab28d40c3a3c5d76 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=cbcc1878cf286e1554e2909484c4cfb7 2500w" />

The image above compares generation with the same parameters using [dreamshaper\_8](https://civitai.com/models/4384?modelVersionId=128713) directly versus using the [blindbox\_V1Mix](https://civitai.com/models/25995/blindbox) LoRA model.
As you can see, by using a LoRA model, we can generate images in different styles without adjusting the base model.

We will demonstrate how to use a LoRA model. All LoRA variants: Lycoris, loha, lokr, locon, etc... are used in the same way.

In this example, we will learn how to load and use a LoRA model in [ComfyUI](https://github.com/comfyanonymous/ComfyUI), covering the following topics:

1. Installing a LoRA model
2. Generating images using a LoRA model
3. A simple introduction to the `Load LoRA` node

## Required Model Installation

Download the [dreamshaper\_8.safetensors](https://civitai.com/api/download/models/128713?type=Model\&format=SafeTensor\&size=pruned\&fp=fp16) file and put it in your `ComfyUI/models/checkpoints` folder.

Download the [blindbox\_V1Mix.safetensors](https://civitai.com/api/download/models/32988?type=Model\&format=SafeTensor\&size=full\&fp=fp16) file and put it in your `ComfyUI/models/loras` folder.

## LoRA Workflow File

Download the image below and **drag it into ComfyUI** to load the workflow.
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/lora.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5f67dbeed58fd00da65100432c06edc7" alt="ComfyUI Workflow - LoRA" data-og-width="768" width="768" data-og-height="768" height="768" data-path="images/tutorial/basic/lora/lora.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/lora.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8bafbca505fc7df69aa336e757af2882 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/lora.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=d5a60578805b6a5e1c95e6eaf7820f2a 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/lora.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5b6afce06fbc666994656a7ca34dd096 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/lora.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=861c7ccacfcd1824c3e69eaa45c4b64c 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/lora.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7d6a66db46caf528a187be5b098abf48 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/lora.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7134404206b433d3dd4ea0c83c1de8c8 2500w" />

<Tip>
  Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.
</Tip>

## Complete the Workflow Step by Step

Follow the steps in the diagram below to ensure the workflow runs correctly.

![ComfyUI Workflow - LoRA Flow Diagram](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/lora.png)

1. Ensure `Load Checkpoint` loads `dreamshaper_8.safetensors`
2. Ensure `Load LoRA` loads `blindbox_V1Mix.safetensors`
3. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to generate the image

## Load LoRA Node Introduction

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=86dd2ba28327b5c6c182a9fb4f4404bb" alt="Load LoRA Node" data-og-width="807" width="807" data-og-height="443" height="443" data-path="images/comfy_core/loaders/load_lora.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=eb9fa4352e0ba183d5f066d31a5cbc7b 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d79c7730598eae59e4e426ba148cc305 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3d668b9ec7f28887c32a5258c69e6bce 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1663b82a24c88b4dbfc910e98d3e1705 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cdbe392bf89945708e98a6bbc1dbc7e7 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f43a1ea6e81cb1b59d7ee7694ecf6e34 2500w" />

Models in the `ComfyUI\models\loras` folder will be detected by ComfyUI and can be loaded using this node.

### Input Types

| Parameter Name   | Function                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------ |
| `model`          | Connect to the base model                                                                              |
| `clip`           | Connect to the CLIP model                                                                              |
| `lora_name`      | Select the LoRA model to load and use                                                                  |
| `strength_model` | Affects how strongly the LoRA influences the model weights; higher values make the LoRA style stronger |
| `strength_clip`  | Affects how strongly the LoRA influences the CLIP text embeddings                                      |

### Output Types

| Parameter Name | Function                                             |
| -------------- | ---------------------------------------------------- |
| `model`        | Outputs the model with LoRA adjustments applied      |
| `clip`         | Outputs the CLIP model with LoRA adjustments applied |

This node supports chain connections, allowing multiple `Load LoRA` nodes to be linked in series to apply multiple LoRA models. For more details, please refer to [ComfyUI Multiple LoRAs Example](/tutorials/basic/multiple-loras)

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=905ee3b2883bf67bd986989f57f62caf" alt="LoRA Node Chain Connection" data-og-width="1200" width="1200" data-og-height="380" height="380" data-path="images/tutorial/basic/lora/chain_link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=d58794719ae40d147a4de000c8c1c7b3 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=03d1653a50204f3708deaddb5415b072 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aa5a208389e3a0df9c0530685c6dbcb3 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=18b1343ad60feae04be40cef047226c3 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c4d1622631b43b2605038b768c6f079e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=0f9cbc8e9ac1682794e5f3ad07909a77 2500w" />

## Try It Yourself

1. Try modifying the prompt or adjusting different parameters of the `Load LoRA` node, such as `strength_model`, to observe changes in the generated images and become familiar with the `Load LoRA` node.
2. Visit [CivitAI](https://civitai.com/models) to download other kinds of LoRA models and try using them.
