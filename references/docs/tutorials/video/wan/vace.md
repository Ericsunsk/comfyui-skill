> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Wan2.1 VACE Video Examples

> This article introduces how to complete Wan VACE video generation examples in ComfyUI

<Warning>
  As we have made adjustments to the template and added related usage and instructions for CausVid LoRA, this document needs to be updated and requires some preparation time. Until then, please refer to the notes in the template for usage
</Warning>

## About VACE

VACE 14B is an open-source unified video editing model launched by the Alibaba Tongyi Wanxiang team. Through integrating multi-task capabilities, supporting high-resolution processing and flexible multi-modal input mechanisms, this model significantly improves the efficiency and quality of video creation.

The model is open-sourced under the [Apache-2.0](https://github.com/ali-vilab/VACE?tab=Apache-2.0-1-ov-file) license and can be used for personal or commercial purposes.

Here is a comprehensive analysis of its core features and technical highlights:

* Multi-modal input: Supports multiple input forms including text, images, video, masks, and control signals
* Unified architecture: Single model supports multiple tasks with freely combinable functions
* Motion transfer: Generates coherent actions based on reference videos
* Local replacement: Replaces specific areas in videos through masks
* Video extension: Completes actions or extends backgrounds
* Background replacement: Preserves subjects while changing environmental backgrounds

Currently VACE has released two versions - 1.3B and 14B. Compared to the 1.3B version, the 14B version supports 720P resolution output with better image details and stability.

| Model                                                       | 480P | 720P |
| ----------------------------------------------------------- | ---- | ---- |
| [VACE-1.3B](https://huggingface.co/Wan-AI/Wan2.1-VACE-1.3B) | ✅    | ❌    |
| [VACE-14B](https://huggingface.co/Wan-AI/Wan2.1-VACE-14B)   | ✅    | ✅    |

Related model weights and code repositories:

* [VACE-1.3B](https://huggingface.co/Wan-AI/Wan2.1-VACE-1.3B)
* [VACE-14B](https://huggingface.co/Wan-AI/Wan2.1-VACE-14B)
* [Github](https://github.com/ali-vilab/VACE)
* [VACE Project Homepage](https://ali-vilab.github.io/VACE-Page/)

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

## Model Download and Loading in Workflows

Since the workflows covered in this document all use the same workflow template, we can first complete the model download and loading information introduction, then enable/disable different inputs through Bypassing different nodes to achieve different workflows.
The model download information is already embedded in the workflow information in specific examples, so you can also complete the model download when downloading specific example workflows.

### Model Download

**diffusion\_models**
[wan2.1\_vace\_14B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors)
[wan2.1\_vace\_1.3B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_1.3B_fp16.safetensors)

<Tip>
  If you have used Wan Video related workflows before, you have already downloaded the following model files.
</Tip>

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true)

Choose one version from **Text encoders** to download

* [umt5\_xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors?download=true)
* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true)

File save location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └─── wan2.1_vace_14B_fp16.safetensors
│   ├── 📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors # or umt5_xxl_fp16.safetensors
│   └── 📂 vae/
│       └──  wan_2.1_vae.safetensors
```

### Model Loading

Since the models used in the workflows covered in this document are consistent, the workflows are also the same, and only the nodes are bypassed to enable/disable different inputs, please refer to the following image to ensure that the corresponding models are correctly loaded in different workflows.

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d46629d2ee7cfa1b942d4d92217992b1" alt="Wan2.1 VACE Model Loading" data-og-width="2910" width="2910" data-og-height="1394" height="1394" data-path="images/tutorial/video/wan/wan-vace-model-loading.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=91477fcc563509d8b100585ddebac58e 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fc8e48cf61a14dfcefa53557fd607bba 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4c95a9bfd255626b27f53e53ef190f74 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e1541bcd0a68bf62b80881009dc45ce6 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9c721327faf7e078b44f4e22c3c17f80 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a59ba6ef698d23b87b13b21c56dba925 2500w" />

1. Make sure the `Load Diffusion Model` node has loaded `wan2.1_vace_14B_fp16.safetensors`
2. Make sure the `Load CLIP` node has loaded `umt5_xxl_fp8_e4m3fn_scaled.safetensors` or `umt5_xxl_fp16.safetensors`
3. Make sure the `Load VAE` node has loaded `wan_2.1_vae.safetensors`

### How to toggle Node Bypass Status

When a node is set to Bypass status, data passing through the node will not be affected by the node and will be output directly. We often set nodes to Bypass status when we don't need them.
Here are three ways to toggle a node's Bypass status:

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=3a57352f6bc6f1c16ce0792d384d16fd" alt="Toggle Bypass" data-og-width="1830" width="1830" data-og-height="1128" height="1128" data-path="images/interface/nodes/cancel-bypass.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=7d117f2ce9b248c5dfef9a2a60f4e19f 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4aaf480c01ed83648e715bc1db351865 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=672c588fab6405b4abe849298ed662ff 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c1bf919830e35f35c02b847721aeebc7 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=62d75544a82f04cfa7c5861cdeeed1c0 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=27e6b1f470ec9a7e5879b57330d50bee 2500w" />

1. After selecting the node, click the arrow in the indicator section of the selection toolbox to quickly toggle the node's Bypass status
2. After selecting the node, right-click the node and select `Mode` -> `Always` to switch to Always mode
3. After selecting the node, right-click the node and select the `Bypass` option to toggle the Bypass status

## VACE Text-to-Video Workflow

<Tip>
  If you cannot load the workflow from mp4 file, please ensure that your ComfyUI front-end version is up to date version in [requirements.txt](https://github.com/comfyanonymous/ComfyUI/blob/master/requirements.txt) , make sure you can load the workflow from mp4 file.

  Currently 1.19.9 is the latest ComfyUI front-end version in the requirements.txt file.
</Tip>

### 1. Workflow Download

Download the video below and drag it into ComfyUI to load the corresponding workflow

<video controls className="w-full aspect-video" src="https://github.com/Comfy-Org/example_workflows/raw/refs/heads/main/video/wan/vace/vace-t2v.mp4" />

### 2. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6f24e0be5f1ee91ea5becd79501053bd" alt="image" data-og-width="3018" width="3018" data-og-height="1394" height="1394" data-path="images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0cd5b40ceedcf75c9fbde402ce4a14da 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b1f90e2fdac271316123b90a857234f5 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ff5306447eb8ac27b41493f81403e6a7 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=82b65902537bc52e8bec0cd1ab902533 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7ed23e4062bcd3eef1f7fb626e5e963d 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6c2b3687c3865ee1cd442b9adf3c8812 2500w" />

Please follow the numbered steps in the image to ensure smooth workflow execution

1. Enter positive prompts in the `CLIP Text Encode (Positive Prompt)` node
2. Enter negative prompts in the `CLIP Text Encode (Negative Prompt)` node
3. Set the image dimensions (640x640 resolution recommended for first run) and frame count (video duration) in `WanVaceToVideo`
4. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute video generation
5. Once generated, the video will automatically save to `ComfyUI/output/video` directory (subfolder location depends on `save video` node settings)

<Tip>
  During testing with a 4090 GPU:

  * 720x1280 resolution, generating 81 frames takes about 40 minutes
  * 640x640 resolution, generating 49 frames takes about 7 minutes

  However, 720P video quality is better.
</Tip>

## VACE Image-to-Video Workflow

You can continue using the workflow above, just unbypass the `Load image` node in **Load reference image** and input your image. You can also use the image below - in this file we've already set up the corresponding parameters.

### 1. Workflow Download

Download the video below and drag it into ComfyUI to load the corresponding workflow

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/i2v/vace_i2v.mp4" />

Please download the image below as input

![vace-i2v-input](https://github.com/Comfy-Org/example_workflows/raw/refs/heads/main/video/wan/vace/i2v/input.jpg)

### 2. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e22bf953a5900de76c55ed9af3881ea3" alt="Workflow Steps" data-og-width="2912" width="2912" data-og-height="1317" height="1317" data-path="images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7f1807f6dad3f93106ff5ad6329c8f7c 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c09e0a08107d4a6ae30a4a5784c6e652 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b7863d0b4601fa037084d2d008131601 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=531e554960d84d24b2ba6d4facadba50 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ae5cd06c50fc44a1fc4e690c4c3d4821 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7a4bb7922bc8e81b1bc4b5ddc1f3c8e8 2500w" />

Please follow the numbered steps in the image to ensure smooth workflow execution

1. Input the corresponding image in the `Load image` node
2. You can modify and edit prompts like in the text-to-video workflow
3. Set the image dimensions (640x640 resolution recommended for first run) and frame count (video duration) in `WanVaceToVideo`
4. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute video generation
5. Once generated, the video will automatically save to `ComfyUI/output/video` directory (subfolder location depends on `save video` node settings)

<Tip>
  You may want to use nodes like getting image dimensions to set the resolution, but due to width and height step requirements of the corresponding nodes, you may get error messages if your image dimensions are not divisible by 16.
</Tip>

### 3. Additional Workflow Notes

VACE also supports inputting multiple reference images in a single image to generate corresponding videos. You can see related examples on the VACE project [page](https://ali-vilab.github.io/VACE-Page/)

## VACE Video-to-Video Workflow

### 1. Workflow Download

Download the video below and drag it into ComfyUI to load the corresponding workflow

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/vace_v2v.mp4" />

We will use the following materials as input:

1. Input image for reference
   ![v2v-input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/input.jpg)

2. The video below has been preprocessed and will be used to control video generation

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/post+depth.mp4" />

3. The video below is the original video. You can download these materials and use preprocessing nodes like [comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) to preprocess the images

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/original.mp4" />

### 2. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a59e79204a1faf9b3f63c482b65df764" alt="Workflow Steps" data-og-width="2912" width="2912" data-og-height="1317" height="1317" data-path="images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2e445a8b2597f81581dffcb4e122bdaa 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ee5d4773ce441c2ca25e9e738a6affde 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=dbc1798f5324e9a62b5415b61c321364 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=65372a3779b7c267e7c36b1b937a9499 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c68336ae95a110ec9eb9214c8c45b79f 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fb99bc848cb951a0c43388166fec7d77 2500w" />

Please follow the numbered steps in the image to ensure smooth workflow execution

1. Input the reference image in the `Load Image` node under `Load reference image`
2. Input the control video in the `Load Video` node under `Load control video`. Since the provided video is preprocessed, no additional processing is needed
3. If you need to preprocess the original video yourself, you can modify the `Image preprocessing` group or use `comfyui_controlnet_aux` nodes to complete the preprocessing
4. Modify prompts
5. Set the image dimensions (640x640 resolution recommended for first run) and frame count (video duration) in `WanVaceToVideo`
6. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute video generation
7. Once generated, the video will automatically save to `ComfyUI/output/video` directory (subfolder location depends on `save video` node settings)

## VACE Video Outpainting Workflow

\[To be updated]

## VACE First-Last Frame Video Generation

\[To be updated]

To ensure that the first and last frames are effective, the video `length` setting must satisfy that `length-1` is divisible by 4.

The corresponding `Batch_size` setting must satisfy `Batch_size = length - 2`

## Related Node Documentation

Please refer to the documentation below to learn about related nodes

<Card title="WanVaceToVideo Node Documentation" icon="book" href="/built-in-nodes/conditioning/video-models/wan-vace-to-video">
  WanVaceToVideo Node Documentation
</Card>

<Card title="TrimVideoLatent Node Documentation" icon="book" href="/built-in-nodes/latent/video/trim-video-latent">
  ComfyUI TrimVideoLatent Node Documentation
</Card>
