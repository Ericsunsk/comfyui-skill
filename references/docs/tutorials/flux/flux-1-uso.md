> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ByteDance USO ComfyUI Native Workflow example

> Unified Style and Subject-Driven Generation with ByteDance's USO model

**USO (Unified Style-Subject Optimized)** is a model developed by ByteDance's UXO Team that unifies style-driven and subject-driven generation tasks.
Built on FLUX.1-dev architecture, the model achieves both style similarity and subject consistency through disentangled learning and style reward learning (SRL).

USO supports three main approaches:

* **Subject-Driven**: Place subjects into new scenes while maintaining identity consistency
* **Style-Driven**: Apply artistic styles to new content based on reference images
* **Combined**: Use both subject and style references simultaneously

**Related Links**

* [Project Page](https://bytedance.github.io/USO/)
* [GitHub](https://github.com/bytedance/USO)
* [Model Weights](https://huggingface.co/bytedance-research/USO)

## ByteDance USO ComfyUI Native Workflow

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

### 1. Workflow and input

Download the image below and drag it into ComfyUI to load the corresponding workflow.

![Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/flux/bytedance-uso/bytedance-uso.png)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/flux1_dev_uso_reference_image_gen.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux1_dev_uso_reference_image_gen&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

Use the image below as an input image.

![input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/flux/bytedance-uso/input.png)

### 2. Model links

**checkpoints**

* [flux1-dev-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors)

**loras**

* [uso-flux1-dit-lora-v1.safetensors](https://huggingface.co/Comfy-Org/USO_1.0_Repackaged/resolve/main/split_files/loras/uso-flux1-dit-lora-v1.safetensors)

**model\_patches**

* [uso-flux1-projector-v1.safetensors](https://huggingface.co/Comfy-Org/USO_1.0_Repackaged/resolve/main/split_files/model_patches/uso-flux1-projector-v1.safetensors)

**clip\_visions**

* [sigclip\_vision\_patch14\_384.safetensors](https://huggingface.co/Comfy-Org/sigclip_vision_384/resolve/main/sigclip_vision_patch14_384.safetensors)

Please download all models and place them in the following directories:

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── flux1-dev-fp8.safetensors
│   ├── 📂 loras/
│   │   └── uso-flux1-dit-lora-v1.safetensors
│   ├── 📂 model_patches/
│   │   └── uso-flux1-projector-v1.safetensors
│   ├── 📂 clip_visions/
│   │   └── sigclip_vision_patch14_384.safetensors
```

### 3. Workflow instructions

<img src="https://mintcdn.com/dripart/3zBG7o3F8mQK7Rdk/images/tutorial/flux/flux1_uso_reference_image_gen.jpg?fit=max&auto=format&n=3zBG7o3F8mQK7Rdk&q=85&s=60e1dc7cccd4b732ff2a6e24767d7630" alt="Workflow instructions" data-og-width="2000" width="2000" data-og-height="1188" height="1188" data-path="images/tutorial/flux/flux1_uso_reference_image_gen.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/3zBG7o3F8mQK7Rdk/images/tutorial/flux/flux1_uso_reference_image_gen.jpg?w=280&fit=max&auto=format&n=3zBG7o3F8mQK7Rdk&q=85&s=610ae03284c242865999544b959c66bb 280w, https://mintcdn.com/dripart/3zBG7o3F8mQK7Rdk/images/tutorial/flux/flux1_uso_reference_image_gen.jpg?w=560&fit=max&auto=format&n=3zBG7o3F8mQK7Rdk&q=85&s=f175cef9066b7736a66927c13417631d 560w, https://mintcdn.com/dripart/3zBG7o3F8mQK7Rdk/images/tutorial/flux/flux1_uso_reference_image_gen.jpg?w=840&fit=max&auto=format&n=3zBG7o3F8mQK7Rdk&q=85&s=9a0b273f5e59dac1948b29bb5dfb8f6b 840w, https://mintcdn.com/dripart/3zBG7o3F8mQK7Rdk/images/tutorial/flux/flux1_uso_reference_image_gen.jpg?w=1100&fit=max&auto=format&n=3zBG7o3F8mQK7Rdk&q=85&s=d185827366c42e43dd057be377ff4010 1100w, https://mintcdn.com/dripart/3zBG7o3F8mQK7Rdk/images/tutorial/flux/flux1_uso_reference_image_gen.jpg?w=1650&fit=max&auto=format&n=3zBG7o3F8mQK7Rdk&q=85&s=356a8a3c5689c6a623bf97ecde0881d7 1650w, https://mintcdn.com/dripart/3zBG7o3F8mQK7Rdk/images/tutorial/flux/flux1_uso_reference_image_gen.jpg?w=2500&fit=max&auto=format&n=3zBG7o3F8mQK7Rdk&q=85&s=52b6b8eb1387a8fad683ad23b4033e3a 2500w" />

1. Load models:
   * 1.1 Ensure the `Load Checkpoint` node has `flux1-dev-fp8.safetensors` loaded
   * 1.2 Ensure the `LoraLoaderModelOnly` node has `dit_lora.safetensors` loaded
   * 1.3 Ensure the `ModelPatchLoader` node has `projector.safetensors` loaded
   * 1.4 Ensure the `Load CLIP Vision` node has `sigclip_vision_patch14_384.safetensors` loaded
2. Content Reference:
   * 2.1 Click `Upload` to upload the input image we provided
   * 2.2 The `ImageScaleToMaxDimension` node will scale your input image for content reference, 512px will keep more character features, but if you only use the character's head as input, the final output image often has issues like the character taking up too much space. Setting it to 1024px gives much better results.
3. In the example, we only use the `content reference` image input. If you want to use the `style reference` image input, you can use `Ctrl-B` to bypass the marked node group.
4. Write your prompt or keep default
5. Set the image size if you need
6. The EasyCache node is for inference acceleration, but it will also sacrifice some quality and details. You can bypass it (Ctrl+B) if you don't need to use it.
7. Click the `Run` button, or use the shortcut `Ctrl(Cmd) + Enter` to run the workflow

### 4. Additional Notes

1. Style reference only:

We also provide a workflow that only uses style reference in the same workflow we provided

<img src="https://mintcdn.com/dripart/6BfRVG5RoFiMLPEQ/images/tutorial/flux/flux1_uso_reference_image_gen_style_reference_only.jpg?fit=max&auto=format&n=6BfRVG5RoFiMLPEQ&q=85&s=d5f16dbe97ac74b1bf01587aaabe12b8" alt="Workflow" data-og-width="4366" width="4366" data-og-height="2498" height="2498" data-path="images/tutorial/flux/flux1_uso_reference_image_gen_style_reference_only.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/6BfRVG5RoFiMLPEQ/images/tutorial/flux/flux1_uso_reference_image_gen_style_reference_only.jpg?w=280&fit=max&auto=format&n=6BfRVG5RoFiMLPEQ&q=85&s=fad6ae6e6aa55a9d4d459db8676e2488 280w, https://mintcdn.com/dripart/6BfRVG5RoFiMLPEQ/images/tutorial/flux/flux1_uso_reference_image_gen_style_reference_only.jpg?w=560&fit=max&auto=format&n=6BfRVG5RoFiMLPEQ&q=85&s=57afc7c22638d7b3dcebc4f8ec71dac2 560w, https://mintcdn.com/dripart/6BfRVG5RoFiMLPEQ/images/tutorial/flux/flux1_uso_reference_image_gen_style_reference_only.jpg?w=840&fit=max&auto=format&n=6BfRVG5RoFiMLPEQ&q=85&s=d09612e1f21d5b99febd75ce686f788e 840w, https://mintcdn.com/dripart/6BfRVG5RoFiMLPEQ/images/tutorial/flux/flux1_uso_reference_image_gen_style_reference_only.jpg?w=1100&fit=max&auto=format&n=6BfRVG5RoFiMLPEQ&q=85&s=76e13af6286a5566eda2b66a669d9f87 1100w, https://mintcdn.com/dripart/6BfRVG5RoFiMLPEQ/images/tutorial/flux/flux1_uso_reference_image_gen_style_reference_only.jpg?w=1650&fit=max&auto=format&n=6BfRVG5RoFiMLPEQ&q=85&s=675299a02175c33325ea77435434ba96 1650w, https://mintcdn.com/dripart/6BfRVG5RoFiMLPEQ/images/tutorial/flux/flux1_uso_reference_image_gen_style_reference_only.jpg?w=2500&fit=max&auto=format&n=6BfRVG5RoFiMLPEQ&q=85&s=5868e6410eed5e4b64453a0f0e0ea092 2500w" />
The only different is we replaced the `content reference` node and only use an `Empty Latent Image` node.

2. You can also bypass whole `Style Reference` group and use the workflow as a text to image workflow, which means this workflow has 4 variations

* Only use content (subject) reference
* Only use style reference
* Mixed content and style reference
* As a text to image workflow
