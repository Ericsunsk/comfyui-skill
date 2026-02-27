> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Ideogram 3.0 API Node Official Examples

> This guide covers how to use the Ideogram 3.0 Partner node in ComfyUI

Ideogram 3.0 is a powerful text-to-image model by Ideogram, known for its photorealistic quality, accurate text rendering, and consistent style control.

The [Ideogram V3](/built-in-nodes/partner-node/image/ideogram/ideogram-v3) node currently supports two modes:

* Text-to-Image mode
* Image Editing mode (when both image and mask inputs are provided)

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

## Ideogram 3.0 Node Documentation

Check the following documentation for detailed node parameter settings:

* [Ideogram V3](/built-in-nodes/partner-node/image/ideogram/ideogram-v3)

## Ideogram 3.0 API Node Text-to-Image Mode

When using [Ideogram V3](/built-in-nodes/partner-node/image/ideogram/ideogram-v3) without image and mask inputs, the node operates in Text-to-Image mode.

### 1. Download Workflow File

Download and drag the following file into ComfyUI to load the workflow:

![Ideogram 3.0 ComfyUI Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/ideogram/v3/ideogram_v3_t2i.png)

### 2. Complete the Workflow Steps

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3f51da844d34d588570a037c3ef7a264" alt="Ideogram 3.0 Workflow Steps" data-og-width="2037" width="2037" data-og-height="1250" height="1250" data-path="images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=fb13382fe73f03cb4c7ce1e863ce4097 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a849b6be7e0a3149ef1ed52c58109eac 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cce20da548057f45ea7ed32691d6e10e 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=48413ebebe11db98eaf9f0858b0ee76c 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b87b10ed4fc43827aa9b213cb48a816d 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/ideogram/ideogram_v3_t2i.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=07083fad209c20ec07201c3e7ac45721 2500w" />

Follow the numbered steps to complete the basic workflow:

1. Enter your image description in the `prompt` field of the `Ideogram V3` node
2. Click `Run` or use shortcut `Ctrl(cmd) + Enter` to generate the image
3. After the API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory

## Ideogram 3.0 API Node Image Editing Mode

\[To be updated]
