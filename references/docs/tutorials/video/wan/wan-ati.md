> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan ATI ComfyUI Native Workflow Tutorial

> Using trajectory control for video generation.

**ATI (Any Trajectory Instruction)** is a controllable video generation framework proposed by the ByteDance team. ATI is implemented based on Wan2.1 and supports unified control of objects, local regions, and camera motion in videos through arbitrary trajectory instructions.

Project URL: [https://github.com/bytedance/ATI](https://github.com/bytedance/ATI)

## Key Features

* **Unified Motion Control**: Supports trajectory control for multiple motion types including objects, local regions, and camera movements.
* **Interactive Trajectory Editor**: Visual tool that allows users to freely draw and edit motion trajectories on images.
* **Wan2.1 Compatible**: Based on the official Wan2.1 implementation, compatible with environments and model structures.
* **Rich Visualization Tools**: Supports visualization of input trajectories, output videos, and trajectory overlays.

## WAN ATI Trajectory Control Workflow Example

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

### 1. Workflow Download

Download the video below and drag it into ComfyUI to load the corresponding workflow

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/ati/wan_ati.mp4" />

We will use the following image as input:
![v2v-input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/ati/input.jpg)

### 2. Model Download

If you haven't successfully downloaded the model files from the workflow, you can try downloading them manually using the links below

**Diffusion Model**

* [Wan2\_1-I2V-ATI-14B\_fp8\_e4m3fn.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true)

**Text encoders**   Chose one of following model

* [umt5\_xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors?download=true)
* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true)

**clip\_vision**

* [clip\_vision\_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors)

File save location

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   └───Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors # or other version
│   ├───📂 clip_vision/
│   │   └─── clip_vision_h.safetensors
│   └───📂 vae/
│       └──  wan_2.1_vae.safetensors
```

### 3. Complete the workflow execution step by step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=300a2b5bd7002d944e1224e22ed4cd92" alt="Workflow step diagram" data-og-width="3746" width="3746" data-og-height="2924" height="2924" data-path="images/tutorial/video/wan/wan_ati_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c8046adac94511cc1fb4c3f5d0e6b033 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=abcae62b721b60748ae2af6b4f1b1f52 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1b107bdd946e957568fed198a02c35c0 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f08203be22e16cbe402365df10d8963e 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=19745c84e95bc68703f514f5a0303259 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=aa23cb94ca4f9edea4bba0aafdddeb31 2500w" />

Please follow the numbered steps in the image to ensure smooth execution of the corresponding workflow

1. Ensure the `Load Diffusion Model` node has loaded the `Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors` model
2. Ensure the `Load CLIP` node has loaded the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
3. Ensure the `Load VAE` node has loaded the `wan_2.1_vae.safetensors` model
4. Ensure the `Load CLIP Vision` node has loaded the `clip_vision_h.safetensors` model
5. Upload the provided input image in the `Load Image` node
6. Trajectory editing: Currently there is no corresponding trajectory editor in ComfyUI yet, you can use the following link to complete trajectory editing
   * [Online Trajectory Editing Tool](https://comfyui-wiki.github.io/Trajectory-Annotation-Tool/)
7. If you need to modify the prompts (positive and negative), please make changes in the `CLIP Text Encoder` node numbered `5`
8. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation
