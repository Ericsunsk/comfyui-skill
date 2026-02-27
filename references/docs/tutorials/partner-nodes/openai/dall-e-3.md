> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI DALL·E 3 Node

> Learn how to use the OpenAI DALL·E 3 Partner node to generate images in ComfyUI

OpenAI DALL·E 3 is part of the ComfyUI Partner Nodes series, allowing users to generate images through OpenAI's **DALL·E 3** model. This node supports text-to-image generation functionality.

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1d4da35db8baddcd1321ef98365e26d0" alt="OpenAI DALL·E 3 node screenshot" data-og-width="1576" width="1576" data-og-height="966" height="966" data-path="images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c4991a2a05a37c4f63b9251cc4f5cb66 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=bdb4fb6d52ed938a4a6f3dfb830e79f2 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f4de073cc71e3209f66be6eb0f45a575 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e525c1ca97e0ee9bd5e0b812e812530d 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d50bd7dabc5e9e5adca0683bc6777de4 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b1867a36a2203ad0a1b2fba9117a42ec 2500w" />

## Node Overview

DALL·E 3 is OpenAI's latest image generation model, capable of creating detailed and high-quality images based on text prompts. Through this node in ComfyUI, you can directly access DALL·E 3's generation capabilities without leaving the ComfyUI interface.

The **OpenAI DALL·E 3** node generates images synchronously through OpenAI's image generation API. It receives text prompts and returns images that match the description.

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

## Parameter Details

### Required Parameters

| Parameter | Type | Description                                                                                                                  |
| --------- | ---- | ---------------------------------------------------------------------------------------------------------------------------- |
| prompt    | Text | Text prompt for generating images. Supports multi-line input, can describe in detail the image content you want to generate. |

### Widget Parameters

| Parameter | Type    | Options                         | Default Value | Description                                                                                                                               |
| --------- | ------- | ------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| seed      | Integer | 0-2147483647                    | 0             | Random seed used to control the generation result                                                                                         |
| quality   | Option  | standard, hd                    | standard      | Image quality setting. The "hd" option generates higher quality images but may require more computational resources                       |
| style     | Option  | natural, vivid                  | natural       | Image style. "Vivid" tends to generate hyperrealistic and dramatic images, while "natural" produces more natural, less exaggerated images |
| size      | Option  | 1024x1024, 1024x1792, 1792x1024 | 1024x1024     | Size of the generated image. You can choose square or rectangular images in different orientations                                        |

## Usage Examples

You can download the image below and drag it into ComfyUI to load the corresponding workflow
![ComfyUI openai-dall-e-3 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-3/text2image.png)

Since the corresponding workflow is very simple, you can also directly add the **OpenAI DALL·E 3** node in ComfyUI, input the description of the image you want to generate, and then run the workflow

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=29cd1bbda083d98eb24196d554586c43" alt="ComfyUI openai-dall-e-3 workflow" data-og-width="2308" width="2308" data-og-height="1059" height="1059" data-path="images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=80240ed5377b1c5215e92795dd950b86 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2b522272027cc91a93db758416496694 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66c4318cfa7a4b18b34a18122cd34116 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=398e16e036cc013d9774512302038da7 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8df52f2b31d8d1c39306f259007c5659 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=401dc6e74fc88045c42dbf90557fd82f 2500w" />

1. Add the **OpenAI DALL·E 3** node in ComfyUI
2. Enter the description of the image you want to generate in the prompt text box
3. Adjust optional parameters as needed (quality, style, size, etc.)
4. Run the workflow to generate the image

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
