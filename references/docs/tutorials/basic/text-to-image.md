> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Text to Image Workflow

> This guide will help you understand the concept of text-to-image in AI art generation and complete a text-to-image workflow in ComfyUI

This guide aims to introduce you to ComfyUI's text-to-image workflow and help you understand the functionality and usage of various ComfyUI nodes.

In this document, we will:

* Complete a text-to-image workflow
* Gain a basic understanding of diffusion model principles
* Learn about the functions and roles of workflow nodes
* Get an initial understanding of the SD1.5 model

We'll start by running a text-to-image workflow, followed by explanations of related concepts. Please choose the relevant sections based on your needs.

## About Text to Image

**Text to Image** is a fundamental process in AI art generation that creates images from text descriptions, with **diffusion models** at its core.

The text-to-image process requires the following elements:

* **Artist:** The image generation model
* **Canvas:** The latent space
* **Image Requirements (Prompts):** Including positive prompts (elements you want in the image) and negative prompts (elements you don't want)

This text-to-image generation process can be simply understood as telling your requirements (positive and negative prompts) to an **artist (the image model)**, who then creates what you want based on these requirements.

## ComfyUI Text to Image Workflow Example Guide

### 1. Preparation

Ensure you have at least one SD1.5 model file in your `ComfyUI/models/checkpoints` folder, such as [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors)

If you haven't installed it yet, please refer to the model installation section in [Getting Started with ComfyUI AI Art Generation](/get_started/first_generation).

### 2. Loading the Text to Image Workflow

Download the image below and **drag it into ComfyUI** to load the workflow:

<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/text-to-image-workflow.png" alt="ComfyUI-Text to Image Workflow" />

<Tip>
  Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.
</Tip>

### 3. Loading the Model and Generating Your First Image

After installing the image model, follow the steps in the image below to load the model and generate your first image

![Image Generation](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/text-to-image-workflow.png)

Follow these steps according to the image numbers:

1. In the **Load Checkpoint** node, use the arrows or click the text area to ensure **v1-5-pruned-emaonly-fp16.safetensors** is selected, and the left/right arrows don't show **null** text
2. Click the `Queue` button or use the shortcut `Ctrl + Enter` to execute image generation

After the process completes, you should see the resulting image in the **Save Image** node interface, which you can right-click to save locally

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=92b100190dd8f91abb37b01cc2e09a59" alt="ComfyUI First Image Generation Result" data-og-width="2642" width="2642" data-og-height="1390" height="1390" data-path="images/tutorial/gettingstarted/first-image-generation-8-result.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f0c2219d45e70c2f21ebd64032fddb50 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9391713ee886380f8302e396975a94aa 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ace21872a174725c45788b7ce5ce8a34 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a579037cd0b65cd2115280f8eee6e80b 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8dba16d2de187f3f6356af67ee1040ef 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=adfc35ce5d546ca79f140b45dee3fe2d 2500w" />

<Tip>If you're not satisfied with the result, try running the generation multiple times. Each time you run it, **KSampler** will use a different random seed based on the `seed` parameter, so each generation will produce different results</Tip>

### 4. Start Experimenting

Try modifying the text in the **CLIP Text Encoder**

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=94d83f96b628279b5b2fc865d522886e" alt="CLIP Text Encoder" data-og-width="778" width="778" data-og-height="477" height="477" data-path="images/comfy_core/conditioning/clip_text_encode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1d5e4f945f83db77e339f0301ffb365c 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=67671fa5fc37408cf9e2f315c8ff16f3 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f3cb23d3f4aba2f500b2d350f0a2a7c3 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a6fbf2d76a7722260d317152e5977c61 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ef744de37e931396fa5e6417730d7e9e 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1cd01f8ad444d9a4c2a18dae3cb6b4b1 2500w" />

The `Positive` connection to the KSampler node represents positive prompts, while the `Negative` connection represents negative prompts

Here are some basic prompting principles for the SD1.5 model:

* Use English whenever possible
* Separate prompts with English commas `,`
* Use phrases rather than long sentences
* Use specific descriptions
* Use expressions like `(golden hour:1.2)` to increase the weight of specific keywords, making them more likely to appear in the image. `1.2` is the weight, `golden hour` is the keyword
* Use keywords like `masterpiece, best quality, 4k` to improve generation quality

Here are several prompt examples you can try, or use your own prompts for generation:

**1. Anime Style**

Positive prompts:

```
anime style, 1girl with long pink hair, cherry blossom background, studio ghibli aesthetic, soft lighting, intricate details

masterpiece, best quality, 4k
```

Negative prompts:

```
low quality, blurry, deformed hands, extra fingers
```

**2. Realistic Style**

Positive prompts:

```
(ultra realistic portrait:1.3), (elegant woman in crimson silk dress:1.2), 
full body, soft cinematic lighting, (golden hour:1.2), 
(fujifilm XT4:1.1), shallow depth of field, 
(skin texture details:1.3), (film grain:1.1), 
gentle wind flow, warm color grading, (perfect facial symmetry:1.3)
```

Negative prompts:

```
(deformed, cartoon, anime, doll, plastic skin, overexposed, blurry, extra fingers)
```

**3. Specific Artist Style**

Positive prompts:

```
fantasy elf, detailed character, glowing magic, vibrant colors, long flowing hair, elegant armor, ethereal beauty, mystical forest, magical aura, high detail, soft lighting, fantasy portrait, Artgerm style
```

Negative prompts:

```
blurry, low detail, cartoonish, unrealistic anatomy, out of focus, cluttered, flat lighting
```

## Text to Image Working Principles

The entire text-to-image process can be understood as a **reverse diffusion process**. The [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) we downloaded is a pre-trained model that can **generate target images from pure Gaussian noise**. We only need to input our prompts, and it can generate target images through denoising random noise.

```mermaid  theme={null}
graph LR
A[Pure Gaussian Noise] --> B[Iterative Denoising]
B --> C[Intermediate Latents]
C --> D[Final Generated Image]
E[Text Prompts] --> F[CLIP Encoder]
F --> G[Semantic Vectors]
G --> B
```

We need to understand two concepts:

1. **Latent Space:** Latent Space is an abstract data representation method in diffusion models. Converting images from pixel space to latent space reduces storage space and makes it easier to train diffusion models and reduce denoising complexity. It's like architects using blueprints (latent space) for design rather than designing directly on the building (pixel space), maintaining structural features while significantly reducing modification costs
2. **Pixel Space:** Pixel Space is the storage space for images, which is the final image we see, used to store pixel values.

If you want to learn more about diffusion models, you can read these papers:

* [Denoising Diffusion Probabilistic Models (DDPM)](https://arxiv.org/pdf/2006.11239)
* [Denoising Diffusion Implicit Models (DDIM)](https://arxiv.org/pdf/2010.02502)
* [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/pdf/2112.10752)

## ComfyUI Text to Image Workflow Node Explanation

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/text-image-workflow.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3e22321faba12644c781cecc5746a71e" alt="ComfyUI Text to Image Workflow Explanation" data-og-width="2640" width="2640" data-og-height="1384" height="1384" data-path="images/tutorial/basic/text-image-workflow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/text-image-workflow.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=00f7db5a22d5a7d186adee653c14761c 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/text-image-workflow.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7fb01ec47ce2e701c513881a9e3f1e5b 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/text-image-workflow.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=25e071ca07a29643537ea8bdb3893cb3 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/text-image-workflow.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4fed435b700cfe00931c32027881b801 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/text-image-workflow.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=9c6ccc91e4d28cad1700033497cd6dfd 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/text-image-workflow.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5d3f62df6ef74b998814b604721c465f 2500w" />

### A. Load Checkpoint Node

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_checkpoint.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1a046abe89763dd49e42f2447974a1f8" alt="Load Checkpoint" data-og-width="807" width="807" data-og-height="384" height="384" data-path="images/comfy_core/loaders/load_checkpoint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_checkpoint.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=24e18a1cdc77c62189fc29c677e7165e 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_checkpoint.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=dd577f103a62c2124ca61cde280cbe4e 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_checkpoint.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3bdc09d0944ef1c60230e73a742c8621 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_checkpoint.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7861410e82e36ff7dd08b5c3cbb842a6 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_checkpoint.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8824a755aba210b2a804502b0d49f907 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_checkpoint.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=86d741df610277979074c4353306c907 2500w" />

This node is typically used to load the image generation model. A `checkpoint` usually contains three components: `MODEL (UNet)`, `CLIP`, and `VAE`

* `MODEL (UNet)`: The UNet model responsible for noise prediction and image generation during the diffusion process
* `CLIP`: The text encoder that converts our text prompts into vectors that the model can understand, as the model cannot directly understand text prompts
* `VAE`: The Variational AutoEncoder that converts images between pixel space and latent space, as diffusion models work in latent space while our images are in pixel space

### B. Empty Latent Image Node

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/empty_latent_image.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e40da4b9e1953fa2488277c47a310187" alt="Empty Latent Image" data-og-width="855" width="855" data-og-height="420" height="420" data-path="images/comfy_core/latent/empty_latent_image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/empty_latent_image.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f598f452e7fcd96ced27d409aa37f86a 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/empty_latent_image.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b348ec3897d361910c46d1451782cc77 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/empty_latent_image.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=367ddd1429f0a9d5cade86c337ca7f27 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/empty_latent_image.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ae1d7f0228de9d381974bdd4264aceb2 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/empty_latent_image.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4bd95609794ead59eb95569f6442bb47 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/empty_latent_image.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=53285a3dfa681f7680a2a907707b176f 2500w" />

Defines a latent space that outputs to the KSampler node. The Empty Latent Image node constructs a **pure noise latent space**

You can think of its function as defining the canvas size, which determines the dimensions of our final generated image

### C. CLIP Text Encoder Node

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=94d83f96b628279b5b2fc865d522886e" alt="CLIP Text Encoder" data-og-width="778" width="778" data-og-height="477" height="477" data-path="images/comfy_core/conditioning/clip_text_encode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1d5e4f945f83db77e339f0301ffb365c 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=67671fa5fc37408cf9e2f315c8ff16f3 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f3cb23d3f4aba2f500b2d350f0a2a7c3 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a6fbf2d76a7722260d317152e5977c61 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ef744de37e931396fa5e6417730d7e9e 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/conditioning/clip_text_encode.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1cd01f8ad444d9a4c2a18dae3cb6b4b1 2500w" />

Used to encode prompts, which are your requirements for the image

* The `Positive` condition input connected to the KSampler node represents positive prompts (elements you want in the image)
* The `Negative` condition input connected to the KSampler node represents negative prompts (elements you don't want in the image)

The prompts are encoded into semantic vectors by the `CLIP` component from the `Load Checkpoint` node and output as conditions to the KSampler node

### D. KSampler Node

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=aed5e1f863c37948107cfcb3458955b7" alt="KSampler" data-og-width="854" width="854" data-og-height="767" height="767" data-path="images/comfy_core/sampling/k_sampler.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f891fb24b7fcbb6616bad811d797cd10 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d3597cfd9ef1b324ceb8b8e529246540 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e714d81c3a3214ef9fe1da89cdc2efd3 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5001918af1c739866639c03df51a3c19 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ff62cab54c0c1fa1432d98c69877706d 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=350b8494ce4c1e004ddd94f7977563d7 2500w" />

The **KSampler** is the core of the entire workflow, where the entire noise denoising process occurs, ultimately outputting a latent space image

```mermaid  theme={null}
graph LR
A[Diffusion Model] --> B{KSampler}
C[Random Noise<br>Latent Space] --> B
D[CLIP Semantic Vectors] --> B
B --> E[Denoised Latent]
```

Here's an explanation of the KSampler node parameters:

| Parameter Name               | Description                        | Function                                                                                                    |
| ---------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **model**                    | Diffusion model used for denoising | Determines the style and quality of generated images                                                        |
| **positive**                 | Positive prompt condition encoding | Guides generation to include specified elements                                                             |
| **negative**                 | Negative prompt condition encoding | Suppresses unwanted content                                                                                 |
| **latent\_image**            | Latent space image to be denoised  | Serves as the input carrier for noise initialization                                                        |
| **seed**                     | Random seed for noise generation   | Controls generation randomness                                                                              |
| **control\_after\_generate** | Seed control mode after generation | Determines seed variation pattern in batch generation                                                       |
| **steps**                    | Number of denoising iterations     | More steps mean finer details but longer processing time                                                    |
| **cfg**                      | Classifier-free guidance scale     | Controls prompt constraint strength (too high leads to overfitting)                                         |
| **sampler\_name**            | Sampling algorithm name            | Determines the mathematical method for denoising path                                                       |
| **scheduler**                | Scheduler type                     | Controls noise decay rate and step size allocation                                                          |
| **denoise**                  | Denoising strength coefficient     | Controls noise strength added to latent space, 0.0 preserves original input features, 1.0 is complete noise |

In the KSampler node, the latent space uses `seed` as an initialization parameter to construct random noise, and semantic vectors `Positive` and `Negative` are input as conditions to the diffusion model

Then, based on the number of denoising steps specified by the `steps` parameter, denoising is performed. Each denoising step uses the denoising strength coefficient specified by the `denoise` parameter to denoise the latent space and generate a new latent space image

### E. VAE Decode Node

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/vae_decode.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a9c0a75f0e442062a837289c5639a205" alt="VAE Decode" data-og-width="854" width="854" data-og-height="370" height="370" data-path="images/comfy_core/latent/vae_decode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/vae_decode.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2f0afe5cd50c2c9ca8b99a19b72e7add 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/vae_decode.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=08f5dc2c949c7b17285c0bf5c1727d58 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/vae_decode.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=49bf1587c6eefcb9834168b240a50beb 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/vae_decode.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cbf29d240a132456bbdf3a1a397b4a15 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/vae_decode.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=bd71062051c89305967dbbef0ec36d08 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/vae_decode.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d07f2b9bfb33486727f2ad936277eabd 2500w" />

Converts the latent space image output from the **KSampler** into a pixel space image

### F. Save Image Node

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/save_image.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=986a4163337dce0354c90b4bfb4471b2" alt="Save Image" data-og-width="854" width="854" data-og-height="410" height="410" data-path="images/comfy_core/image/save_image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/save_image.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ca1af2cc43f687bf101878f2f20c67b8 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/save_image.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5928edfb970bf83050ba0c2f37756bac 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/save_image.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4f06fdc7b9d3452aa2ee19621c014c09 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/save_image.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b2c95b4fff95a5c73c77db8ad148b947 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/save_image.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=fcab88dcda0bd79518bbafc0a4e791b8 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/save_image.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3a1d97fbb025ba4129567ed912cc2f84 2500w" />

Previews and saves the decoded image from latent space to the local `ComfyUI/output` folder

## Introduction to SD1.5 Model

**SD1.5 (Stable Diffusion 1.5)** is an AI image generation model developed by [Stability AI](https://stability.ai/). It's the foundational version of the Stable Diffusion series, trained on **512×512** resolution images, making it particularly good at generating images at this resolution. With a size of about 4GB, it runs smoothly on **consumer-grade GPUs (e.g., 6GB VRAM)**. Currently, SD1.5 has a rich ecosystem, supporting various plugins (like ControlNet, LoRA) and optimization tools.
As a milestone model in AI art generation, SD1.5 remains the best entry-level choice thanks to its open-source nature, lightweight architecture, and rich ecosystem. Although newer versions like SDXL/SD3 have been released, its value for consumer-grade hardware remains unmatched.

### Basic Information

* **Release Date**: October 2022
* **Core Architecture**: Based on Latent Diffusion Model (LDM)
* **Training Data**: LAION-Aesthetics v2.5 dataset (approximately 590M training steps)
* **Open Source Features**: Fully open-source model/code/training data

### Advantages and Limitations

Model Advantages:

* Lightweight: Small size, only about 4GB, runs smoothly on consumer GPUs
* Low Entry Barrier: Supports a wide range of plugins and optimization tools
* Mature Ecosystem: Extensive plugin and tool support
* Fast Generation: Smooth operation on consumer GPUs

Model Limitations:

* Detail Handling: Hands/complex lighting prone to distortion
* Resolution Limits: Quality degrades for direct 1024x1024 generation
* Prompt Dependency: Requires precise English descriptions for control
