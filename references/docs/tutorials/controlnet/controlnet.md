> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI ControlNet Usage Example

> This guide will introduce you to the basic concepts of ControlNet and demonstrate how to generate corresponding images in ComfyUI

Achieving precise control over image creation in AI image generation cannot be done with just one click.
It typically requires numerous generation attempts to produce a satisfactory image. However, the emergence of **ControlNet** has effectively addressed this challenge.

ControlNet is a conditional control generation model based on diffusion models (such as Stable Diffusion),
first proposed by [Lvmin Zhang](https://lllyasviel.github.io/) and Maneesh Agrawala et al. in 2023 in the paper [Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543).

ControlNet models significantly enhance the controllability of image generation and the ability to reproduce details by introducing multimodal input conditions,
such as edge detection maps, depth maps, and pose keypoints.

These conditioning constraints make image generation more controllable, allowing multiple ControlNet models to be used simultaneously during the drawing process for better results.

Before ControlNet, we could only rely on the model to generate images repeatedly until we were satisfied with the results, which involved a lot of randomness.

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=81acd50958fd1df511237b3ba90b1b06" alt="Images generated with random seeds in ComfyUI" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/controlnet/generated_with_random_seed.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ecea01007c3a2d375a0ea70846fcefa0 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7225cef825a3c4ff365c741a360ddc0a 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=1bbe42f0369bfa8d9891671b41979534 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=eee86e1fe36b8fe048e43a510e531bcf 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7d1a369b55b8fcfdd9b1b465e3346c53 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/generated_with_random_seed.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5a64bd353fbadff7b85acc589e19f8ed 2500w" />

With the advent of ControlNet, we can control image generation by introducing additional conditions.
For example, we can use a simple sketch to guide the image generation process, producing images that closely align with our sketch.

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=36c37d9cadfaabb3690404f8828143a7" alt="Sketch-controlled image generation in ComfyUI" data-og-width="1024" width="1024" data-og-height="512" height="512" data-path="images/tutorial/controlnet/scribble_example.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c442f3baa2efb48d21d7b037ce97acf1 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a024658d6d9270ce18185ccaf6fe820b 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ab4ce66b96385a6f6c07346f39a67f4c 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9a2e79c32dfcdb73342e36682e147520 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c03cc09cfcef43cb12dd0d90d8d57026 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/scribble_example.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c8ae34966713cae3564c467f7ab5e0fe 2500w" />

In this example, we will guide you through installing and using ControlNet models in [ComfyUI](https://github.com/comfyanonymous/ComfyUI), and complete a sketch-controlled image generation example.

![ComfyUI ControlNet Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/scribble_controlnet.png)

<Tip>
  The workflows for other types of ControlNet V1.1 models are similar to this example. You only need to select the appropriate model and upload the corresponding reference image based on your needs.
</Tip>

## ControlNet Image Preprocessing Information

Different types of ControlNet models typically require different types of reference images:

![Reference Images](https://github.com/Fannovel16/comfyui_controlnet_aux/blob/main/examples/CNAuxBanner.jpg?raw=true)

> Image source: [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

Since the current **Comfy Core** nodes do not include all types of **preprocessors**, in the actual examples in this documentation, we will provide pre-processed images.
However, in practical use, you may need to use custom nodes to preprocess images to meet the requirements of different ControlNet models. Below are some relevant custom nodes:

* [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
* [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

## ComfyUI ControlNet Workflow Example Explanation

### 1. ControlNet Workflow Assets

Please download the workflow image below and drag it into ComfyUI to load the workflow:

![ComfyUI Workflow - ControlNet](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/scribble_controlnet.png)

<Tip>
  Images with workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.
  This image already includes download links for the corresponding models, and dragging it into ComfyUI will automatically prompt for downloads.
</Tip>

Please download the image below, which we will use as input:

![ComfyUI Sketch Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/scribble_input.png)

### 2. Manual Model Installation

<Note>
  If your network cannot successfully complete the automatic download of the corresponding models, please try manually downloading the models below and placing them in the specified directories:
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
  In this example, you could also use the VAE model embedded in dreamCreationVirtual3DECommerce\_v10.safetensors, but we're following the model author's recommendation to use a separate VAE model.
</Note>

### 3. Step-by-Step Workflow Execution

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d26abbfd1993f28b88efcf6231246945" alt="ComfyUI Workflow - ControlNet Flow Diagram" data-og-width="2000" width="2000" data-og-height="1086" height="1086" data-path="images/tutorial/controlnet/flow_diagram_scribble.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=08969e36a1eda27b8d60fb77cb41afee 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=94b8fabbcd1f910e52bf9834d3ac5678 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0e809d2f8d501e7e308408d46a6a8588 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6fea2381caed335cac0b7073ef9366e0 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2d8133f58fc8c11cacf2ed11e8c181bd 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_scribble.png?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a1c8aec6bfe0316295dcf600b09cebe2 2500w" />

1. Ensure that `Load Checkpoint` can load **dreamCreationVirtual3DECommerce\_v10.safetensors**
2. Ensure that `Load VAE` can load **vae-ft-mse-840000-ema-pruned.safetensors**
3. Click `Upload` in the `Load Image` node to upload the input image provided earlier
4. Ensure that `Load ControlNet` can load **control\_v11p\_sd15\_scribble\_fp16.safetensors**
5. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation

## Related Node Explanations

### Load ControlNet Node Explanation

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c3a99d9bd08baaedb7a4d426cc930880" alt="load controlnet" data-og-width="807" width="807" data-og-height="294" height="294" data-path="images/comfy_core/loaders/load_controlnet_model.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1d65dc81220e679eb2f17860ffe92562 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3d499a7fab5e9656b3043440bb259906 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=54654343fb221fc3ae377467f2c799a6 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e363dc10dfa46d6f2e26e94018ef47ba 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4c90104f34b30cc2e7943bc047639345 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_controlnet_model.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=eaa65efbc295ed4f2bd3a8885acc02d0 2500w" />

Models located in `ComfyUI\models\controlnet` will be detected by ComfyUI and can be loaded through this node.

### Apply ControlNet Node Explanation

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=de9e90df2dcfe5cc7020a8c9cdb40a65" alt="apply controlnet" data-og-width="778" width="778" data-og-height="547" height="547" data-path="images/comfy_core/conditioning/controlnet/apply_controlnet.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d2589a80afb77a1dd0d7fa12ae34142c 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=25ed3a4735b06b267519ac4313bcbaca 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=0b18dfc1c8fdd26f07a00c4d5e422f16 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=984444ad3f286a57a48cad3e9d30cb59 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=adbb7c39e09866c7c85fc9bbb59c9ebc 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c1257bb2026d9ef99421d5474e1dea23 2500w" />

This node accepts the ControlNet model loaded by `load controlnet` and generates corresponding control conditions based on the input image.

**Input Types**

| Parameter Name  | Function                                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `positive`      | Positive conditioning                                                                                                                      |
| `negative`      | Negative conditioning                                                                                                                      |
| `control_net`   | The ControlNet model to be applied                                                                                                         |
| `image`         | Preprocessed image used as reference for ControlNet application                                                                            |
| `vae`           | VAE model input                                                                                                                            |
| `strength`      | Strength of ControlNet application; higher values increase ControlNet's influence on the generated image                                   |
| `start_percent` | Determines when to start applying ControlNet as a percentage; e.g., 0.2 means ControlNet guidance begins when 20% of diffusion is complete |
| `end_percent`   | Determines when to stop applying ControlNet as a percentage; e.g., 0.8 means ControlNet guidance stops when 80% of diffusion is complete   |

**Output Types**

| Parameter Name | Function                                           |
| -------------- | -------------------------------------------------- |
| `positive`     | Positive conditioning data processed by ControlNet |
| `negative`     | Negative conditioning data processed by ControlNet |

You can use chain connections to apply multiple ControlNet models, as shown in the image below. You can also refer to the [Mixing ControlNet Models](/tutorials/controlnet/mixing-controlnets) guide to learn more about combining multiple ControlNet models.
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6fc3e75414f05e6c62062b4b746dc855" alt="apply controlnet chain link" data-og-width="1500" width="1500" data-og-height="1050" height="1050" data-path="images/tutorial/controlnet/apply_controlnet_chain_link.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=da6928840e7317cf4c0cc56cddd3bef9 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=be2b48a1a8c3f852ffbc1e0e7fa06f54 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8488372f56c5d9e7a4f95574094bcd25 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3893bbb66fd156f76713a5d51623cd12 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aab42fb6856dc99be46f00bb333e8a6f 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c8dee2a84c69fc57166788cae6387f17 2500w" />

<Note>
  You might see the `Apply ControlNet(Old)` node in some early workflows, which is an early version of the ControlNet node. It is currently deprecated and not visible by default in search and node lists.
  <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=eaf2f8df7456df845f7408495d19b9e8" alt="apply controlnet old" data-og-width="778" width="778" data-og-height="370" height="370" data-path="images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d1b70261b17b6e3b46c4ed91e1be1fd4 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9f81de62d9574bcb8b0519488cdc4195 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b0878d93dea28563986e3a1e2c77450b 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a5d3fdd9887f00d55fc68161fbed2ca6 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e34942778977bc4a0898c09123123b26 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/controlnet/apply_controlnet_old.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=11a8f3eb731d988689ce245a0a327d8d 2500w" />
  To enable it, go to **Settings** --> **comfy** --> **Node** and enable the `Show deprecated nodes in search` option. However, it's recommended to use the new node.
</Note>

## Start Your Exploration

1. Try creating similar sketches, or even draw your own, and use ControlNet models to generate images to experience the benefits of ControlNet.
2. Adjust the `Control Strength` parameter in the Apply ControlNet node to control the influence of the ControlNet model on the generated image.
3. Visit the [ControlNet-v1-1\_fp16\_safetensors](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/tree/main) repository to download other types of ControlNet models and try using them to generate images.
