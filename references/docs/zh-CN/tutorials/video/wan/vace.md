> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Wan2.1 VACE 视频示例

> 本文介绍了如何在 ComfyUI 中完成 Wan2.1 VACE 视频生成示例

<Warning>
  由于目前我们已经对模板做了调整，并增加了 CausVid LoRA 的相关使用及说明，本篇文档需要进行更新，还需一定准备时间，在此之前请参考模板中的备注信息进行使用
</Warning>

## 关于 VACE

VACE 14B 是阿里通义万相团队推出的开源视频编辑统一模型。该模型通过整合多任务能力、支持高分辨率处理及灵活的多模态输入机制，显著提升了视频创作的效率与质量。

该模型基于 [Apache-2.0](https://github.com/ali-vilab/VACE?tab=Apache-2.0-1-ov-file) 协议开源，可用于个人商业用途。

以下是其核心特性与技术亮点的综合分析：

* 多模态输入:支持文本、图像、视频、遮罩、控制信号等多种输入形式
* 统一架构:单一模型支持多种任务,可自由组合功能
* 动作迁移:基于参考视频生成连贯动作
* 局部替换:通过遮罩替换视频中的特定区域
* 视频扩展:补全动作或扩展背景
* 背景替换:保留主体更换环境背景

目前 VACE 发布了 1.3B 和 14B 两个版本，14B 版本相比 1.3B 版本，支持 720P 分辨率输出,画面细节和稳定性更好。

| 模型                                                          | 480P | 720P |
| ----------------------------------------------------------- | ---- | ---- |
| [VACE-1.3B](https://huggingface.co/Wan-AI/Wan2.1-VACE-1.3B) | ✅    | ❌    |
| [VACE-14B](https://huggingface.co/Wan-AI/Wan2.1-VACE-14B)   | ✅    | ✅    |

相关模型权重和代码仓库：

* [VACE-1.3B](https://huggingface.co/Wan-AI/Wan2.1-VACE-1.3B)
* [VACE-14B](https://huggingface.co/Wan-AI/Wan2.1-VACE-14B)
* [Github](https://github.com/ali-vilab/VACE)
* [VACE 项目主页](https://ali-vilab.github.io/VACE-Page/)

## 模型下载及在工作流中的加载

由于本篇文档中设计的几个工作流都使用同一套工作流模板，所以我们可以先完成模型下载及加载的信息介绍，然后通过 Bypass 不同的节点来启用/ 禁用不同的输入来实现不同的工作流。
在具体示例中对应的工作流信息中已经嵌入了模型下载信息，所以你也可以在下载具体示例的工作流时来完成模型下载。

### 模型下载

**diffusion\_models**
[wan2.1\_vace\_14B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors)
[wan2.1\_vace\_1.3B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_1.3B_fp16.safetensors)

<Tip>
  如果你之前使用过 Wan Video 相关的工作流，下面的模型文件你已经下载过了。
</Tip>

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true)

从**Text encoders** 选择一个版本进行下载

* [umt5\_xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors?download=true)
* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true)

文件保存位置

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └─── wan2.1_vace_14B_fp16.safetensors # 或 wan2.1_vace_1.3B_fp16.safetensors
│   ├── 📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors # 或 umt5_xxl_fp16.safetensors
│   └── 📂 vae/
│       └──  wan_2.1_vae.safetensors
```

### 模型加载

由于在本篇指南中，我们所使用的模型是一致的，工作流也相同，只是 Bypass 了部分的节点来启用/ 禁用不同的输入，请参考下面的图片确保在对应不同的工作流中，对应的模型都已正确加载

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d46629d2ee7cfa1b942d4d92217992b1" alt="Wan2.1 VACE 模型加载" data-og-width="2910" width="2910" data-og-height="1394" height="1394" data-path="images/tutorial/video/wan/wan-vace-model-loading.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=91477fcc563509d8b100585ddebac58e 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fc8e48cf61a14dfcefa53557fd607bba 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4c95a9bfd255626b27f53e53ef190f74 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e1541bcd0a68bf62b80881009dc45ce6 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9c721327faf7e078b44f4e22c3c17f80 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a59ba6ef698d23b87b13b21c56dba925 2500w" />

1. 确保 `Load Diffusion Model` 节点加载了 `wan2.1_vace_14B_fp16.safetensors`
2. 确保 `Load CLIP` 节点加载了 `umt5_xxl_fp8_e4m3fn_scaled.safetensors` 或者 `umt5_xxl_fp16.safetensors`
3. 确保 `Load VAE` 节点加载了 `wan_2.1_vae.safetensors`

### 如何取消节点的 Bypass 状态

当一个节点被设置为 Bypass 状态时，通过该节点的数据将不受节点的影响，直接输出，下面是如何取消节点的 Bypass 状态的三种方法
我们通常在不需要一些节点时设置节点的 Bypass 状态，而不用将它们从节点中删除改变工作流。

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=3a57352f6bc6f1c16ce0792d384d16fd" alt="取消 Bypass" data-og-width="1830" width="1830" data-og-height="1128" height="1128" data-path="images/interface/nodes/cancel-bypass.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=7d117f2ce9b248c5dfef9a2a60f4e19f 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4aaf480c01ed83648e715bc1db351865 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=672c588fab6405b4abe849298ed662ff 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c1bf919830e35f35c02b847721aeebc7 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=62d75544a82f04cfa7c5861cdeeed1c0 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=27e6b1f470ec9a7e5879b57330d50bee 2500w" />

1. 选中节点后，在选择工具箱中点击标识部分的箭头，即可快速切换节点的 Bypass 状态
2. 选中节点后，鼠标右键点击节点，选择 `模式(Mode)` -> `总是(Always)` 切换到 Always 模式
3. 选中节点后，鼠标右键点击节点，选择 `绕过(Bypass)` 选项，切换 Bypass 状态

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

## VACE 文生视频工作流

<Tip>
  如果无法从 mp4 文件加载工作流，请确保你的 ComfyUI 前端版本是最新的版本，请参考 [requirements.txt](https://github.com/comfyanonymous/ComfyUI/blob/master/requirements.txt) ，确保你能够从 mp4 文件加载工作流。

  目前 1.19.9 是 requirements.txt 文件中的最新 ComfyUI 前端版本。
</Tip>

### 1. 工作流下载

下载下面视频，并拖入 ComfyUI 中，以加载对应的工作流

<video controls className="w-full aspect-video" src="https://github.com/Comfy-Org/example_workflows/raw/refs/heads/main/video/wan/vace/vace-t2v.mp4" />

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6f24e0be5f1ee91ea5becd79501053bd" alt="图像" data-og-width="3018" width="3018" data-og-height="1394" height="1394" data-path="images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0cd5b40ceedcf75c9fbde402ce4a14da 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b1f90e2fdac271316123b90a857234f5 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ff5306447eb8ac27b41493f81403e6a7 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=82b65902537bc52e8bec0cd1ab902533 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7ed23e4062bcd3eef1f7fb626e5e963d 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6c2b3687c3865ee1cd442b9adf3c8812 2500w" />

请参照图片序号进行逐步确认，来保证对应工作流的顺利运行

1. 在 `CLIP Text Encode (Positive Prompt)` 节点中输入正向提示词
2. 在 `CLIP Text Encode (Negative Prompt)` 节点中输入负向提示词
3. 在 `WanVaceToVideo` 设置对应图像的尺寸（首次运行建议设置 640\*640 的分辨率），帧数（视频的时长）
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成
5. 生成完成后对应的视频会自动保存到 `ComfyUI/output/video` 目录下（子文件夹位置取决于 `save video` 节点设置）

<Tip>
  在测试过程中，使用 4090 显卡：

  * 720\*1280 的分辨率，生成 81 帧视频需要 40 分钟左右
  * 640\*640 的分辨率，生成 49 帧视频需要 7 分钟左右

  但相对的 720P 的视频质量会更好。
</Tip>

## VACE 图生视频工作流

你可以继续使用上面的工作流文件，只需要将 **Load reference image** 的 `Load image` 节点的 Bypass 取消，并输入对应的图片，你也可以使用下面的图片，在这个文件里，我们已经完成了对应的参数设置。

### 1. 工作流下载

下载下面的视频，并拖入 ComfyUI 中，以加载对应的工作流

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/i2v/vace_i2v.mp4" />

请下载下面图片作为输入图片

![vace-i2v-input](https://github.com/Comfy-Org/example_workflows/raw/refs/heads/main/video/wan/vace/i2v/input.jpg)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e22bf953a5900de76c55ed9af3881ea3" alt="工作流步骤图" data-og-width="2912" width="2912" data-og-height="1317" height="1317" data-path="images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7f1807f6dad3f93106ff5ad6329c8f7c 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c09e0a08107d4a6ae30a4a5784c6e652 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b7863d0b4601fa037084d2d008131601 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=531e554960d84d24b2ba6d4facadba50 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ae5cd06c50fc44a1fc4e690c4c3d4821 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7a4bb7922bc8e81b1bc4b5ddc1f3c8e8 2500w" />

请参照图片序号进行逐步确认，来保证对应工作流的顺利运行

1. 在 `Load image` 节点中输入对应的图片
2. 你可以像文生图工作流一样完成来进行提示词的修改和编辑
3. 在 `WanVaceToVideo` 设置对应图像的尺寸（首次运行建议设置 640\*640 的分辨率），帧数（视频的时长）
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成
5. 生成完成后对应的视频会自动保存到 `ComfyUI/output/video` 目录下（子文件夹位置取决于 `save video` 节点设置）

<Tip>
  你可能会使用类似获取图片尺寸一点的节点来设置对应的分辨率，但是由于对应节点有宽度和高度的步长要求，会导致如果你的图片尺寸无法被 16 整除时，可能会出现报错提示。
</Tip>

### 3. 工作流补充说明

VACE 还支持在一张图像中输入多个参考图像，来生成对应的视频，你可以在 VACE 的项目页中看到相关的[示例](https://ali-vilab.github.io/VACE-Page/)

## VACE 视频到视频工作流

### 1. 工作流下载

下载下面的视频并拖入 ComfyUI 中，以加载对应的工作流

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/vace_v2v.mp4" />

我们将使用下面的素材作为输入:

1. 用于参考图像的输入图片
   ![v2v-input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/input.jpg)

2. 下面的视频已经经过预处理，我们将用于控制视频的生成

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/post+depth.mp4" />

3. 下面的视频是原始视频，你可以下载下面的素材来使用类似 [comfyui\_controlnet\_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) 这样的预处理节点来对图像进行预处理

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/original.mp4" />

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a59e79204a1faf9b3f63c482b65df764" alt="工作流步骤图" data-og-width="2912" width="2912" data-og-height="1317" height="1317" data-path="images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2e445a8b2597f81581dffcb4e122bdaa 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ee5d4773ce441c2ca25e9e738a6affde 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=dbc1798f5324e9a62b5415b61c321364 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=65372a3779b7c267e7c36b1b937a9499 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c68336ae95a110ec9eb9214c8c45b79f 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fb99bc848cb951a0c43388166fec7d77 2500w" />

请参照图片序号进行逐步确认，来保证对应工作流的顺利运行

1. 在 `Load reference image` 中的 `Load Image` 节点输入参考图片
2. 在 `Load control video` 中的 `Load Video` 节点输入控制视频，由于提供的视频是经过预处理的，所以你不需要进行额外的处理
3. 如果你需要自己针对原始视频进行预处理，可以修改 `Image preprocessing` 分组，或者使用 `comfyui_controlnet_aux` 节点来完成对应的节点预处理
4. 修改提示词
5. 在 `WanVaceToVideo` 设置对应图像的尺寸（首次运行建议设置 640\*640 的分辨率），帧数（视频的时长）
6. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成
7. 生成完成后对应的视频会自动保存到 `ComfyUI/output/video` 目录下（子文件夹位置取决于 `save video` 节点设置）

## VACE 视频扩展工作流

\[待更新]

## VACE 首尾帧视频生成

\[待更新]

要保证首尾帧生效，需要满足：

* 对应视频 `length` 设置需要满足 `length-1` 后能够被 `4` 整除
* 对应的 `Batch_size` 设置需要满足 `Batch_size = length - 2`

## 相关节点文档

请查阅下面的文档了解相关的节点

<Card title="WanVaceToVideo 节点文档" icon="book" href="/zh-CN/built-in-nodes/conditioning/video-models/wan-vace-to-video">
  WanVaceToVideo 节点文档
</Card>

<Card title="TrimVideoLatent 节点文档" icon="book" href="/zh-CN/built-in-nodes/latent/video/trim-video-latent">
  ComfyUI TrimVideoLatent 节点文档
</Card>
