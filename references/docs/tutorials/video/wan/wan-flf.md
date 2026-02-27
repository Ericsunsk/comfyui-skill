> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Wan2.1 FLF2V Native Example

> This guide explains how to complete Wan2.1 FLF2V video generation examples in ComfyUI

Wan FLF2V (First-Last Frame Video Generation) is an open-source video generation model developed by the Alibaba Tongyi Wanxiang team. Its open-source license is [Apache 2.0](https://github.com/Wan-Video/Wan2.1?tab=Apache-2.0-1-ov-file).
Users only need to provide two images as the starting and ending frames, and the model automatically generates intermediate transition frames, outputting a logically coherent and naturally flowing 720p high-definition video.

**Core Technical Highlights**

1. **Precise First-Last Frame Control**: The matching rate of first and last frames reaches 98%, defining video boundaries through starting and ending scenes, intelligently filling intermediate dynamic changes to achieve scene transitions and object morphing effects.
2. **Stable and Smooth Video Generation**: Using CLIP semantic features and cross-attention mechanisms, the video jitter rate is reduced by 37% compared to similar models, ensuring natural and smooth transitions.
3. **Multi-functional Creative Capabilities**: Supports dynamic embedding of Chinese and English subtitles, generation of anime/realistic/fantasy and other styles, adapting to different creative needs.
4. **720p HD Output**: Directly generates 1280×720 resolution videos without post-processing, suitable for social media and commercial applications.
5. **Open-source Ecosystem Support**: Model weights, code, and training framework are fully open-sourced, supporting deployment on mainstream AI platforms.

**Technical Principles and Architecture**

1. **DiT Architecture**: Based on diffusion models and Diffusion Transformer architecture, combined with Full Attention mechanism to optimize spatiotemporal dependency modeling, ensuring video coherence.
2. **3D Causal Variational Encoder**: Wan-VAE technology compresses HD frames to 1/128 size while retaining subtle dynamic details, significantly reducing memory requirements.
3. **Three-stage Training Strategy**: Starting from 480P resolution pre-training, gradually upgrading to 720P, balancing generation quality and computational efficiency through phased optimization.

**Related Links**

* **GitHub Repository**: [GitHub](https://github.com/Wan-Video/Wan2.1)
* **Hugging Face Model Page**: [Hugging Face](https://huggingface.co/Wan-AI/Wan2.1-FLF2V-14B-720P)
* **ModelScope Community**: [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-FLF2V-14B-720P)

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

## Wan2.1 FLF2V 720P ComfyUI Native Workflow Example

### 1. Download Workflow Files and Related Input Files

<Tip>
  Since this model is trained on high-resolution images, using smaller sizes may not yield good results. In the example, we use a size of 720 \* 1280, which may cause users with lower VRAM hard to run smoothly and will take a long time to generate.
  If needed, please adjust the video generation size for testing. A small generation size may not produce good output with this model, please notice that.
</Tip>

Please download the WebP file below, and drag it into ComfyUI to load the corresponding workflow. The workflow has embedded the corresponding model download file information.

![Wan2.1 FLF2V 720P f16 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1_flf2v/wan2.1_flf2v_720_f16.webp)

Please download the two images below, which we will use as the starting and ending frames of the video

![start\_image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1_flf2v/input/start_image.png)
![end\_image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1_flf2v/input/end_image.png)

### 2. Manual Model Installation

If corresponding

All models involved in this guide can be found [here](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files).

**diffusion\_models** Choose one version based on your hardware conditions

* FP16:[wan2.1\_flf2v\_720p\_14B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_flf2v_720p_14B_fp16.safetensors?download=true)
* FP8:[wan2.1\_flf2v\_720p\_14B\_fp8\_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_flf2v_720p_14B_fp8_e4m3fn.safetensors)

<Tip>
  If you have previously tried Wan Video related workflows, you may already have the following files.
</Tip>

Choose one version from **Text encoders** for download,

* [umt5\_xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors?download=true)
* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true)

**CLIP Vision**

* [clip\_vision\_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true)

File Storage Location

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── wan2.1_flf2v_720p_14B_fp16.safetensors           # or FP8 version
│   ├── text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors           # or your chosen version
│   ├── vae/
│   │   └──  wan_2.1_vae.safetensors
│   └── clip_vision/
│       └──  clip_vision_h.safetensors   
```

### 3. Complete Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f52356ef98601526215d4c21802f261f" alt="Wan2.1 FLF2V 720P Native Workflow Steps" data-og-width="2361" width="2361" data-og-height="1623" height="1623" data-path="images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=bad90a020284dacfc3a2ca4c15efcf4e 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f4dfb39e04e712cef989a2d2f0e5ee0c 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0ecd3d88d56303af22e744f38f3feefc 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6b7a7d6e2f1f0efa36421362c685e0fb 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=cdc5e13ece470f7d4b3fb9fae5176ae0 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=00569638fd71ae80e7d36880b04fdf07 2500w" />

1. Ensure the `Load Diffusion Model` node has loaded `wan2.1_flf2v_720p_14B_fp16.safetensors` or `wan2.1_flf2v_720p_14B_fp8_e4m3fn.safetensors`
2. Ensure the `Load CLIP` node has loaded `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
3. Ensure the `Load VAE` node has loaded `wan_2.1_vae.safetensors`
4. Ensure the `Load CLIP Vision` node has loaded `clip_vision_h.safetensors`
5. Upload the starting frame to the `Start_image` node
6. Upload the ending frame to the `End_image` node
7. (Optional) Modify the positive and negative prompts, both Chinese and English are supported
8. (**Important**) In `WanFirstLastFrameToVideo` we use 720*1280 as default size.because it's a 720P model, so using a small size will not yield good output. Please use size around 720*1280 for good generation.
9. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation
