> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Wan2.1 Fun Control 视频示例

> 本文介绍了如何在 ComfyUI 中完成 Wan2.1 Fun Control 使用控制视频来完成视频生成的示例

## 关于 Wan2.1-Fun-Control

**Wan2.1-Fun-Control** 是阿里团队推出的开源视频生成与控制项目，通过引入创新性的控制代码（Control Codes）机制，结合深度学习和多模态条件输入，能够生成高质量且符合预设控制条件的视频。该项目专注于通过多模态控制条件实现对生成视频内容的精准引导。

目前 Fun Control 模型支持多种控制条件，包括 **Canny（线稿）**、**Depth（深度）**、**OpenPose（人体姿势）**、**MLSD（几何边缘）** 等，同时支持使用 **轨迹控制**。
模型还支持多分辨率视频预测，分辨率可选 512、768 和 1024，帧率为每秒 16 帧，最长可生成 81 帧（约 5 秒）的视频。

模型版本方面：

* **1.3B** 轻量版：适合本地部署和快速推理，**对显存要求较低**
* **14B** 高性能版：模型体积达 32GB+，效果更优但 **需高显存支持**

下面是相关代码仓库的示例

* [Wan2.1-Fun-1.3B-Control](https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-Control)
* [Wan2.1-Fun-14B-Control](https://huggingface.co/alibaba-pai/Wan2.1-Fun-14B-Control)
* 代码仓库：[VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun)

**目前 ComfyUI 已原生支持了 Wan2.1 Fun Control 模型** ，在开始本篇教程前，请更新你的 ComfyUI 保证你的版本在[这个提交](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82)版本之后

在本篇指南中我们将提供两个工作流：

* 仅使用原生的 Comfy Core 节点的工作流
* 使用自定义节点的工作流

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

<Tip>
  由于目前原生节点在视频支持方面有所欠缺，完全使用原生节点的工作流是为了能保证在使用过程中用户不需要安装自定义节点就可以完成对应的工作流, 但在视频相关的生成中，我们发现现阶段很难在不使用自定义节点的情况下同时提供良好的使用体验，所以在本篇指南中我们提供了两个版本的工作流。
</Tip>

## 相关模型安装

这些模型你仅需要安装一次，另外在对应的工作流图片中也包含了模型下载信息，你可以选择你喜欢的方式下载模型。

下面的模型你可以在 [Wan\_2.1\_ComfyUI\_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) 和 [Wan2.1-Fun](https://huggingface.co/collections/alibaba-pai/wan21-fun-67e4fb3b76ca01241eb7e334) 找到

点击对应链接进行下载，如果你之前使用过 Wan 相关的工作流，那么你仅需要下载 **Diffusino models**

**Diffusion models** 选择 1.3B 或 14B, 14B 的文件体积更大（32GB）但是对于运行显存要求也较高，

* [wan2.1\_fun\_control\_1.3B\_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_fun_control_1.3B_bf16.safetensors?download=true)
* [Wan2.1-Fun-14B-Control](https://huggingface.co/alibaba-pai/Wan2.1-Fun-14B-Control/blob/main/diffusion_pytorch_model.safetensors?download=true)： 建议下载后重命名为 `Wan2.1-Fun-14B-Control.safetensors`

**Text encoders** 选择下面两个模型中的一个，fp16 精度体积较大对性能要求高

* [umt5\_xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors?download=true)
* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true)

**CLIP Vision**

* [clip\_vision\_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true)

文件保存位置

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── wan2.1_fun_control_1.3B_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   └── 📂 vae/
│   │   └── wan_2.1_vae.safetensors
│   └── 📂 clip_vision/
│       └──  clip_vision_h.safetensors                 
```

## ComfyUI 原生工作流

在此工作流中，我们使用转换成 WebP 格式的视频，这是因为目前`Load Image` 节点还不支持 mp4 格式的视频，另外我们使用 Canny Edge 来对原始的视频进行图像的预处理, 由于经常有用户在安装自定义节点过程中遇到安装失败和环境的问题，所以这一版本的工作流完全使用原生节点来实现，来优先保证体验。

感谢我们强大的 ComfyUI 作者们，他们带来了功能丰富的相关节点，如果你需要直接查看相关版本直接查看[使用自定义节点的工作流](#使用自定义节点的工作流)

### 1. 工作流相关文件下载

#### 1.1 工作流文件

下载下面的图片，并拖入 ComfyUI 中以加载对应的工作流

![Wan2.1 Fun Control 原生工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/wan2.1_fun_control/wan2.1_fun_control_native.webp)

#### 1.2 输入图片及视频下载

请下载下面的图片及视频，我们将作为输入。

![输入参考图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/wan2.1_fun_control/input/01-portrait_remix.png)

![输入参考视频](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/wan2.1_fun_control/input/01-portrait_video.webp)

### 2. 按步骤完成工作流

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_native_flow_diagram.png?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=97774a50d0e95007c34d94a6eb2d9580" alt="Wan2.1 Fun Control 工作流步骤" data-og-width="2201" width="2201" data-og-height="1907" height="1907" data-path="images/tutorial/video/wan/fun_control_native_flow_diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_native_flow_diagram.png?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7223492ed08271f6722dbbbc03205e47 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_native_flow_diagram.png?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=94960baeeaa96f9a0bac5a2e627135e6 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_native_flow_diagram.png?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c323157e3482f4dbc1882e395bee4fac 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_native_flow_diagram.png?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ca92e9b2239e9d1c69e9409b1b8eadd4 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_native_flow_diagram.png?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4aea0fb344f2738824e3a551c32535a6 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_native_flow_diagram.png?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=cddab1cd5381dd9ba96f510f18ad5809 2500w" />

1. 确保 `Load Diffusion Model` 节点加载了 `wan2.1_fun_control_1.3B_bf16.safetensors`
2. 确保 `Load CLIP` 节点加载了 `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
3. 确保 `Load VAE` 节点加载了 `wan_2.1_vae.safetensors`
4. 确保 `Load CLIP Vision` 节点加载了 `clip_vision_h.safetensors `
5. 在 `Load Image` 节点（已被重命名为`Start_image`） 上传起始帧
6. 在第二个 `Load Image` 节点上传用于控制视频。注意： 目前这个节点还不支持 mp4 只能使用 Webp 视频
7. （可选）修改 Prompt 使用中英文都可以
8. （可选）在 `WanFunControlToVideo` 修改对应视频的尺寸，不要使用过大的尺寸
9. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成

### 3. 使用说明

* 由于我们需要和控制视频一致的帧数输入到 `WanFunControlToVideo`  节点，如果对应的帧数数值大于实际的控制视频帧数，将会导致多余的帧不符合控制条件的画面出现，这个问题我们将在[使用自定义节点的工作流](#使用自定义节点的工作流)中解决
* 使用类似 [ComfyUI-comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) 来实现更丰富的控制

## 使用自定义节点的工作流

我们将需要安装下面两个自定义节点：

* [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
* [ComfyUI-comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

你可以使用 [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager) 安装缺失节点的功能或者参照对应自定义节点包的安装说明来完成对应节点的安装

### 1. 工作流相关文件下载

#### 1.1 工作流文件

下载下面的图片，并拖入 ComfyUI 中以加载对应的工作流

![工作流文件](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/wan2.1_fun_control/wan2.1_fun_control_use_custom_nodes.webp)

<Note>
  由于视频文件体积较大，你也可以点击[这里](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/wan2.1_fun_control/wan2.1_fun_control_use_custom_nodes.json)下载 Json 格式的工作流文件。
</Note>

#### 1.2 输入图片及视频下载

请下载下面的图片及视频，我们将会用于输入
![输入参考图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/wan2.1_fun_control/input/02-robot's_eye.png)

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/wan2.1_fun_control/input/02-man's_eye.mp4" />

### 2. 按步骤完成工作流

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_using_custom_nodes_flow_diagram.png?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b22315f2f052e9196bd49b3d95a983f5" alt="Wan2.1 Fun Control 使用自定义节点的工作流步骤" data-og-width="2201" width="2201" data-og-height="1907" height="1907" data-path="images/tutorial/video/wan/fun_control_using_custom_nodes_flow_diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_using_custom_nodes_flow_diagram.png?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=675cdc7eefa6f2533ec005c00aed0019 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_using_custom_nodes_flow_diagram.png?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d8a519cf9a760ea5f1d4948b646566ba 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_using_custom_nodes_flow_diagram.png?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=259d2448c192245c2a0797c045025a5f 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_using_custom_nodes_flow_diagram.png?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0968a67a850f1668fc03a7fffa5a3f80 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_using_custom_nodes_flow_diagram.png?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d7f950bcd4b060a60ffb6d63b8df3184 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_using_custom_nodes_flow_diagram.png?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c056f1c3a7bc09933386c9f8182c7254 2500w" />

> 模型部分基本是一致的，如果你已经体验过仅使用原生节点的工作流，你可以直接上传对应的图片然后运行即可

1. 确保 `Load Diffusion Model` 节点加载了 `wan2.1_fun_control_1.3B_bf16.safetensors`
2. 确保 `Load CLIP` 节点加载了 `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
3. 确保 `Load VAE` 节点加载了 `wan_2.1_vae.safetensors`
4. 确保 `Load CLIP Vision` 节点加载了 `clip_vision_h.safetensors `
5. 在 `Load Image` 节点上传起始帧
6. 在 `Load Video(Upload)` 自定义节点上传 mp4 格式视频，请注意对应工作流有对默认的 `frame_load_cap`进行了调整
7. `DWPose Estimator` 处针对当前图像仅使用了 `detect_face` 的选项
8. （可选）修改 Prompt 使用中英文都可以
9. （可选）在 `WanFunControlToVideo` 修改对应视频的尺寸，不要使用过大的尺寸
10. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成

### 3. 工作流说明

感谢 ComfyUI 社区作者带来的自定义节点包

* 在这个示例中使用了 `Load Video(Upload)` 来实现对 mp4 视频的支持
* `Load Video(Upload)` 中获取到的 `video_info` 我们得以对输出的视频保持同样的 `fps`
* 你可以替换 `DWPose Estimator` 为 `ComfyUI-comfyui_controlnet_aux` 节点包中的其它预处理器

## 使用技巧

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/apply_multi_control_videos.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7bb51781350a318a61068b1b369b816f" alt="Apply Multi Control Videos" data-og-width="1726" width="1726" data-og-height="1156" height="1156" data-path="images/tutorial/video/wan/apply_multi_control_videos.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/apply_multi_control_videos.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=46a23cf7862f32a64df3d1d01b73e577 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/apply_multi_control_videos.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6fbce18d1761b87f42e37a0cbf323124 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/apply_multi_control_videos.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b7d1094d3948dae2188e0e859d6d0b6e 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/apply_multi_control_videos.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2af733309ec65443188bbaecae9023fe 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/apply_multi_control_videos.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5e17b08c24145eb84e7abc14360042b8 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/apply_multi_control_videos.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ca67be00b8e19483845fb3c12bed1cd4 2500w" />

* 一个有用的技巧是，你可以结合多种图像预处理技术，然后使用 `Image Blend` 节点来实现同时应用多种控制方法的目的。
* 你可以使用 `ComfyUI-VideoHelperSuite` 的 `Video Combine` 节点来实现将对应视频存储为 mp4 格式
* 我们使用 `SaveAnimatedWEBP` 是因为我们目前并不支持在 **mp4** 中嵌入工作流信息, 而且有些自定义节点可能没有考虑工作流嵌入，为了在视频中保存工作流，所以我们选择 `SaveAnimatedWEBP` 节点。
* 不要设置过大的画面尺寸，这可能导致采样过程非常耗时，可以试着先生成小尺寸的图片然后再进行采样放大
* 发挥你的想象力，在这个工作流基础上加上一些文生图或者其它类型的工作流，实现直接从文本到视频生成风格转换
* 在 `WanFunControlToVideo` 节点中，`control_video` 不是必须的，所以有时候你可以不使用控制视频，先生成特别小尺寸的视频比如 320x320，然后使用再把它们作为控制视频输入来获得确定的结果

## 其它 Wan2.1 Fun Control 或者视频相关自定义节点

* [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
* [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
