> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Flux.1 ControlNet Examples

> This guide will demonstrate workflow examples using Flux.1 ControlNet.

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9796a0a85863c068c836ff7351b21729" alt="Flux.1 Canny Controlnet" data-og-width="1600" width="1600" data-og-height="434" height="434" data-path="images/tutorial/flux/flux-1-canny-controlnet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c8a38bf940731ef4f191acfbc4e7331d 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=57197282f571d9d7fbe9da9afac18d91 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f0e887ea60fdcab432c04e9b9b8cd8be 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9a2e438661c73dba661598d8c85993fa 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7718559f1774a5378b2cce821a00e5db 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-canny-controlnet.png?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=232c092e87b8022fe2e34d113796c18e 2500w" />
<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=34c23b4e92011bb86fe97bc966441d80" alt="Flux.1 Depth Controlnet" data-og-width="1600" width="1600" data-og-height="285" height="285" data-path="images/tutorial/flux/flux-1-depth-controlnet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=65ff60ff81d6db718aaa5d0990150a0f 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5df60b44abf1779409b2531f58c372d7 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=af9afb5910abd39fcdd9fb3a96c728a6 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=471f82a699282e9f0d1ea5e1a5ed8bb1 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8b0b4a5361b74724b97d8984fc34abb6 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-1-depth-controlnet.png?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=70accae2c7aaa0600b3d99827bd2b634 2500w" />

## FLUX.1 ControlNet Model Introduction

