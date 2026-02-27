> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Wan2.2 Fun Inp Start-End Frame Video Generation Example

> This article introduces how to use ComfyUI to complete the Wan2.2 Fun Inp start-end frame video generation example

**Wan2.2-Fun-Inp** is a start-end frame controlled video generation model launched by Alibaba PAI team. It supports inputting **start and end frame images** to generate intermediate transition videos, providing creators with greater creative control. The model is released under the **Apache 2.0 license** and supports commercial use.

**Key Features**:

* **Start-End Frame Control**: Supports inputting start and end frame images to generate intermediate transition videos, enhancing video coherence and creative freedom
* **High-Quality Video Generation**: Based on the Wan2.2 architecture, outputs film-level quality videos
* **Multi-Resolution Support**: Supports generating videos at 512×512, 768×768, 1024×1024 and other resolutions to suit different scenarios

**Model Version**:

* **14B High-Performance Version**: Model size exceeds 32GB, with better results but requires high VRAM

Below are the relevant model weights and code repositories:

* [🤗Wan2.2-Fun-Inp-14B](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP)
* Code repository: [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun)

## ComfyOrg Wan2.2 Fun InP & Control Youtube Live Stream Replay

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/YcAerNYIvho?si=Zh8tzRwI_OTAFx3m" title="ComfyUI Selection Toolbox New Features" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Wan2.2 Fun Inp Start-End Frame Video Generation Workflow Example

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

This workflow provides two versions:

1. A version using [Wan2.2-Lightning](https://huggingface.co/lightx2v/Wan2.2-Lightning) 4-step LoRA from lightx2v for accelerated video generation
2. A fp8\_scaled version without acceleration LoRA

Below are the test results using an RTX4090D 24GB VRAM GPU at 640×640 resolution with 81 frames

| Model Type                | VRAM Usage | First Generation Time | Second Generation Time |
| ------------------------- | ---------- | --------------------- | ---------------------- |
| fp8\_scaled               | 83%        | ≈ 524s                | ≈ 520s                 |
| fp8\_scaled + 4-step LoRA | 89%        | ≈ 138s                | ≈ 79s                  |

Since the acceleration with LoRA is significant but the video dynamic is lost,  the provided workflows enable the accelerated LoRA version by default. If you want to enable the other workflow, select it and use **Ctrl+B** to activate.

### 1. Download Workflow File

Please update your ComfyUI to the latest version, and find "**Wan2.2 Fun Inp**" under the menu `Workflow` -> `Browse Templates` -> `Video` to load the workflow.

Or, after updating ComfyUI to the latest version, download the workflow below and drag it into ComfyUI to load.

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_animate.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_14B_fun_inpaint&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

Use the following materials as the start and end frames

![Wan2.2 Fun Control ComfyUI Workflow Start Frame Material](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_inp/start_image.png)
![Wan2.2 Fun Control ComfyUI Workflow End Frame Material](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_inp/end_image.png)

### 2. Models

**Diffusion Model**

* [wan2.2\_fun\_inpaint\_high\_noise\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_inpaint_high_noise_14B_fp8_scaled.safetensors)
* [wan2.2\_fun\_inpaint\_low\_noise\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_inpaint_low_noise_14B_fp8_scaled.safetensors)

**Lightning LoRA (Optional, for acceleration)**

* [wan2.2\_i2v\_lightx2v\_4steps\_lora\_v1\_high\_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors)
* [wan2.2\_i2v\_lightx2v\_4steps\_lora\_v1\_low\_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**Text Encoder**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_fun_inpaint_high_noise_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_fun_inpaint_low_noise_14B_fp8_scaled.safetensors
│   ├───📂 loras/
│   │   ├─── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
│   │   └─── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

### 3. Workflow Guide

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3d87de35d3eaa2f9599c35e9963c6c18" alt="Workflow Step Image" data-og-width="4182" width="4182" data-og-height="2048" height="2048" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=595d1eedd8f8e7dabb57e67b8e08c818 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3b61565f90b622b60617fa5ae68d5ab6 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=67aeb504b9f7d07edead943a7e3ef955 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=75c98443817fdd4732c5bffee6d7a030 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=737315a4d31d70f14414243e982f6a67 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7c038f0c1ba94de7333fd79ebaa03bb2 2500w" />

<Note>
  This workflow uses LoRA. Please make sure the corresponding Diffusion model and LoRA are matched.
</Note>

1. **High noise** model and **LoRA** loading
   * Ensure the `Load Diffusion Model` node loads the `wan2.2_fun_inpaint_high_noise_14B_fp8_scaled.safetensors` model
   * Ensure the `LoraLoaderModelOnly` node loads the `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors`
2. **Low noise** model and **LoRA** loading
   * Ensure the `Load Diffusion Model` node loads the `wan2.2_fun_inpaint_low_noise_14B_fp8_scaled.safetensors` model
   * Ensure the `LoraLoaderModelOnly` node loads the `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors`
3. Ensure the `Load CLIP` node loads the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
4. Ensure the `Load VAE` node loads the `wan_2.1_vae.safetensors` model
5. Upload the start and end frame images as materials
6. Enter your prompt in the Prompt group
7. Adjust the size and video length in the `WanFunInpaintToVideo` node
   * Adjust the `width` and `height` parameters. The default is `640`. We set a smaller size, but you can modify it as needed.
   * Adjust the `length`, which is the total number of frames. The current workflow fps is 16. For example, if you want to generate a 5-second video, you should set it to 5\*16 = 80.
8. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation
