> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Image to Image Workflow

> This guide will help you understand and complete an image to image workflow

## What is Image to Image

Image to Image is a workflow in ComfyUI that allows users to input an image and generate a new image based on it.

Image to Image can be used in scenarios such as:

* Converting original image styles, like transforming realistic photos into artistic styles
* Converting line art into realistic images
* Image restoration
* Colorizing old photos
* ... and other scenarios

To explain it with an analogy:
It's like asking an artist to create a specific piece based on your reference image.

If you carefully compare this tutorial with the [Text to Image](/tutorials/basic/text-to-image) tutorial,
you'll notice that the Image to Image process is very similar to Text to Image,
just with an additional input reference image as a condition. In Text to Image, we let the artist (image model) create freely based on our prompts,
while in Image to Image, we let the artist create based on both our reference image and prompts.

## ComfyUI Image to Image Workflow Example Guide

### Model Installation

Download the [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) file and put it in your `ComfyUI/models/checkpoints` folder.

### Image to Image Workflow and Input Image

Download the image below and **drag it into ComfyUI** to load the workflow:
![Image to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image_to_image/workflow.png)

<Tip>
  Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.
</Tip>

Download the image below and we will use it as the input image:
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f8d1c4f2afa4a80f07a6ad862506c832" alt="Example Image" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/basic/img2img/input.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=2cf62d99d9595053f961e18bbae104fa 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=25ee69405b3bb78b8ad9fffa930324ec 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=96d0a0acd6f76c4b3d547f5911dd2888 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=54694dfd7f86ad5d13363b8123ed95cb 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7dcb3f779c1a36505bde2f7f50828ea3 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=fa0782cbc1a84bc318679384cbbb0873 2500w" />

### Complete the Workflow Step by Step

Follow the steps in the diagram below to ensure the workflow runs correctly.

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=dd85418c3e8070eb5c3f491a89fd29b3" alt="ComfyUI Image to Image Workflow - Steps" data-og-width="1197" width="1197" data-og-height="779" height="779" data-path="images/tutorial/basic/img2img/image-to-image-02-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1b0cc094853876eb09edcd81575f3171 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4630801bea3f11270b97b29cfcc77bea 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4935b3f629d63f2bf0c8a79fa864eb16 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ba9c51655e26715be1b316c307c3a761 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=90406adf554c73a31ffe9b86cfea06ed 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=d813a71613511b97258f4b01317f565a 2500w" />

1. Ensure `Load Checkpoint` loads  **v1-5-pruned-emaonly-fp16.safetensors**
2. Upload the input image to the `Load Image` node
3. Click `Queue` or press `Ctrl/Cmd + Enter` to generate

## Key Points of Image to Image Workflow

The key to the Image to Image workflow lies in the `denoise` parameter in the `KSampler` node, which should be **less than 1**

If you've adjusted the `denoise` parameter and generated images, you'll notice:

* The smaller the `denoise` value, the smaller the difference between the generated image and the reference image
* The larger the `denoise` value, the larger the difference between the generated image and the reference image

This is because `denoise` determines the strength of noise added to the latent space image after converting the reference image. If `denoise` is 1, the latent space image will become completely random noise, making it the same as the latent space generated by the `empty latent image` node, losing all characteristics of the reference image.

For the corresponding principles, please refer to the principle explanation in the [Text to Image](/tutorials/basic/text-to-image) tutorial.

## Try It Yourself

1. Try modifying the `denoise` parameter in the **KSampler** node, gradually changing it from 1 to 0, and observe the changes in the generated images
2. Replace with your own prompts and reference images to generate your own image effects
