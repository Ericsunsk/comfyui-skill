> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Wan2.2 Fun Control 视频控制生成示例

> 本文介绍了如何在 ComfyUI 中完成 Wan2.2 Fun Control 使用控制视频来完成视频生成的示例

**Wan2.2-Fun-Control** 是 Alibaba PAI 团队推出的新一代视频生成与控制模型，通过引入创新性的控制代码（Control Codes）机制，结合深度学习和多模态条件输入，能够生成高质量且符合预设控制条件的视频。该模型采用 **Apache 2.0 许可协议**发布，支持商业使用。

**核心功能**：

* **多模态控制**：支持多种控制条件，包括 **Canny（线稿）**、**Depth（深度）**、**OpenPose（人体姿势）**、**MLSD（几何边缘）** 等，同时支持使用 **轨迹控制**
* **高质量视频生成**：基于 Wan2.2 架构，输出影视级质量视频
* **多语言支持**：支持中英文等多语言提示词输入

下面是相关模型权重和代码仓库：

* [🤗Wan2.2-Fun-A14B-Control](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control)
* 代码仓库：[VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun)

## ComfyOrg Wan2.2 Fun InP & Control Youtube 直播回放

对于 ComfyUI Wan2.2 的使用，我们有进行了直播，你可以查看这些回放了解如何使用

<iframe className="w-full aspect-video rounded-xl" src="//player.bilibili.com/player.html?isOutside=true&aid=115027747082114&bvid=BV1DVbrzdEFR&cid=31697013072&p=1&autoplay=0" title="ComfyUI Selection Toolbox New Features" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Wan2.2 Fun Control 视频控制生成工作流示例

<Tip>
  <Tabs>
    <Tab title="便携版或手动安装用户">
      请确保你的 ComfyUI 已经更新。

      * [ComfyUI 下载](https://www.comfy.org/download)
      * [ComfyUI 更新教程](/zh-CN/installation/update_comfyui)

      本指南里的工作流可以在 ComfyUI 的[工作流模板](/zh-CN/interface/features/template)中找到。如果找不到，可能是 ComfyUI 没有更新。

      如果加载工作流时有节点缺失，可能原因有：

      1. 你用的不是最新开发版（nightly）。
      2. 你用的是稳定版或桌面版（没有包含最新的更新）。
      3. 启动时有些节点导入失败。
    </Tab>

    <Tab title="桌面版或云端用户">
      * 桌面版是基于 ComfyUI 稳定版本构建的，它会在有新的桌面稳定版本发布时自动更新。
      * [Cloud](https://cloud.comfy.org) 会在 ComfyUI 稳定版本发布后更新，我们会同步更新 Cloud。

      所以，如果你发现本教程中有任何核心节点缺失，那是因为对应的节点支持还在开发中没有发布正式的稳定版，请等待下一个稳定版本发布。
    </Tab>
  </Tabs>
</Tip>

这里提供的工作流包含了两个版本：

1. 使用了 lightx2v 的 [Wan2.2-Lightning](https://huggingface.co/lightx2v/Wan2.2-Lightning) 4 步 LoRA : 但可能导致生成的视频动态会有损失，但速度会更快
2. 没有使用加速 LoRA 的 fp8\_scaled 版本

下面是使用 RTX4090D 24GB 显存 GPU 测试的结果 640\*640 分辨率， 81 帧长度的用时对比

| 模型类型                   | 分辨率     | 显存占用 | 首次生成时长 | 第二次生成时长 |
| ---------------------- | ------- | ---- | ------ | ------- |
| fp8\_scaled            | 640×640 | 83%  | ≈ 524秒 | ≈ 520秒  |
| fp8\_scaled + 4步LoRA加速 | 640×640 | 89%  | ≈ 138秒 | ≈ 79秒   |

由于使用了4 步 LoRA 对于初次使用工作流的用户体验较好， 但可能导致生成的视频动态会有损失， 我们默认启用了使用了加速 LoRA 版本，如果你需要启用另一组的工作流，框选后使用 **Ctrl+B** 即可启用

### 1. 工作流及素材下载

下载下面的视频或者 JSON 文件并拖入 ComfyUI 中以加载对应的工作流

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_control/wan2.2_14B_fun_inp.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_fun_control.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

请下载下面的图片及视频，我们将作为输入。

![输入起始图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_control/input.jpg)

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/wan2.2_fun_control/control_video.mp4" />

> 这里我们使用了经过预处理的视频, 可以直接用于控制视频生成

### 2. 手动下载模型

下面的模型你可以在 [Wan\_2.2\_ComfyUI\_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) 找到

**Diffusion Model**

* [wan2.2\_fun\_control\_high\_noise\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors)
* [wan2.2\_fun\_control\_low\_noise\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors)

\*\* Wan2.2-Lightning LoRA (可选，用于加速)\*\*

* [wan2.2\_i2v\_lightx2v\_4steps\_lora\_v1\_high\_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors)
* [wan2.2\_i2v\_lightx2v\_4steps\_lora\_v1\_low\_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**Text Encoder**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

File save location

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors
│   ├───📂 loras/
│   │   ├─── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
│   │   └─── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

### 3. 按步骤完成工作流

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1c5d26bea52f7f790ac6059e7a195c8d" alt="Wan2.2 Fun Control 工作流步骤" data-og-width="4088" width="4088" data-og-height="2138" height="2138" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d8ed6961696acf9bc7873cc8e2205ef9 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b2fbdef2bebb0062d41edce5d6956d94 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1cff6e967bef4a5c089cd08078b7bea3 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7d37bf6785db4ef7d541381860663513 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=472acf76ca37f17786fd3950c3ca0857 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=bc7b5ea03c54650e9773d6c0e766d281 2500w" />

<Note>
  这个工作流是使用了 LoRA 的工作流，请确保对应的 Diffusion model 和 LoRA 是一致的, high noise 和 low noise 的模型和 LoRA 需要对应使用
</Note>

1. **High noise** 模型及 **LoRA** 加载

* 确保 `Load Diffusion Model` 节点加载了 `wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors` 模型
* 确保 `LoraLoaderModelOnly` 节点加载了 `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors`

2. **Low noise** 模型及 **LoRA** 加载

* 确保 `Load Diffusion Model` 节点加载了 `wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors` 模型
* 确保 `LoraLoaderModelOnly` 节点加载了 `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors`

3. 确保 `Load CLIP` 节点加载了 `umt5_xxl_fp8_e4m3fn_scaled.safetensors` 模型
4. 确保 `Load VAE` 节点加载了 `wan_2.1_vae.safetensors` 模型
5. 在 `Load Image` 节点上传起始帧
6. 在第二个 `Load video` 节点控制视频的 pose 视频, 提供的视频已经经过预处理可以直接使用
7. 由于我们提供的视频是预处理过的 pose 视频，所以对应的视频图像预处理节点需要禁用，你可以选中后使用 Ctrl + B\` 来禁用
8. 修改 Prompt 使用中英文都可以
9. 在 `Wan22FunControlToVideo` 修改对应视频的尺寸, 默认设置了 640\*640 的分辨率来避免低显存用户使用这个工作流时过于耗时
10. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成

### 补充说明

由于在 ComfyUI 自带的节点中，预处理器节点只有 Canny 的预处理器，你可以使用使用类似 [ComfyUI-comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) 来实现其它类型的图像预处理
