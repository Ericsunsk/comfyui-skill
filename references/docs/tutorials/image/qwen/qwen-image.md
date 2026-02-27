> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen-Image ComfyUI Native Workflow Example

> Qwen-Image is a 20B parameter MMDiT (Multimodal Diffusion Transformer) model open-sourced under the Apache 2.0 license.

**Qwen-Image** is the first image generation foundation model released by Alibaba's Qwen team. It's a 20B parameter MMDiT (Multimodal Diffusion Transformer) model open-sourced under the Apache 2.0 license. The model has made significant advances in **complex text rendering** and **precise image editing**, achieving high-fidelity output for multiple languages including English and Chinese.

**Model Highlights**:

* **Excellent Multilingual Text Rendering**: Supports high-precision text generation in multiple languages including English, Chinese, Korean, Japanese, maintaining font details and layout consistency
* **Diverse Artistic Styles**: From photorealistic scenes to impressionist paintings, from anime aesthetics to minimalist design, fluidly adapting to various creative prompts

**Related Links**:

* [GitHub](https://github.com/QwenLM/Qwen-Image)
* [Hugging Face](https://huggingface.co/Qwen/Qwen-Image)
* [ModelScope](https://modelscope.cn/models/qwen/Qwen-Image)

Currently Qwen-Image has multiple ControlNet support options available:

* [Qwen-Image-DiffSynth-ControlNets/model\_patches](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/tree/main/split_files/model_patches): Includes canny, depth, and inpaint models
* [qwen\_image\_union\_diffsynth\_lora.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/blob/main/split_files/loras/qwen_image_union_diffsynth_lora.safetensors): Image structure control LoRA supporting canny, depth, pose, lineart, softedge, normal, openpose
* InstantX ControlNet: To be updated

## ComfyOrg Qwen-Image live stream

**Qwen-Image in ComfyUI - Lightning & LoRAs**

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/WBFHwrpYRtY?si=uREGRhBDryTJBIry" title="Qwen-Image in ComfyUI - Lightning & LoRAs / August 15th, 2025" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

**Qwen-Image ControlNet in ComfyUI - DiffSynth**

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/bXMClHfEFn4?si=dcaNdqOMSwvu3t8x" title="Qwen-Image ControlNet in ComfyUI - DiffSynth / August 26th, 2025" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Qwen-Image Native Workflow Example

<Tip>
  <Tabs>
    <Tab title="Portable or self deployed users">
      Make sure your ComfyUI is updated.

      * [Download ComfyUI](https://www.comfy.org/download)
      * [Update Guide](/installation/update_comfyui)

      Workflows in this guide can be found in the [Workflow Templates](/interface/features/template).
      If you can't find them in the template, your ComfyUI may be outdated. (Desktop version's update will delay sometime)

      If nodes are missing when loading a workflow, possible reasons:

      1. You are not using the latest ComfyUI version (Nightly version)
      2. Some nodes failed to import at startup
    </Tab>

    <Tab title="Desktop or Cloud users">
      * The Desktop is base on ComfyUI stable release, it will auto-update when there is a new Desktop stable release available.
      * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

      So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.
    </Tab>
  </Tabs>
</Tip>

<a href="https://cloud.comfy.org/?template=image_qwen_image&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#7c3aed', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginBottom: '1rem'}}>
  Run on Comfy Cloud
</a>

There are three different models used in the workflow attached to this document:

1. Qwen-Image original model fp8\_e4m3fn
2. 8-step accelerated version: Qwen-Image original model fp8\_e4m3fn with lightx2v 8-step LoRA
3. Distilled version: Qwen-Image distilled model fp8\_e4m3fn

**VRAM Usage Reference**
GPU: RTX4090D 24GB

| Model Used                            | VRAM Usage | First Generation | Second Generation |
| ------------------------------------- | ---------- | ---------------- | ----------------- |
| fp8\_e4m3fn                           | 86%        | ≈ 94s            | ≈ 71s             |
| fp8\_e4m3fn with lightx2v 8-step LoRA | 86%        | ≈ 55s            | ≈ 34s             |
| Distilled fp8\_e4m3fn                 | 86%        | ≈ 69s            | ≈ 36s             |

### 1. Workflow File

After updating ComfyUI, you can find the workflow file in the templates, or drag the workflow below into ComfyUI to load it.
![Qwen-image Text-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/qwen/qwen-image.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Workflow for Qwen-Image Official Model</p>
</a>

Distilled version

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/qwen/image_qwen_image_distill.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Workflow for Distilled Model</p>
</a>

### 2. Model Download

**Available Models in ComfyUI**

* Qwen-Image\_bf16 (40.9 GB)
* Qwen-Image\_fp8 (20.4 GB)
* Distilled versions (non-official, requires only 15 steps)

All models are available at [Huggingface](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main) and [Modelscope](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI/files)

**Diffusion model**

* [qwen\_image\_fp8\_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors)

Qwen\_image\_distill

* [qwen\_image\_distill\_full\_fp8\_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/non_official/diffusion_models/qwen_image_distill_full_fp8_e4m3fn.safetensors)
* [qwen\_image\_distill\_full\_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/non_official/diffusion_models/qwen_image_distill_full_bf16.safetensors)

<Note>
  - The original author of the distilled version recommends using 15 steps with cfg 1.0.
  - According to tests, this distilled version also performs well at 10 steps with cfg 1.0. You can choose either euler or res\_multistep based on the type of image you want.
</Note>

**LoRA**

* [Qwen-Image-Lightning-8steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-8steps-V1.0.safetensors)

**Text encoder**

* [qwen\_2.5\_vl\_7b\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**VAE**

[qwen\_image\_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors)

**Model Storage Location**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── qwen_image_fp8_e4m3fn.safetensors
│   │   └── qwen_image_distill_full_fp8_e4m3fn.safetensors ## 蒸馏版
│   ├── 📂 loras/
│   │   └── Qwen-Image-Lightning-8steps-V1.0.safetensors   ## 8步加速 LoRA 模型
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

### 3. Workflow Instructions

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=123e11f9be1c31a9e3a3c0ff1df299da" alt="Step Guide" data-og-width="3111" width="3111" data-og-height="1829" height="1829" data-path="images/tutorial/image/qwen/image_qwen_image-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fd031c2e037ec5ada7bfc72d5dab4f32 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=890775205ed1e33ad3de3e01136e1c73 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ffb8a3d81da16b3c663cc7d6ca3a1e86 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=807ca8d050cb51f8f4b5057a00d6ad41 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2938f2fc67819563457a78ebea810aae 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2b234cc0550c4157b194d76f8e1066ee 2500w" />

1. Make sure the `Load Diffusion Model` node has loaded `qwen_image_fp8_e4m3fn.safetensors`
2. Make sure the `Load CLIP` node has loaded `qwen_2.5_vl_7b_fp8_scaled.safetensors`
3. Make sure the `Load VAE` node has loaded `qwen_image_vae.safetensors`
4. Make sure the `EmptySD3LatentImage` node is set with the correct image dimensions
5. Set your prompt in the `CLIP Text Encoder` node; currently, it supports at least English, Chinese, Korean, Japanese, Italian, etc.
6. If you want to enable the 8-step acceleration LoRA by lightx2v, select the node and use `Ctrl + B` to enable it, and modify the Ksampler settings as described in step 8
7. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow
8. For different model versions and workflows, adjust the KSampler parameters accordingly

<Note>
  The distilled model and the 8-step acceleration LoRA by lightx2v do not seem to be compatible for simultaneous use. You can experiment with different combinations to verify if they can be used together.
</Note>

## Qwen Image InstantX ControlNet Workflow

This is a ControlNet model, so you can use it as normal ControlNet.

<a href="https://cloud.comfy.org/?template=image_qwen_image_instantx_controlnet&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#7c3aed', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginBottom: '1rem'}}>
  Run on Comfy Cloud
</a>

### 1. Workflow and Input Images

Download the image below and drag it into ComfyUI to load the workflow
![workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-instantx-controlnet/image_qwen_image_instantx_controlnet.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_instantx_controlnet.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Format Workflow</p>
</a>

Download the image below as input
![input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-instantx-controlnet/input.jpg)

### 2. Model Links

1. InstantX Controlnet

Download [Qwen-Image-InstantX-ControlNet-Union.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-InstantX-ControlNets/resolve/main/split_files/controlnet/Qwen-Image-InstantX-ControlNet-Union.safetensors) and save it to the `ComfyUI/models/controlnet/` folder

2. **Lotus Depth model**

We will use this model to generate the depth map of the image. The following two models need to be downloaded:

**Diffusion Model**

* [lotus-depth-d-v1-1.safetensors](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors)

**VAE Model**

* [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors)  or any SD1.5 VAE

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── lotus-depth-d-v1-1.safetensors
│   └── vae/
│       └──  lvae-ft-mse-840000-ema-pruned.safetensors
```

> You can also use custom nodes like [comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) to generate depth map.

### 3. Workflow Instructions

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a73a3f375691a80eb87a6cec12c48ad9" alt="Process Instructions" data-og-width="3800" width="3800" data-og-height="1730" height="1730" data-path="images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d1c3841692bb9868512816925f74ba85 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4633d161d5b014a83c5cf2deec05ea2f 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fbd0674ae9fd596c5975e6c02d235136 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=dae55f9d59a7d33e3bf20ca9a032aabf 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=56b395e407793ea121f6f1497c45316a 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_instantx_controlnet.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b6eceab00f771c33de88f74f8e498d19 2500w" />

1. Ensure that the `Load ControlNet Model` node correctly loads the `Qwen-Image-InstantX-ControlNet-Union.safetensors` model
2. Upload input image
3. This subgraph uses the Lotus Depth model. You can find it in the templates or edit the subgraph to learn more, make sure all the models are loaded correctly
4. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

## Qwen Image ControlNet DiffSynth-ControlNets Model Patches Workflow

<a href="https://cloud.comfy.org/?template=image_qwen_image_controlnet_patch&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#7c3aed', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginBottom: '1rem'}}>
  Run on Comfy Cloud
</a>

This model is actually not a ControlNet, but a Model patch that supports three different control modes: canny, depth, and inpaint.

Original model address: [DiffSynth-Studio/Qwen-Image ControlNet](https://www.modelscope.cn/collections/Qwen-Image-ControlNet-6157b44e89d444)
Comfy Org rehost address: [Qwen-Image-DiffSynth-ControlNets/model\_patches](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/tree/main/split_files/model_patches)

### 1. Workflow and Input Images

Download the image below and drag it into ComfyUI to load the corresponding workflow
![workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-controlnet-model-patch/image_qwen_image_controlnet_patch.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_controlnet_patch.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Format Workflow</p>
</a>

Download the image below as input:

![input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-controlnet-model-patch/input.png)

### 2. Model Links

Other models are the same as the Qwen-Image basic workflow. You only need to download the models below and save them to the `ComfyUI/models/model_patches` folder

* [qwen\_image\_canny\_diffsynth\_controlnet.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_canny_diffsynth_controlnet.safetensors)
* [qwen\_image\_depth\_diffsynth\_controlnet.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_depth_diffsynth_controlnet.safetensors)
* [qwen\_image\_inpaint\_diffsynth\_controlnet.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_inpaint_diffsynth_controlnet.safetensors)

### 3. Workflow Usage Instructions

Currently, diffsynth has three patch models: Canny, Depth, and Inpaint.

If you're using ControlNet-related workflows for the first time, you need to understand that control images need to be preprocessed into supported image formats before they can be used and recognized by the model.

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3459806aaf59d27e2e1554c4bd2d0de7" alt="Input Type Diagram" data-og-width="5920" width="5920" data-og-height="2438" height="2438" data-path="images/tutorial/image/qwen/controlnet_input_types.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=98a48facb7eecc0ecf0cb783d620a17c 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=dc05aface8427790488a1db20060354f 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fd4d165a1edd3ce9459f5210155c37b5 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3dc34a088c42b62b73cf344071944115 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ec72ea0b9fa642056de6f6700df2bbf9 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/controlnet_input_types.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f3a9a233cc4c513b7818b9463fae0ac4 2500w" />

* Canny: Processed canny edge, line art contours
* Depth: Preprocessed depth map showing spatial relationships
* Inpaint: Requires using Mask to mark areas that need to be repainted

Since this patch model is divided into three different models, you need to select the correct preprocessing type when inputting to ensure proper image preprocessing.

**Canny Model ControlNet Usage Instructions**

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ca49f6ba72d3897cb14614314bc0d3c8" alt="Canny Workflow" data-og-width="3800" width="3800" data-og-height="2046" height="2046" data-path="images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1dd6c853b2c2b9cc69877f3f3088a583 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b25f3d2ecff52c8a63ee0b671200b38e 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3a09344131390ad832d0948cac2f5d32 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=48aedbe0e779c62f482183934754ba33 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=bc723145ccca9fa5f4b766d49da10ae8 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-canny.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6f5f3196d120979c783e841fb2deb82f 2500w" />

1. Ensure that `qwen_image_canny_diffsynth_controlnet.safetensors` is loaded
2. Upload input image for subsequent processing
3. The Canny node is a native preprocessing node that will preprocess the input image according to your set parameters to control generation
4. If needed, you can modify the `strength` in the `QwenImageDiffsynthControlnet` node to control the intensity of line art control
5. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

> For using qwen\_image\_depth\_diffsynth\_controlnet.safetensors, you need to preprocess the image into a depth map and replace the `image processing` part. For this usage, please refer to the InstantX processing method in this document. Other parts are similar to using the Canny model.

**Inpaint Model ControlNet Usage Instructions**
<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c3a3493ab00a11eba1e634624b40a2c1" alt="Inpaint Workflow" data-og-width="3808" width="3808" data-og-height="2046" height="2046" data-path="images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2cd61275d4f008dd88c8f80d79e8abc4 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=85f2dcdc8fce631cc8977a168af9f580 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7d330a90db88bf316006c5f17dba19f0 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=74930608b678ed937bf707bb02341fd6 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3c3e6b0170c96a481cb1a969bc891f4b 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_controlnet_patch-inpaint.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7ec9aeca94135ef2945033492dfbad82 2500w" />

For the Inpaint model, it requires using the [Mask Editor](/interface/maskeditor) to draw a mask and use it as input control condition.

1. Ensure that `ModelPatchLoader` loads the `qwen_image_inpaint_diffsynth_controlnet.safetensors` model
2. Upload image and use the [Mask Editor](/interface/maskeditor) to draw a mask. You need to connect the `mask` output of the corresponding `Load Image` node to the `mask` input of `QwenImageDiffsynthControlnet` to ensure the corresponding mask is loaded
3. Use the `Ctrl-B` shortcut to set the original Canny in the workflow to bypass mode, making the corresponding Canny node processing ineffective
4. In `CLIP Text Encoder`, input what you want to change the masked area to
5. If needed, you can modify the `strength` in the `QwenImageDiffsynthControlnet` node to control the corresponding control intensity
6. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

## Qwen Image Union ControlNet LoRA Workflow

<a href="https://cloud.comfy.org/?template=image_qwen_image_union_control_lora&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#7c3aed', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginBottom: '1rem'}}>
  Run on Comfy Cloud
</a>

Original model address: [DiffSynth-Studio/Qwen-Image-In-Context-Control-Union](https://www.modelscope.cn/models/DiffSynth-Studio/Qwen-Image-In-Context-Control-Union/)
Comfy Org rehost address: [qwen\_image\_union\_diffsynth\_lora.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/blob/main/split_files/loras/qwen_image_union_diffsynth_lora.safetensors): Image structure control LoRA supporting canny, depth, pose, lineart, softedge, normal, openpose

### 1. Workflow and Input Images

Download the image below and drag it into ComfyUI to load the workflow
![workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-union-control-lora/image_qwen_image_union_control_lora.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_union_control_lora.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Format Workflow</p>
</a>

Download the image below as input

![workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/qwen/qwen-image-union-control-lora/input.png)

### 2. Model Links

Download the model below. Since this is a LoRA model, it needs to be saved to the `ComfyUI/models/loras/` folder

* [qwen\_image\_union\_diffsynth\_lora.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/blob/main/split_files/loras/qwen_image_union_diffsynth_lora.safetensors): Image structure control LoRA supporting canny, depth, pose, lineart, softedge, normal, openpose

### 3. Workflow Instructions

This model is a unified control LoRA that supports canny, depth, pose, lineart, softedge, normal, openpose controls. Since many image preprocessing native nodes are not fully supported, you should use something like [comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) to complete other image preprocessing.

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=428cafa03e7759a771c9f1e63d759dd0" alt="Union Control LoRA" data-og-width="3800" width="3800" data-og-height="2238" height="2238" data-path="images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e964f8cad5f3b943f677dc4c7d5ef992 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=8ed100d1fc4a43f99736ced29d2d51e3 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5316d6291981443405e65adb048b2f6f 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=58bd2cda362ebf0909786bb5cdb6f7ac 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7e1152f424d5746e13ffeb149b3336ee 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/image_qwen_image_union_control_lora.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c212ec01f142df185da8ce853571b99f 2500w" />

1. Ensure that `LoraLoaderModelOnly` correctly loads the `qwen_image_union_diffsynth_lora.safetensors` model
2. Upload input image
3. If needed, you can adjust the `Canny` node parameters. Since different input images require different parameter settings to get better image preprocessing results, you can try adjusting the corresponding parameter values to get more/fewer details
4. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

> For other types of control, you also need to replace the image processing part.
