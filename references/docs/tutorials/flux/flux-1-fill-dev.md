> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Flux.1 fill dev Example

> This guide demonstrates how to use Flux.1 fill dev to create Inpainting and Outpainting workflows.

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-fill-dev-demo.jpeg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e9b567aff5fbd43dce197d819f5f028e" alt="Flux.1 fill dev" data-og-width="2425" width="2425" data-og-height="1439" height="1439" data-path="images/tutorial/flux/flux-fill-dev-demo.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-fill-dev-demo.jpeg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b9ff2e9905b59dfd976d6fa3ad5b5383 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-fill-dev-demo.jpeg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=23a6543c141339e5de834a2226eac292 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-fill-dev-demo.jpeg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=91df5bbb329f8f721c9a5249974b9dfd 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-fill-dev-demo.jpeg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7cc6c43d71043ce741e6383c5248bad7 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-fill-dev-demo.jpeg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=48578042c0e47ddecbed8ad434fd2636 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-fill-dev-demo.jpeg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c4a294a48eaebafc00d865acec53be32 2500w" />

## Introduction to Flux.1 fill dev Model

Flux.1 fill dev is one of the core tools in the [FLUX.1 Tools suite](https://blackforestlabs.ai/flux-1-tools/) launched by [Black Forest Labs](https://blackforestlabs.ai/), specifically designed for image inpainting and outpainting.

Key features of Flux.1 fill dev:

* Powerful image inpainting and outpainting capabilities, with results second only to the commercial version FLUX.1 Fill \[pro].
* Excellent prompt understanding and following ability, precisely capturing user intent while maintaining high consistency with the original image.
* Advanced guided distillation training technology, making the model more efficient while maintaining high-quality output.
* Friendly licensing terms, with generated outputs usable for personal, scientific, and commercial purposes, please refer to the [FLUX.1 \[dev\] non-commercial license](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) for details.

Open Source Repository: [FLUX.1 \[dev\]](https://huggingface.co/black-forest-labs/FLUX.1-dev)

This guide will demonstrate inpainting and outpainting workflows based on the Flux.1 fill dev model.
If you're not familiar with inpainting and outpainting workflows, you can refer to [ComfyUI Layout Inpainting Example](/tutorials/basic/inpaint) and [ComfyUI Image Extension Example](/tutorials/basic/outpaint) for some related explanations.

## Flux.1 Fill dev and related models installation

Before we begin, let's complete the installation of the Flux.1 Fill dev model files. The inpainting and outpainting workflows will use exactly the same model files.
If you've previously used the full version of the [Flux.1 Text-to-Image workflow](/tutorials/flux/flux-1-text-to-image),
then you only need to download the **flux1-fill-dev.safetensors** model file in this section.

However, since downloading the corresponding model requires agreeing to the corresponding usage agreement, please visit the [black-forest-labs/FLUX.1-Fill-dev](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev) page and make sure you have agreed to the corresponding agreement as shown in the image below.
<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_fill_dev_agreement.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=388a26b32b5841dbf6ef32f31537e43d" alt="Flux Agreement" data-og-width="2000" width="2000" data-og-height="1091" height="1091" data-path="images/tutorial/flux/flux1_fill_dev_agreement.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_fill_dev_agreement.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e931f6ec07f32ef3e50afb225580be12 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_fill_dev_agreement.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2aaed9bcdc52c7f57b48692fdce76071 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_fill_dev_agreement.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=cf0a3480405e849938cd569eba919065 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_fill_dev_agreement.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b30a92913ebf2f5a8232df354bb8558c 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_fill_dev_agreement.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f9147bf0268a4d70f6c6bff96381449a 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_fill_dev_agreement.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=251f4c63f5860161b93afcff28180161 2500w" />

Complete model list:

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true)
* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)
* [flux1-fill-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev/resolve/main/flux1-fill-dev.safetensors?download=true)

File storage location:

