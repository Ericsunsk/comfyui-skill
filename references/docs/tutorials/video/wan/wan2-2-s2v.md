> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan2.2-S2V Audio-Driven Video Generation ComfyUI Native Workflow Example

> This is a native workflow example for Wan2.2-S2V audio-driven video generation in ComfyUI.

We're excited to announce that Wan2.2-S2V, the advanced audio-driven video generation model, is now natively supported in ComfyUI! This powerful AI model can transform static images and audio inputs into dynamic video content, supporting dialogue, singing, performance, and various creative content needs.

**Model Highlights**

* **Audio-Driven Video Generation**: Transforms static images and audio into synchronized videos
* **Cinematic-Grade Quality**: Generates film-quality videos with natural expressions and movements
* **Minute-Level Generation**: Supports long-form video creation
* **Multi-Format Support**: Works with full-body and half-body characters
* **Enhanced Motion Control**: Generates actions and environments from text instructions

Wan2.2 S2V Code: [GitHub](https://github.com/aigc-apps/VideoX-Fun)
Wan2.2 S2V Model: [Hugging Face](https://huggingface.co/Wan-AI/Wan2.2-S2V-14B)

## Wan2.2 S2V ComfyUI Native Workflow

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

### 1. Download Workflow File

Download the following workflow file and drag it into ComfyUI to load the workflow.

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_s2v/wan2.2-s2v.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_s2v.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_14B_s2v&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

Download the following image and audio as input:
![input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_s2v/input.jpg)

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_s2v/input_audio.MP3" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Input  Audio</p>
</a>

### 2. Model Links

You can find the models in [our repo](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)

**diffusion\_models**

* [wan2.2\_s2v\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_s2v_14B_fp8_scaled.safetensors)
* [wan2.2\_s2v\_14B\_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_s2v_14B_bf16.safetensors)

**audio\_encoders**

* [wav2vec2\_large\_english\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/audio_encoders/wav2vec2_large_english_fp16.safetensors)

**vae**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**text\_encoders**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_s2v_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_s2v_14B_bf16.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   ├───📂 audio_encoders/ # Create one if you can't find this folder
│   │   └─── wav2vec2_large_english_fp16.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

### 3. Workflow Instructions

<img src="https://mintcdn.com/dripart/ht3vzHrjy1qaRsl9/images/tutorial/video/wan/wan_2.2_14b_s2v.jpg?fit=max&auto=format&n=ht3vzHrjy1qaRsl9&q=85&s=295f87179e12d937cbfbcc3e21d474c0" alt="Workflow Instructions" data-og-width="4000" width="4000" data-og-height="2131" height="2131" data-path="images/tutorial/video/wan/wan_2.2_14b_s2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/ht3vzHrjy1qaRsl9/images/tutorial/video/wan/wan_2.2_14b_s2v.jpg?w=280&fit=max&auto=format&n=ht3vzHrjy1qaRsl9&q=85&s=5205bb7cb437730ee400253eabd457d2 280w, https://mintcdn.com/dripart/ht3vzHrjy1qaRsl9/images/tutorial/video/wan/wan_2.2_14b_s2v.jpg?w=560&fit=max&auto=format&n=ht3vzHrjy1qaRsl9&q=85&s=93c52b494e66a77e048c0a4a02839259 560w, https://mintcdn.com/dripart/ht3vzHrjy1qaRsl9/images/tutorial/video/wan/wan_2.2_14b_s2v.jpg?w=840&fit=max&auto=format&n=ht3vzHrjy1qaRsl9&q=85&s=e15f5e98797ff26315e7a8cbeff62231 840w, https://mintcdn.com/dripart/ht3vzHrjy1qaRsl9/images/tutorial/video/wan/wan_2.2_14b_s2v.jpg?w=1100&fit=max&auto=format&n=ht3vzHrjy1qaRsl9&q=85&s=bc70484c0ad625edbf5657a5fa294cb8 1100w, https://mintcdn.com/dripart/ht3vzHrjy1qaRsl9/images/tutorial/video/wan/wan_2.2_14b_s2v.jpg?w=1650&fit=max&auto=format&n=ht3vzHrjy1qaRsl9&q=85&s=79fd15e0520faac165db2b7763df58c2 1650w, https://mintcdn.com/dripart/ht3vzHrjy1qaRsl9/images/tutorial/video/wan/wan_2.2_14b_s2v.jpg?w=2500&fit=max&auto=format&n=ht3vzHrjy1qaRsl9&q=85&s=6ccabebbab0bc20c0c0fc415ba3ab9aa 2500w" />

#### 3.1 About Lightning LoRA

#### 3.2 About fp8\_scaled and bf16 Models

You can find both models [here](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models):

* [wan2.2\_s2v\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_s2v_14B_fp8_scaled.safetensors)
* [wan2.2\_s2v\_14B\_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_s2v_14B_bf16.safetensors)

This template uses `wan2.2_s2v_14B_fp8_scaled.safetensors`, which requires less VRAM. But you can try `wan2.2_s2v_14B_bf16.safetensors` to reduce quality degradation.

#### 3.3 Step-by-Step Operation Instructions

**Step 1: Load Models**

1. **Load Diffusion Model**: Load `wan2.2_s2v_14B_fp8_scaled.safetensors` or `wan2.2_s2v_14B_bf16.safetensors`
   * The provided workflow uses `wan2.2_s2v_14B_fp8_scaled.safetensors`, which requires less VRAM
   * But you can try `wan2.2_s2v_14B_bf16.safetensors` to reduce quality degradation

2. **Load CLIP**: Load `umt5_xxl_fp8_e4m3fn_scaled.safetensors`

3. **Load VAE**: Load `wan_2.1_vae.safetensors`

4. **AudioEncoderLoader**: Load `wav2vec2_large_english_fp16.safetensors`

5. **LoraLoaderModelOnly**: Load `wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors` (Lightning LoRA)
   * We tested all wan2.2 lightning LoRAs. Since this is not a LoRA specifically trained for Wan2.2 S2V, many key values don't match, but we added it because it significantly reduces generation time. We will continue to optimize this template
   * Using it will cause significant dynamic and quality loss
   * If you find the output quality too poor, you can try the original 20-step workflow

6. **LoadAudio**: Upload our provided audio file or your own audio

7. **Load Image**: Upload reference image

8. **Batch sizes**: Set according to the number of Video S2V Extend subgraph nodes you add
   * Each Video S2V Extend subgraph adds 77 frames to the final output
   * For example: If you added 2 Video S2V Extend subgraphs, the batch size should be 3, which means the total number of sampling iterations
   * **Chunk Length**: Keep the default value of 77

9. **Sampler Settings**: Choose different settings based on whether you use Lightning LoRA
   * With 4-step Lightning LoRA: steps: 4, cfg: 1.0
   * Without 4-step Lightning LoRA: steps: 20, cfg: 6.0

10. **Size Settings**: Set the output video dimensions

11. **Video S2V Extend**: Video extension subgraph nodes. Since our default frames per sampling is 77, and this is a 16fps model, each extension will generate 77 / 16 = 4.8125 seconds of video
    * You need some calculation to match the number of video extension subgraph nodes with the input audio length. For example: If input audio is 14s, the total frames needed are 14x16=224, each video extension is 77 frames, so you need 224/77 = 2.9, rounded up to 3 video extension subgraph nodes

12. Use Ctrl-Enter or click the Run button to execute the workflow
