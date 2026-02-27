> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan2.2 视频生成ComfyUI 官方原生工作流示例

> 阿里云通义万相2.2视频生成模型在ComfyUI中的官方使用指南

<iframe className="w-full aspect-video rounded-xl" src="//player.bilibili.com/player.html?isOutside=true&aid=114930791549176&bvid=BV1gk8EzaEGt&cid=31337744098&p=1" title="ComfyUI Selection Toolbox New Features" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

通义万相 2.2（Wan 2.2）是阿里云推出的新一代多模态生成模型。该模型采用创新的 MoE（Mixture of Experts）架构，由高噪专家模型和低噪专家模型组成，能够根据去噪时间步进行专家模型划分，从而生成更高质量的视频内容。

Wan 2.2 具备三大核心特性：影视级美学控制，深度融合专业电影工业的美学标准，支持光影、色彩、构图等多维度视觉控制；大规模复杂运动，轻松还原各类复杂运动并强化运动的流畅度和可控性；精准语义遵循，在复杂场景和多对象生成方面表现卓越，更好还原用户的创意意图。
模型支持文生视频、图生视频等多种生成模式，适用于内容创作、艺术创作、教育培训等多种应用场景。

[Wan2.2 提示词指南](https://alidocs.dingtalk.com/i/nodes/jb9Y4gmKWrx9eo4dCql9LlbYJGXn6lpz)

## 模型亮点

* **影视级美学控制**：专业镜头语言，支持光影、色彩、构图等多维度视觉控制
* **大规模复杂运动**：流畅还原各类复杂运动，强化运动可控性和自然度
* **精准语义遵循**：复杂场景理解，多对象生成，更好还原创意意图
* **高效压缩技术**：5B版本高压缩比VAE，显存优化，支持混合训练

## Wan2.2 开源模型版本

Wan2.2 系列模型基于 Apache2.0 开源协议，支持商业使用。Apache2.0 许可证允许您自由使用、修改和分发这些模型，包括商业用途，只需保留原始版权声明和许可证文本。

| 模型类型 | 模型名称            | 参数量 | 主要功能                                | 模型仓库                                                                |
| ---- | --------------- | --- | ----------------------------------- | ------------------------------------------------------------------- |
| 混合模型 | Wan2.2-TI2V-5B  | 5B  | 支持文本生成视频和图像生成视频的混合版本，单一模型满足两大核心任务需求 | 🤗 [Wan2.2-TI2V-5B](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)   |
| 图生视频 | Wan2.2-I2V-A14B | 14B | 将静态图像转换为动态视频，保持内容一致性和流畅的动态过程        | 🤗 [Wan2.2-I2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B) |
| 文生视频 | Wan2.2-T2V-A14B | 14B | 从文本描述生成高质量视频，具备影视级美学控制和精准语义遵循       | 🤗 [Wan2.2-T2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B) |

## ComfyOrg Wan2.2 直播回放

对于 ComfyUI Wan2.2 的使用，我们有进行了直播，你可以查看这些回放了解如何使用

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/Z0yo16LzReA?si=I-BlUfktxqt9URQk" title="ComfyUI Wan2.2 直播回放" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/z62QLQ3XqSA?si=yUenvPa9Q4-VX28M" title="ComfyUI Wan2.2 深入" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/0fyZhXga8P8?si=PMv9xQLP32wP8Ni9" title="ComfyUI Wan2.2 深入 #2" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

本篇教程将使用 [🤗 Comfy-Org/Wan\_2.2\_ComfyUI\_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)的版本进行

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

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ccf5d56775dac715ac40f767978d4371" alt="Wan2.2 template" data-og-width="3450" width="3450" data-og-height="1944" height="1944" data-path="images/tutorial/video/wan/wan2_2/template.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3a370d08de0764cc851c0d08de9183a3 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a8eb6733fb6a6bfabafe1722bf428f9c 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=974dda9a8a36e0e56e489d60c8252c1e 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d1ecdc72c324c21a14e3c75260dc6636 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e9298fea453b141f231b98eacda03c8a 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=dae5c8f09553dc9f5e2895c24b4200cf 2500w" />

## Wan2.2 TI2V 5B 混合版本工作流示例

<Tip>
  Wan2.2 5B 版本配合 ComfyUI 原生 offloading功能，能很好地适配 8GB 显存。
</Tip>

### 1. 工作流文件下载

请更新你的 ComfyUI 到最新版本，并通过菜单 `工作流` -> `浏览模板` -> `视频` 找到 “Wan2.2 5B video generation” 以加载工作流

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan_2_2_5B_t2v.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_5B_ti2v.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_5B_ti2v&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

### 2. 手动下载模型

**Diffusion Model**

* [wan2.2\_ti2v\_5B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors)

**VAE**

* [wan2.2\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan2.2_vae.safetensors)

**Text Encoder**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   └───wan2.2_ti2v_5B_fp16.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan2.2_vae.safetensors
```

### 3. 按步骤完成工作流

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=964289dd7f3c51119c95f98372dbd209" alt="步骤图" data-og-width="4182" width="4182" data-og-height="2027" height="2027" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=610a2a4f3a050187e58ce0fd61b619be 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=81da2a077caa2ab0fac0a5b7947711dc 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=294f3d3cb6eb69d1e145b5678c0294ad 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3dbca42c849ead6457dad35ce4b640de 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9e8b8ebbe5cb9458449ea202ef0bb518 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=bff729d4a7943a3877a619933770601e 2500w" />

1. 确保`Load Diffusion Model`节点加载了 `wan2.2_ti2v_5B_fp16.safetensors` 模型
2. 确保`Load CLIP`节点加载了 `umt5_xxl_fp8_e4m3fn_scaled.safetensors` 模型
3. 确保`Load VAE`节点加载了 `wan2.2_vae.safetensors` 模型
4. （可选）如果你需要进行图生视频，可以使用快捷键 Ctrl+B 来启用 `Load image` 节点来上传图片
5. （可选）在`Wan22ImageToVideoLatent` 你可以进行尺寸的设置调整，和视频总帧数 `length` 调整
6. （可选）如果你需要修改提示词（正向及负向）请在序号`5` 的 `CLIP Text Encoder` 节点中进行修改
7. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成

## Wan2.2 14B T2V 文生视频工作流示例

### 1. 工作流文件下载

请更新你的 ComfyUI 到最新版本，并通过菜单  `工作流` -> `浏览模板` -> `视频` 找到 “Wan2.2 14B T2V”

或者更新你的 ComfyUI 到最新版本后，下载下面的工作流并拖入 ComfyUI 以加载工作流

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan_2_2_14B_t2v.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_t2v.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_14B_t2v&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

### 2. 手动下载模型

**Diffusion Model**

* [wan2.2\_t2v\_high\_noise\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors)
* [wan2.2\_t2v\_low\_noise\_14B\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**Text Encoder**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

### 3. 按步骤完成工作流

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0ce44ad0e8f5e8dff6c9324404ee5e46" alt="步骤图" data-og-width="4182" width="4182" data-og-height="2255" height="2255" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=36116adfbdba4e7bcb67ad6c9e613387 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3070fc1eb3736451054f1f1336c7b1d6 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9acc8bdb71542b8a4c940eeede74dc68 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2255e183d00f8dbfa3878add257c1436 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=fc533adad23782d442693837f3b88b65 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7c240ef2b8046c79384a72e4fb1dd6ef 2500w" />

1. 确保第一个 `Load Diffusion Model`节点加载了 `wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors` 模型
2. 确保第二个 `Load Diffusion Model`节点加载了 `wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors` 模型
3. 确保`Load CLIP`节点加载了 `umt5_xxl_fp8_e4m3fn_scaled.safetensors` 模型
4. 确保`Load VAE`节点加载了 `wan_2.1_vae.safetensors` 模型
5. （可选）在`EmptyHunyuanLatentVideo` 你可以进行尺寸的设置调整，和视频总帧数 `length` 调整
6. 如果你需要修改提示词（正向及负向）请在序号`6` 的 `CLIP Text Encoder` 节点中进行修改
7. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成

## Wan2.2 14B I2V 图生视频工作流示例

### 1. 工作流文件

请更新你的 ComfyUI 到最新版本，并通过菜单  `工作流` -> `浏览模板` -> `视频` 找到 “Wan2.2 14B I2V” 以加载工作流

或者更新你的 ComfyUI 到最新版本后，下载下面的工作流并拖入 ComfyUI 以加载工作流

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan_2_2_14B_i2v.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_i2v.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_14B_i2v&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

你可以使用下面的图片作为输入
![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/input.jpg)

### 2. 手动下载模型

**Diffusion Model**

* [wan2.2\_i2v\_high\_noise\_14B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp16.safetensors)
* [wan2.2\_i2v\_low\_noise\_14B\_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp16.safetensors)

**VAE**

* [wan\_2.1\_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors)

**Text Encoder**

* [umt5\_xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_i2v_low_noise_14B_fp16.safetensors
│   │   └─── wan2.2_i2v_high_noise_14B_fp16.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

### 3. 按步骤完成工作流

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a9c4c6cfa365f7a0e4d7274b6c799316" alt="步骤图" data-og-width="4182" width="4182" data-og-height="2336" height="2336" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=73611770041093ac8431217ffd97ee54 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=96b2ee5717f5a981d9d1143880d7c5fa 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=65141a2c12393339961080a4d94dbb11 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a326793c8feabd5de08c85f6d828269f 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3cc839df08cf7f06bc745de92236981d 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9b3c4bf4352fb753e9878098452bfb39 2500w" />

1. 确保第一个 `Load Diffusion Model`节点加载了 `wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors` 模型
2. 确保第二个 `Load Diffusion Model`节点加载了 `wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors` 模型
3. 确保`Load CLIP`节点加载了 `umt5_xxl_fp8_e4m3fn_scaled.safetensors` 模型
4. 确保`Load VAE`节点加载了 `wan_2.1_vae.safetensors` 模型
5. 在 `Load Image` 节点上传作为起始帧的图像
6. 如果你需要修改提示词（正向及负向）请在序号`6` 的 `CLIP Text Encoder` 节点中进行修改
7. 可选）在`EmptyHunyuanLatentVideo` 你可以进行尺寸的设置调整，和视频总帧数 `length` 调整
8. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成

## Wan2.2 14B FLF2V 首尾帧视频生成工作流示例

首尾帧工作流使用模型位置与 I2V 部分完全一致

### 1. 工作流及素材生成

下载下面的视频或者 JSON 格式工作流在 ComfyUI 中打开

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan22_14B_flf2v.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/video_wan2_2_14B_flf2v.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 格式工作流</p>
</a>

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=video_wan2_2_14B_flf2v&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

下载下面的素材作为输入

![Input Material](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan22_14B_flf2v_start_image.png)
![Input Material](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/2.2/wan22_14B_flf2v_end_image.png)

### 2. 按步骤完成工作流

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6def22f3de024219e66dd4ea7cae7c03" alt="步骤图" data-og-width="2091" width="2091" data-og-height="1540" height="1540" data-path="images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c49a70cd83704dc313144a224d8b384e 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f387777923416ff75fda5318b3dea01f 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=41dc482b545e11b4c666b38b03239b8d 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=789e93dc113653a909d3f01799b50430 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c1844f0c2b70aacf3262350ab824f4af 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ae6a4485c77f8a75a12983129ebe5251 2500w" />

1. 在第一个 `Load Image` 节点上传作为起始帧的图像
2. 在第二个 `Load Image` 节点上传作为起始帧的图像
3. 在 `WanFirstLastFrameToVideo` 上修改尺寸设置
   * 我们默认设置了一个比较小的尺寸，防止低显存用户运行占用过多资源
   * 如果你有足够的显存，可以尝试 720P 左右尺寸
4. 根据你的首尾帧撰写合适的提示词
5. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频生成

## 社区资源

### GGUF 版本

* [bullerwins/Wan2.2-I2V-A14B-GGUF/](https://huggingface.co/bullerwins/Wan2.2-I2V-A14B-GGUF/)
* [bullerwins/Wan2.2-T2V-A14B-GGUF](https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF)
* [QuantStack/Wan2.2 GGUFs](https://huggingface.co/collections/QuantStack/wan22-ggufs-6887ec891bdea453a35b95f3)

**自定义节点**
[City96/ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)

### WanVideoWrapper

* [Kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)

**Wan2.2 models**

* [Kijai/WanVideo\_comfy\_fp8\_scaled](https://hf-mirror.com/Kijai/WanVideo_comfy_fp8_scaled)

**Wan2.1 models**

* [Kijai/WanVideo\_comfy/Lightx2v](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v)

**Lightx2v 4steps LoRA**

* [Wan2.2-T2V-A14B-4steps-lora-rank64-V1](https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-rank64-V1)
