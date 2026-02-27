> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Stability AI Stable Diffusion 3.5 API Node ComfyUI Official Example

> This article will introduce how to use Stability AI Stable Diffusion 3.5 Partner node's text-to-image and image-to-image capabilities in ComfyUI

The [Stability AI Stable Diffusion 3.5 Image](/built-in-nodes/partner-node/image/stability-ai/stability-ai-stable-diffusion-3-5-image) node allows you to use Stability AI's Stable Diffusion 3.5 model to create high-quality, detail-rich image content through text prompts or reference images.

In this guide, we will show you how to set up workflows for both text-to-image and image-to-image generation using this node.

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

## Stability AI Stable Diffusion 3.5 Text-to-Image Workflow

### 1. Workflow File Download

The image below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow.

![Stability AI Stable Diffusion 3.5 Text-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/stable_diffusion_3-5-t2i.png)

### 2. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d56ae409c1f885bb54a8ca91144e3924" alt="Stability AI Stable Diffusion 3.5 Text-to-Image Step Guide" data-og-width="2906" width="2906" data-og-height="1541" height="1541" data-path="images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3fc95a0f3863b12372071e30f7db967 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6385f4d8d5f053a9b608fe4d49917f28 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=71ea0bc7452504f29f729cfc08b9f607 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=48221dfbf9e9eb8728573fe7cb1a147f 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5192b0e55ad55767337260df769cc989 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f3dd577e99c20a7a81e1ddf5bbaa62e6 2500w" />

You can follow the numbered steps in the image to complete the basic text-to-image workflow:

1. (Optional) Modify the `prompt` parameter in the `Stability AI Stable Diffusion 3.5 Image` node to input your desired image description. More detailed prompts often result in better image quality.
2. (Optional) Select the `model` parameter to choose which SD 3.5 model version to use.
3. (Optional) Select the `style_preset` parameter to control the visual style of the image. Different presets produce images with different stylistic characteristics, such as "cinematic" or "anime". Select "None" to not apply any specific style.
4. (Optional) Edit the `String(Multiline)` to modify negative prompts, specifying elements you don't want to appear in the generated image.
5. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation.
6. After the API returns results, you can view the generated image in the `Save Image` node. The image will also be saved to the `ComfyUI/output/` directory.

### 3. Additional Notes

* **Prompt**: The prompt is one of the most important parameters in the generation process. Detailed, clear descriptions lead to better results. Can include elements like scene, subject, colors, lighting, and style.
* **CFG Scale**: Controls how closely the generator follows the prompt. Higher values make the image more closely match the prompt description, but too high may result in oversaturated or unnatural results.
* **Style Preset**: Offers various preset styles for quickly defining the overall style of the image.
* **Negative Prompt**: Used to specify elements you don't want to appear in the generated image.
* **Seed Parameter**: Can be used to reproduce or fine-tune generation results, helpful for iteration during creation.
* Currently the `Load Image` node is in "Bypass" mode. To enable it, refer to the step guide and right-click the node to set "Mode" to "Always" to enable input, switching to image-to-image mode.
* `image_denoise` has no effect when there is no input image.

## Stability AI Stable Diffusion 3.5 Image-to-Image Workflow

### 1. Workflow File Download

The image below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow.

![Stability AI Stable Diffusion 3.5 Image-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/sd3-5-i2i/stable_diffusion_3_5-i2i.png)

Download the image below to use as input
!\[Stability AI Stable Diffusion 3.5 Image-to-Image Workflow Input Image]\(![Stability AI Stable Diffusion 3.5 图生图工作流输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/sd3-5-i2i/input.jpg)

### 2. Complete the Workflow Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3f31575a609f91bd083cc22a99cf3991" alt="Stability AI Stable Diffusion 3.5 Image-to-Image Step Guide" data-og-width="2436" width="2436" data-og-height="1446" height="1446" data-path="images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9f2daefb02ba44d89b0719d823a2d95f 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5e6ace02b6a2b117837959e9f2fe94fa 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e928b22ef9e3ef164f237c2031e74375 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=80a9cf25056d6eeb67f923d785a2467a 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e7fa6441ad2093f0130824c03077d4ff 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2c00041d1f7f670570580d8134180e18 2500w" />

You can follow the numbered steps in the image to complete the image-to-image workflow:

1. Load a reference image through the `Load Image` node, which will serve as the basis for generation.
2. (Optional) Modify the `prompt` parameter in the `Stability AI Stable Diffusion 3.5 Image` node to describe elements you want to change or enhance in the reference image.
3. (Optional) Select the `style_preset` parameter to control the visual style of the image. Different presets produce images with different stylistic characteristics.
4. (Optional|Important) Adjust the `image_denoise` parameter (range 0.0-1.0) to control how much the original image is modified:
   * Values closer to 0.0 make the generated image more similar to the input reference image (at 0.0, it's basically identical to the original)
   * Values closer to 1.0 make the generated image more like pure text-to-image generation (at 1.0, it's as if no reference image was provided)
5. (Optional) Edit the `String(Multiline)` to modify negative prompts, specifying elements you don't want to appear in the generated image.
6. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation.
7. After the API returns results, you can view the generated image in the `Save Image` node. The image will also be saved to the `ComfyUI/output/` directory.

### 3. Additional Notes

The image below shows a comparison of results with and without input image using the same parameter settings:

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=13d41c3d9718abe4d40321b5d9a85b70" alt="Stability AI Stable Diffusion 3.5 With/Without Image Input Comparison" data-og-width="1400" width="1400" data-og-height="700" height="700" data-path="images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b87317f78e02060552894bfe586bcb2c 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=67e2f9597c292ec17a3a9cb80b83c3cc 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d2a40aa65ca5f640fcb5229d6a3c1035 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=425f0b61b27ea3885160969ed294a1e9 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=657ee7666879076cbcd47d8aba120d41 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=07bcc8bf00ade469352cbb56067c819d 2500w" />

**Image Denoise**: This parameter determines how much of the original image's features are preserved during generation. It's the most crucial adjustment parameter in image-to-image mode. The image below shows the effects of different denoising strengths:

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=db7a75bbb9c6151f093fb9881f88a522" alt="Stability AI Stable Diffusion 3.5 Image-to-Image Denoise Strength Explanation" data-og-width="2100" width="2100" data-og-height="1400" height="1400" data-path="images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a3a2d76f4fed07b3016b5a53f43e26b9 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=530d2d1c0bcb789ec9b05f7e20286adf 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=52bd9d150069a3f81a0885a81d2b3590 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=da006a1ef9d06fc15e72d1151cfa7430 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=08a6c0ea76307d1733345b5238e588dd 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=98434f7a1c0823f4217bc3fb5d1d4f04 2500w" />

* **Reference Image Selection**: Choosing images with clear subjects and good composition usually yields better results.
* **Prompt Tips**: In image-to-image mode, prompts should focus more on elements you want to change or enhance, rather than describing everything already present in the image.
* **Mode Switching**: When an input image is provided, the node automatically switches from text-to-image mode to image-to-image mode, and aspect ratio parameters are ignored.

## Related Node Details

You can refer to the documentation below to understand detailed parameter settings for the corresponding node

<Card title="Stability Stable Diffusion 3.5 Image Node Documentation" icon="book" href="/built-in-nodes/partner-node/image/stability-ai/stability-ai-stable-diffusion-3-5-image">
  Stability Stable Diffusion 3.5 Image API Node Documentation
</Card>
