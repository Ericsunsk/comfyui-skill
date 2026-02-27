> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan ATI ComfyUI 原生工作流教程

> 使用轨迹控制视频生成。

**ATI（Any Trajectory Instruction）** 是由字节跳动团队提出的可控视频生成框架。ATI 基于 Wan2.1 实现，支持通过任意轨迹指令对视频中的物体、局部区域及摄像机运动进行统一控制。

项目地址：[https://github.com/bytedance/ATI](https://github.com/bytedance/ATI)

## 主要特性

* **统一运动控制**：支持物体、局部、摄像机等多种运动类型的轨迹控制。
* **交互式轨迹编辑器**：可视化工具，用户可在图片上自由绘制、编辑运动轨迹。
* **兼容 Wan2.1**：基于 Wan2.1 官方实现，环境和模型结构兼容。
* **丰富的可视化工具**：支持输入轨迹、输出视频及轨迹可视化。

## WAN ATI 轨迹控制工作流示例

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

### 1. 工作流下载

下载下面的视频并拖入 ComfyUI 中，以加载对应的工作流

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/ati/wan_ati.mp4" />

我们将使用下面的素材作为输入:
![v2v-input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/ati/input.jpg)

### 2. 模型下载

如果你没有成功下载工作流中的模型文件，可以尝试使用下面的链接手动下载

**Diffusion Model**

* [Wan2\_1-I2V-ATI-14B\_fp8\_e4m3fn.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true)

**Text encoders**   Chose one of following model

* [umt5\_xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors?download=true)
* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true)

**clip\_vision**

* [clip\_vision\_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors)

File save location

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   └───Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors # or other version
│   ├───📂 clip_vision/
│   │   └─── clip_vision_h.safetensors
│   └───📂 vae/
│       └──  wan_2.1_vae.safetensors
```

### 3. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=300a2b5bd7002d944e1224e22ed4cd92" alt="工作流步骤图" data-og-width="3746" width="3746" data-og-height="2924" height="2924" data-path="images/tutorial/video/wan/wan_ati_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c8046adac94511cc1fb4c3f5d0e6b033 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=abcae62b721b60748ae2af6b4f1b1f52 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1b107bdd946e957568fed198a02c35c0 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f08203be22e16cbe402365df10d8963e 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=19745c84e95bc68703f514f5a0303259 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=aa23cb94ca4f9edea4bba0aafdddeb31 2500w" />

请参照图片序号进行逐步确认，来保证对应工作流的顺利运行

1. 确保`Load Diffusion Model`节点加载了 `Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors` 模型
2. 确保`Load CLIP`节点加载了 `umt5_xxl_fp8_e4m3fn_scaled.safetensors` 模型
3. 确保`Load VAE`节点加载了 `wan_2.1_vae.safetensors` 模型
4. 确保`Load CLIP Vision`节点加载了 `clip_vision_h.safetensors` 模型
5. 在 `Load Image` 节点上传提供的输入图片
6. 轨迹编辑： 目前 ComfyUI 中还未有对应的轨迹编辑器，你可以使用下面的链接来完成轨迹编辑
   * [在线轨迹编辑工具](https://comfyui-wiki.github.io/Trajectory-Annotation-Tool/)
7. 如果你需要修改提示词（正向及负向）请在序号`5` 的 `CLIP Text Encoder` 节点中进行修改
8. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成
