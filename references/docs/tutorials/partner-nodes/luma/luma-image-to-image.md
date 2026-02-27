> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Image to Image API Node ComfyUI Official Example

> This guide covers how to use the Luma Image to Image Partner node in ComfyUI

The [Luma Image to Image](/built-in-nodes/partner-node/image/luma/luma-image-to-image) node allows you to modify existing images based on text prompts using Luma AI technology, while preserving certain features and structures from the original image.

In this guide, we'll show you how to set up an image-to-image workflow using this node.

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

## Luma Image to Image Node Documentation

Check the following documentation for detailed node parameter settings:

<Card title="Luma Image to Image Node Documentation" icon="book" href="/built-in-nodes/partner-node/image/luma/luma-image-to-image">
  Luma Image to Image API Node Documentation
</Card>

## Luma Image to Image API Node Workflow

<Tip>
  This feature works well for changing objects and shapes. However, it may not be ideal for color changes. We recommend using lower weight values, around 0.0 to 0.1.
</Tip>

### 1. Download Workflow File

Download and drag the following image into ComfyUI to load the workflow (workflow information is included in the image metadata):

![Luma Image to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2i/luma_i2i.png)

Download this image to use as input:

![Luma Image to Image Workflow Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2i/input.png)

### 2. Complete the Workflow Steps

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0169a042868519a3cd76ef832fdc714a" alt="Luma Image to Image Workflow Steps" data-og-width="2577" width="2577" data-og-height="1139" height="1139" data-path="images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d8384233bba5478b0c86cfc9decc214f 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=54c9dad2fe0366b78de2adc1993c1323 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3fd59ee81bfac6a5ecda6aa722f8d102 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d13fff5d7609ac2fa5805b6849635c88 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7b3d318fc1eb089f8ff39b63bf4ff8ee 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0ddc3da1e3aeb0b4c3f9bff7e0407975 2500w" />

Follow these numbered steps:

1. Click **Upload** on the `Load Image` node to upload your input image
2. (Optional) Modify the workflow prompts
3. (Optional) Adjust `image_weight` to change input image influence (lower values stay closer to original)
4. Click `Run` or use shortcut `Ctrl(cmd) + Enter` to generate the image
5. After API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory

### 3. Results with Different `image_weight` Values

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d6fc32e5bdbf4f1368f73cfac583643d" alt="Weight Comparison" data-og-width="3150" width="3150" data-og-height="1173" height="1173" data-path="images/tutorial/api_nodes/luma/i2i_image_weight.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=084939a3ef759130180a46e36b0b240c 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=359a906ca12d76263eba36a4e55185c0 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=826d2123c3c5f8497e92b3f977bfaac7 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=dcf51db85f394a66dffadbf651eeba7b 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=563736803d4fa3ec5e92d9c0f05ec5cb 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7403afda95b9ca243af876284db65271 2500w" />
