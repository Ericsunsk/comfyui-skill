> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Image Upscale Workflow

> This guide explains the concept of image upscaling in AI drawing and demonstrates how to implement an image upscaling workflow in ComfyUI

## What is Image Upscaling?

Image Upscaling is the process of converting low-resolution images to high-resolution using algorithms.
Unlike traditional interpolation methods, AI upscaling models (like ESRGAN) can intelligently reconstruct details while maintaining image quality.

For instance, the default SD1.5 model often struggles with large-size image generation.
To achieve high-resolution results,we typically generate smaller images first and then use upscaling techniques.

This article covers one of many upscaling methods in ComfyUI. In this tutorial, we'll guide you through:

1. Downloading and installing upscaling models
2. Performing basic image upscaling
3. Combining text-to-image workflows with upscaling

<Note>
  Looking for more advanced upscaling options? Check out our comprehensive [Image Upscaling Guide](/tutorials/utility/image-upscale) which covers various models and use cases including portrait enhancement, product photography, and more.
</Note>

## Upscaling Workflow

### Model Installation

Required ESRGAN models download:

<Steps>
  <Step title="Visit OpenModelDB">
    Visit [OpenModelDB](https://openmodeldb.info/) to search and download upscaling models (e.g., RealESRGAN)

        <img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e5a63a5efe9b72af78d7331179cef6ba" alt="openmodeldb" data-og-width="1200" width="1200" data-og-height="1209" height="1209" data-path="images/tutorial/basic/upscale/upscale_OpenModelDB.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ed2e223f6fdf3841a3268e3925c214ca 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e5a012d3e1827c0033d192b40e2657a7 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f0a8e3b96e3812e0bc4382fe006e04ff 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f04936c9b6c0215a784cb29d11e68b3d 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b9220bb51a7b9f2fc281b3ec66a6777a 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=afc0f1083e090bf02b462353ff7f3f64 2500w" />

    As shown:

    1. Filter models by image type using the category selector
    2. The model's magnification factor is indicated in the top-right corner (e.g., 2x in the screenshot)

    We'll use the [4x-ESRGAN](https://openmodeldb.info/models/4x-ESRGAN) model for this tutorial. Click the `Download` button on the model detail page.

        <img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=678b9869dfcf612056bdc38fcec2f8f4" alt="OpenModelDB_download" data-og-width="1200" width="1200" data-og-height="848" height="848" data-path="images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=273b61c09d981babb85968599141f7d6 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=9866ff347c00df5b0db446a5edcd8ae3 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=60b259f6fb7173ba85796c8b863ce144 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5cef836154d2c860ea2dc76490cc22d7 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=065f7e6200a9087c87f66257c677357e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB_download.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=729c1efb8a117ebbd815b0a91e479e2a 2500w" />
  </Step>

  <Step title="Save Model Files in Directory">
    Save the model file (.pth) in `ComfyUI/models/upscale_models` directory
  </Step>
</Steps>

### Workflow and Assets

Download and drag the following image into ComfyUI to load the basic upscaling workflow:
![Upscale workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/upscale_workflow.png)

<Tip>
  Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.
</Tip>

Use this image in smaller size as input:
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ce8c5f3cd94c0cbde5ded50f09204d5b" alt="Upscale-input" data-og-width="512" width="512" data-og-height="512" height="512" data-path="images/tutorial/basic/upscale/upscale-input.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1babcd7fcdcb1f3b2cc953c79f237753 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6d8772a8c139cb4aa8f8554855552b1e 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a331ba6e2e35bef944d672990a9f39ce 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=af8cd385a69e8c69d4a9166cfb0056c9 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=2c79e1219e9af3bed8c72cc5a79caca6 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6ec8647f560daf3c2fe61670edc8fbca 2500w" />

### Complete the Workflow Step by Step

Follow the steps in the diagram below to ensure the workflow runs correctly.

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=632d1202982e8e7c59974a4152304967" alt="Upscale workflow" data-og-width="2136" width="2136" data-og-height="1192" height="1192" data-path="images/tutorial/basic/upscale/upscale_simple_workflow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=90de763eac7f4f322269592af72d6328 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=edd7e70f7b9f80178b08b3984b7c3eec 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3c3000421314917ba8de3b74b754b15d 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6f53afad6d2ed56c155aa57d5ea9083e 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=252e00d8d5f0b8f48554c4f9bf3a8b5b 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f48238be1a23ac57b5f766cdadf8dcd2 2500w" />

1. Ensure `Load Upscale Model` loads `4x-ESRGAN.pth`
2. Upload the input image to the `Load Image` node
3. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to generate the image

The core components are the `Load Upscale Model` and `Upscale Image (Using Model)` nodes, which receive an image input and upscale it using the selected model.

## Text-to-Image Combined Workflow

After mastering basic upscaling, we can combine it with the [text-to-image](/tutorials/basic/text-to-image) workflow. For text-to-image basics, refer to the [text-to-image tutorial](/tutorials/basic/text-to-image).

Download and drag this image into ComfyUI to load the combined workflow:
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=98c8d536f0a76025092f8fec157002f8" alt="Text-to-image upscale workflow" data-og-width="2533" width="2533" data-og-height="941" height="941" data-path="images/tutorial/basic/upscale/esrgan_example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=13fc9ef8db862b4c5b60289c5fe256ef 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4b8d819e10d503a630e98b092944c1f5 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b2dff912bcc2413b84f9d43fe88c1093 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=99dae3b712b3ad7b1b9cfa7d71db947d 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f128f8649d0fc1d8f9bbd6e36fb49a3e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6f130e45a1bcd061fe4e4bc21301e1dc 2500w" />

This workflow connects the text-to-image output image directly to the upscaling nodes for final processing.

## Additional Tips

<Tip>
  Model characteristics:

  * **RealESRGAN**: General-purpose upscaling
  * **BSRGAN**: Excels with text and sharp edges
  * **SwinIR**: Preserves natural textures, ideal for landscapes
</Tip>

1. **Chained Upscaling**: Combine multiple upscale nodes (e.g., 2x → 4x) for ultra-high magnification
2. **Hybrid Workflow**: Connect upscale nodes after generation for "generate+enhance" pipelines
3. **Comparative Testing**: Different models perform better on specific image types - test multiple options
