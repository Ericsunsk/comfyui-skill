> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# LTX-Video

[LTX-Video](https://huggingface.co/Lightricks/LTX-Video) is a very efficient video model by lightricks. The important thing with this model is to give it long descriptive prompts.

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

## Multi Frame Control

Allows you to control the video with a series of images. You can download the input images: [starting frame](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/house1.png) and [ending frame](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/house2.png).

<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/workflow.webp" alt="LTX-Video Multi Frame Control" />

<Tip>
  Drag the video directly into ComfyUI to run the workflow.
</Tip>

## Image to Video

Allows you to control the video with a first [frame image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/i2v/girl1.png).

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=ltxv_image_to_video&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/i2v/workflow.webp" alt="LTX-Video Image to Video" />

<Tip>
  Drag the video directly into ComfyUI to run the workflow.
</Tip>

## Text to Video

<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/t2v.webp" alt="LTX-Video Text to Video" />

<Tip>
  Drag the video directly into ComfyUI to run the workflow.
</Tip>

## Requirements

Download the following models and place them in the locations specified below:

* [ltx-video-2b-v0.9.5.safetensors](https://huggingface.co/Lightricks/LTX-Video/resolve/main/ltx-video-2b-v0.9.5.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/mochi_preview_repackaged/resolve/main/split_files/text_encoders/t5xxl_fp16.safetensors?download=true)

```
├── checkpoints/
│   └── ltx-video-2b-v0.9.5.safetensors
└── text_encoders/
    └── t5xxl_fp16.safetensors
```
