> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Hunyuan Video Examples

> This guide shows how to use Hunyuan Text-to-Video and Image-to-Video workflows in ComfyUI

<video controls className="w-full aspect-video" src="https://github.com/user-attachments/assets/442afb73-3092-454f-bc46-02361c285930" />

Hunyuan Video series is developed and open-sourced by [Tencent](https://huggingface.co/tencent), featuring a hybrid architecture that supports both [Text-to-Video](https://github.com/Tencent/HunyuanVideo) and [Image-to-Video](https://github.com/Tencent/HunyuanVideo-I2V) generation with a parameter scale of 13B.

Technical features:

* **Core Architecture:** Uses a DiT (Diffusion Transformer) architecture similar to Sora, effectively fusing text, image, and motion information to improve consistency, quality, and alignment between generated video frames. A unified full-attention mechanism enables multi-view camera transitions while ensuring subject consistency.
* **3D VAE:** The custom 3D VAE compresses videos into a compact latent space, making image-to-video generation more efficient.
* **Superior Image-Video-Text Alignment:** Utilizing MLLM text encoders that excel in both image and video generation, better following text instructions, capturing details, and performing complex reasoning.

You can learn more through the official repositories: [Hunyuan Video](https://github.com/Tencent/HunyuanVideo) and [Hunyuan Video-I2V](https://github.com/Tencent/HunyuanVideo-I2V).

This guide will walk you through setting up both **Text-to-Video** and **Image-to-Video** workflows in ComfyUI.

<Tip>
  The workflow images in this tutorial contain metadata with model download information.

  Simply drag them into ComfyUI or use the menu `Workflows` -> `Open (ctrl+o)` to load the corresponding workflow, which will prompt you to download the required models.

  Alternatively, this guide provides direct model links if automatic downloads fail or you are not using the Desktop version. All models are available [here](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files) for download.
</Tip>

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

## Common Models for All Workflows

The following models are used in both Text-to-Video and Image-to-Video workflows. Please download and save them to the specified directories:

* [clip\_l.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/text_encoders/clip_l.safetensors?download=true)
* [llava\_llama3\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/text_encoders/llava_llama3_fp8_scaled.safetensors?download=true)
* [hunyuan\_video\_vae\_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/vae/hunyuan_video_vae_bf16.safetensors?download=true)

Storage location:

```
ComfyUI/
├── models/
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── llava_llama3_fp8_scaled.safetensors
│   ├── vae/
│   │   └── hunyuan_video_vae_bf16.safetensors
```

## Hunyuan Text-to-Video Workflow

Hunyuan Text-to-Video was open-sourced in December 2024, supporting 5-second short video generation through natural language descriptions in both Chinese and English.

### 1. Workflow

Download the image below and drag it into ComfyUI to load the workflow:
![ComfyUI Workflow - Hunyuan Text-to-Video](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/t2v/kitchen.webp)

### 2. Manual Models Installation

Download [hunyuan\_video\_t2v\_720p\_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/diffusion_models/hunyuan_video_t2v_720p_bf16.safetensors?download=true) and save it to the `ComfyUI/models/diffusion_models` folder.

Ensure you have all these model files in the correct locations:

```
ComfyUI/
├── models/
│   ├── text_encoders/
│   │   ├── clip_l.safetensors                       // Shared model
│   │   └── llava_llama3_fp8_scaled.safetensors      // Shared model
│   ├── vae/
│   │   └── hunyuan_video_vae_bf16.safetensors       // Shared model
│   └── diffusion_models/
│       └── hunyuan_video_t2v_720p_bf16.safetensors  // T2V model
```

### 3. Steps to Run the Workflow

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8cf9db23e82c1c31702966878d7d6326" alt="ComfyUI Hunyuan Video T2V Workflow" data-og-width="4004" width="4004" data-og-height="1810" height="1810" data-path="images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=46ecaef5c813cfe73e61b8f9f4cdbe6b 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5d87f06e2721307cf44973080a3cc4c1 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=351426c249545789f7fddcd6bfdbd545 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5f7c8c5315be22ad33d24525c7ea75af 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=121b5d422c627eb576f607141c91084c 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7c1054fb6ba08ec4b3f388ecbd1292c2 2500w" />

1. Ensure the `DualCLIPLoader` node has loaded these models:
   * clip\_name1: clip\_l.safetensors
   * clip\_name2: llava\_llama3\_fp8\_scaled.safetensors
2. Ensure the `Load Diffusion Model` node has loaded `hunyuan_video_t2v_720p_bf16.safetensors`
3. Ensure the `Load VAE` node has loaded `hunyuan_video_vae_bf16.safetensors`
4. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

<Tip>
  When the `length` parameter in the `EmptyHunyuanLatentVideo` node is set to 1, the model can generate a static image.
</Tip>

## Hunyuan Image-to-Video Workflow

Hunyuan Image-to-Video model was open-sourced on March 6, 2025, based on the HunyuanVideo framework. It transforms static images into smooth, high-quality videos and also provides LoRA training code to customize special video effects like hair growth, object transformation, etc.

Currently, the Hunyuan Image-to-Video model has two versions:

* v1 "concat": Better motion fluidity but less adherence to the image guidance
* v2 "replace": Updated the day after v1, with better image guidance but seemingly less dynamic compared to v1

<div class="flex justify-between">
  <div class="text-center">
    <p>v1 "concat"</p>

    <img src="https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video.webp" alt="HunyuanVideo v1" />
  </div>

  <div class="text-center">
    <p>v2 "replace"</p>

    <img src="https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video_v2.webp" alt="HunyuanVideo v2" />
  </div>
</div>

### Shared Model for v1 and v2 Versions

Download the following file and save it to the `ComfyUI/models/clip_vision` directory:

* [llava\_llama3\_vision.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/clip_vision/llava_llama3_vision.safetensors?download=true)

### V1 "concat" Image-to-Video Workflow

#### 1. Workflow and Asset

Download the workflow image below and drag it into ComfyUI to load the workflow:
![ComfyUI Workflow - Hunyuan Image-to-Video v1](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v1_robot.webp)

Download the image below, which we'll use as the starting frame for the image-to-video generation:
![Starting Frame](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/hunyuan-video/i2v/robot-ballet.png)

#### 2. Related models manual installation

* [hunyuan\_video\_image\_to\_video\_720p\_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/diffusion_models/hunyuan_video_image_to_video_720p_bf16.safetensors?download=true)

Ensure you have all these model files in the correct locations:

```
ComfyUI/
├── models/
│   ├── clip_vision/
│   │   └── llava_llama3_vision.safetensors                     // I2V shared model
│   ├── text_encoders/
│   │   ├── clip_l.safetensors                                  // Shared model
│   │   └── llava_llama3_fp8_scaled.safetensors                 // Shared model
│   ├── vae/
│   │   └── hunyuan_video_vae_bf16.safetensors                  // Shared model
│   └── diffusion_models/
│       └── hunyuan_video_image_to_video_720p_bf16.safetensors  // I2V v1 "concat" version model
```

#### 3. Steps to Run the Workflow

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66d1fd271cc2a45a4fbcd92850074912" alt="ComfyUI Hunyuan Video I2V v1 Workflow" data-og-width="4604" width="4604" data-og-height="1780" height="1780" data-path="images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c69870b0963cf8328ef655ada46aff2e 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b8445274ec2b9c64952eca5d43d80afd 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7d2f125a2e28660e4fe97dca2c223951 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=91eab50c724944dc6cf09f2213360ea4 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6aacdffc0aa5c73dc82ca3857f89761b 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=080cb021fdef78a1b6dbbf5538f4a2fc 2500w" />

1. Ensure that `DualCLIPLoader` has loaded these models:
   * clip\_name1: clip\_l.safetensors
   * clip\_name2: llava\_llama3\_fp8\_scaled.safetensors
2. Ensure that `Load CLIP Vision` has loaded `llava_llama3_vision.safetensors`
3. Ensure that `Load Image Model` has loaded `hunyuan_video_image_to_video_720p_bf16.safetensors`
4. Ensure that `Load VAE` has loaded `vae_name: hunyuan_video_vae_bf16.safetensors`
5. Ensure that `Load Diffusion Model` has loaded `hunyuan_video_image_to_video_720p_bf16.safetensors`
6. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

### v2 "replace" Image-to-Video Workflow

The v2 workflow is essentially the same as the v1 workflow. You just need to download the **replace** model and use it in the `Load Diffusion Model` node.

#### 1. Workflow and Asset

Download the workflow image below and drag it into ComfyUI to load the workflow:
![ComfyUI Workflow - Hunyuan Image-to-Video v2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v2_fennec_gril.webp)

Download the image below, which we'll use as the starting frame for the image-to-video generation:
![Starting Frame](https://comfyanonymous.github.io/ComfyUI_examples/flux/flux_dev_example.png)

#### 2. Related models manual installation

* [hunyuan\_video\_v2\_replace\_image\_to\_video\_720p\_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/diffusion_models/hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors?download=true)

Ensure you have all these model files in the correct locations:

```
ComfyUI/
├── models/
│   ├── clip_vision/
│   │   └── llava_llama3_vision.safetensors                                // I2V shared model
│   ├── text_encoders/
│   │   ├── clip_l.safetensors                                             // Shared model
│   │   └── llava_llama3_fp8_scaled.safetensors                            // Shared model
│   ├── vae/
│   │   └── hunyuan_video_vae_bf16.safetensors                             // Shared model
│   └── diffusion_models/
│       └── hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors  // V2 "replace" version model
```

#### 3. Steps to Run the Workflow

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f26ddd8edc837fbf9d2bb4f6459a82ee" alt="ComfyUI Hunyuan Video I2V v2 Workflow" data-og-width="4604" width="4604" data-og-height="1780" height="1780" data-path="images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d8baea25dfcaf7566c43eee90ddf30e2 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=095646b3588b08ac62943b23d4a4a381 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c4fb1b7af59a8236189b723f182384c0 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=41e6f324ab148f773a1fbf7a68d1eecc 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a428533a8b26e8a34f7cdc240d60a0c3 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c4af9cc4415d6b5c355bae31a57488ae 2500w" />

1. Ensure the `DualCLIPLoader` node has loaded these models:
   * clip\_name1: clip\_l.safetensors
   * clip\_name2: llava\_llama3\_fp8\_scaled.safetensors
2. Ensure the `Load CLIP Vision` node has loaded `llava_llama3_vision.safetensors`
3. Ensure the `Load Image Model` node has loaded `hunyuan_video_image_to_video_720p_bf16.safetensors`
4. Ensure the `Load VAE` node has loaded `hunyuan_video_vae_bf16.safetensors`
5. Ensure the `Load Diffusion Model` node has loaded `hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors`
6. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

## Try it yourself

Here are some images and prompts we provide. Based on that content or make an adjustment to create your own video.

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=16d6b0ea15e14c74e8d2e5bfacfe4bf8" alt="example" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=fb99a02e45e6c7f270d9ce083790314c 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d9a4f1f52d7215e48a374391428822af 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9e906c0b832af401f05c4cc052dc8fcf 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c8da46339d87ae93596c5e61bd5ec0c3 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=19badecb5287b9aa7230d6e5610f5d09 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d4a1c639e320e34572b495821a1a9408 2500w" />

```
Futuristic robot dancing ballet, dynamic motion, fast motion, fast shot, moving scene
```

***

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f8a76a691a7a9ebda088941350538375" alt="example" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/advanced/hunyuanvideo/samurai.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8a06ce9e5abc61680c56b8f50d351b51 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=69324963fb61e59c1228c1bc8e74e230 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=23bd95f28cf382d0653eabb11f7db077 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=87ce3e4a1a8df22d48cdec2b10c27fdb 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ba0bedcdaa6d746d03cea491e9ecd1db 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=766950cfbd96fde9037be7605cf3674e 2500w" />

```
Samurai waving sword and hitting the camera. camera angle movement, zoom in, fast scene, super fast, dynamic
```

***

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=aa2ce4f30c4d367170a8a696e62a7c7e" alt="example" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/advanced/hunyuanvideo/a_flying_car.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6a8b34642f416da105998b377bde9dc8 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=25f4eb4f74901534255e2b0bf552c218 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=f68ad26ec9cef9228518da359e75acb8 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=321b298270f365989f9ff1b39d8f9b97 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=58b7c90be2e12ad056058c47720e5fbe 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e3d9e0536bdf426014c8f8a27de20065 2500w" />

```
flying car fastly moving and flying through the city
```

***

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=875b086bd33ac131bda4fe6c718b9bc7" alt="example" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/advanced/hunyuanvideo/cyber_car_race.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ba4b75e9f735ba0cc5f136bec09360f9 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c4a722a42e56ba171385fc7a78893227 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=4a04c0664b3e5bb3d6441243e5a7802c 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=eab9135cbe99a2b42a3bf29cc901736a 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=2a2173570ea181e0711e6984dd13e3c8 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ea36cb8fda2435a47eec887bb130d6d8 2500w" />

```
cyberpunk car race in night city, dynamic, super fast, fast shot
```
