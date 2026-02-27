> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Ovis-Image ComfyUI Workflow Example

> Ovis-Image is a 7B text-to-image model specifically optimized for high-quality text rendering, designed to operate efficiently under stringent computational constraints.

**Ovis-Image** is a 7B text-to-image model built upon [Ovis-U1](https://github.com/AIDC-AI/Ovis-U1), specifically optimized for high-quality text rendering. It delivers text rendering quality comparable to much larger 20B-class systems while remaining compact enough to run on widely accessible hardware.

**Model Highlights**:

* **Strong Text Rendering at 7B Scale**: Delivers text rendering quality comparable to much larger 20B-class systems like Qwen-Image and competitive with leading closed-source models like GPT4o in text-centric scenarios
* **High Fidelity on Text-Heavy Prompts**: Excels on prompts that demand tight alignment between linguistic content and rendered typography (e.g., posters, banners, logos, UI mockups, infographics)
* **Accurate Bilingual Text Rendering**: Produces legible, correctly spelled, and semantically consistent text in both Chinese and English across diverse fonts, sizes, and aspect ratios
* **Efficiency and Deployability**: Fits on a single high-end GPU with moderate memory, supports low-latency interactive use

**Related Links**:

* [GitHub](https://github.com/AIDC-AI/Ovis-Image)
* [Hugging Face](https://huggingface.co/AIDC-AI/Ovis-Image-7B)

## Ovis-Image text-to-image workflow

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_ovis_text_to_image.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow File</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=image_ovis_text_to_image&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on ComfyUI Cloud</p>
</a>

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

## Model links

**text\_encoders**

* [ovis\_2.5.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/text_encoders/ovis_2.5.safetensors)

**diffusion\_models**

* [ovis\_image\_bf16.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/diffusion_models/ovis_image_bf16.safetensors)

**vae**

* [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors)

**Model Storage Location**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── ovis_2.5.safetensors
│   ├── 📂 diffusion_models/
│   │      └── ovis_image_bf16.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```
