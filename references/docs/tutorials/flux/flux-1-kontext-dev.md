> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Flux Kontext Dev Native Workflow Example

> ComfyUI Flux Kontext Dev Native Workflow Example.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/Y7L_cbNJHj0?si=zuaRiU3qJYMNW2uv" title="ComfyUI Selection Toolbox New Features" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## About FLUX.1 Kontext Dev

FLUX.1 Kontext is a breakthrough multimodal image editing model from Black Forest Labs that supports simultaneous text and image input, intelligently understanding image context and performing precise editing. Its development version is an open-source diffusion transformer model with 12 billion parameters, featuring excellent context understanding and character consistency maintenance, ensuring that key elements such as character features and composition layout remain stable even after multiple iterative edits.

It shares the same core capabilities as the FLUX.1 Kontext suite:

* Character Consistency: Preserves unique elements in images across multiple scenes and environments, such as reference characters or objects in the image.
* Editing: Makes targeted modifications to specific elements in the image without affecting other parts.
* Style Reference: Generates novel scenes while preserving the unique style of the reference image according to text prompts.
* Interactive Speed: Minimal latency in image generation and editing.

While the previously released API version offers the highest fidelity and speed, FLUX.1 Kontext \[Dev] runs entirely on local machines, providing unparalleled flexibility for developers, researchers, and advanced users who wish to experiment.

### Version Information

* **\[FLUX.1 Kontext \[pro]** - Commercial version, focused on rapid iterative editing
* **FLUX.1 Kontext \[max]** - Experimental version with stronger prompt adherence
* **FLUX.1 Kontext \[dev]** - Open source version (used in this tutorial), 12B parameters, mainly for research

Currently in ComfyUI, you can use all these versions, where [Pro and Max versions](/tutorials/partner-nodes/black-forest-labs/flux-1-kontext) can be called through API nodes, while the Dev open source version please refer to the instructions in this guide.

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

## Model Download

To run the workflows in this guide successfully, you first need to download the following model files. You can also directly get the model download links from the corresponding workflows, which already contain the model file download information.

**Diffusion Model**

* [flux1-dev-kontext\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/flux1-kontext-dev_ComfyUI/resolve/main/split_files/diffusion_models/flux1-dev-kontext_fp8_scaled.safetensors)

<Tip>
  If you want to use the original weights, you can visit Black Forest Labs' related repository to obtain and use the original model weights.
</Tip>

**VAE**

* [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/blob/main/split_files/vae/ae.safetensors)

**Text Encoder**

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) or [t5xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors)

Model save location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── flux1-dev-kontext_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensor
│   └── 📂 text_encoders/
│       ├── clip_l.safetensors
│       └── t5xxl_fp16.safetensors or t5xxl_fp8_e4m3fn_scaled.safetensors
```

## Flux.1 Kontext Dev Workflow

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_kontext_dev_basic&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

This workflow uses the `Load Image(from output)` node to load the image to be edited, making it more convenient for you to access the edited image for multiple rounds of editing.

### 1. Workflow and Input Image Download

Download the following files and drag them into ComfyUI to load the corresponding workflow

![ComfyUI Flux.1 Kontext Pro Image API Node Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/kontext/dev/flux_1_kontext_dev_basic.png)

**Input Image**

![ComfyUI Flux Kontext Native Workflow Input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/kontext/dev/rabbit.jpg)

### 2. Complete the workflow step by step

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=90995e36fa39a53693aeff3b560c60ef" alt="Workflow Step Guide" data-og-width="3214" width="3214" data-og-height="2066" height="2066" data-path="images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=00aff823a946c2b826884d073a9cf534 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=87af4329e8112a8a49bd9f9960e472d3 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2dd7fca1d798423ca45abd085bc295ed 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0d810c51e34794160b6def779a6bb09d 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ebc044d661f75d01cec6d4c2aa299001 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=85a5abb63a36a2f172e64239f41a4b78 2500w" />
You can refer to the numbers in the image to complete the workflow run:

1. In the `Load Diffusion Model` node, load the `flux1-dev-kontext_fp8_scaled.safetensors` model
2. In the `DualCLIP Load` node, ensure that `clip_l.safetensors` and `t5xxl_fp16.safetensors` or `t5xxl_fp8_e4m3fn_scaled.safetensors` are loaded
3. In the `Load VAE` node, ensure that `ae.safetensors` model is loaded
4. In the `Load Image(from output)` node, load the provided input image
5. In the `CLIP Text Encode` node, modify the prompts, only English is supported
6. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

## Flux Kontext Prompt Techniques

### 1. Basic Modifications

* Simple and direct: `"Change the car color to red"`
* Maintain style: `"Change to daytime while maintaining the same style of the painting"`

### 2. Style Transfer

**Principles:**

* Clearly name style: `"Transform to Bauhaus art style"`
* Describe characteristics: `"Transform to oil painting with visible brushstrokes, thick paint texture"`
* Preserve composition: `"Change to Bauhaus style while maintaining the original composition"`

### 3. Character Consistency

**Framework:**

* Specific description: `"The woman with short black hair"` instead of "she"
* Preserve features: `"while maintaining the same facial features, hairstyle, and expression"`
* Step-by-step modifications: Change background first, then actions

### 4. Text Editing

* Use quotes: `"Replace 'joy' with 'BFL'"`
* Maintain format: `"Replace text while maintaining the same font style"`

## Common Problem Solutions

### Character Changes Too Much

❌ Wrong: `"Transform the person into a Viking"`
✅ Correct: `"Change the clothes to be a viking warrior while preserving facial features"`

### Composition Position Changes

❌ Wrong: `"Put him on a beach"`
✅ Correct: `"Change the background to a beach while keeping the person in the exact same position, scale, and pose"`

### Style Application Inaccuracy

❌ Wrong: `"Make it a sketch"`
✅ Correct: `"Convert to pencil sketch with natural graphite lines, cross-hatching, and visible paper texture"`

## Core Principles

1. **Be Specific and Clear** - Use precise descriptions, avoid vague terms
2. **Step-by-step Editing** - Break complex modifications into multiple simple steps
3. **Explicit Preservation** - State what should remain unchanged
4. **Verb Selection** - Use "change", "replace" rather than "transform"

## Best Practice Templates

**Object Modification:**
`"Change [object] to [new state], keep [content to preserve] unchanged"`

**Style Transfer:**
`"Transform to [specific style], while maintaining [composition/character/other] unchanged"`

**Background Replacement:**
`"Change the background to [new background], keep the subject in the exact same position and pose"`

**Text Editing:**
`"Replace '[original text]' with '[new text]', maintain the same font style"`

> **Remember:** The more specific, the better. Kontext excels at understanding detailed instructions and maintaining consistency.
