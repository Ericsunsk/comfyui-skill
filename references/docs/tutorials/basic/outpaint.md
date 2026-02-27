> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Outpainting Workflow Example

> This guide will introduce you to the outpainting workflow in ComfyUI and walk you through an outpainting example

This guide will introduce you to the concept of outpainting in AI image generation and how to create an outpainting workflow in ComfyUI. We will cover:

* Using outpainting workflow to extend an image
* Understanding and using outpainting-related nodes in ComfyUI
* Mastering the basic outpainting process

## About Outpainting

In AI image generation, we often encounter situations where an existing image has good composition but the canvas area is too small, requiring us to extend the canvas to get a larger scene. This is where outpainting comes in.

Basically, it requires similar content to [Inpainting](/tutorials/basic/inpaint), but we use different nodes to **build the mask**.

Outpainting applications include:

* **Scene Extension:** Expand the scene range of the original image to show a more complete environment
* **Composition Adjustment:** Optimize the overall composition by extending the canvas
* **Content Addition:** Add more related scene elements to the original image

## ComfyUI Outpainting Workflow Example Explanation

### Preparation

#### 1. Model Installation

Download the following model file and save it to `ComfyUI/models/checkpoints` directory:

* [512-inpainting-ema.safetensors](https://huggingface.co/stabilityai/stable-diffusion-2-inpainting/blob/main/512-inpainting-ema.safetensors)

#### 2. Input Image

Prepare an image you want to extend. In this example, we will use the following image:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/input.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=70f072d92be155e740f8763e0265240f" alt="ComfyUI Outpainting Input Image" data-og-width="512" width="512" data-og-height="512" height="512" data-path="images/tutorial/basic/outpaint/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/input.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=92d887b2159264b61ff97551fa3a0103 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/input.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4f4d454456ab5017e926209f958140c6 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/input.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3dbb31383ffba50c728506ca5fa52fe4 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/input.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f0b35b7011f4ab4bf79adfba40bfc172 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/input.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=9b22ac3f4d4bcc2ce494612fdbd16990 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/input.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=0660b6dcbdcf5d09d4e4f59390b9e639 2500w" />

#### 3. Outpainting Workflow

Download the image below and **drag it into ComfyUI** to load the workflow:

![ComfyUI Outpainting Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/outpaint.png)

<Tip>
  Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.
</Tip>

### Outpainting Workflow Usage Explanation

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/outpainting_workflow.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b56842f634fedc85c66bccd0ead52bb6" alt="ComfyUI Outpainting Workflow Diagram" data-og-width="1818" width="1818" data-og-height="1160" height="1160" data-path="images/tutorial/basic/outpaint/outpainting_workflow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/outpainting_workflow.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=2d2fedc029bd619540fb6adcabc415c0 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/outpainting_workflow.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=454f1af3352dfe61d228fea298b902e3 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/outpainting_workflow.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=bd27f876157ca9c98c2c92065b4e15b2 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/outpainting_workflow.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1521fb04beb2fb50363dbb73ad117d22 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/outpainting_workflow.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=0be5decddd0c7f26d3a0198090ec5978 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/outpainting_workflow.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b99fa7a0d0db884d881f3c2c9187936c 2500w" />

The key steps of the outpainting workflow are as follows:

1. Load the locally installed model file in the `Load Checkpoint` node
2. Click the `Upload` button in the `Load Image` node to upload your image
3. Click the `Queue` button or use the shortcut `Ctrl + Enter` to execute the image generation

In this workflow, we mainly use the `Pad Image for outpainting` node to control the direction and range of image extension. This is actually an [Inpaint](/tutorials/basic/inpaint) workflow, but we use different nodes to build the mask.

### Pad Image for outpainting Node

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/pad_image_for_outpainting.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9a9eaf8b01a18692b50a684cbff5d8e1" alt="Pad Image for outpainting Node" data-og-width="852" width="852" data-og-height="570" height="570" data-path="images/comfy_core/image/pad_image_for_outpainting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/pad_image_for_outpainting.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e8eac3ee3ddf56488f7db2514850e050 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/pad_image_for_outpainting.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c230cbc648eb8ee05ec65eff86c0e913 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/pad_image_for_outpainting.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1998b2a7e14e5f5331b7c8156619782f 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/pad_image_for_outpainting.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=def26927601a05dc6e10c769e1b5827e 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/pad_image_for_outpainting.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d091d198e5b0262df6919f666e62ac9b 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/pad_image_for_outpainting.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cc14e0965caf245349ee55ec4579cd31 2500w" />

This node accepts an input image and outputs an extended image with a corresponding mask, where the mask is built based on the node parameters.

#### Input Parameters

| Parameter Name | Function                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `image`        | Input image                                                                                                                           |
| `left`         | Left padding amount                                                                                                                   |
| `top`          | Top padding amount                                                                                                                    |
| `right`        | Right padding amount                                                                                                                  |
| `bottom`       | Bottom padding amount                                                                                                                 |
| `feathering`   | Controls the smoothness of the transition between the original image and the added padding, higher values create smoother transitions |

#### Output Parameters

| Parameter Name | Function                                                                   |
| -------------- | -------------------------------------------------------------------------- |
| `image`        | Output `image` represents the padded image                                 |
| `mask`         | Output `mask` indicates the original image area and the added padding area |

#### Node Output Content

After processing by the `Pad Image for outpainting` node, the output image and mask preview are as follows:

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=cc8fd3e8159dca0e8abf9def1bfe6d39" alt="Pad Image for outpainting Node Results" data-og-width="1600" width="1600" data-og-height="798" height="798" data-path="images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c818dadb5ede0cc54de33eb23f095474 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=35588369ee8d526a7d9583e559cddd2d 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3a772936215ac2c9975c902a01d3b354 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c81e37842480fa81ab070d0dcfc24ea4 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6bf66f3539d9127bf68c64a1dc5997cf 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e6aaaf090bcdda387b8fc9f289f5d7cf 2500w" />

You can see the corresponding output results:

* The `Image` output is the extended image
* The `Mask` output is the mask marking the extension areas
