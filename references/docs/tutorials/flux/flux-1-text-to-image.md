> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Flux.1 Text-to-Image Workflow Example

> This guide provides a brief introduction to the Flux.1 model and guides you through using the Flux.1 model for text-to-image generation with examples including the full version and the FP8 Checkpoint version.

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=199a3f0f9e2381586b482029d246f4bb" alt="Flux" data-og-width="2048" width="2048" data-og-height="1171" height="1171" data-path="images/tutorial/flux/flux_example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=809f1427a04668bc20fde161f79f8e8c 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=51679c65a29520e2eae4d5e529eb9d22 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2b562246e400efca7612f7fd228beb60 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=142b51a1bc19a56ef5264c3ccd6beb61 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f5dab39f12ef469b89729d99a3c2eb63 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d9ced5a2d86b6ba2613c57ec43339ed9 2500w" />
Flux is one of the largest open-source text-to-image generation models, with 12B parameters and an original file size of approximately 23GB. It was developed by [Black Forest Labs](https://blackforestlabs.ai/), a team founded by former Stable Diffusion team members.
Flux is known for its excellent image quality and flexibility, capable of generating high-quality, diverse images.

Currently, the Flux.1 model has several main versions:

* **Flux.1 Pro:** The best performing model, closed-source, only available through API calls.
* **[Flux.1 \[dev\]：](https://huggingface.co/black-forest-labs/FLUX.1-dev)** Open-source but limited to non-commercial use, distilled from the Pro version, with performance close to the Pro version.
* **[Flux.1 \[schnell\]：](https://huggingface.co/black-forest-labs/FLUX.1-schnell)** Uses the Apache2.0 license, requires only 4 steps to generate images, suitable for low-spec hardware.

**Flux.1 Model Features**

* **Hybrid Architecture:** Combines the advantages of Transformer networks and diffusion models, effectively integrating text and image information, improving the alignment accuracy between generated images and prompts, with excellent fidelity to complex prompts.
* **Parameter Scale:** Flux has 12B parameters, capturing more complex pattern relationships and generating more realistic, diverse images.
* **Supports Multiple Styles:** Supports diverse styles, with excellent performance for various types of images.

In this example, we'll introduce text-to-image examples using both Flux.1 Dev and Flux.1 Schnell versions, including the full version model and the simplified FP8 Checkpoint version.

* **Flux Full Version:** Best performance, but requires larger VRAM resources and installation of multiple model files.
* **Flux FP8 Checkpoint:** Requires only one fp8 version of the model, but quality is slightly reduced compared to the full version.

<Tip>
  All workflow images's Metadata contains the corresponding model download information. You can load the workflows by:

  * Dragging them directly into ComfyUI
  * Or using the menu `Workflows` -> `Open（ctrl+o）`

  If you're not using the Desktop Version or some models can't be downloaded automatically, please refer to the manual installation sections to save the model files to the corresponding folder.
  Make sure your ComfyUI is updated to the latest version before starting.
</Tip>

## Flux.1 Full Version Text-to-Image Example

<Note>
  If you can't download models from [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev), make sure you've logged into Huggingface and agreed to the corresponding repository's license agreement.
  <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7171d72127bc5b3d6943996a9ef06970" alt="Flux Agreement" data-og-width="3330" width="3330" data-og-height="1854" height="1854" data-path="images/tutorial/flux/flux_agreement.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5fed306c4f611f1edaef827dc6e0d8b6 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8d2968fdc71af13b4993583d9bd77c6d 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6d731ba033d2044414a352f927521f4c 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=205f214d986b9eee863b1ac7b644adf5 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f03cb20f999349c5c6d8bfde63b817e2 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0e6f751cb15e267efa77287ebee79f35 2500w" />
</Note>

### Flux.1 Dev

#### 1. Workflow File

Please download the image below and drag it into ComfyUI to load the workflow.
![Flux Dev Original Version Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/text-to-image/flux_dev_t5fp16.png)

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_dev_checkpoint_example&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

#### 2. Manual Model Installation

<Note>
  * The `flux1-dev.safetensors` file requires agreeing to the [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) agreement before downloading via browser.
  * If your VRAM is low, you can try using [t5xxl\_fp8\_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors?download=true) to replace the `t5xxl_fp16.safetensors` file.
</Note>

Please download the following model files:

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) Recommended when your VRAM is greater than 32GB.
* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)
* [flux1-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors)

Storage location:

```
ComfyUI/
├── models/
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── t5xxl_fp16.safetensors
│   ├── vae/
│   │   └── ae.safetensors
│   └── diffusion_models/
│       └── flux1-dev.safetensors
```

#### 3. Steps to Run the Workflow

Please refer to the image below to ensure all model files are loaded correctly

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fbdc3a3b3b795328425b4ab854b77f13" alt="ComfyUI Flux Dev Workflow" data-og-width="3000" width="3000" data-og-height="1564" height="1564" data-path="images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=62b855e6dc0a2c7009437c4c405e2e08 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=980bc0272a2045ad438bed17c14d169b 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8716a037e0507c3299e61752ec61cd1e 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=1d329ee0b53c6148550d31521dbd0d5b 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a4d8ce8f0c9a1266bef3e52f91883bd7 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8b49df11330394e528d2c476d30a7cfc 2500w" />

1. Ensure the `DualCLIPLoader` node has the following models loaded:
   * clip\_name1: t5xxl\_fp16.safetensors
   * clip\_name2: clip\_l.safetensors
2. Ensure the `Load Diffusion Model` node has `flux1-dev.safetensors` loaded
3. Make sure the `Load VAE` node has `ae.safetensors` loaded
4. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

<Tip>
  Thanks to Flux's excellent prompt following capability, we don't need any negative prompts
</Tip>

### Flux.1 Schnell

#### 1. Workflow File

Please download the image below and drag it into ComfyUI to load the workflow.

![Flux Schnell Version Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/text-to-image/flux_schnell_t5fp8.png)

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_schnell&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

#### 2. Manual Models Installation

<Note>
  In this workflow, only two model files are different from the Flux1 Dev version workflow. For t5xxl, you can still use the fp16 version for better results.

  * **t5xxl\_fp16.safetensors** -> **t5xxl\_fp8.safetensors**
  * **flux1-dev.safetensors** -> **flux1-schnell.safetensors**
</Note>

Complete model file list:

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp8\_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors?download=true)
* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)
* [flux1-schnell.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/flux1-schnell.safetensors)

