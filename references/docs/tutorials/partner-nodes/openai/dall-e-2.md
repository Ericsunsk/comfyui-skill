> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI DALL·E 2 Node

> Learn how to use the OpenAI DALL·E 2 Partner node to generate images in ComfyUI

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=42a0b800a337494eebec116cfea8d71a" alt="OpenAI DALL·E 2 node screenshot" data-og-width="1576" width="1576" data-og-height="954" height="954" data-path="images/comfy_core/api_nodes/openai-dall-e-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6ecf05f49bca8201e70d91bf6c39e2c5 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5d03fc5dc0289a0219f278b0747bf2b4 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9d8742d23f44e4a6f2752bd0126f6fd0 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=41023d403a268fed8120a91446837843 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=41fd9ca39c2d652fcaed9889c2ed3b59 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8434b4a8a25e5b2d86286d44d31a778a 2500w" />

OpenAI DALL·E 2 is part of the ComfyUI Partner Nodes series, allowing users to generate images through OpenAI's **DALL·E 2** model.

This node supports:

* Text-to-image generation
* Image editing functionality (inpainting through masks)

## Node Overview

The **OpenAI DALL·E 2** node generates images synchronously through OpenAI's image generation API. It receives text prompts and returns images that match the description.

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

| Parameter | Description                                                   |
| --------- | ------------------------------------------------------------- |
| `prompt`  | Text prompt describing the image content you want to generate |

### Widget Parameters

| Parameter | Description                                                                | Options/Range                     | Default Value |
| --------- | -------------------------------------------------------------------------- | --------------------------------- | ------------- |
| `seed`    | Seed value for image generation (currently not implemented in the backend) | 0 to 2^31-1                       | 0             |
| `size`    | Output image dimensions                                                    | "256x256", "512x512", "1024x1024" | "1024x1024"   |
| `n`       | Number of images to generate                                               | 1 to 8                            | 1             |

### Optional Parameters

| Parameter | Description                                | Options/Range   | Default Value |
| --------- | ------------------------------------------ | --------------- | ------------- |
| `image`   | Optional reference image for image editing | Any image input | None          |
| `mask`    | Optional mask for local inpainting         | Mask input      | None          |

## Usage Method

## Workflow Examples

This Partner node currently supports two workflows:

* Text to Image
* Inpainting

<Note>
  Image to Image workflow is not supported
</Note>

### Text to Image Example

The image below contains a simple text-to-image workflow. Please download the corresponding image and drag it into ComfyUI to load the workflow.
![ComfyUI openai-dall-e-2 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-2/text2image.png)

The corresponding example is very simple
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cd0262919a3be35855c9891b6de8c9c0" alt="ComfyUI openai-dall-e-2 workflow example" data-og-width="3086" width="3086" data-og-height="1423" height="1423" data-path="images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=766a95093f1ef90769a2e02718dd27a8 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=315f7cb9d4b49293c18476e725869615 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1f52369d732c2040e395861d57fca2ba 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=60d125ab1c8f9759cda7a14a81fbedd1 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=dd64dbeec33bba7c9329dcb56746cf41 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=135961dddf3f7b28a431a5a92899db51 2500w" />

You only need to load the `OpenAI DALL·E 2` node, input the description of the image you want to generate in the `prompt` node, connect a `Save Image` node, and then run the workflow.

### Inpainting Workflow

DALL·E 2 supports image editing functionality, allowing you to use a mask to specify the area to be replaced. Below is a simple inpainting workflow example:

#### 1. Workflow File Download

Download the image below and drag it into ComfyUI to load the corresponding workflow.

![ComfyUI openai-dall-e-2 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-2/inpainting.png)

We will use the image below as input:
![ComfyUI openai-dall-e-2 workflow input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-2/input.jpg)

#### 2. Workflow File Usage Instructions

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=29719686459aadec1d533f8fe26e0370" alt="ComfyUI openai-dall-e-2 workflow example" data-og-width="3609" width="3609" data-og-height="1425" height="1425" data-path="images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bb303fab72131dd5d985117514275fea 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cb22d377322c4e1db0d9866ee9c46843 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1eb5f9818cfc708f620a4e8861b64b83 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=719e8e5bd24b645cbae7c36aee1ee03e 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f4a7e78a2c9be90d26800628267ab236 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0aaad83a58eb9bd3beed8ee0afa5b959 2500w" />

Since this workflow is relatively simple, if you want to manually implement the corresponding workflow yourself, you can follow the steps below:

1. Use the `Load Image` node to load the image
2. Right-click on the load image node and select `MaskEditor`
3. In the mask editor, use the brush to draw the area you want to redraw
4. Connect the loaded image to the `image` input of the **OpenAI DALL·E 2** node
5. Connect the mask to the `mask` input of the **OpenAI DALL·E 2** node
6. Edit the prompt in the `prompt` node
7. Run the workflow

**Notes**

* If you want to use the image editing functionality, you must provide both an image and a mask (both are required)
* The mask and image must be the same size
* When inputting large images, the node will automatically resize the image to an appropriate size
* The URLs returned by the API are valid for a short period, please save the results promptly
* Each generation consumes credits, charged according to image size and quantity

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
