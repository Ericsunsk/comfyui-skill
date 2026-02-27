> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI GPT-Image-1 Node

> Learn how to use the OpenAI GPT-Image-1 Partner node to generate images in ComfyUI

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=243b4200a707b55f1c4fd88d4edf51a9" alt="OpenAI GPT-Image-1 Node Screenshot" data-og-width="1576" width="1576" data-og-height="1123" height="1123" data-path="images/comfy_core/api_nodes/openai-gpt-image-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2d4ad0d8fdf6ac49815d5de1f21c0df7 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=868f4b2403c8ce07803227285cd6f2fc 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ab08d31d2151a589f569d13cc10692ce 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5993067ce1d818c9bcfd5147537ae256 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f2e101e964fad443efd7374c2f9ce37b 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=44cf580b967693bfdc2c49a6cc25aeb7 2500w" />

OpenAI GPT-Image-1 is part of the ComfyUI Partner nodes series that allows users to generate images through OpenAI's **GPT-Image-1** model. This is the same model used for image generation in ChatGPT 4o.

This node supports:

* Text-to-image generation
* Image editing functionality (inpainting through masks)

## Node Overview

The **OpenAI GPT-Image-1** node synchronously generates images through OpenAI's image generation API. It receives text prompts and returns images matching the description. GPT-Image-1 is OpenAI's most advanced image generation model currently available, capable of creating highly detailed and realistic images.

<Tip>
  To use the API nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [API Nodes Overview](/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the API nodes.
</Tip>

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

## Parameter Description

### Required Parameters

| Parameter | Type | Description                                                   |
| --------- | ---- | ------------------------------------------------------------- |
| `prompt`  | Text | Text prompt describing the image content you want to generate |

### Widget Parameters

| Parameter    | Type    | Options                               | Default | Description                                             |
| ------------ | ------- | ------------------------------------- | ------- | ------------------------------------------------------- |
| `seed`       | Integer | 0-2147483647                          | 0       | Random seed used to control generation results          |
| `quality`    | Option  | low, medium, high                     | low     | Image quality setting, affects cost and generation time |
| `background` | Option  | opaque, transparent                   | opaque  | Whether the returned image has a background             |
| `size`       | Option  | auto, 1024x1024, 1024x1536, 1536x1024 | auto    | Size of the generated image                             |
| `n`          | Integer | 1-8                                   | 1       | Number of images to generate                            |

### Optional Parameters

| Parameter | Type  | Options         | Default | Description                                                 |
| --------- | ----- | --------------- | ------- | ----------------------------------------------------------- |
| `image`   | Image | Any image input | None    | Optional reference image for image editing                  |
| `mask`    | Mask  | Mask input      | None    | Optional mask for inpainting (white areas will be replaced) |

## Usage Examples

### Text-to-Image Example

The image below contains a simple text-to-image workflow. Please download the image and drag it into ComfyUI to load the corresponding workflow.
![ComfyUI openai-gpt-image-1 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/text2image.png)

The corresponding workflow is very simple:
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e7308997e027153d914a61418a9c0058" alt="ComfyUI openai-gpt-image-1 workflow example" data-og-width="3580" width="3580" data-og-height="1956" height="1956" data-path="images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e21f0cd8c845d34ed3fd4016bce71fd5 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e06c844a22bd4bf1e2fca9ef2052f720 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=34f42055304ee347d962051da6a00102 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3ad0d9e30f20fe8c535d4238e331a5bc 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=24830df172d325f9593696d59c0aedcf 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a3b050cf1382fb378f45aac540259d0c 2500w" />

You only need to load the `OpenAI GPT-Image-1` node, input the description of the image you want to generate in the `prompt` node, connect a `Save Image` node, and then run the workflow.

### Image-to-Image Example

The image below contains a simple image-to-image workflow. Please download the image and drag it into ComfyUI to load the corresponding workflow.
![ComfyUI openai-gpt-image-1 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/image2image.png)

We will use the image below as input:
![ComfyUI openai-gpt-image-1 workflow input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/input.webp)

In this workflow, we use the `OpenAI GPT-Image-1` node to generate images and the `Load Image` node to load the input image, then connect it to the `image` input of the `OpenAI GPT-Image-1` node.

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=05cab30de9ab5bc2e0865c0a367f82fc" alt="ComfyUI openai-gpt-image-1 workflow example" data-og-width="3180" width="3180" data-og-height="1114" height="1114" data-path="images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=419c2f8470d671c9f9876ba8d2b64379 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=402654cfaf0701617b2e0d6c2b47414e 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1916ef7321e796d7e31b3d05462d64ce 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b5b6d1a301172a877855fb42c896e978 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=08ea4d43044625afecb002b0cedd6aaf 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c7a65d6109ebd439564cb1830c93db00 2500w" />

### Multiple Image Input Example

Please download the image below and drag it into ComfyUI to load the corresponding workflow.

![Multiple Image Input Example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/multiple_image_input.png)

Use the hat image below as an additional input image.
![Hat](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/hat.webp)

The corresponding workflow is shown in the image below:
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=125236ed762b17ae1e711fa702663f74" alt="Multiple Image Input Example" data-og-width="1432" width="1432" data-og-height="748" height="748" data-path="images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a51e55f0d4de107f42cdc2f576d798f9 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7ffbaa360a6a18c11e1c37c4cb93de6a 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c95bf1edf0e7c09b269693788d856149 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c0fad9f36754684b3fa540c2f4e5575a 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cd3e53553401ddbdf57db68659c30be7 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=07213db91090f513a00548170a21c346 2500w" />

The `Batch Images` node is used to load multiple images into the `OpenAI GPT-Image-1` node.

### Inpainting Workflow

GPT-Image-1 also supports image editing functionality, allowing you to specify areas to replace using a mask. Below is a simple inpainting workflow example:

Download the image below and drag it into ComfyUI to load the corresponding workflow. We will continue to use the input image from the image-to-image workflow section.

![ComfyUI openai-gpt-image-1 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/inpaint.png)

The corresponding workflow is shown in the image
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=12d74944bf8905025606740b820918a8" alt="ComfyUI openai-gpt-image-1 workflow example" data-og-width="3154" width="3154" data-og-height="1156" height="1156" data-path="images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6fef6c79f60a91ae564e84f8361dd5a7 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1cf77f379b0f0326bdc4165f445c87b4 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d23e66dde56fcab9ea4cf500151848ec 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=fa900de7686e8c71a858c4e0e24c7687 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=60618c269a1433faf14fa72fb7da0a97 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=937496ea2ab4f3b6bda82b20bd43db80 2500w" />

Compared to the image-to-image workflow, we use the MaskEditor in the `Load Image` node through the right-click menu to draw a mask, then connect it to the `mask` input of the `OpenAI GPT-Image-1` node to complete the workflow.

**Notes**

* The mask and image must be the same size
* When inputting large images, the node will automatically resize the image to an appropriate size

## FAQs

<AccordionGroup>
  <Accordion title="Why can't I find the API nodes?">
    Please update your ComfyUI to the latest version (the latest commit or the latest [desktop version](https://www.comfy.org/download)).
    We may add more API support in the future, and the corresponding nodes will be updated, so please keep your ComfyUI up to date.

    <Tip>
      Please note that you need to distinguish between the nightly version and the release version.
      In some cases, the latest `release` version may not be updated in time compared to the `nightly` version.
      Since we are still iterating quickly, please ensure you are using the latest version when you cannot find the corresponding node.
    </Tip>
  </Accordion>

  <Accordion title="Why can't I use / log in to the API Nodes?">
    API access requires that your current request is based on a secure network environment. The current requirements for API access are as follows:

    * The local network only allows access from `127.0.0.1` or `localhost`, which may mean that you cannot use the API Nodes in a ComfyUI service started with the `--listen` parameter in a LAN environment.
    * Able to access our API service normally (a proxy service may be required in some regions).
    * Your account does not have enough [credits](/interface/credits).
  </Accordion>

  <Accordion title="Why can't I use API node even after logging in, or why does it keep asking me to log in while using?">
    * Currently, only `127.0.0.1` or `localhost` access is supported.
    * Ensure your account has enough credits.
  </Accordion>

  <Accordion title="Can API Nodes be used for free?">
    API Nodes require credits for API calls to closed-source models, so they do not support free usage.
  </Accordion>

  <Accordion title="How to purchase credits?">
    Please refer to the following documentation:

    1. [Comfy Account](/interface/user): Find the `User` section in the settings menu to log in.
    2. [Credits](/interface/credits): After logging in, the settings interface will show the credits menu. You can purchase credits in `Settings` → `Credits`. We use a prepaid system, so there will be no unexpected charges.
    3. Complete the payment through Stripe.
    4. Check if the credits have been updated. If not, try restarting or refreshing the page.
  </Accordion>

  <Accordion title="Are unused credits refundable?">
    Currently, we do not support refunds for credits.
    If you believe there is an error resulting in unused balance due to technical issues, please [contact support](mailto:support@comfy.org).
  </Accordion>

  <Accordion title="Can credits go negative?">
    Credits are not intended to be used as a negative balance or credit line. However, due to race conditions where partner nodes don't always report costs before execution, a single execution may consume more credits than your remaining balance and temporarily result in a negative balance after completion. When your balance is negative, you will not be able to run Partner Nodes until you top up and restore a positive balance. Please ensure you have enough credits before making API calls.
  </Accordion>

  <Accordion title="Where can I check usage and expenses?">
    Please visit the [Credits](/interface/credits) menu after logging in to check the corresponding credits.
  </Accordion>

  <Accordion title="Is it possible to use my own API Key?">
    Currently, the API Nodes are still in the testing phase and do not support this feature yet, but we have considered adding it.
  </Accordion>

  <Accordion title="Do credits expire?">
    No, your credits do not expire.
  </Accordion>

  <Accordion title="Can credits be transferred or shared?">
    No, your credits cannot be transferred to other users and are limited to the currently logged-in account, but we do not restrict the number of devices that can log in.
  </Accordion>

  <Accordion title="Can I use the same account on different devices?">
    We do not limit the number of devices that can log in; you can use your account anywhere you want.
  </Accordion>

  <Accordion title="How can I request for my account or information to be deleted??">
    Email a request to [support@comfy.org](mailto:support@comfy.org) and we will delete your information
  </Accordion>
</AccordionGroup>