FLUX.1 Canny and Depth are two powerful models from the [FLUX.1 Tools](https://blackforestlabs.ai/flux-1-tools/) launched by [Black Forest Labs](https://blackforestlabs.ai/). This toolkit is designed to add control and guidance capabilities to FLUX.1, enabling users to modify and recreate real or generated images.

**FLUX.1-Depth-dev** and **FLUX.1-Canny-dev** are both 12B parameter Rectified Flow Transformer models that can generate images based on text descriptions while maintaining the structural features of the input image.
The Depth version maintains the spatial structure of the source image through depth map extraction techniques, while the Canny version uses edge detection techniques to preserve the structural features of the source image, allowing users to choose the appropriate control method based on different needs.

Both models have the following features:

* Top-tier output quality and detail representation
* Excellent prompt following ability while maintaining consistency with the original image
* Trained using guided distillation techniques for improved efficiency
* Open weights for the research community
* API interfaces (pro version) and open-source weights (dev version)

Additionally, Black Forest Labs also provides **FLUX.1-Depth-dev-lora** and **FLUX.1-Canny-dev-lora** adapter versions extracted from the complete models.
These can be applied to the FLUX.1 \[dev] base model to provide similar functionality with smaller file size, especially suitable for resource-constrained environments.

We will use the full version of **FLUX.1-Canny-dev** and **FLUX.1-Depth-dev-lora** to complete the workflow examples.

<Tip>
  All workflow images's Metadata contains the corresponding model download information. You can load the workflows by:

  * Dragging them directly into ComfyUI
  * Or using the menu `Workflows` -> `Open（ctrl+o）`

  If you're not using the Desktop Version or some models can't be downloaded automatically, please refer to the manual installation sections to save the model files to the corresponding folder.

  For image preprocessors, you can use the following custom nodes to complete image preprocessing. In this example, we will provide processed images as input.

  * [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
  * [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
</Tip>

## FLUX.1-Canny-dev Complete Version Workflow

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_canny_model_example&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

### 1. Workflow and Asset

Please download the workflow image below and drag it into ComfyUI to load the workflow

![ComfyUI Workflow - ControlNet](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/controlnet/flux-1-canny-dev.png)

Please download the image below, which we will use as the input image

![ComfyUI Flux.1 Canny Controlnet input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/controlnet/flux-1-canny-dev-input.png)

### 2. Manual Models Installation

<Note>
  If you have previously used the [complete version of Flux related workflows](/tutorials/flux/flux-1-text-to-image), then you only need to download the **flux1-canny-dev.safetensors** model file.
  Since you need to first agree to the terms of [black-forest-labs/FLUX.1-Canny-dev](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev), please visit the [black-forest-labs/FLUX.1-Canny-dev](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev) page and make sure you have agreed to the corresponding terms as shown in the image below.
  <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=64b9b0d0d2b8dd332dc1184dde9689be" alt="Flux Agreement" data-og-width="2000" width="2000" data-og-height="1091" height="1091" data-path="images/tutorial/flux/flux1_canny_dev_agreement.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c3aacab6b791cf60520a0b4be1ee988b 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=72cde7f0cde89233c51a28598dcf996c 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8d31cbd9704522774e3363a4174f1c50 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=37052cd503baba8bda5a10f153ad0710 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=656f8dcc4afab76118ed6ed3e7e253cf 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_canny_dev_agreement.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=96568aa34dc2455b23148d6796b480c5 2500w" />
</Note>

Complete model list:

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true)
* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)
* [flux1-canny-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev/resolve/main/flux1-canny-dev.safetensors?download=true) (Please ensure you have agreed to the corresponding repo's terms)

File storage location:

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

### 3. Step-by-Step Workflow Execution

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9dfe7fc30106a96d837a93cb27958e42" alt="ComfyUI Flux.1 Canny Controlnet Step Process" data-og-width="4000" width="4000" data-og-height="1736" height="1736" data-path="images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=751235f8031159be58c382a114dc43f3 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=1946bcd3dec56bbf062cedb8bcbd8b97 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=bca1ef585a0acbc78fc4d51140ec10b1 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0f4cbe67dcf79a8af597b3d5f8becacd 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a9f35eb1702f847f6b6300918be03393 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_canny_dev.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=52c23b72214d6382f24f54c603962406 2500w" />

1. Make sure `ae.safetensors` is loaded in the `Load VAE` node
2. Make sure `flux1-canny-dev.safetensors` is loaded in the `Load Diffusion Model` node
3. Make sure the following models are loaded in the `DualCLIPLoader` node:
   * clip\_name1: t5xxl\_fp16.safetensors
   * clip\_name2: clip\_l.safetensors
4. Upload the provided input image in the `Load Image` node
5. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

### 4. Start Your Experimentation

Try using the [FLUX.1-Depth-dev](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev) model to complete the Depth version of the workflow

You can use the image below as input
![ComfyUI Indoor Depth Map](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/controlnet/depth-t2i-adapter_input.png)

Or use the following custom nodes to complete image preprocessing:

* [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet)
* [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

## FLUX.1-Depth-dev-lora Workflow

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_depth_lora_example&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

The LoRA version workflow builds on the complete version by adding the LoRA model. Compared to the [complete version of the Flux workflow](/tutorials/flux/flux-1-text-to-image), it adds nodes for loading and using the corresponding LoRA model.

### 1. Workflow and Asset

Please download the workflow image below and drag it into ComfyUI to load the workflow

![ComfyUI Workflow - ControlNet](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/controlnet/flux-1-depth-dev-lora.png)

Please download the image below, which we will use as the input image

![ComfyUI Flux.1 Depth Controlnet input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/controlnet/flux-1-depth-dev-lora-input.png)

### 2. Manual Model Download

<Tip>
  If you have previously used the [complete version of Flux related workflows](/tutorials/flux/flux-1-text-to-image), then you only need to download the **flux1-depth-dev-lora.safetensors** model file.
</Tip>

Complete model list:

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true)
* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)
* [flux1-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors?download=true)
* [flux1-depth-dev-lora.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev-lora/resolve/main/flux1-depth-dev-lora.safetensors?download=true)

File storage location:

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

### 3. Step-by-Step Workflow Execution

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ea682a93040eac4c930e05a66e08dd7f" alt="ComfyUI Flux.1 Depth Controlnet Step Process" data-og-width="4000" width="4000" data-og-height="1703" height="1703" data-path="images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=19eb4f1db7a87249bac15f18632c01c7 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9f8739c81b7752be484a37383bad0027 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fbe919a88bd28aa323efdad92ece7161 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b0b2d96d4c2bbea7738e5d4a7c377324 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e888396047285644984cc46db06f5922 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_1_depth_dev_lora.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=16ae6afd59005c12beb9612a542a4f01 2500w" />

1. Make sure `flux1-dev.safetensors` is loaded in the `Load Diffusion Model` node
2. Make sure `flux1-depth-dev-lora.safetensors` is loaded in the `LoraLoaderModelOnly` node
3. Make sure the following models are loaded in the `DualCLIPLoader` node:
   * clip\_name1: t5xxl\_fp16.safetensors
   * clip\_name2: clip\_l.safetensors
4. Upload the provided input image in the `Load Image` node
5. Make sure `ae.safetensors` is loaded in the `Load VAE` node
6. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

### 4. Start Your Experimentation

Try using the [FLUX.1-Canny-dev-lora](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev-lora) model to complete the Canny version of the workflow

Use [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet) or [ComfyUI ControlNet aux](https://github.com/Fannovel16/comfyui_controlnet_aux) to complete image preprocessing

## Community Versions of Flux Controlnets

XLab and InstantX + Shakker Labs have released Controlnets for Flux.

**InstantX:**

* [FLUX.1-dev-Controlnet-Canny](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Canny/blob/main/diffusion_pytorch_model.safetensors)
* [FLUX.1-dev-ControlNet-Depth](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Depth/blob/main/diffusion_pytorch_model.safetensors)
* [FLUX.1-dev-ControlNet-Union-Pro](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/blob/main/diffusion_pytorch_model.safetensors)

**XLab**: [flux-controlnet-collections](https://huggingface.co/XLabs-AI/flux-controlnet-collections)

Place these files in the `ComfyUI/models/controlnet` directory.

You can visit [Flux Controlnet Example](https://raw.githubusercontent.com/comfyanonymous/ComfyUI_examples/refs/heads/master/flux/flux_controlnet_example.png) to get the corresponding workflow image, and use the image from [here](https://raw.githubusercontent.com/comfyanonymous/ComfyUI_examples/refs/heads/master/flux/girl_in_field.png) as the input image.
