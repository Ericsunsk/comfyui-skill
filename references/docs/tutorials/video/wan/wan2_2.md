> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan2.2 Video Generation ComfyUI Official Native Workflow Example

> Official usage guide for Alibaba Cloud Tongyi Wanxiang 2.2 video generation model in ComfyUI

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/S45XQXFOutM?si=Qvfco7Cyr_3akZ3Hv" title="ComfyUI Selection Toolbox New Features" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Wan 2.2 is a new generation multimodal generative model launched by WAN AI. This model adopts an innovative MoE (Mixture of Experts) architecture, consisting of high-noise and low-noise expert models. It can divide expert models according to denoising timesteps, thus generating higher quality video content.

Wan 2.2 has three core features: cinematic-level aesthetic control, deeply integrating professional film industry aesthetic standards, supporting multi-dimensional visual control such as lighting, color, and composition; large-scale complex motion, easily restoring various complex motions and enhancing the smoothness and controllability of motion; precise semantic compliance, excelling in complex scenes and multi-object generation, better restoring users' creative intentions.
The model supports multiple generation modes such as text-to-video and image-to-video, suitable for content creation, artistic creation, education and training, and other application scenarios.

[Wan2.2 Prompt Guide](https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y)

## Model Highlights

* **Cinematic-level Aesthetic Control**: Professional camera language, supports multi-dimensional visual control such as lighting, color, and composition
* **Large-scale Complex Motion**: Smoothly restores various complex motions, enhances motion controllability and naturalness
* **Precise Semantic Compliance**: Complex scene understanding, multi-object generation, better restoring creative intentions
* **Efficient Compression Technology**: 5B version with high compression ratio VAE, memory optimization, supports mixed training

## Wan2.2 Open Source Model Versions

The Wan2.2 series models are based on the Apache 2.0 open source license and support commercial use. The Apache 2.0 license allows you to freely use, modify, and distribute these models, including for commercial purposes, as long as you retain the original copyright notice and license text.

| Model Type     | Model Name      | Parameters | Main Function                                                                                                                | Model Repository                                                    |
| -------------- | --------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Hybrid Model   | Wan2.2-TI2V-5B  | 5B         | Hybrid version supporting both text-to-video and image-to-video, a single model meets two core task requirements             | 🤗 [Wan2.2-TI2V-5B](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)   |
| Image-to-Video | Wan2.2-I2V-A14B | 14B        | Converts static images into dynamic videos, maintaining content consistency and smooth dynamic process                       | 🤗 [Wan2.2-I2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B) |
| Text-to-Video  | Wan2.2-T2V-A14B | 14B        | Generates high-quality videos from text descriptions, with cinematic-level aesthetic control and precise semantic compliance | 🤗 [Wan2.2-T2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B) |

## ComfyOrg Wan2.2 Live Streams

For ComfyUI Wan2.2 usage, we have conducted live streams, which you can view to learn how to use them.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/Z0yo16LzReA?si=I-BlUfktxqt9URQk" title="ComfyUI Wan2.2 Live Streams" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/z62QLQ3XqSA?si=yUenvPa9Q4-VX28M" title="ComfyUI Wan2.2 Deep Dive" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/0fyZhXga8P8?si=PMv9xQLP32wP8Ni9" title="ComfyUI Wan2.2 Deep Dive #2" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

This tutorial will use the [🤗 Comfy-Org/Wan\_2.2\_ComfyUI\_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) version.

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

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ccf5d56775dac715ac40f767978d4371" alt="Wan2.2 template" data-og-width="3450" width="3450" data-og-height="1944" height="1944" data-path="images/tutorial/video/wan/wan2_2/template.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3a370d08de0764cc851c0d08de9183a3 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a8eb6733fb6a6bfabafe1722bf428f9c 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=974dda9a8a36e0e56e489d60c8252c1e 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d1ecdc72c324c21a14e3c75260dc6636 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e9298fea453b141f231b98eacda03c8a 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=dae5c8f09553dc9f5e2895c24b4200cf 2500w" />

## Wan2.2 TI2V 5B Hybrid Version Workflow Example

<Tip>
  The Wan2.2 5B version should fit well on 8GB vram with the ComfyUI native offloading.
</Tip>

### 1. Download Workflow File

Please update your ComfyUI to the latest version, and through the menu `Workflow` -> `Browse Templates` -> `Video`, find "Wan2.2 5B video generation" to load the workflow.

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan_2_2_5B_t2v.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_5B_ti2v.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow File</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_5B_ti2v&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

### 2. Manually Download Models

**Diffusion Model**

* [wan2.2\_ti2v\_5B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors)

**VAE**

* [wan2.2\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan2.2_vae.safetensors)

**Text Encoder**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   └───wan2.2_ti2v_5B_fp16.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan2.2_vae.safetensors
```

### 3. Follow the Steps

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=964289dd7f3c51119c95f98372dbd209" alt="Step Diagram" data-og-width="4182" width="4182" data-og-height="2027" height="2027" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=610a2a4f3a050187e58ce0fd61b619be 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=81da2a077caa2ab0fac0a5b7947711dc 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=294f3d3cb6eb69d1e145b5678c0294ad 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3dbca42c849ead6457dad35ce4b640de 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9e8b8ebbe5cb9458449ea202ef0bb518 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=bff729d4a7943a3877a619933770601e 2500w" />

1. Ensure the `Load Diffusion Model` node loads the `wan2.2_ti2v_5B_fp16.safetensors` model.
2. Ensure the `Load CLIP` node loads the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model.
3. Ensure the `Load VAE` node loads the `wan2.2_vae.safetensors` model.
4. (Optional) If you need to perform image-to-video generation, you can use the shortcut Ctrl+B to enable the `Load image` node to upload an image.
5. (Optional) In the `Wan22ImageToVideoLatent` node, you can adjust the size settings and the total number of video frames (`length`).
6. (Optional) If you need to modify the prompts (positive and negative), please do so in the `CLIP Text Encoder` node at step 5.
7. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.

## Wan2.2 14B T2V Text-to-Video Workflow Example

### 1. Workflow File

Please update your ComfyUI to the latest version, and through the menu `Workflow` -> `Browse Templates` -> `Video`, find "Wan2.2 14B T2V" to load the workflow.

Or update your ComfyUI to the latest version, then download the following video and drag it into ComfyUI to load the workflow.

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan_2_2_14B_t2v.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_t2v.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow File</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_14B_t2v&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

### 2. Manually Download Models

**Diffusion Model**

* [wan2.2\_t2v\_high\_noise\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors)
* [wan2.2\_t2v\_low\_noise\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**Text Encoder**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

### 3. Follow the Steps

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0ce44ad0e8f5e8dff6c9324404ee5e46" alt="Step Diagram" data-og-width="4182" width="4182" data-og-height="2255" height="2255" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=36116adfbdba4e7bcb67ad6c9e613387 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3070fc1eb3736451054f1f1336c7b1d6 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9acc8bdb71542b8a4c940eeede74dc68 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2255e183d00f8dbfa3878add257c1436 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fc533adad23782d442693837f3b88b65 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7c240ef2b8046c79384a72e4fb1dd6ef 2500w" />

1. Ensure the first `Load Diffusion Model` node loads the `wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors` model.
2. Ensure the second `Load Diffusion Model` node loads the `wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors` model.
3. Ensure the `Load CLIP` node loads the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model.
4. Ensure the `Load VAE` node loads the `wan_2.1_vae.safetensors` model.
5. (Optional) In the `EmptyHunyuanLatentVideo` node, you can adjust the size settings and the total number of video frames (`length`).
6. (Optional) If you need to modify the prompts (positive and negative), please do so in the `CLIP Text Encoder` node at step 5.
7. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.

## Wan2.2 14B I2V Image-to-Video Workflow Example

### 1. Workflow File

Please update your ComfyUI to the latest version, and through the menu `Workflow` -> `Browse Templates` -> `Video`, find "Wan2.2 14B I2V" to load the workflow.

Or update your ComfyUI to the latest version, then download the following video and drag it into ComfyUI to load the workflow.

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan_2_2_14B_i2v.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_i2v.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow File</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_14B_i2v&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

You can use the following image as input:
![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/input.jpg)

### 2. Manually Download Models

**Diffusion Model**

* [wan2.2\_i2v\_high\_noise\_14B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp16.safetensors)
* [wan2.2\_i2v\_low\_noise\_14B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp16.safetensors)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**Text Encoder**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_i2v_low_noise_14B_fp16.safetensors
│   │   └─── wan2.2_i2v_high_noise_14B_fp16.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

### 3. Follow the Steps

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a9c4c6cfa365f7a0e4d7274b6c799316" alt="Step Diagram" data-og-width="4182" width="4182" data-og-height="2336" height="2336" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=73611770041093ac8431217ffd97ee54 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=96b2ee5717f5a981d9d1143880d7c5fa 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=65141a2c12393339961080a4d94dbb11 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a326793c8feabd5de08c85f6d828269f 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3cc839df08cf7f06bc745de92236981d 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9b3c4bf4352fb753e9878098452bfb39 2500w" />

1. Make sure the first `Load Diffusion Model` node loads the `wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors` model.
2. Make sure the second `Load Diffusion Model` node loads the `wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors` model.
3. Make sure the `Load CLIP` node loads the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model.
4. Make sure the `Load VAE` node loads the `wan_2.1_vae.safetensors` model.
5. In the `Load Image` node, upload the image to be used as the initial frame.
6. If you need to modify the prompts (positive and negative), do so in the `CLIP Text Encoder` node at step 6.
7. (Optional) In `EmptyHunyuanLatentVideo`, you can adjust the size settings and the total number of video frames (`length`).
8. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.

## Wan2.2 14B FLF2V Workflow Example

The first and last frame workflow uses the same model locations as the I2V section.

### 1. Workflow and Input Material Preparation

Download the video or the JSON workflow below and open it in ComfyUI.

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan22_14B_flf2v.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_flf2v.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_14B_flf2v&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

Download the following images as input materials:

![Input Material](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan22_14B_flf2v_start_image.png)
![Input Material](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan22_14B_flf2v_end_image.png)

### 2. Follow the Steps

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6def22f3de024219e66dd4ea7cae7c03" alt="Step Diagram" data-og-width="2091" width="2091" data-og-height="1540" height="1540" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c49a70cd83704dc313144a224d8b384e 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f387777923416ff75fda5318b3dea01f 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=41dc482b545e11b4c666b38b03239b8d 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=789e93dc113653a909d3f01799b50430 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c1844f0c2b70aacf3262350ab824f4af 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ae6a4485c77f8a75a12983129ebe5251 2500w" />

1. Upload the image to be used as the starting frame in the first `Load Image` node.
2. Upload the image to be used as the ending frame in the second `Load Image` node.
3. Adjust the size settings in the `WanFirstLastFrameToVideo` node.
   * By default, a relatively small size is set to prevent low VRAM users from consuming too many resources.
   * If you have enough VRAM, you can try a resolution around 720P.
4. Write appropriate prompts according to your first and last frames.
5. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.

## Community Resources

### GGUF Versions

* [bullerwins/Wan2.2-I2V-A14B-GGUF/](https://huggingface.co/bullerwins/Wan2.2-I2V-A14B-GGUF/)
* [bullerwins/Wan2.2-T2V-A14B-GGUF](https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF)
* [QuantStack/Wan2.2 GGUFs](https://huggingface.co/collections/QuantStack/wan22-ggufs-6887ec891bdea453a35b95f3)

**Custom Node**
[City96/ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)

### WanVideoWrapper

[Kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)

**Wan2.2 models**
[Kijai/WanVideo\_comfy\_fp8\_scaled](https://hf-mirror.com/Kijai/WanVideo_comfy_fp8_scaled)

**Wan2.1 models**
[Kijai/WanVideo\_comfy/Lightx2v](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v)

**Lightx2v 4steps LoRA**

* [Wan2.2-T2V-A14B-4steps-lora-rank64-V1](https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-rank64-V1)
