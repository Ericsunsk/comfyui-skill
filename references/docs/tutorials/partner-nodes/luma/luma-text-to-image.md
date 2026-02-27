> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Text to Image API Node ComfyUI Official Example

> This guide explains how to use the Luma Text to Image Partner node in ComfyUI

The [Luma Text to Image](/built-in-nodes/partner-node/image/luma/luma-text-to-image) node allows you to generate high-quality images from text prompts using Luma AI's advanced technology, capable of creating photorealistic content and artistic style images.

In this guide, we'll show you how to set up workflows using this node for text-to-image generation.

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

## Luma Text to Image Node Documentation

You can refer to the following documentation for detailed parameter settings:

<Card title="Luma Text to Image Node Documentation" icon="book" href="/built-in-nodes/partner-node/image/luma/luma-text-to-image">
  Luma Text to Image API Node Documentation
</Card>

<Card title="Luma Reference Node Documentation" icon="book" href="/built-in-nodes/partner-node/image/luma/luma-reference">
  Luma Reference API Node Documentation
</Card>

## Luma Text to Image API Node Workflow

When the `Luma Text to Image` node is used without any image inputs, it functions as a text-to-image workflow. In this guide, we've created examples using `style_image` and `image_luma_ref` to showcase Luma AI's excellent image processing capabilities.

### 1. Download Workflow Files

The workflow information is included in the metadata of the image below. Download and drag it into ComfyUI to load the workflow.

![Luma Text to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/luma_t2i.png)

Please download these images for input:

![Input Image - Reference](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/input_ref.png)
![Input Image - Style](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/input_style.png)

### 2. Follow Steps to Run the Workflow

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3122c711034e8270d086ae8c139cb64" alt="Luma Text to Image Workflow Steps" data-og-width="2796" width="2796" data-og-height="1694" height="1694" data-path="images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=34ce72b35a6ce916e2a7cf68bf4d7fab 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b76ef973b5623f2575f08f49279a2c96 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9dbd9de85a6331dbc3dcc0c231adc666 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=870888519eeb09fdabafdf4b867be154 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=69acf9a0fa4ce079286baa22ba66be8d 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=82a2b77c63649c49c8ceae305f539915 2500w" />

Follow the numbered steps in the image to complete the basic workflow:

1. Upload the reference image in the `Load image` node
2. Upload the style reference image in the `Load image (renamed to styleref)` node
3. (Optional) Modify the prompts in the `Luma Text to Image` node
4. (Optional) Adjust the `style_image_weight` to control the style reference image's influence
5. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to generate the image
6. After the API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7f47d2d3a6acdde87df046460afa393f" alt="Style Image Weight Comparison" data-og-width="2100" width="2100" data-og-height="1867" height="1867" data-path="images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=155cadfd9a346447a26ece679de9b2b8 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e2b792354983726d5c33e3c69f8273a5 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0bbb226eb88b380096e0a52238f80898 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1889cb637e62fdcc7b2be4b7ee925355 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7d237e41b44d0249359126ae88c8d1c6 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5e6f5eb502e8347dc1267d7bff119215 2500w" />

### 3. Additional Notes

* The [node](/built-in-nodes/partner-node/image/luma/luma-text-to-image) allows up to 4 reference images and character references simultaneously.
* To enable multiple image inputs, right-click on the purple "Bypassed" nodes and set their `mode` to `always`
