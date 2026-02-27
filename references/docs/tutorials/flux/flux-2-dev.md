> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Flux.2 Dev Example

> This guide provides a brief introduction to the Flux.2 model and guides you through using the Flux.2 Dev model for text-to-image generation in ComfyUI.

<iframe width="560" height="315" src="https://www.youtube.com/embed/TzTS74Ii23A?si=f2NFmhNbU2VI3PwX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## About FLUX.2

[FLUX.2](https://bfl.ai/blog/flux-2) is a next-generation image model from [Black Forest Labs](https://blackforestlabs.ai/), delivering up to 4MP photorealistic output with far better lighting, skin, fabric, and hand detail. It adds reliable multi-reference consistency (up to 10 images), improved editing precision, better visual understanding, and professional-class text rendering.

**Key Features:**

* **Multi-Reference Consistency:** Reliably maintains identity, product geometry, textures, materials, wardrobe, and composition intent across multiple outputs
* **High-Resolution Photorealism:** Generates images up to 4MP with real-world lighting behavior, spatial reasoning, and physics-aware detail
* **Professional-Grade Control:** Exact pose control, hex-code accurate brand colors, any aspect ratio, and structured prompting for programmatic workflows
* **Usable Text Rendering:** Produces clean, legible text across UI screens, infographics, and multi-language content

**Available Models:**

* **FLUX.2 Dev:** Open-source model (used in this tutorial)
* **FLUX.2 Pro:** API version from Black Forest Labs

<Note>
  We are using quantized weights in this workflow. The original FLUX.2 repository is available [here](https://huggingface.co/black-forest-labs/FLUX.2-dev/).
</Note>

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

## Flux.2 Dev Workflow

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_flux2.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow File</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_flux2&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

## Model links

**text\_encoders**

* [mistral\_3\_small\_flux2\_bf16.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_bf16.safetensors)

**diffusion\_models**

* [flux2\_dev\_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors)

**vae**

* [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors)

**Model Storage Location**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── mistral_3_small_flux2_bf16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── flux2_dev_fp8mixed.safetensors
│   └── 📂 vae/
│          └── flux2-vae.safetensors
```