```
ComfyUI/
├── models/
│   ├── text_encoders/
│   │    ├── clip_l.safetensors
│   │    └── t5xxl_fp16.safetensors
│   ├── vae/
│   │    └── ae.safetensors
│   └── diffusion_models/
│        └── flux1-fill-dev.safetensors
```

## Flux.1 Fill dev inpainting workflow

### 1. Inpainting workflow and asset

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/inpaint/flux_fill_inpaint.png" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Workflow Image</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_fill_inpaint_example&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

Please download the image below and drag it into ComfyUI to load the corresponding workflow
![ComfyUI Flux.1 inpaint](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/inpaint/flux_fill_inpaint.png)

Please download the image below, we will use it as the input image
![ComfyUI Flux.1 inpaint input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/inpaint/flux_fill_inpaint_input.png)

<Note>
  The corresponding image already contains an alpha channel, so you don't need to draw a mask separately.
  If you want to draw your own mask, please [click here](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/inpaint/flux_fill_inpaint_input_original.png) to get the image without a mask, and refer to the MaskEditor usage section in the [ComfyUI Layout Inpainting Example](/tutorials/basic/inpaint#using-the-mask-editor) to learn how to draw a mask in the `Load Image` node.
</Note>

### 2. Steps to run the workflow

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_inpaint.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8d4238c0487b7ddf527ec044aa02d578" alt="ComfyUI Flux.1 Fill dev Inpainting Workflow" data-og-width="4000" width="4000" data-og-height="2163" height="2163" data-path="images/tutorial/flux/flow_diagram_inpaint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_inpaint.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=1d8a3d3fcce18ee64563486bd76097fc 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_inpaint.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c86c70674d8643e5f6f59191d7d620b2 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_inpaint.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=bba1c4942e902354ce3042f16a26ff43 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_inpaint.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6b802ce2d64055da8708a830a6608968 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_inpaint.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=630ceb021fdf1fc335975f475236c73e 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_inpaint.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=77f2eaa8ba13517df4d9492f17ea55aa 2500w" />

1. Ensure the `Load Diffusion Model` node has `flux1-fill-dev.safetensors` loaded.
2. Ensure the `DualCLIPLoader` node has the following models loaded:
   * clip\_name1: `t5xxl_fp16.safetensors`
   * clip\_name2: `clip_l.safetensors`
3. Ensure the `Load VAE` node has `ae.safetensors` loaded.
4. Upload the input image provided in the document to the `Load Image` node; if you're using the version without a mask, remember to complete the mask drawing using the mask editor
5. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

## Flux.1 Fill dev Outpainting Workflow

### 1. Outpainting workflow and asset

Please download the image below and drag it into ComfyUI to load the corresponding workflow
![ComfyUI Flux.1 outpaint](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/outpaint/flux_fill_dev_outpaint.png)

Please download the image below, we will use it as the input image
![ComfyUI Flux.1 outpaint input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/outpaint/flux_fill_dev_outpaint_input.png)

### 2. Steps to run the workflow

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_outpaint.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5f152f459be5f120b3895636685cb3d3" alt="ComfyUI Flux.1 Fill dev Outpainting Workflow" data-og-width="4000" width="4000" data-og-height="2159" height="2159" data-path="images/tutorial/flux/flow_diagram_outpaint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_outpaint.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d68cb7ec13cce28e41d5b129e5556bfa 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_outpaint.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=cd1347b12b768b5d154d93f934f82545 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_outpaint.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d903a9a469414f553c4db60cedc0f334 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_outpaint.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a3e792313923fcb209d769d742020460 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_outpaint.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=116cb8593bab3731e6f5e3a06f95d51c 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_outpaint.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7af097f3ebfc0ec39ff8b85309d88c02 2500w" />

1. Ensure the `Load Diffusion Model` node has `flux1-fill-dev.safetensors` loaded.
2. Ensure the `DualCLIPLoader` node has the following models loaded:
   * clip\_name1: `t5xxl_fp16.safetensors`
   * clip\_name2: `clip_l.safetensors`
3. Ensure the `Load VAE` node has `ae.safetensors` loaded.
4. Upload the input image provided in the document to the `Load Image` node
5. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow
