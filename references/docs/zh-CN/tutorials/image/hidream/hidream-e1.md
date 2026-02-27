> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 原生版本 HiDream-E1, E1.1 工作流示例

> 本篇将引导了解并完成 ComfyUI 原生版本 HiDream-I1 文生图工作流实例

![HiDream-E1 演示](https://raw.githubusercontent.com/HiDream-ai/HiDream-E1/refs/heads/main/assets/demo.jpg)

HiDream-E1 是智象未来(HiDream-ai) 正式开源的交互式图像编辑大模型，是基于 HiDream-I1 构建的图像编辑模型。

可以使用自然语言来实现对图像的编辑，该模型基于 [MIT 许可证](https://github.com/HiDream-ai/HiDream-E1?tab=MIT-1-ov-file) 发布，支持用于个人项目、科学研究以及商用。
通过与此前发布的 [hidream-i1](/zh-CN/tutorials/image/hidream/hidream-i1)的共同组合，实现了 **从图像生成到编辑的** 创作能力。

| 名称              | 更新时间      | 推理步数 | 分辨率       | HuggingFace 仓库                                                          |
| --------------- | --------- | ---- | --------- | ----------------------------------------------------------------------- |
| HiDream-E1-Full | 2025-4-28 | 28   | 768x768   | 🤗 [HiDream-E1-Full](https://huggingface.co/HiDream-ai/HiDream-E1-Full) |
| HiDream-E1.1    | 2025-7-16 | 28   | 动态（1百万像素） | 🤗 [HiDream-E1.1](https://huggingface.co/HiDream-ai/HiDream-E1-1)       |

[HiDream E1 - Github](https://github.com/HiDream-ai/HiDream-E1)

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

## HiDream E1 及 E1.1 工作流相关模型

本篇指南涉及的所有模型你都可以在[这里](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files)找到, E1, E1.1 除了 Diffusion model 之外都是用相同的模型
我们在对应的工作流文件中也以包含了对应的模型信息，你可以选择手动下载模型保存，或者在加载工作流后按工作流提示进行下载，推荐使用 E1.1

这个模型的运行对显存占用要求极高，具体显存占用请参考对应部分的说明

**Diffusion Model**

你不用同时下载这两个模型，由于 E1.1 是基于 E1 的迭代版本，在实际测试中它的质量和效果较 E1 都有较大提升

* [hidream\_e1\_1\_bf16.safetensors(推荐)](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_e1_1_bf16.safetensors) 34.2GB
* [hidream\_e1\_full\_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_e1_full_bf16.safetensors) 34.2GB

**Text Encoder**：

* [clip\_l\_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_l_hidream.safetensors) 236.12MB
* [clip\_g\_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_g_hidream.safetensors) 1.29GB
* [t5xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors) 4.8GB
* [llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/llama_3.1_8b_instruct_fp8_scaled.safetensors) 8.46GB

**VAE**

* [ae.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/vae/ae.safetensors) 319.77MB

> 这个是 Flux 的 VAE 模型，如果你之前使用过 Flux 的工作流，你可能已经下载了这个文件。

文件保存位置

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├─── clip_l_hidream.safetensors
│   │   ├─── clip_g_hidream.safetensors
│   │   ├─── t5xxl_fp8_e4m3fn_scaled.safetensors
│   │   └─── llama_3.1_8b_instruct_fp8_scaled.safetensors
│   └── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 diffusion_models/
│       ├── hidream_e1_1_bf16.safetensors
│       └── hidream_e1_full_bf16.safetensors
```

## HiDream E1.1 ComfyUI 原生工作流示例

E1.1 是于 2025年7月16日更新迭代的版本, 这个版本支持动态一百万分辨率，在工作流中使用了 `Scale Image to Total Pixels` 节点来将输入图片动态调整为 1百万像素

<Tip>
  这里是在测试使用时对应的显存占用参考：

  1. A100 40GB (VRAM 使用率 95%)：第一次生成: 211s，第二次生成: 73s

  2. 4090D 24GB (VRAM 使用率 98%)

  * 完整版本: Out of memory
  * FP8\_e4m3fn\_fast (VRAM 98%) 第一次生成: 120s， 第二次生成: 91s
</Tip>

### 1. HiDream E1.1 工作流及相关素材

下载下面的图片并拖入 ComfyUI 已加载对应工作流及模型
![HiDream E1.1 工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/hidream/e1.1/hidream_e1_1.png)

下载下面的图片作为输入
![HiDream E1.1 工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/hidream/e1.1/input.webp)

### 2. 按步骤完成 HiDream-e1 工作流运行

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/hidream/hidream-e1-1-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7cb0e9f7bd4629121f484f14e68e2841" alt="hidream_e1_1_guide" data-og-width="4148" width="4148" data-og-height="2916" height="2916" data-path="images/tutorial/image/hidream/hidream-e1-1-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/hidream/hidream-e1-1-guide.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=345082b53e21270a783026072c4ef950 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/hidream/hidream-e1-1-guide.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6a52a7c80d70d13ed104ac61b5a9af7d 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/hidream/hidream-e1-1-guide.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3cda12787ff791f14a2eb90746687af8 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/hidream/hidream-e1-1-guide.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=84326c20c1ba5dd8b2733ffa4ac39703 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/hidream/hidream-e1-1-guide.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a4782832f10b467aa09cc2fd554908c4 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/hidream/hidream-e1-1-guide.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0878bb2ace3e4cd9ecc116ad86ea3ea5 2500w" />

按步骤完成工作流的运行

1. 确保`Load Diffusion Model` 节点加载了 `hidream_e1_1_bf16.safetensors` 模型
2. 确保`QuadrupleCLIPLoader` 中四个对应的 text encoder 被正确加载
   * clip\_l\_hidream.safetensors
   * clip\_g\_hidream.safetensors
   * t5xxl\_fp8\_e4m3fn\_scaled.safetensors
   * llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors
3. 确保`Load VAE` 节点中使用的是 `ae.safetensors` 文件
4. 在 `Load Image` 节点中加载提供的输入或你需要的图片
5. 在`Empty Text Encoder(Positive)` 节点中输入 **想要对图片进行的修改**
6. 在`Empty Text Encoder(Negative)` 节点中输入 **不想要在画面中出现的内容**
7. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片生成

### 3. 工作流补充说明

* 由于 HiDream E1.1 支持的是动态总像素为一百万像素输入，所以工作流使用了 `Scale Image to Total Pixels` 来将所有输入图片进行处理转化，这可能会导致比例尺寸相对于输入图片会有所变化
* 使用 fp16 版本的模型，在实际测试过程中，在 A100 40GB 和 4090D 24GB 时使用完整版本时会 Out of memory，所以工作流默认设置了使用 `fp8_e4m3fn_fast` 来进行推理

## HiDream E1 ComfyUI 原生 工作流示例

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=hidream_e1_full&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

E1 是于 2025 年 4 月 28 日发布的，这个模型只支持 768\*768 的分辨率

### 1. HiDream-e1 工作流及相关素材

<Tip>
  供参考，本文工作流在 Google Colab L4 22.5GB显存下采样步数 28步首次运行消耗 500s,第二次运行消耗 370s。
</Tip>

#### 1.1 下载工作流文件

请下载下面的图片并拖入 ComfyUI 中，工作流已包含模型下载信息，加载后将会提示你进行对应的模型下载。

![ComfyUI 原生 HiDream-e1 工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hidream_e1/hidream_e1_full.png)

#### 1.2 下载输入图片

请下载下面的图片，我们将用于输入

![ComfyUI 原生 HiDream-e1 工作流 输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hidream_e1/input.webp)

### 2. 按步骤完成 HiDream-e1 工作流运行

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_e1_full_step_guide.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c218858bea510e5fd5ab71f7885cd7db" alt="hidream_e1_full_step_guide" data-og-width="2277" width="2277" data-og-height="1725" height="1725" data-path="images/tutorial/advanced/hidream/hidream_e1_full_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_e1_full_step_guide.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c5330924f662371659a846e0465cce44 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_e1_full_step_guide.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=25ab45c23a4736ea6215efc616e69a90 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_e1_full_step_guide.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=4a8921e2fe6e4939a27b66aec62aa33c 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_e1_full_step_guide.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=5ca055a649e143526bbae0a8f2960699 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_e1_full_step_guide.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=7727631573100f50a4baf1a39ac2fa07 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_e1_full_step_guide.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=f939a5dd407c8cb786d8215281f14e0c 2500w" />

按步骤完成工作流的运行

1. 确保`Load Diffusion Model` 节点加载了 `hidream_e1_full_bf16.safetensors` 模型
2. 确保`QuadrupleCLIPLoader` 中四个对应的 text encoder 被正确加载
   * clip\_l\_hidream.safetensors
   * clip\_g\_hidream.safetensors
   * t5xxl\_fp8\_e4m3fn\_scaled.safetensors
   * llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors
3. 确保`Load VAE` 节点中使用的是 `ae.safetensors` 文件
4. 在 `Load Image` 节点中加载我们之前下载的输入图片
5. （重要）在`Empty Text Encoder(Positive)` 节点中输入 **想要修改的画面的提示词**
6. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片生成

### ComfyUI HiDream-e1 工作流补充说明

* 可能需要修改多次提示词或者进行多次的生成才能得到较好的结果
* 这个模型在改变图片风格上比较难保持一致性，需要尽可能完善提示词
* 由于模型支持的是 768\*768 的分辨率，在实际测试中调整过其它尺寸，在其它尺寸下图像表现能力不佳，甚至差异较大
