> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Image to Video API Node ComfyUI Official Example

> Learn how to use the Luma Image to Video Partner node in ComfyUI

The [Luma Image to Video](/built-in-nodes/partner-node/video/luma/luma-image-to-video) node allows you to convert static images into smooth, dynamic videos using Luma AI's advanced technology, bringing life and motion to your images.

In this guide, we'll show you how to set up a workflow for image-to-video conversion using this node.

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

## Luma Image to Video Node Documentation

Check out the following documentation to learn more about the node's parameters:

<Card title="Luma Image to Video Node Docs" icon="book" href="/built-in-nodes/partner-node/video/luma/luma-image-to-video">
  Luma Image to Video Partner node documentation
</Card>

<Card title="Luma Concepts Node Docs" icon="book" href="/built-in-nodes/partner-node/video/luma/luma-concepts">
  Luma Concepts Partner node documentation
</Card>

## Image to Video Workflow with Luma API Node

The Luma Image to Video node requires at least one image input (`first_image` or `last_image`) along with text prompts to determine the video's motion effects. In this guide, we've created an example using `first_image` and `luma_concepts` to showcase Luma AI's video generation capabilities.

### 1. Download the Workflow

The workflow information is included in the metadata of the video below. Download and drag it into ComfyUI to load the workflow.

![Luma Image to Video Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2v/luma_i2v.mp4)

Download the following image to use as input:

![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2v/input.png)

### 2. Follow the Workflow Steps

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f55c824ff729382814a2e86e35b9f309" alt="Luma Image to Video Workflow Steps" data-og-width="2492" width="2492" data-og-height="1515" height="1515" data-path="images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=87d66e016ff643f5d0d9e260ffe5f2b3 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6f939ce7a2ebb6f25c9c8a9f896282a4 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4c67f8b817722d7d9cbf51c97b755e6f 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3517730a261ab09b09da43b354a4f181 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f4f6e700862bf6483f1c1fe8bfc3cabc 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2v_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=eb3983d8bd61e7e960ef16bc385706d5 2500w" />

Follow these basic steps to run the workflow:

1. Upload your input image in the `first_image` node
2. (Optional) Write prompts in the Luma Image to Video node to describe how you want the image animated
3. (Optional) Modify the `Luma Concepts` node to control camera movement for professional cinematography
4. Click `Run` or use `Ctrl(cmd) + Enter` to generate the video
5. Once the API returns results, view the generated video in the `Save Video` node. The video will also be saved to the `ComfyUI/output/` directory

### 3. Additional Notes

* **Image Input Requirements**: At least one of `first_image` or `last_image` is required, with a maximum of 1 image per input
* **Luma Concepts**: Controls camera movement for professional video effects
* **Seed Parameter**: Only determines if the node should rerun, doesn't affect generation results
* **Enable Input Nodes**: Right-click on purple "Bypass" mode nodes and set "mode" to "always" to enable inputs
* **Model Selection**: Different video generation models have unique characteristics, adjustable via the model parameter
* **Resolution and Duration**: Adjust output video resolution and length using resolution and duration parameters
