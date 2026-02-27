> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Inpainting Workflow

> This guide will introduce you to the inpainting workflow in ComfyUI, walk you through an inpainting example, and cover topics like using the mask editor

This article will introduce the concept of inpainting in AI image generation and guide you through creating an inpainting workflow in ComfyUI. We'll cover:

* Using inpainting workflows to modify images
* Using the ComfyUI mask editor to draw masks
* `VAE Encoder (for Inpainting)` node

## About Inpainting

In AI image generation, we often encounter situations where we're satisfied with the overall image but there are elements we don't want or that contain errors. Simply regenerating might produce a completely different image, so using inpainting to fix specific parts becomes very useful.

It's like having an **artist (AI model)** paint a picture, but we're still not satisfied with the specific details. We need to tell the artist **which areas to adjust (mask)**, and then let them **repaint (inpaint)** according to our requirements.

Common inpainting scenarios include:

* **Defect Repair:** Removing unwanted objects, fixing incorrect AI-generated body parts, etc.
* **Detail Optimization:** Precisely adjusting local elements (like modifying clothing textures, adjusting facial expressions)
* And other scenarios

## ComfyUI Inpainting Workflow Example

### Model and Resource Preparation

#### 1. Model Installation

Download the [512-inpainting-ema.safetensors](https://huggingface.co/Comfy-Org/stable_diffusion_2.1_repackaged/resolve/main/512-inpainting-ema.safetensors)  file and put it in your `ComfyUI/models/checkpoints` folder:

#### 2. Inpainting Asset

Please download the following image which we'll use as input:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a6557da482429ba4feff636d36f1bb54" alt="ComfyUI Inpainting Input Image" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/basic/inpaint/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ab6da5c62e779df51cab0462652ae03b 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=89b7bba32e0e50aa5e0b14a1780f9f81 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c8a4c7369adda8b0e594c36c1253ad69 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a5e3e567978c89496e6b301e17889a40 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3f207a73f6d035e655d204467aa9a97f 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ff19842492f61b33b7c7b6bb7fe8a791 2500w" />

<Note>This image already contains an alpha channel (transparency mask), so you don't need to manually draw a mask. This tutorial will also cover how to use the mask editor to draw masks.</Note>

#### 3. Inpainting Workflow

Download the image below and **drag it into ComfyUI** to load the workflow:

![ComfyUI Inpainting Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/sd1.5_inpaint.png)

<Tip>
  Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.
</Tip>

### ComfyUI Inpainting Workflow Example Explanation

Follow the steps in the diagram below to ensure the workflow runs correctly.

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=eec79976ea5771763a00668de7c15bc3" alt="ComfyUI Inpainting Workflow" data-og-width="2000" width="2000" data-og-height="1108" height="1108" data-path="images/tutorial/basic/inpaint/inpaint_workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a6fdc071447c0798d9beb2ad963249c1 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=483c6cc059ba949df3d3ae302e904dfc 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=dae548fecc00b515bbf698f15457f760 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e4e471b6cd770836162c82a14c31590f 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=937ae7a877e2ad00b161f1489d599207 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=551b69ce8a2eb8e4f52ca448abb87366 2500w" />

1. Ensure `Load Checkpoint` loads `512-inpainting-ema.safetensors`
2. Upload the input image to the `Load Image` node
3. Click `Queue` or use `Ctrl + Enter` to generate

For comparison, here's the result using the [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) model:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=36916904f9884b5bc3c62f6b60ec17e8" alt="SD1.5 Inpainting Result" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=793ae8991e483962785f4a1ebdc66931 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5f36ef651544636822ef6b910cf93a45 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b8f76ae73e41564f61668de75dd3784f 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e04c184d8e04180645be207d60754f2b 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b725d2042a4228df0f14498cfbb742a7 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=07e4eaecd7725da7adb146d9a06e37d6 2500w" />

You will find that the results generated by the [512-inpainting-ema.safetensors](https://huggingface.co/Comfy-Org/stable_diffusion_2.1_repackaged/resolve/main/512-inpainting-ema.safetensors) model have better inpainting effects and more natural transitions.
This is because this model is specifically designed for inpainting, which helps us better control the generation area, resulting in improved inpainting effects.

Do you remember the analogy we've been using? Different models are like artists with varying abilities, but each artist has their own limits. Choosing the right model can help you achieve better generation results.

You can try these approaches to achieve better results:

1. Modify positive and negative prompts with more specific descriptions
2. Try multiple runs using different seeds in the `KSampler` for different generation results
3. After learning about the mask editor in this tutorial, you can re-inpaint the generated results to achieve satisfactory outcomes.

Next, we'll learn about using the **Mask Editor**. While our input image already includes an `alpha` transparency channel (the area we want to edit),
so manual mask drawing isn't necessary, you'll often use the Mask Editor to create masks in practical applications.

### Using the Mask Editor

First right-click the `Save Image` node and select `Copy(Clipspace)`:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7d1bfea21723437c4ca09bba34edd1ed" alt="Copy Image to Clipboard" data-og-width="751" width="751" data-og-height="1112" height="1112" data-path="images/tutorial/basic/inpaint/inpaint_copy_clipspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=471161782a68a4a1c9b6b93f90c359bf 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=19e42850cde5a3165aa297c9839a9262 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ecc873dc3f9a633fee9cb2f030aec515 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3e31c622dd7630f5eb12bed77beffb1a 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=232b22932471ab2713a99b4c9dbd9ad0 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=587e879f30a86eb915838ef2aba36ddd 2500w" />

Then right-click the **Load Image** node and select `Paste(Clipspace)`:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=42c942d88b97c696f6f2ed59f7ff9bc8" alt="Paste Image" data-og-width="750" width="750" data-og-height="947" height="947" data-path="images/tutorial/basic/inpaint/inpaint_paste_clipspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=947f8a2ba53d5e91da74d83cbe7de177 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aa0df4dd3f7700f2c817fdfeb6af7db8 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7ec2cdd378a38fa9baab14823b4089b3 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3ca8dc639d673d4c6094d48bb1112491 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3ee5a66e68a9f6b2f3c72621986f5f6e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=547532ec78c09b89905cf4a1efa28175 2500w" />

Right-click the **Load Image** node again and select `Open in MaskEditor`:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=682a66f54e0f61366c42e553d50f4e76" alt="Open Mask Editor" data-og-width="894" width="894" data-og-height="1000" height="1000" data-path="images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8aec5f48665275dbe971f1e6b06a8689 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=0d5c93b36e0bdb80bdd09329e4ae1f3a 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e1eda1fc545857dbd5f5d7544c0562f8 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=fcf26f11d3563e21c4f6c1a821b98ce5 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3fe4854c50fe874a310e8b08efa118e8 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4c0739d96a8d0b998a8be453bdeca656 2500w" />

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint-maskeditor.gif?s=217f481d8cd4e22183c0dd1551f3e831" alt="Mask Editor Demo" data-og-width="960" width="960" data-og-height="720" height="720" data-path="images/tutorial/basic/inpaint/inpaint-maskeditor.gif" data-optimize="true" data-opv="3" />

1. Adjust brush parameters on the right panel
2. Use eraser to correct mistakes
3. Click `Save` when finished

The drawn content will be used as a Mask input to the VAE Encoder (for Inpainting) node for encoding

Then try adjusting your prompts and generating again until you achieve satisfactory results.

## VAE Encoder (for Inpainting) Node

Comparing this workflow with [Text-to-Image](/tutorials/basic/text-to-image) and [Image-to-Image](/tutorials/basic/image-to-image), you'll notice the main differences are in the VAE section's conditional inputs.
In this workflow, we use the **VAE Encoder (for Inpainting)** node, specifically designed for inpainting to help us better control the generation area and achieve better results.

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2eeecee7cf23a0e1ab7b1a996256278f" alt="VAE Encoder (for Inpainting) Node" data-og-width="854" width="854" data-og-height="440" height="440" data-path="images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a4dab6ea6ede77a88491abcca4486b12 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=504884ff3853ee9e623e077c85092b5c 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=93307ae96b3c05fc271dd06af325a6c9 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=120a4315d7eaeaacf754647e55f620d4 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=267f53b6551eeac2952cea05913f6ff3 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a27dd641b206b80d3e6e79154b5b16f5 2500w" />

**Input Types**

| Parameter Name | Function                                                                                                                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pixels`       | Input image to be encoded into latent space.                                                                                                          |
| `vae`          | VAE model used to encode the image from pixel space to latent space.                                                                                  |
| `mask`         | Image mask specifying which areas need modification.                                                                                                  |
| `grow_mask_by` | Pixel value to expand the original mask outward, ensuring a transition area around the mask to avoid hard edges between inpainted and original areas. |

**Output Types**

| Parameter Name | Function                                    |
| -------------- | ------------------------------------------- |
| `latent`       | Image encoded into latent space by the VAE. |
