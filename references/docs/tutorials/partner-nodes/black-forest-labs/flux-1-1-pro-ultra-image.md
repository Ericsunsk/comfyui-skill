> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux 1.1 Pro Ultra Image API Node ComfyUI Official Workflow Examples

> This guide covers how to use the Flux 1.1 Pro Ultra Image Partner node in ComfyUI

FLUX 1.1 Pro Ultra is a high-performance AI image generation tool by BlackForestLabs, featuring ultra-high resolution and efficient generation capabilities. It supports up to 4MP resolution (4x the standard version) while keeping single image generation time under 10 seconds - 2.5x faster than similar high-resolution models.

The tool offers two core modes:

* **Ultra Mode**: Designed for high-resolution needs, perfect for advertising and e-commerce where detail magnification is important. It accurately reflects prompts while maintaining generation speed.
* **Raw Mode**: Focuses on natural realism, optimizing skin tones, lighting, and landscape details. Reduces the "AI look" and is ideal for photography and realistic style creation.

We now support the Flux 1.1 Pro Ultra Image node in ComfyUI. This guide will cover:

* Flux 1.1 Pro Text-to-Image
* Flux 1.1 Pro Image-to-Image (Remix)

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

## Flux 1.1 Pro Ultra Image Node Documentation

Check the following documentation for detailed node parameter settings:

* [Flux 1.1 Pro Ultra Image](/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg)

## Flux 1.1 \[pro] Text-to-Image Tutorial

### 1. Download Workflow File

Download and drag the following file into ComfyUI to load the workflow:

![Flux 1.1 pro Text-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_t2i.png)

### 2. Complete the Workflow Steps

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b9403dd3baf434686961672addef2a39" alt="Workflow Steps" data-og-width="3030" width="3030" data-og-height="1370" height="1370" data-path="images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1dcf01f603e0a9405e06db0f203f6b2b 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=475c7975f874a7fb2bc09755400ac4e0 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2d73cf69387fdf0e83acebf0361a8ceb 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a59ca6310db555c0f8a3be86b7f76f42 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c1790db75c5aaf75635767c055599d12 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=fae50fb73c4fa303b17c6a4ee900bcfd 2500w" />

Follow the numbered steps to complete the basic workflow:

1. (Optional) Modify the prompt in the `Flux 1.1 [pro] Ultra Image` node
2. (Optional) Set `raw` parameter to `false` for more realistic output
3. Click `Run` or use shortcut `Ctrl(cmd) + Enter` to generate the image
4. After the API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory

## Flux 1.1\[pro] Image-to-Image Tutorial

When adding an `image_prompt` to the node input, the output will blend features from the input image (Remix). The `image_prompt_strength` value affects the blend ratio: higher values make the output more similar to the input image.

### 1. Download Workflow File

Download and drag the following file into ComfyUI, or right-click the purple node in the Text-to-Image workflow and set `mode` to `always` to enable `image_prompt` input:

![Flux 1.1 pro Image-to-Image Remix](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_i2i.png)

We'll use this image as input:
![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-3/text2image.png)

### 2. Complete the Workflow Steps

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0217606be6c3f599e3d6ebd2fb14829a" alt="Workflow Steps" data-og-width="2825" width="2825" data-og-height="1076" height="1076" data-path="images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ea1043fe60afb4874f2a0cfa7bfaaf88 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a326c96e4efbd900ad8889d6664465e6 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1583add49f0c0dd731630ddab7564d9c 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=61e7728a9cf17f93396d1af290ae15af 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2dbfbff8d7cb2552ed5daad1e6d1e8c6 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ea4e5fc6ce0dd3dfa287970ed4bc7b29 2500w" />

Follow these numbered steps:

1. Click **Upload** on the `Load Image` node to upload your input image
2. (Optional) Adjust `image_prompt_strength` in `Flux 1.1 [pro] Ultra Image` to change the blend ratio
3. Click `Run` or use shortcut `Ctrl(cmd) + Enter` to generate the image
4. After the API returns results, view the generated image in the `Save Image` node. Images are saved to the `ComfyUI/output/` directory

Here's a comparison of outputs with different `image_prompt_strength` values:
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=eea7014b92e63f0b8d1bb50d5dae11c3" alt="Comparison" data-og-width="3150" width="3150" data-og-height="1173" height="1173" data-path="images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c3fd516ee3fbd72d0d7d5d408a2e3841 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4988d52a69ca1108662a380aabfc3bec 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b85cf288f13cad89155e50242583eb1a 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=24dd19e8afa467fb104b8dd75352afd6 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66c3a578ec5b785123d53d9bfa5b3b29 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4e199e171ba2aaf90d64bc1e911cd2b0 2500w" />
