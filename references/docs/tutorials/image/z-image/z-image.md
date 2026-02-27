> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Z-Image ComfyUI Workflow Example

> Z-Image is a 6B parameter efficient image generation foundation model with single-stream diffusion transformer for community-driven fine-tuning and custom development.

**Z-Image (造相)** is a powerful and highly efficient image generation model with **6B** parameters, developed by Alibaba's Tongyi Lab. It uses a **Scalable Single-Stream DiT** (S3-DiT) architecture where text, visual semantic tokens, and image VAE tokens are concatenated at the sequence level to serve as a unified input stream, maximizing parameter efficiency.

Z-Image (Base) is the non-distilled foundation model designed for community-driven fine-tuning and custom development.

**Model Highlights**:

* **Photorealistic Quality**: Delivers strong photorealistic image generation while maintaining excellent aesthetic quality
* **Accurate Bilingual Text Rendering**: Excels at accurately rendering complex Chinese and English text
* **Prompt Enhancing & Reasoning**: Prompt Enhancer empowers the model with reasoning capabilities
* **Fine-tuning Ready**: Ideal base model for custom training and adaptation

**Related Links**:

* [GitHub](https://github.com/Tongyi-MAI/Z-Image)
* [Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image)
* [ModelScope](https://modelscope.cn/models/Tongyi-MAI/Z-Image)

## Z-Image text-to-image workflow

<CardGroup cols={2}>
  <Card title="Download Workflow" icon="download" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_z_image.json">
    Download the Z-Image text-to-image workflow JSON file.
  </Card>

  <Card title="Run on ComfyUI Cloud" icon="cloud" href="https://cloud.comfy.org/?template=image_z_image&utm_source=docs&utm_medium=inhouse_social&utm_campaign=z_image_launch">
    Run this workflow directly on ComfyUI Cloud.
  </Card>
</CardGroup>

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

## Z-Image model downloads

<CardGroup cols={2}>
  <Card title="qwen_3_4b.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors">
    Text encoder for Z-Image.
  </Card>

  <Card title="z_image_bf16.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/z_image/resolve/main/split_files/diffusion_models/z_image_bf16.safetensors">
    Diffusion model for Z-Image.
  </Card>

  <Card title="ae.safetensors" icon="download" href="https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors">
    VAE for Z-Image.
  </Card>
</CardGroup>

**Model Storage Location**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_3_4b.safetensors
│   ├── 📂 diffusion_models/
│   │      └── z_image_bf16.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```
