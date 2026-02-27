> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Runway API Node Image Generation ComfyUI Official Example

> This article will introduce how to use Runway nodes in ComfyUI for text-to-image and reference-to-image generation

Runway is a company focused on generative AI, providing powerful image generation capabilities. Its models support features such as style transfer, image extension, and detail control. Currently, ComfyUI has integrated the Runway API, allowing you to directly use the related nodes in ComfyUI for image generation.

In this guide, we will walk you through the following workflows:

* Text-to-image
* Reference-to-image

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

## Runway Image Text-to-Image Workflow

### 1. Workflow File Download

The image below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow.

![ComfyUI Runway Image Text to Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/text_to_image.png)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66f4bf5de975a5f0302d930e352605ff" alt="ComfyUI Runway Image Text to Image Step Guide" data-og-width="2842" width="2842" data-og-height="1260" height="1260" data-path="images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=126eb9ab59ac3fa69464dcca17d562c9 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4a77fa7bbaf5dc855339285e728bc27a 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=73094b95981662d3901cd4510050449b 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a604909a3fa461af35535f68ead78758 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4951668dc502679fe8d2c0e229330b28 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1c41ecbce818d39424610c0a5ee21efa 2500w" />

You can refer to the numbers in the image to complete the basic text-to-image workflow execution:

1. In the `Runway Text to Image` node, input your prompt in the `prompt` field
2. (Optional) Adjust the `ratio` setting to set different output aspect ratios
3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute image generation.
4. After waiting for the API to return results, you can view the generated image in the `Save Image` node (right-click to save). The corresponding image will also be saved to the `ComfyUI/output/` directory.

## Runway Image Reference-to-Image Workflow

### 1. Workflow and Input Image Download

The image below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow.

![ComfyUI Runway Image Reference to Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/reference_to_image/runway_reference_to_image.png)

Download the image below for input

![ComfyUI Runway Image Reference to Image Input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/reference_to_image/input.png)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f0ce702cc2a6a03d887072416d78c241" alt="ComfyUI Runway Image Reference to Image Step Guide" data-og-width="2842" width="2842" data-og-height="1260" height="1260" data-path="images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=696ef8ecc46427bd46c7830c11b24f49 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1956bc38e424e3e757f63ee07fa88957 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8d03e7a6eca51b29251bf9606b86e351 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=894ba54fbd13795bac0e847936fed65c 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=423127ac47ecb8310a3a451a35b4e522 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c97748843c91858030259f11b2ad526e 2500w" />

You can refer to the numbers in the image to complete the basic reference-to-image workflow execution:

1. In the `Load Image` node, load the provided input image
2. In the `Runway Text to Image` node, input your prompt in the `prompt` field and adjust dimensions
3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute image generation.
4. After waiting for the API to return results, you can view the generated image in the `Save Image` node (right-click to save). The corresponding image will also be saved to the `ComfyUI/output/` directory.
