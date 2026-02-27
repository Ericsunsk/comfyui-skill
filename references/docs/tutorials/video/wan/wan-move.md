> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Wan-Move Workflow Example

> Wan-Move is a motion-controllable video generation model via latent trajectory guidance, enabling fine-grained point-level motion control for image-to-video generation.

**Wan-Move** is a motion-controllable video generation framework developed by Alibaba's Tongyi Lab. It enables users to control object motion in generated videos by specifying point trajectories on the input image, making image-to-video generation more precise and controllable.

**Key Features**:

* **High-Quality 5s 480p Motion Control**: Generates 5-second, 480p videos with fine-grained motion controllability
* **Latent Trajectory Guidance**: Represents motion conditions by propagating first frame features along trajectories
* **Fine-grained Point-level Control**: Object motions are represented with dense point trajectories, enabling precise region-level control
* **No Architecture Changes**: Seamlessly integrates into Wan-I2V-14B without extra motion modules

**Related Links**:

* [GitHub](https://github.com/ali-vilab/Wan-Move)
* [Hugging Face](https://huggingface.co/Ruihang/Wan-Move-14B-480P)
* [Paper](https://arxiv.org/abs/2512.08765)

## Wan-Move image-to-video workflow

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wanmove_480p.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold', marginRight: '10px'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow File</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wanmove_480p&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
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

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

**clip\_vision**

* [clip\_vision\_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors)

**loras**

* [lightx2v\_I2V\_14B\_480p\_cfg\_step\_distill\_rank64\_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors)

**diffusion\_models**

* [Wan21-WanMove\_fp8\_scaled\_e4m3fn\_KJ.safetensors](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/WanMove/Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors)

**vae**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**Model Storage Location**

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 clip_vision/
│   │      └── clip_vision_h.safetensors
│   ├── 📂 loras/
│   │      └── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors
│   └── 📂 vae/
│          └── wan_2.1_vae.safetensors
```
