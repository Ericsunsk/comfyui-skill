> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux.1 Krea Dev ComfyUI Workflow Tutorial

> Best open-source FLUX model developed by Black Forest Labs in collaboration with Krea, focusing on unique aesthetic style and natural details, avoiding AI look, providing exceptional realism and image quality.

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=79640b1911971da78cf2bedb7b3b75ca" alt="Flux.1 Krea Dev Poster" data-og-width="1080" width="1080" data-og-height="1080" height="1080" data-path="images/tutorial/flux/flux_1_krea_dev_poster.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=390f151f239fedcd7a2e146ca35f51da 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f1a852ee1703607ed39688d813bf3e9b 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=308ab9d5ef0e1f83061eb5d74e531671 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b3cbd4470da7891978a4b8f5439c14ef 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ff33d86c5935c09641c4b708e80c5310 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=4554765c9af26d7e9eb85ed813ab3f57 2500w" />

[Flux.1 Krea Dev](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev) is an advanced text-to-image generation model developed in collaboration between Black Forest Labs (BFL) and Krea. This is currently the best open-source FLUX model, specifically designed for text-to-image generation.

**Model Features**

* **Unique Aesthetic Style**: Focuses on generating images with unique aesthetics, avoiding common "AI look" appearance
* **Natural Details**: Does not produce blown-out highlights, maintaining natural detail representatio
* **Exceptional Realism**: Provides outstanding realism and image quality
* **Fully Compatible Architecture**: Fully compatible architecture design with FLUX.1 \[dev]

**Model License**
This model is released under the [flux-1-dev-non-commercial-license](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/blob/main/LICENSE.md)

## Flux.1 Krea Dev ComfyUI Workflow

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

#### 1. Workflow Files

Download the image or JSON below and drag it into ComfyUI to load the corresponding workflow
![Flux Krea Dev Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/krea/flux1_krea_dev.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/flux1_krea_dev.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux1_krea_dev&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

#### 2. Manual Model Installation

Please download the following model files:
**Diffusion model**

* [flux1-krea-dev\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/FLUX.1-Krea-dev_ComfyUI/blob/main/split_files/diffusion_models/flux1-krea-dev_fp8_scaled.safetensors)

If you want to pursue higher quality and have enough VRAM, you can try the original model weights

* [flux1-krea-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/resolve/main/flux1-krea-dev.safetensors)

<Note>
  The `flux1-dev.safetensors` file requires agreeing to the [black-forest-labs/FLUX.1-Krea-dev](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/) agreement before downloading via browser.
</Note>

If you have used Flux related workflows before, the following models are the same and don't need to be downloaded again

**Text encoders**

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) Recommended when your VRAM is greater than 32GB.
* [t5xxl\_fp8\_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors)  For Low VRAM

**VAE**

* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)

File save location:

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └── flux1-krea-dev_fp8_scaled.safetensors or flux1-krea-dev.safetensors
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── t5xxl_fp16.safetensors or t5xxl_fp8_e4m3fn.safetensors
│   ├── vae/
│   │   └── ae.safetensors

```

#### 3. Step-by-step Verification to Ensure Workflow Runs Properly

<Tip>
  For low VRAM users, this model may not run smoothly on your device, you can wait for the community to provide FP8 or GGUF version.
</Tip>

Please refer to the image below to ensure all model files have been loaded correctly

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8475817d518de939bb6c5aabf8c1770e" alt="ComfyUI Flux Krea Dev Workflow" data-og-width="2814" width="2814" data-og-height="1612" height="1612" data-path="images/tutorial/flux/flux_1_krea_dev_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f1cd1077597c59efb7e11a44f9219456 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ea811a58031f7fcd99426c1c0b947a30 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=69fffd2a3c686f40d6566e2a70cb4595 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f7b6f4b5fc50d7b92ea8155e2b8949a8 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7c17e7b576636ce9a86483cc6bcf70e7 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f198e11cc581093f11e1ff1ce37e2d11 2500w" />

1. Ensure that `flux1-krea-dev_fp8_scaled.safetensors` or `flux1-krea-dev.safetensors` is loaded in the `Load Diffusion Model` node
   * `flux1-krea-dev_fp8_scaled.safetensors` is recommended for low VRAM users
   * `flux1-krea-dev.safetensors` is the original weights, if you have enough VRAM like 24GB you can use it for better quality
2. Ensure the following models are loaded in the `DualCLIPLoader` node:
   * clip\_name1: t5xxl\_fp16.safetensors or t5xxl\_fp8\_e4m3fn.safetensors
   * clip\_name2: clip\_l.safetensors
3. Ensure that `ae.safetensors` is loaded in the `Load VAE` node
4. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow
