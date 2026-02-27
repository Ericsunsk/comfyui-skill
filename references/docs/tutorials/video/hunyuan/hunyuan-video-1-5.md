> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# HunyuanVideo 1.5

> Learn how to use HunyuanVideo 1.5, a lightweight 8.3B parameter model for high-quality video generation on consumer GPUs

[HunyuanVideo 1.5](https://github.com/Tencent/HunyuanVideo) is a lightweight 8.3B parameter model developed by Tencent's Hunyuan team. It delivers flagship-quality video generation on consumer GPUs (24GB VRAM), dramatically lowering the barrier to entry without compromising on quality.

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

## Model highlights

* **Compact powerhouse**: Delivers SOTA performance comparable to larger models while running on consumer hardware.
* **Versatile generation**: Supports high-quality Text-to-Video and Image-to-Video (5-10s) with exceptional consistency.
* **Precise control**: Strong instruction following for camera movements, physics, and emotional expressions.
* **Cinematic quality**: Native 720p output (upscalable to 1080p) with professional aesthetics.
* **Rich features**: Supports diverse styles (realistic, anime, 3D) and in-video text rendering (Chinese/English).

## Workflow templates

[video\_hunyuan\_video\_1.5\_720p\_i2v.json](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_hunyuan_video_1.5_720p_i2v.json)

[video\_hunyuan\_video\_1.5\_720p\_t2v.json](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_hunyuan_video_1.5_720p_t2v.json)

## Model links

**text\_encoders**

* [qwen\_2.5\_vl\_7b\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)
* [byt5\_small\_glyphxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors)

**diffusion\_models**

* [hunyuanvideo1.5\_1080p\_sr\_distilled\_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors)
* [hunyuanvideo1.5\_720p\_t2v\_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_720p_t2v_fp16.safetensors)

**vae**

* [hunyuanvideo15\_vae\_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/vae/hunyuanvideo15_vae_fp16.safetensors)

Model Storage Location

```
:open_file_folder: ComfyUI/
├── :open_file_folder: models/
│   ├── :open_file_folder: text_encoders/
│   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   │      └── byt5_small_glyphxl_fp16.safetensors
│   ├── :open_file_folder: diffusion_models/
│   │      ├── hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors
│   │      └── hunyuanvideo1.5_720p_t2v_fp16.safetensors
│   └── :open_file_folder: vae/
│          └── hunyuanvideo15_vae_fp16.safetensors
```
