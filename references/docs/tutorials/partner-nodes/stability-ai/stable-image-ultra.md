> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Stability AI Stable Image Ultra API Node ComfyUI Official Example

> This article will introduce how to use the Stability AI Stable Image Ultra Partner node's text-to-image and image-to-image capabilities in ComfyUI

The [Stability Stable Image Ultra](/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-ultra.jpg) node allows you to use Stability AI's Stable Image Ultra model to create high-quality, detailed image content through text prompts or reference images.

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

## Stability AI Stable Image Ultra Text-to-Image Workflow

### 1. Workflow File Download

The workflow information is included in the metadata of the image below. Please download and drag it into ComfyUI to load the corresponding workflow.

![Stability AI Stable Image Ultra Text-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/stable_image_ultra_t2i.png)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bbbb22660e1757bfba34771d438e968d" alt="Stability AI Stable Image Ultra Text-to-Image Step Guide" data-og-width="2366" width="2366" data-og-height="959" height="959" data-path="images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cf51af0c2f320a2f05286ebd71ef883c 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c087debb849a1e5f4af365113850d9b5 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a441c8deeef138d41a2a212a70e38084 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=912ac3ba2ee9ce14a54e5ac52141bcce 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=167f4386090ad7a7d80b0e8051557dbf 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b47f2835f4939457adb23d1429389271 2500w" />

You can follow the numbered steps in the image to complete the basic text-to-image workflow:

1. (Optional) Modify the `prompt` parameter in the `Stability AI Stable Image Ultra` node to input your desired image description. More detailed prompts often lead to better image quality. You can use the `(word:weight)` format to control specific word weights, for example: `The sky was crisp (blue:0.3) and (green:0.8)` indicates the sky is blue and green, but green is more prominent.
2. (Optional) Select the `style_preset` parameter to control the visual style of the image. Different preset styles will produce images with different stylistic characteristics, such as "cinematic", "anime", etc. Selecting "None" will not apply any specific style.
3. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation.
4. After the API returns the result, you can view the generated image in the `Save Image` node, and the image will also be saved to the `ComfyUI/output/` directory.

### 3. Additional Notes

* **Prompt**: The prompt is one of the most important parameters in the generation process. Detailed, clear descriptions will lead to better results. It can include elements like scene, subject, colors, lighting, and style.
* **Style Preset**: Provides multiple preset styles such as cinematic, anime, digital art, etc., which can quickly define the overall style of the image.
* **Negative Prompt**: Used to specify elements you don't want to appear in the generated image, helping avoid common issues like extra limbs or distorted faces.
* **Seed Parameter**: Can be used to reproduce or fine-tune generation results, helpful for iteration during the creative process.
* Currently, the `Load Image` node is in "Bypass" mode. To enable it, refer to the step guide and right-click on the corresponding node to set "Mode" to "Always" to enable input, which will switch to image-to-image mode.

## Stability AI Stable Image Ultra Image-to-Image Workflow

### 1. Workflow File Download

The workflow information is included in the metadata of the image below. Please download and drag it into ComfyUI to load the corresponding workflow.

![Stability Stable Image Ultra Image-to-Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/i2i/stable_image_ultra_i2i.png)

Download the image below which we will use as input
![Stability Stable Image Ultra Image-to-Image Workflow Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/i2i/input.png)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=90799d9abc85f845d786eac7f204f778" alt="Stability Stable Image Ultra Image-to-Image Step Guide" data-og-width="2366" width="2366" data-og-height="959" height="959" data-path="images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2c343c6ac266e26c96fc27cb4a48e1d6 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bf35f2db6f76912b4b443b81e5ffdde1 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=dbc6c0ae0b2f44e2ed9c0eeab2643693 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0d0b599d4dee680889ccab25c18a6e90 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=56f6fd121ece0e1e7aedb8758beedd98 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a1f259d1251093d0ae76fdad82d6a3c7 2500w" />

You can follow the numbered steps in the image to complete the image-to-image workflow:

1. Load a reference image through the `Load Image` node, which will serve as the basis for generation.
2. (Optional) Modify the `prompt` parameter in the `Stability Stable Image Ultra` node to describe elements you want to change or enhance in the reference image.
3. (Optional) Adjust the `image_denoise` parameter (range 0.0-1.0) to control the degree of modification to the original image:
   * Values closer to 0.0 will make the generated image more similar to the input reference image
   * Values closer to 1.0 will make the generated image more like pure text-to-image generation
4. (Optional) You can also set `style_preset` and other parameters to further control the generation effect.
5. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the image generation.
6. After the API returns the result, you can view the generated image in the `Save Image` node, and the image will also be saved to the `ComfyUI/output/` directory.

### 3. Additional Notes

**Image Denoise**: This parameter determines how much of the original image's features are preserved during generation, and is the most crucial adjustment parameter in image-to-image mode. The image below shows the effects of different denoising strengths

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8cb266b02864aff7664f56bb1d0e8890" alt="Stability Stable Image Ultra Image-to-Image Denoise Explanation" data-og-width="2100" width="2100" data-og-height="1400" height="1400" data-path="images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=38d6772021197d309aeea0b412187d16 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5dcd1d04635b534f9b9574904102857b 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a6bae9f044fe9ea86e11e92b6378e5fa 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8c75d228c89aa01a470e45e108bdce71 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d0864c9de07f0aedcb22b88f71392f95 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5c759a07cf3ed8d4212f151afbe676be 2500w" />

* **Reference Image Selection**: Choosing images with clear subjects and good composition usually leads to better results.
* **Prompt Tips**: In image-to-image mode, prompts should focus more on what you want to change or enhance, rather than describing all elements already present in the image.

## Related Node Documentation

You can refer to the documentation below for detailed parameter settings and more information about the corresponding nodes

<Card title="Stability Stable Image Ultra Node Documentation" icon="book" href="/built-in-nodes/partner-node/image/stability-ai/stability-ai-stable-image-ultra">
  Stability Stable Image Ultra API Node Documentation
</Card>
