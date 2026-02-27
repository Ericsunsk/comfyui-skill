> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan2.2 Animate ComfyUI native workflow

> Unified character animation and replacement framework with precise motion and expression replication.

Wan-Animate is a unified framework for character animation and replacement developed by the WAN Team.

The model can animate any character based on a performer’s video, precisely replicating the performer’s facial expressions and movements to generate highly realistic character videos.

It can also replace characters in a video with animated characters, preserving their expressions and movements while replicating the original lighting and color tone for seamless environmental integration.

## Model Highlights

* Dual Mode Functionality: A single architecture supports both animation and replacement functions, enabling easy operation switching.
* Advanced Body Motion Control: Uses spatially-aligned skeleton signals for accurate body movement replication
* Precise Motion and Expression: Accurately reproduces the movements and facial expressions from the reference video.
* Natural Environment Integration: Seamlessly blends the replaced character with the original video environment.
* Smooth Long Video Generation: Iterative generation ensures consistent motion and visual flow in extended videos

## ComfyOrg Wan2.2 Animate stream replay

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/5kb-rP0m5BA?si=lbIYkCP5akkG2N6D" title="Wan 2.2 Animate in ComfyUI with Flipping Sigmas / September 19th, 2025" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

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

## About Wan2.2 Animate workflow

In this docs, we will provide two workflow:

1. Workflow that only uses core nodes (It is incomplete; you need to preprocess the image by yourself first)
2. Workflow that includes some custom nodes (It is complete; you can use it directly, but some new user might not know how to install the custom nodes)

## Wan2.2 Anmate ComfyUI native workflow(without custom nodes)

### 1. Download Workflow File

Download the following workflow file and drag it into ComfyUI to load the workflow.

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_animate.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download JSON Workflow</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_14B_animate&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

Download materials below as input:

**Reference Image:**
![Reference\_Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_animate/ref_image.png)

**Input Video**

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_animate/original_video.mp4" />

### 2. Model links

**diffusion\_models**

* [Wan2\_2-Animate-14B\_fp8\_e4m3fn\_scaled\_KJ.safetensors](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/Wan22Animate/Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors) This is the model that from Kijai's repo
* [wan2.2\_animate\_14B\_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_animate_14B_bf16.safetensors) original model weight

**clip\_visions**

* [clip\_vision\_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors)

**loras**

* [lightx2v\_I2V\_14B\_480p\_cfg\_step\_distill\_rank64\_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) 这是一个 4 步的加速 lora

**vae**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**text\_encoders**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors
│   │   └─── wan2.2_animate_14B_bf16.safetensors
│   ├───📂 loras/
│   │   └─── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   ├───📂 clip_visions/ 
│   │   └─── clip_vision_h.safetensors
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

### 3. Install custom nodes

Download the following workflow file and drag it into ComfyUI to load the workflow, if you have [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) installed, you can just click the `Install missing nodes` button to install the missing nodes.

We need to install the following custom nodes:

* [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
* [ComfyUI-comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

If you don't know how to install custom nodes please refer to [How to install custom nodes](/installation/install_custom_node)

### 4. Workflow Instructions

The Wan2.2 animate has two modes: Mix and move

* Mix: use the reference image to replace the character in the video
* Move: Use the character movement from the input video to animate the character in the reference image (like Wan2.2 Fun Control)

#### 4.1 Mix mode

<img src="https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan_2.2_14b_animate.jpg?fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=d451c51be227ab808ff8aa2723a054ad" alt="Workflow Instructions" data-og-width="4088" width="4088" data-og-height="4096" height="4096" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_14b_animate.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan_2.2_14b_animate.jpg?w=280&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=83c177be0fee53c909f8af41a80fc6d4 280w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan_2.2_14b_animate.jpg?w=560&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=1700a85f1f06283a5af25b5f85a83b2d 560w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan_2.2_14b_animate.jpg?w=840&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=07870a19b2e634c84b68949ab4353af6 840w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan_2.2_14b_animate.jpg?w=1100&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=44a7243272099fd5935aa7b65202ad1e 1100w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan_2.2_14b_animate.jpg?w=1650&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=1b7831761ee0e4274f488857484d8056 1650w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan_2.2_14b_animate.jpg?w=2500&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=cb092054225dc49519fb8b350fe45e34 2500w" />

0. If you are running this workflow for the first time, please use a small size for video generation, in case you don't have enough VRAM to run the workflow, and due to the `WanAnimateToVideo` limited, the video width or height should be multiples of 16.
1. Make sure all the models are loaded correctly
2. Update the prompt if you want
3. Upload the reference image, the character is this image will be the target character
4. You can use the videos we provided as input videos for the first time， the **DWPose Estimator** node  in [comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) will preprocess the input video to pose and face control videos
5. The `Points Editor` is from [KJNodes](https://github.com/kijai/ComfyUI-KJNodes/), by default this node will not load the first frame from the input video, you need to run the workflow once or manually upload the first frame
   * Bleow the `Points Editor` node, we have added note about how this node work, and how to edit it please refer to it
6. For the "Video Extend" group, it's in order to extend to the output video length
   * Each `Video Extend` will extend another 77 frames(Around 4.8125 seconds)
   * If your input video is less then 5s, you might not need it
   * If you want to extend longer, you need to copy and paste multiple times, you need to link the `batch_images` from last Video Extend to next one, and also the `video_frame_offset` from last Video Extend to next one
7. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute video generation

#### 4.2 Move mode

We used [subgraph](/interface/features/subgraph) in the Wan2.2 animate workflow, here is how to switching to move mode:

<img src="https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan2.2_animate_subgraph.jpg?fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=193caf05c2494550d6b92318523c54a4" alt="Subgraph" data-og-width="1228" width="1228" data-og-height="1206" height="1206" data-path="images/tutorial/video/wan/wan2_2/wan2.2_animate_subgraph.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan2.2_animate_subgraph.jpg?w=280&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=d1d50af10d00c280d4ebf10f1bfd0eee 280w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan2.2_animate_subgraph.jpg?w=560&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=23a3b3c0db8a431aebad4da9f6c34d7a 560w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan2.2_animate_subgraph.jpg?w=840&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=776ecdf12ca9d2158f3a962f7862e613 840w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan2.2_animate_subgraph.jpg?w=1100&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=041c2d30fd31f983cac31f1ddeae29b3 1100w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan2.2_animate_subgraph.jpg?w=1650&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=e19c71b745f74c7b295607b89c4a01a4 1650w, https://mintcdn.com/dripart/UGcNWAMSJO6Toi_8/images/tutorial/video/wan/wan2_2/wan2.2_animate_subgraph.jpg?w=2500&fit=max&auto=format&n=UGcNWAMSJO6Toi_8&q=85&s=835d846ddc484de3bd0aff40e394e023 2500w" />

If you want to switch to Move mode, you can disconnect `background_video` and `character_mask` inputs from the `Video Sampling and output(Subgraph)` node.
