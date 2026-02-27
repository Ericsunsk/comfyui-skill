> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Native HiDream-I1 Text-to-Image Workflow Example

> This guide will walk you through completing a ComfyUI native HiDream-I1 text-to-image workflow example

![HiDream-I1 Demo](https://raw.githubusercontent.com/HiDream-ai/HiDream-I1/main/assets/demo.jpg)

HiDream-I1 is a text-to-image model officially open-sourced by HiDream-ai on April 7, 2025. The model has 17B parameters and is released under the [MIT license](https://github.com/HiDream-ai/HiDream-I1/blob/main/LICENSE), supporting personal projects, scientific research, and commercial use.
It currently performs excellently in multiple benchmark tests.

## Model Features

**Hybrid Architecture Design**
A combination of Diffusion Transformer (DiT) and Mixture of Experts (MoE) architecture:

* Based on Diffusion Transformer (DiT), with dual-stream MMDiT modules processing multimodal information and single-stream DiT modules optimizing global consistency.
* Dynamic routing mechanism flexibly allocates computing resources, enhancing complex scene processing capabilities and delivering excellent performance in color restoration, edge processing, and other details.

**Multimodal Text Encoder Integration**
Integrates four text encoders:

* OpenCLIP ViT-bigG, OpenAI CLIP ViT-L (visual semantic alignment)
* T5-XXL (long text parsing)
* Llama-3.1-8B-Instruct (instruction understanding)
  This combination achieves SOTA performance in complex semantic parsing of colors, quantities, spatial relationships, etc., with Chinese prompt support significantly outperforming similar open-source models.

**Original Model Versions**

HiDream-ai provides three versions of the HiDream-I1 model to meet different needs. Below are the links to the original model repositories:

| Model Name      | Description    | Inference Steps | Repository Link                                                         |
| --------------- | -------------- | --------------- | ----------------------------------------------------------------------- |
| HiDream-I1-Full | Full version   | 50              | [🤗 HiDream-I1-Full](https://huggingface.co/HiDream-ai/HiDream-I1-Full) |
| HiDream-I1-Dev  | Distilled dev  | 28              | [🤗 HiDream-I1-Dev](https://huggingface.co/HiDream-ai/HiDream-I1-Dev)   |
| HiDream-I1-Fast | Distilled fast | 16              | [🤗 HiDream-I1-Fast](https://huggingface.co/HiDream-ai/HiDream-I1-Fast) |

## About This Workflow Example

In this example, we will use the repackaged version from ComfyOrg. You can find all the model files we'll use in this example in the [HiDream-I1\_ComfyUI](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/) repository.

<Tip>
  Before starting, please update your ComfyUI version to ensure it's at least after this [commit](https://github.com/comfyanonymous/ComfyUI/commit/9ad792f92706e2179c58b2e5348164acafa69288) to make sure your ComfyUI has native support for HiDream
</Tip>

## HiDream-I1 Workflow

The model requirements for different ComfyUI native HiDream-I1 workflows are basically the same, with only the [diffusion models](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files/diffusion_models) files being different.

If you don't know which version to choose, please refer to the following suggestions:

* **HiDream-I1-Full** can generate the highest quality images
* **HiDream-I1-Dev** balances high-quality image generation with speed
* **HiDream-I1-Fast** can generate images in just 16 steps, suitable for scenarios requiring real-time iteration

For the **dev** and **fast** versions, negative prompts are not needed, so please set the `cfg` parameter to `1.0` during sampling. We have noted the corresponding parameter settings in the relevant workflows.

<Tip>
  The full versions of all three versions require a lot of VRAM - you may need more than 27GB of VRAM to run them smoothly. In the corresponding workflow tutorials,
  we will use the **fp8** version as a demonstration example to ensure that most users can run it smoothly.
  However, we will still provide download links for different versions of the model in the corresponding examples, and you can choose the appropriate file based on your VRAM situation.
</Tip>

### Model Installation

The following model files are common files that we will use.
Please click on the corresponding links to download and save them according to the model file save location.
We will guide you to download the corresponding **diffusion models** in the corresponding workflows.

**text\_encoders**：

* [clip\_l\_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_l_hidream.safetensors)
* [clip\_g\_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_g_hidream.safetensors)
* [t5xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors) This model has been used in many workflows, you may have already downloaded this file.
* [llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/llama_3.1_8b_instruct_fp8_scaled.safetensors)

**VAE**

* [ae.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/vae/ae.safetensors) This is Flux's VAE model, if you have used Flux's workflow before, you may have already downloaded this file.

**diffusion models**
We will guide you to download the corresponding model files in the corresponding workflows.

Model file save location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├─── clip_l_hidream.safetensors
│   │   ├─── clip_g_hidream.safetensors
│   │   ├─── t5xxl_fp8_e4m3fn_scaled.safetensors
│   │   └─── llama_3.1_8b_instruct_fp8_scaled.safetensors
│   └── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 diffusion_models/
│       └── ...               # We will guide you to install in the corresponding version workflow       
```

### HiDream-I1 Full Version Workflow

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=hidream_i1_full&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

#### 1. Model File Download

Please select the appropriate version based on your hardware. Click the link and download the corresponding model file to save it to the `ComfyUI/models/diffusion_models/` folder.

* FP8 version: [hidream\_i1\_full\_fp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_full_fp8.safetensors?download=true) requires more than 16GB of VRAM
* Full version: [hidream\_i1\_full\_f16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_full_fp16.safetensors?download=true) requires more than 27GB of VRAM

#### 2. Workflow File Download

Please download the image below and drag it into ComfyUI to load the corresponding workflow
![HiDream-I1 Full Version Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hidream_i1/hidream_i1_full.png)

#### 3. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=d7cd0444bdb290b4724bf01b80e5b1dd" alt="HiDream-I1 Full Version Flow Diagram" data-og-width="3000" width="3000" data-og-height="1620" height="1620" data-path="images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=57444e4459fbac669797acf7075bd544 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e83e9e59c0847b984af3ad6b178e9494 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=0af3aba1e4b43d3aeadf08304dc004c6 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=b57f0178ad0cf8c1fa5f0490ebfdfcfc 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=fce43e17a4779f1757f9a95948e24858 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6cae50583dbd7b6f091d7e28df1a64e8 2500w" />

Complete the workflow execution step by step

1. Make sure the `Load Diffusion Model` node is using the `hidream_i1_full_fp8.safetensors` file
2. Make sure the four corresponding text encoders in `QuadrupleCLIPLoader` are loaded correctly
   * clip\_l\_hidream.safetensors
   * clip\_g\_hidream.safetensors
   * t5xxl\_fp8\_e4m3fn\_scaled.safetensors
   * llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors
3. Make sure the `Load VAE` node is using the `ae.safetensors` file
4. For the **full** version, you need to set the `shift` parameter in `ModelSamplingSD3` to `3.0`
5. For the `Ksampler` node, you need to make the following settings
   * Set `steps` to `50`
   * Set `cfg` to `5.0`
   * (Optional) Set `sampler` to `lcm`
   * (Optional) Set `scheduler` to `normal`
6. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation

### HiDream-I1 Dev Version Workflow

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=hidream_i1_dev&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

#### 1. Model File Download

Please select the appropriate version based on your hardware, click the link and download the corresponding model file to save to the `ComfyUI/models/diffusion_models/` folder.

* FP8 version: [hidream\_i1\_dev\_fp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_dev_fp8.safetensors?download=true) requires more than 16GB of VRAM
* Full version: [hidream\_i1\_dev\_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_dev_bf16.safetensors?download=true) requires more than 27GB of VRAM

#### 2. Workflow File Download

Please download the image below and drag it into ComfyUI to load the corresponding workflow

![HiDream-I1 Dev Version Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hidream_i1/hidream_i1_dev.png)

#### 3. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ec40487c298368e902ddac3549a23f09" alt="HiDream-I1 Dev Version Flow Diagram" data-og-width="3000" width="3000" data-og-height="1620" height="1620" data-path="images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=60089a16b296f7931777fe5f516c75c5 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c9a5c339380b2cda2c81ffc22c107ce2 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=68a3b8434c000845e1a3d21d60c2c295 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=572ccba5e3ae07b49d4afd76bebfd633 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=83780daf5a04294791d7209439e2eb04 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=19149609d7810003a767599a3845c702 2500w" />
Complete the workflow execution step by step

1. Make sure the `Load Diffusion Model` node is using the `hidream_i1_dev_fp8.safetensors` file
2. Make sure the four corresponding text encoders in `QuadrupleCLIPLoader` are loaded correctly
   * clip\_l\_hidream.safetensors
   * clip\_g\_hidream.safetensors
   * t5xxl\_fp8\_e4m3fn\_scaled.safetensors
   * llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors
3. Make sure the `Load VAE` node is using the `ae.safetensors` file
4. For the **dev** version, you need to set the `shift` parameter in `ModelSamplingSD3` to `6.0`
5. For the `Ksampler` node, you need to make the following settings
   * Set `steps` to `28`
   * (Important) Set `cfg` to `1.0`
   * (Optional) Set `sampler` to `lcm`
   * (Optional) Set `scheduler` to `normal`
6. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation

### HiDream-I1 Fast Version Workflow

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=hidream_i1_fast&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

#### 1. Model File Download

Please select the appropriate version based on your hardware, click the link and download the corresponding model file to save to the `ComfyUI/models/diffusion_models/` folder.

* FP8 version: [hidream\_i1\_fast\_fp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_fast_fp8.safetensors?download=true) requires more than 16GB of VRAM
* Full version: [hidream\_i1\_fast\_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_fast_bf16.safetensors?download=true) requires more than 27GB of VRAM

#### 2. Workflow File Download

Please download the image below and drag it into ComfyUI to load the corresponding workflow

![HiDream-I1 Fast Version Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hidream_i1/hidream_i1_fast.png)

#### 3. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=8969d355742543b20158bbefa4705bfe" alt="HiDream-I1 Fast Version Flow Diagram" data-og-width="3000" width="3000" data-og-height="1620" height="1620" data-path="images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=225090529328f08cae2a900e783a52f7 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=68c6898820435105c79bfbe3cd581f98 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=5029a867eafc2f0dc3ed3ea1947078cd 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=16ac4c99632a3eff8e3c270f5e5ae54c 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=44f8f8b29411aaefc3ce3b903f380abc 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=d49f08328c107693e3d1c6e85e6f9a0d 2500w" />

Complete the workflow execution step by step

1. Make sure the `Load Diffusion Model` node is using the `hidream_i1_fast_fp8.safetensors` file
2. Make sure the four corresponding text encoders in `QuadrupleCLIPLoader` are loaded correctly
   * clip\_l\_hidream.safetensors
   * clip\_g\_hidream.safetensors
   * t5xxl\_fp8\_e4m3fn\_scaled.safetensors
   * llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors
3. Make sure the `Load VAE` node is using the `ae.safetensors` file
4. For the **fast** version, you need to set the `shift` parameter in `ModelSamplingSD3` to `3.0`
5. For the `Ksampler` node, you need to make the following settings
   * Set `steps` to `16`
   * (Important) Set `cfg` to `1.0`
   * (Optional) Set `sampler` to `lcm`
   * (Optional) Set `scheduler` to `normal`
6. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation

## Other Related Resources

### GGUF Version Models

* [HiDream-I1-Full-gguf](https://huggingface.co/city96/HiDream-I1-Full-gguf)
* [HiDream-I1-Dev-gguf](https://huggingface.co/city96/HiDream-I1-Dev-gguf)

You need to use the “Unet Loader (GGUF)” node in City96's [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) to replace the “Load Diffusion Model” node.

### NF4 Version Models

* [HiDream-I1-nf4](https://github.com/hykilpikonna/HiDream-I1-nf4)
* Use the [ComfyUI-HiDream-Sampler](https://github.com/SanDiegoDude/ComfyUI-HiDream-Sampler) node to use the NF4 version model.