File storage location:

```
ComfyUI/
├── models/
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── t5xxl_fp8_e4m3fn.safetensors
│   ├── vae/
│   │   └── ae.safetensors
│   └── diffusion_models/
│       └── flux1-schnell.safetensors
```

#### 3. Steps to Run the Workflow

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6ce852c65510f40dde8069dc6370869d" alt="Flux Schnell Version Workflow" data-og-width="4000" width="4000" data-og-height="1599" height="1599" data-path="images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a693b1cabe10e1403554d980e3235789 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a5df5a560d6209426506c18a01592596 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f6f054bd91ee1e4c652c8131893f7346 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8c7918768349130fe0b64d0d631758a1 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0d8a64ea9b06142e8bb38c00487a2153 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d64840834a702aae0a8d3b0697ed8d27 2500w" />

1. Ensure the `DualCLIPLoader` node has the following models loaded:
   * clip\_name1: t5xxl\_fp8\_e4m3fn.safetensors
   * clip\_name2: clip\_l.safetensors
2. Ensure the `Load Diffusion Model` node has `flux1-schnell.safetensors` loaded
3. Ensure the `Load VAE` node has `ae.safetensors` loaded
4. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

## Flux.1 FP8 Checkpoint Version Text-to-Image Example

The fp8 version is a quantized version of the original Flux.1 fp16 version.
To some extent, the quality of this version will be lower than that of the fp16 version,
but it also requires less VRAM, and you only need to install one model file to try running it.

### Flux.1 Dev

Please download the image below and drag it into ComfyUI to load the workflow.

![Flux Dev fp8 Checkpoint Version Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/text-to-image/flux_dev_fp8.png)

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_dev_full_text_to_image&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

Please download [flux1-dev-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors?download=true) and save it to the `ComfyUI/models/checkpoints/` directory.

Ensure that the corresponding `Load Checkpoint` node loads `flux1-dev-fp8.safetensors`, and you can try to run the workflow.

### Flux.1 Schnell

Please download the image below and drag it into ComfyUI to load the workflow.

![Flux Schnell fp8 Checkpoint Version Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/text-to-image/flux_schnell_fp8.png)

Please download [flux1-schnell-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-schnell/resolve/main/flux1-schnell-fp8.safetensors?download=true) and save it to the `ComfyUI/models/checkpoints/` directory.

Ensure that the corresponding `Load Checkpoint` node loads `flux1-schnell-fp8.safetensors`, and you can try to run the workflow.
