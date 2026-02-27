> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Wan2.1 Video Examples

> This guide demonstrates how to generate videos with first and last frames using Wan2.1 Video in ComfyUI

Wan2.1 Video series is a video generation model open-sourced by Alibaba in February 2025 under the [Apache 2.0 license](https://github.com/Wan-Video/Wan2.1?tab=Apache-2.0-1-ov-file).
It offers two versions:

* 14B (14 billion parameters)
* 1.3B (1.3 billion parameters)
  Covering multiple tasks including text-to-video (T2V) and image-to-video (I2V).
  The model not only outperforms existing open-source models in performance but more importantly, its lightweight version requires only 8GB of VRAM to run, significantly lowering the barrier to entry.

<video controls>
  <source src="https://github.com/user-attachments/assets/4aca6063-60bf-4953-bfb7-e265053f49ef" type="video/mp4" />
</video>

* [Wan2.1 Code Repository](https://github.com/Wan-Video/Wan2.1)
* [Wan2.1 Model Repository](https://huggingface.co/Wan-AI)

<UpdateReminder />

## Wan2.1 ComfyUI Native Workflow Examples

<Tip>
  Please update ComfyUI to the latest version before starting the examples to make sure you have native Wan Video support.
</Tip>

## Model Installation

All models mentioned in this guide can be found [here](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files). Below are the common models you'll need for the examples in this guide, which you can download in advance:

Choose one version from **Text encoders** to download:

* [umt5\_xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors?download=true)
* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true)

**CLIP Vision**

* [clip\_vision\_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true)

File storage locations:

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   ├── ...                  # Let's download the models in the corresponding workflow
│   ├── text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   └── vae/
│   │   └──  wan_2.1_vae.safetensors
│   └── clip_vision/
│       └──  clip_vision_h.safetensors   
```

<Note>
  For diffusion models, we'll use the fp16 precision models in this guide because we've found that they perform better than the bf16 versions. If you need other precision versions, please visit [here](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models) to download them.
</Note>

## Wan2.1 Text-to-Video Workflow

Before starting the workflow, please download [wan2.1\_t2v\_1.3B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_t2v_1.3B_fp16.safetensors?download=true) and save it to the `ComfyUI/models/diffusion_models/` directory.

> If you need other t2v precision versions, please visit [here](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models) to download them.

### 1. Workflow File Download

Download the file below and drag it into ComfyUI to load the corresponding workflow:

![Wan2.1 Text-to-Video Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1/wan2.1_t2v_1.3b.webp)

### 2. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=db6d32906ab2db132e6b92fdb0823419" alt="ComfyUI Wan2.1 Workflow Steps" data-og-width="1901" width="1901" data-og-height="1616" height="1616" data-path="images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3d33a53eefadf27c9e21c3eebb0f57a9 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=10062c75bbe505525ccd60ec14e4e2cc 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=94d8226fa2a59cd9f34ada362cb4505c 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7e82be47f4a146000679fd6d09a6cdf0 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4bbd7285318b9e280ae5c655f81b7579 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=8e08f01a0de9f723a0d074e93768a65d 2500w" />

1. Make sure the `Load Diffusion Model` node has loaded the `wan2.1_t2v_1.3B_fp16.safetensors` model
2. Make sure the `Load CLIP` node has loaded the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
3. Make sure the `Load VAE` node has loaded the `wan_2.1_vae.safetensors` model
4. (Optional) You can modify the video dimensions in the `EmptyHunyuanLatentVideo` node if needed
5. (Optional) If you need to modify the prompts (positive and negative), make changes in the `CLIP Text Encoder` node at number `5`
6. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the video generation

## Wan2.1 Image-to-Video Workflow

**Since Wan Video separates the 480P and 720P models**, we'll need to provide examples for both resolutions in this guide. In addition to using different models, they also have slight parameter differences.

### 480P Version

#### 1. Workflow and Input Image

Download the image below and drag it into ComfyUI to load the corresponding workflow:
![Wan2.1 Image-to-Video Workflow 14B 480P Workflow Example Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1/wan2.1_i2v_14b_480P.webp)

We'll use the following image as input:

![Wan2.1 Image-to-Video Workflow 14B 480P Workflow Example Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1/input/flux_dev_example.png)

#### 2. Model Download

Please download [wan2.1\_i2v\_480p\_14B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_i2v_480p_14B_fp16.safetensors?download=true) and save it to the `ComfyUI/models/diffusion_models/` directory.

#### 3. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=91de28e61a2633cf39b3a52afc2a6459" alt="ComfyUI Wan2.1 Workflow Steps" data-og-width="2318" width="2318" data-og-height="1616" height="1616" data-path="images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e42c99bf5719d85818e6099fac6193b7 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7fd87c3dcdfee4208d08491a1697f2e5 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4f97468699aa3f27a2ab7be260929c58 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=8beddee89d2a19e281b4dc234af0503d 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=97ed81e85ee272d45b89ae54ee6b0e18 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6801f558dfa4f00f5c8d4e2f2e424fd4 2500w" />

1. Make sure the `Load Diffusion Model` node has loaded the `wan2.1_i2v_480p_14B_fp16.safetensors` model
2. Make sure the `Load CLIP` node has loaded the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
3. Make sure the `Load VAE` node has loaded the `wan_2.1_vae.safetensors` model
4. Make sure the `Load CLIP Vision` node has loaded the `clip_vision_h.safetensors` model
5. Upload the provided input image in the `Load Image` node
6. (Optional) Enter the video description content you want to generate in the `CLIP Text Encoder` node
7. (Optional) You can modify the video dimensions in the `WanImageToVideo` node if needed
8. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the video generation

### 720P Version

#### 1. Workflow and Input Image

Download the image below and drag it into ComfyUI to load the corresponding workflow:
![Wan2.1 Image-to-Video Workflow 14B 720P Workflow Example Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1/wan2.1_i2v_14b_720P.webp)

We'll use the following image as input:

![Wan2.1 Image-to-Video Workflow 14B 720P Workflow Example Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1/input/magician.png)

#### 2. Model Download

Please download [wan2.1\_i2v\_720p\_14B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_i2v_720p_14B_fp16.safetensors?download=true) and save it to the `ComfyUI/models/diffusion_models/` directory.

#### 3. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c99af487f3164515ac1ffaf94f0add71" alt="ComfyUI Wan2.1 Workflow Steps" data-og-width="2318" width="2318" data-og-height="1548" height="1548" data-path="images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=412fe69cc3d3e3b86ad4bb5344a3df26 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f5fef8f2d5234b2bd81dd9e84c36b36c 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=025653767f20665e0a01e2c74d325836 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c1ad2a584a20d6a68057edbc30337b6f 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=32d21160c3af6618e6c67ca2fe0f6308 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0fe836f7c7f9de6d13562379d4178171 2500w" />

1. Make sure the `Load Diffusion Model` node has loaded the `wan2.1_i2v_720p_14B_fp16.safetensors` model
2. Make sure the `Load CLIP` node has loaded the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
3. Make sure the `Load VAE` node has loaded the `wan_2.1_vae.safetensors` model
4. Make sure the `Load CLIP Vision` node has loaded the `clip_vision_h.safetensors` model
5. Upload the provided input image in the `Load Image` node
6. (Optional) Enter the video description content you want to generate in the `CLIP Text Encoder` node
7. (Optional) You can modify the video dimensions in the `WanImageToVideo` node if needed
8. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the video generation
