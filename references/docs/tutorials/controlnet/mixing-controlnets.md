> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Mixing ControlNet Examples

> In this example, we will demonstrate how to mix multiple ControlNets and learn to use multiple ControlNet models to control image generation

In AI image generation, a single control condition often fails to meet the requirements of complex scenes. Mixing multiple ControlNets allows you to control different regions or aspects of an image simultaneously, achieving more precise control over image generation.

In certain scenarios, mixing ControlNets can leverage the characteristics of different control conditions to achieve more refined conditional control:

1. **Scene Complexity**: Complex scenes require multiple control conditions working together
2. **Fine-grained Control**: By adjusting the strength parameter of each ControlNet, you can precisely control the degree of influence for each part
3. **Complementary Effects**: Different types of ControlNets can complement each other, compensating for the limitations of single controls
4. **Creative Expression**: Combining different controls can produce unique creative effects

### How to Mix ControlNets

When mixing multiple ControlNets, each ControlNet influences the image generation process according to its applied area. ComfyUI enables multiple ControlNet conditions to be applied sequentially in a layered manner through chain connections in the `Apply ControlNet` node:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6fc3e75414f05e6c62062b4b746dc855" alt="apply controlnet chain link" data-og-width="1500" width="1500" data-og-height="1050" height="1050" data-path="images/tutorial/controlnet/apply_controlnet_chain_link.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=da6928840e7317cf4c0cc56cddd3bef9 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=be2b48a1a8c3f852ffbc1e0e7fa06f54 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8488372f56c5d9e7a4f95574094bcd25 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3893bbb66fd156f76713a5d51623cd12 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aab42fb6856dc99be46f00bb333e8a6f 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/controlnet/apply_controlnet_chain_link.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c8dee2a84c69fc57166788cae6387f17 2500w" />

## ComfyUI ControlNet Regional Division Mixing Example

In this example, we will use a combination of **Pose ControlNet** and **Scribble ControlNet** to generate a scene containing multiple elements: a character on the left controlled by Pose ControlNet and a cat on a scooter on the right controlled by Scribble ControlNet.

### 1. ControlNet Mixing Workflow Assets

Please download the workflow image below and drag it into ComfyUI to load the workflow:
![ComfyUI Workflow - Mixing ControlNet](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/mixing_controlnets.png)

<Tip>
  This workflow image contains Metadata, and can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`. The system will automatically detect and prompt to download the required models.
</Tip>

Input pose image (controls the character pose on the left):

![ComfyUI Workflow - Mixing ControlNet Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/mixing_controlnets_input.png)

Input scribble image (controls the cat and scooter on the right):

![ComfyUI Workflow - Mixing ControlNet Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/mixing_controlnets_input_scribble.png)

### 2. Manual Model Installation

<Note>
  If your network cannot successfully complete the automatic download of the corresponding models, please try manually downloading the models below and placing them in the specified directories:
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

### 3. Step-by-Step Workflow Execution

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b839fc78bb316a334a908ff38389a3d0" alt="ComfyUI Workflow - Mixing ControlNet Flow Diagram" data-og-width="1681" width="1681" data-og-height="1081" height="1081" data-path="images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=27da5acfce3ec4d1907c1ab4afe95905 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3723acd76c10d49c6901565e28b57bf9 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b5b0ec7de5bc6ae4e24f378c5fc0a4ee 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=63546a6d6c61d981bc110e2c1397ab5e 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7674c4309f93a53d6f18734790313eaa 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/controlnet/flow_diagram_mixing_controlnet.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0e0979fa692936407c1b45930df2645d 2500w" />

Follow these steps according to the numbered markers in the image:

1. Ensure that `Load Checkpoint` can load **awpainting\_v14.safetensors**
2. Ensure that `Load VAE` can load **vae-ft-mse-840000-ema-pruned.safetensors**

First ControlNet group using the Openpose model:
3\. Ensure that `Load ControlNet Model` loads **control\_v11p\_sd15\_openpose\_fp16.safetensors**
4\. Click `Upload` in the `Load Image` node to upload the pose image provided earlier

Second ControlNet group using the Scribble model:
5\. Ensure that `Load ControlNet Model` loads **control\_v11p\_sd15\_scribble\_fp16.safetensors**
6\. Click `Upload` in the `Load Image` node to upload the scribble image provided earlier
7\. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation

## Workflow Explanation

#### Strength Balance

When controlling different regions of an image, balancing the strength parameters is particularly important:

* If the ControlNet strength for one region is significantly higher than another, it may cause that region's control effect to overpower and suppress the other region
* It's recommended to set similar strength values for ControlNets controlling different regions, for example, both set to 1.0

#### Prompt Techniques

For regional division mixing, the prompt needs to include descriptions of both regions:

```
"A woman in red dress, a cat riding a scooter, detailed background, high quality"
```

Such a prompt covers both the character and the cat on the scooter, ensuring the model pays attention to both control regions.

## Multi-dimensional Control Applications for a Single Subject

In addition to the regional division mixing shown in this example, another common mixing approach is to apply multi-dimensional control to the same subject. For example:

* **Pose + Depth**: Control character posture and spatial sense
* **Pose + Canny**: Control character posture and edge details
* **Pose + Reference**: Control character posture while referencing a specific style

In this type of application, reference images for multiple ControlNets should be aligned to the same subject, and their strengths should be adjusted to ensure proper balance.

By combining different types of ControlNets and specifying their control regions, you can achieve precise control over elements in your image.
