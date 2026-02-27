> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI OmniGen2 Native Workflow Examples

> ComfyUI OmniGen2 Native Workflow Examples - Unified text-to-image, image editing, and multi-image composition model.

## About OmniGen2

OmniGen2 is a powerful and efficient unified multimodal generation model with approximately **7B** total parameters (3B text model + 4B image generation model). Unlike OmniGen v1, OmniGen2 adopts an innovative dual-path Transformer architecture with completely independent text autoregressive model and image diffusion model, achieving parameter decoupling and specialized optimization.

### Model Highlights

* **Visual Understanding**: Inherits the powerful image content interpretation and analysis capabilities of the Qwen-VL-2.5 foundation model
* **Text-to-Image Generation**: Creates high-fidelity and aesthetically pleasing images from text prompts
* **Instruction-guided Image Editing**: Performs complex, instruction-based image modifications, achieving state-of-the-art performance among open-source models
* **Contextual Generation**: Versatile capabilities to process and flexibly combine diverse inputs (including people, reference objects, and scenes), producing novel and coherent visual outputs

### Technical Features

* **Dual-path Architecture**: Based on Qwen 2.5 VL (3B) text encoder + independent diffusion Transformer (4B)
* **Omni-RoPE Position Encoding**: Supports multi-image spatial positioning and identity distinction
* **Parameter Decoupling Design**: Avoids negative impact of text generation on image quality
* Support for complex text understanding and image understanding
* Controllable image generation and editing
* Excellent detail preservation capabilities
* Unified architecture supporting multiple image generation tasks
* Text generation capability: Can generate clear text content within images

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

## OmniGen2 Model Download

Since this article involves different workflows, the corresponding model files and installation locations are as follows. The download information for model files is also included in the corresponding workflows:

**Diffusion Models**

* [omnigen2\_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/omnigen2_fp16.safetensors)

**VAE**

* [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors)

**Text Encoders**

* [qwen\_2.5\_vl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_fp16.safetensors)

File save location:

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── omnigen2_fp16.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_fp16.safetensors
```

## ComfyUI OmniGen2 Text-to-Image Workflow

### 1. Download Workflow File

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_omnigen2_t2i&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

![Text-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/omnigen2/image_omnigen2_t2i.png)

### 2. Complete Workflow Step by Step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0811f0f5d6dbe974749752b85fa7e3b9" alt="Workflow Step Guide" data-og-width="4148" width="4148" data-og-height="1576" height="1576" data-path="images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=45ad3f6862e902ee370dae6e6c73a6f8 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=740f03d026f930d75bee360164fc5dac 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=102c411e373d18a82c28e4862bd8c1cd 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ae539c85f4bc00c0a4b637f6e6fddf83 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2ab1b75cafc02f71855e7719baaafd9f 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0b2037bfacdd554dc19b67fa276dd876 2500w" />

Please follow the numbered steps in the image for step-by-step confirmation to ensure smooth operation of the corresponding workflow:

1. **Load Main Model**: Ensure the `Load Diffusion Model` node loads `omnigen2_fp16.safetensors`
2. **Load Text Encoder**: Ensure the `Load CLIP` node loads `qwen_2.5_vl_fp16.safetensors`
3. **Load VAE**: Ensure the `Load VAE` node loads `ae.safetensors`
4. **Set Image Dimensions**: Set the generated image dimensions in the `EmptySD3LatentImage` node (recommended 1024x1024)
5. **Input Prompts**:
   * Input positive prompts in the first `CLipTextEncode` node (content you want to appear in the image)
   * Input negative prompts in the second `CLipTextEncode` node (content you don't want to appear in the image)
6. **Start Generation**: Click the `Queue Prompt` button, or use the shortcut `Ctrl(cmd) + Enter` to execute text-to-image generation
7. **View Results**: After generation is complete, the corresponding images will be automatically saved to the `ComfyUI/output/` directory, and you can also preview them in the `SaveImage` node

## ComfyUI OmniGen2 Image Editing Workflow

OmniGen2 has rich image editing capabilities and supports adding text to images

### 1. Download Workflow File

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_omnigen2_image_edit&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

![Text-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/omnigen2/image_omnigen2_image_edit.png)

Download the image below, which we will use as the input image.
![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/image/omnigen2/input_fairy.png)

### 2. Complete Workflow Step by Step

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=09899794b2d041a8c0e0775da557684a" alt="Workflow Step Guide" data-og-width="4056" width="4056" data-og-height="2808" height="2808" data-path="images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6f080c727c50b8152d8b00e92447cb29 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9daf1f956e69bc958427639852c9d1f2 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=abfae5034a336d261b872d0cd18d9b8e 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5a1e3dc977d640a6c15beedcdad9991b 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9a9e59aa4a1b0ade064ad613d8428abf 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2cd7842cc0b4bb00b2416a257fffa06d 2500w" />

1. **Load Main Model**: Ensure the `Load Diffusion Model` node loads `omnigen2_fp16.safetensors`
2. **Load Text Encoder**: Ensure the `Load CLIP` node loads `qwen_2.5_vl_fp16.safetensors`
3. **Load VAE**: Ensure the `Load VAE` node loads `ae.safetensors`
4. **Upload Image**: Upload the provided image in the `Load Image` node
5. **Input Prompts**:
   * Input positive prompts in the first `CLipTextEncode` node (content you want to appear in the image)
   * Input negative prompts in the second `CLipTextEncode` node (content you don't want to appear in the image)
6. **Start Generation**: Click the `Queue Prompt` button, or use the shortcut `Ctrl(cmd) + Enter` to execute text-to-image generation
7. **View Results**: After generation is complete, the corresponding images will be automatically saved to the `ComfyUI/output/` directory, and you can also preview them in the `SaveImage` node

### 3. Additional Workflow Instructions

* If you want to enable the second image input, you can use the shortcut **Ctrl + B** to enable the corresponding node inputs for nodes that are in pink/purple state in the workflow
* If you want to customize dimensions, you can delete the `Get image size` node linked to the `EmptySD3LatentImage` node and input custom dimensions
