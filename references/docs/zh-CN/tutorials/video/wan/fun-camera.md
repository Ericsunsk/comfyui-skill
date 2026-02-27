> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Wan2.1 Fun Camera 官方原生示例

> 本文介绍了如何在 ComfyUI 中使用 Wan2.1 Fun Camera 完成视频生成

## 关于 Wan2.1 Fun Camera

**Wan2.1 Fun Camera** 是阿里团队推出的视频生成项目，专注于通过摄像机运动来控制视频生成效果。

**模型权重下载地址**：

* [14B 版本](https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-14B-Control-Camera)
* [1.3B 版本](https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-1.3B-Control-Camera)

**代码仓库**：[VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun)

**目前 ComfyUI 已原生支持了 Wan2.1 Fun Camera 模型**。

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

## 相关模型安装

这些模型你仅需要安装一次，另外在对应的工作流图片中也包含了模型下载信息，你可以选择你喜欢的方式下载模型。

下面的所有模型你可以在 [Wan\_2.1\_ComfyUI\_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) 找到

**Diffusion Models** 选择 1.3B 或 14B：

* [wan2.1\_fun\_camera\_v1.1\_1.3B\_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors)
* [wan2.1\_fun\_camera\_v1.1\_14B\_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_fun_camera_v1.1_14B_bf16.safetensors)

下面的模型，如果你使用过 Wan2.1 的相关模型，那么你应该已经有了下面的模型，如果没有，请下载下面的模型：

**Text Encoders** 选择其中一个：

* [umt5\_xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors)
* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**CLIP Vision**

* [clip\_vision\_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors)

文件保存位置：

```
📂 ComfyUI/
├── 📂 models/
│ ├── 📂 diffusion_models/
│ │   ├── wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors # 1.3B 版本
│ │   └── wan2.1_fun_camera_v1.1_14B_bf16.safetensors # 14B 版本
│ ├── 📂 text_encoders/
│ │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│ ├── 📂 vae/
│ │   └── wan_2.1_vae.safetensors
│ └── 📂 clip_vision/
│     └── clip_vision_h.safetensors
```

## ComfyUI Wan2.1 Fun Camera 1.3B 原生工作流示例

### 1. 工作流相关文件下载

#### 1.1 工作流文件

下载下面的视频，并拖入 ComfyUI 中以加载对应的工作流：

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/fun-camera/v1.1/wan2.1_fun_camera_1.3B.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/fun-camera/v1.1/wan2.1_fun_camera_1.3B.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

<Note>
  如果你想使用 14B 版本，只需要将模型文件替换为 14B 版本即可，但请注意显存要求。
</Note>

#### 1.2 输入图片下载

请下载下面的图片，我们将作为起始帧：

![输入参考图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/fun-camera/v1.1/wan2.1_fun_camera_1.3B_input.jpg)

### 2. 按步骤完成工作流

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f6fb10f8a36cb9036a66e1e99986c641" alt="Wan2.1 Fun Camera 工作流步骤" data-og-width="3746" width="3746" data-og-height="2130" height="2130" data-path="images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=22ee500d14a988a10103816501d23c79 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f93891d54566878c22b523cb9f72b9e2 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=8dcb5b3cbf393f606d14b25dfc042b90 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c6fea8a46345ac06fa26538615751e30 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1b3de6566e1c172cae30fd29bc01a7cf 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f710b32856e9f27a40efa605fd884871 2500w" />

1. 确保加载了正确版本的模型文件：
   * 1.3B 版本：`wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors`
   * 14B 版本：`wan2.1_fun_camera_v1.1_14B_bf16.safetensors`
2. 确保 `Load CLIP` 节点加载了 `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
3. 确保 `Load VAE` 节点加载了 `wan_2.1_vae.safetensors`
4. 确保 `Load CLIP Vision` 节点加载了 `clip_vision_h.safetensors`
5. 在 `Load Image` 节点上传起始帧
6. 修改 Prompt，如果你使用了你自己的图像输入
7. 在 `WanCameraEmbedding` 节点设置相机动作
8. 点击 `Run` 按钮，或使用快捷键 `Ctrl(cmd) + Enter(回车)` 执行生成

## ComfyUI Wan2.1 Fun Camera 14B 工作流及输入图片

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/fun-camera/v1.1/wan2.1_fun_camera_14B.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/fun-camera/v1.1/wan2.1_fun_camera_14B.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

**输入图片**
![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/fun-camera/v1.1/wan2.1_fun_camera_14B_input.jpg)

## 性能参考

**1.3B 版本**：

* 512×512 RTX 4090 生成 81 帧约需 72 秒

**14B 版本**：

* RTX4090 24GB 显存在生成 512×512 分辨率时可能会出现显存不足, 在 A100 上运行尺寸过大时也出现过显存不足的情况
