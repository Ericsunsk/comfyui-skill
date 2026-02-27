> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen-Image-2512 ComfyUI Native Workflow Example

> Qwen-Image-2512 is the December update of Qwen-Image's text-to-image foundational model, featuring enhanced human realism, finer natural detail, and improved text rendering.

**Qwen-Image-2512** is the December update of Qwen-Image's text-to-image foundational model. Compared to the base Qwen-Image model released in August, Qwen-Image-2512 features significant improvements in image quality and realism.

**Key Enhancements in Qwen-Image-2512**:

* **Enhanced Human Realism**: Significantly reduces the "AI-generated" look and substantially enhances overall image realism, especially for human subjects
* **Finer Natural Detail**: Delivers notably more detailed rendering of landscapes, animal fur, and other natural elements
* **Improved Text Rendering**: Improves the accuracy and quality of textual elements, achieving better layout and more faithful multimodal (text + image) composition

**Official Links**:

* [GitHub Repository](https://github.com/QwenLM/Qwen-Image)
* [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-2512)
* [ModelScope](https://modelscope.cn/models/Qwen/Qwen-Image-2512)
* [Tech Report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf)
* [Blog](https://qwen.ai/blog?id=qwen-image-2512)

## Supported Aspect Ratios

| Aspect Ratio | Resolution |
| ------------ | ---------- |
| 1:1          | 1328x1328  |
| 16:9         | 1664x928   |
| 9:16         | 928x1664   |
| 4:3          | 1472x1104  |
| 3:4          | 1104x1472  |
| 3:2          | 1584x1056  |
| 2:3          | 1056x1584  |

## Qwen-Image-2512 ComfyUI Native Workflow Example

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

<a href="https://cloud.comfy.org/?template=image_qwen_Image_2512&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#7c3aed', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginBottom: '1rem'}}>
  Run on Comfy Cloud
</a>

### 1. Workflow file

After updating ComfyUI, you can find the workflow file from the templates, or drag the workflow below into ComfyUI to load it.

The workflow includes two subgraphs:

* **Text to Image (Qwen-Image 2512)**: Standard 50-step generation
* **Text to Image (Qwen-Image 2512 4steps)**: Accelerated 4-step generation using Lightning LoRA

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_Image_2512.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow</p>
</a>

### 2. Model download

**Text Encoders**

* [qwen\_2.5\_vl\_7b\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**LoRA (Optional - for 4-step Lightning acceleration)**

* [Qwen-Image-Lightning-4steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors)

**Diffusion Models**

* [qwen\_image\_2512\_fp8\_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) (Recommended for most users)
* [qwen\_image\_2512\_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_bf16.safetensors) (If you have enough VRAM and want better quality)

**VAE**

* [qwen\_image\_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors)

**Model Storage Location**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 loras/
│   │      └── Qwen-Image-Lightning-4steps-V1.0.safetensors
│   ├── 📂 diffusion_models/
│   │      ├── qwen_image_2512_bf16.safetensors
│   │      └── qwen_image_2512_fp8_e4m3fn.safetensors
│   └── 📂 vae/
│          └── qwen_image_vae.safetensors
```
