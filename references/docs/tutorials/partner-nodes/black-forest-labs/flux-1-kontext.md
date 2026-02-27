> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Flux.1 Kontext Pro Image API Node Official Example

> This guide will show you how to use the Flux.1 Kontext Pro Image Partner node in ComfyUI to perform image editing

FLUX.1 Kontext is a professional image-to-image editing model developed by Black Forest Labs, focusing on intelligent understanding of image context and precise editing.
It can perform various editing tasks without complex descriptions, including object modification, style transfer, background replacement, character consistency editing, and text editing.
The core advantage of Kontext lies in its excellent context understanding ability and character consistency maintenance, ensuring that key elements such as character features and composition layout remain stable even after multiple iterations of editing.

Currently, ComfyUI has supported two models of Flux.1 Kontext:

* **Kontext Pro** is ideal for editing, composing, and remixing.
* **Kontext Max** pushes the limits on typography, prompt precision, and speed.

In this guide, we will briefly introduce how to use the Flux.1 Kontext Partner nodes to perform image editing through corresponding workflows.

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

## Flux.1 Kontext Multiple Image Input Workflow

We have recently updated to support multiple image input workflows. Using the new `Image Stitch` node, you can stitch multiple images into a single image and edit it using Flux.1 Kontext.

### 1. Workflow File Download

The `metadata` of the images below contains the workflow information. Please download and drag them into ComfyUI to load the corresponding workflow.

![ComfyUI Flux.1 Kontext Pro Image API Node Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/multiple_image_input.png)

Download the following images for input or use your own images:

![ComfyUI Flux.1 Kontext Pro Image API Node Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/girl.jpg)
![ComfyUI Flux.1 Kontext Pro Image API Node Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/dog.jpg)
![ComfyUI Flux.1 Kontext Pro Image API Node Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/sofa.jpg)

### 2. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bf6e2ac1877f37556b354699f1960129" alt="ComfyUI Flux.1 Kontext Pro Image API Node Workflow Steps" data-og-width="3256" width="3256" data-og-height="1326" height="1326" data-path="images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7f8a0ed32e4444d8bf7108e335cd6f05 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7cf0b90ebc65bb64ba464ea3c30bb300 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c545b6d0e39738cd9959cf6de208e751 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=fefb762d6f91c69481f72013e8c39f06 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3517ea12027f6c06c69696c0acdadc5d 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cdb684fa104961afe449e47ff6f72eaf 2500w" />

You can follow the numbered steps in the image to complete the workflow:

1. Upload the provided images in the `Load image` node
2. Modify the necessary parameters in `Flux.1 Kontext Pro Image`:
   * `prompt` Enter the prompt for the image you want to edit
   * `aspect_ratio` Set the aspect ratio of the original image, which must be between 1:4 and 4:1
   * `prompt_upsampling` Set whether to use prompt upsampling. If enabled, it will automatically modify the prompt to get richer results, but the results are not reproducible
3. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image editing
4. After waiting for the API to return results, you can view the edited image in the `Save Image` node, and the corresponding image will also be saved to the `ComfyUI/output/` directory

<Tip>
  The subsequent two workflows only differ in the Partner nodes used. In fact, you only need to modify based on the multiple image input workflow, with no significant differences
</Tip>

## Flux.1 Kontext Pro Image API Node Workflow

### 1. Workflow File Download

The `metadata` of the image below contains the workflow information. Please download and drag it into ComfyUI to load the corresponding workflow.

![ComfyUI Flux.1 Kontext Pro Image API Node Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_pro_image.png)

Download the image below for input or use your own image:

![ComfyUI Flux.1 Kontext Pro Image API Node Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_pro_image_input.png)

### 2. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ff2c42a34894ae54e32a24058ad12755" alt="ComfyUI Flux.1 Kontext Pro Image API Node Workflow Steps" data-og-width="2058" width="2058" data-og-height="1155" height="1155" data-path="images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ea8dbd24df6ed72d7819de96823e92b6 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=08a7e0dbfa39801a533ca2df037271f0 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=95f6734754ec5350ec8e54145e331037 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6ab34242b1b7fd2370f75d6ca31e8b02 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e056cecb55441fcc233c0257040ed298 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=286093e893c5171fdac45dc649fa5d95 2500w" />

You can follow the numbered steps in the image to complete the workflow:

1. Load the image you want to edit in the `Load Image` node
2. (Optional) Modify the necessary parameters in `Flux.1 Kontext Pro Image`
3. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image editing
4. After waiting for the API to return results, you can view the edited image in the `Save Image` node, and the corresponding image will also be saved to the `ComfyUI/output/` directory

## Flux.1 Kontext Max Image API Node Workflow

### 1. Workflow File Download

The `metadata` of the image below contains the workflow information. Please download and drag it into ComfyUI to load the corresponding workflow.

![ComfyUI Flux.1 Kontext Max Image API Node Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_max_image.png)

Download the image below for input or use your own image for demonstration:

![ComfyUI Flux.1 Kontext Max Image API Node Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_max_image_input.png)

### 2. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3f91d4f54822bef88bca4e7024170950" alt="ComfyUI Flux.1 Kontext Max Image API Node Workflow Steps" data-og-width="2132" width="2132" data-og-height="1209" height="1209" data-path="images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a0974111de4d56ee290f83b38764bc44 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=25172a52bda142d3a0a6f332c93ff287 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=389e34b12c1f14bbfdb045ec3de673db 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b72386f9f1950894a91f81f4ad0eedd2 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4c616381e3a7b5092c0fb6d1ae643364 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9076344039b8541827bdb0b8bc092d5d 2500w" />

You can follow the numbered steps in the image to complete the workflow:

1. Load the image you want to edit in the `Load Image` node
2. (Optional) Modify the necessary parameters in `Flux.1 Kontext Max Image`
3. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image editing
4. After waiting for the API to return results, you can view the edited image in the `Save Image` node, and the corresponding image will also be saved to the `ComfyUI/output/` directory

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
