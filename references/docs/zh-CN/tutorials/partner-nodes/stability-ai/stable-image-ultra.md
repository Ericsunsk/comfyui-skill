> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Stability AI Stable Image Ultra 合作伙伴节点 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Stability AI Stable Image Ultra 合作伙伴节点的文生图和图生图功能

[Stability Stable Image Ultra](/zh-CN/built-in-nodes/partner-node/image/stability-ai/stability-ai-stable-image-ultra) 节点允许你使用 Stability AI 的 Stable Image Ultra 模型，通过文本提示词或参考图像创建高质量、细节丰富的图像内容。

本篇指南中，我们将引导你如何使用对应节点来进行文生图和图生图的工作流设置。

<Tip>
  使用 API 节点需要保证你已经正常登录，并在受许可的网络环境下使用，请参考[API 节点总览](/zh-CN/tutorials/partner-nodes/overview)部分文档来了解使用 API 节点的具体使用要求。
</Tip>

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

## Stability AI Stable Image Ultra 文生图工作流

### 1. 工作流文件下载

下面的图片的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![Stability AI Stable Image Ultra 文生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/stable_image_ultra_t2i.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bbbb22660e1757bfba34771d438e968d" alt="Stability AI  Stable Image Ultra 文生图步骤图" data-og-width="2366" width="2366" data-og-height="959" height="959" data-path="images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cf51af0c2f320a2f05286ebd71ef883c 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c087debb849a1e5f4af365113850d9b5 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a441c8deeef138d41a2a212a70e38084 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=912ac3ba2ee9ce14a54e5ac52141bcce 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=167f4386090ad7a7d80b0e8051557dbf 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b47f2835f4939457adb23d1429389271 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. (可选)修改 `Stability AI Stable Image Ultra` 节点中的 `prompt` 参数，输入你想要生成的图像描述。提示词越详细，生成的图像质量往往越好。你可以使用`(词:权重)`格式来控制特定词的权重，例如：`天空是清爽的(蓝色:0.3)和(绿色:0.8)`表示天空是蓝色和绿色的，但绿色更为突出。
2. (可选)选择 `style_preset` 参数来控制图像的视觉风格。不同的预设风格会产生不同风格特点的图像，如"cinematic"（电影感）、"anime"（动漫风格）等。选择"None"则不应用任何特定风格。
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图像的生成。
4. 等待 API 返回结果后，你可在 `Save Image` 节点中查看生成的图像，对应的图像也会被保存至 `ComfyUI/output/` 目录下。

### 3. 补充说明

* **提示词(Prompt)**：提示词是生成过程中最重要的参数之一，详细、清晰的描述会带来更好的效果。可以包含场景、主体、颜色、光照、风格等元素。
* **风格预设(Style Preset)**：提供多种预设风格，如电影感、动漫风、数字艺术等，能够快速定义图像的整体风格。
* **负面提示词(Negative Prompt)**：用于指定不希望在生成图像中出现的元素，可以帮助避免常见问题，如额外的肢体、扭曲的面部等。
* **Seed 参数**：可以用于复现或微调生成结果，对于创作过程中的迭代很有帮助。
* 当前 `Load Image` 节点为 “绕过（Bypass）” 模式，如需启用可以参考步骤图在对应节点上右键然后将“模式（Mode）”设置为“总是（Always）” 来启用输入,即可转为图生图模式

## Stability AI Stable Image Ultra 图生图工作流

### 1. 工作流文件下载

下面的图片的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![Stability Stable Image Ultra 图生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/i2i/stable_image_ultra_i2i.png)

下载下面的图片我们将用于输入图片
![Stability Stable Image Ultra 图生图工作流输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/i2i/input.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=90799d9abc85f845d786eac7f204f778" alt="Stability Stable Image Ultra 图生图步骤图" data-og-width="2366" width="2366" data-og-height="959" height="959" data-path="images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2c343c6ac266e26c96fc27cb4a48e1d6 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bf35f2db6f76912b4b443b81e5ffdde1 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=dbc6c0ae0b2f44e2ed9c0eeab2643693 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0d0b599d4dee680889ccab25c18a6e90 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=56f6fd121ece0e1e7aedb8758beedd98 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_image_ultra_i2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a1f259d1251093d0ae76fdad82d6a3c7 2500w" />

你可参考图片中的序号来完成图生图工作流运行：

1. 通过 `Load Image` 节点加载一张参考图像，该图像将作为生成的基础。
2. (可选)修改 `Stability Stable Image Ultra` 节点中的 `prompt` 参数，描述你希望在参考图像基础上改变或增强的元素。
3. (可选)调整 `image_denoise` 参数（范围0.0-1.0）来控制对原始图像的修改程度：
   * 值越接近0.0，生成的图像越接近输入的参考图像
   * 值越接近1.0，生成的图像越接近纯文本生成的效果
4. (可选)同样可以设置 `style_preset` 和其他参数来进一步控制生成效果。
5. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图像的生成。
6. 等待 API 返回结果后，你可在 `Save Image` 节点中查看生成的图像，对应的图像也会被保存至 `ComfyUI/output/` 目录下。

### 3. 补充说明

**图像去噪强度(Image Denoise)**：这个参数决定了生成过程中保留原始图像特征的程度，是图生图模式中最关键的调节参数,下图是不同的去噪强度下生成的图像效果

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8cb266b02864aff7664f56bb1d0e8890" alt="Stability Stable Image Ultra 图生图去噪强度说明" data-og-width="2100" width="2100" data-og-height="1400" height="1400" data-path="images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=38d6772021197d309aeea0b412187d16 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5dcd1d04635b534f9b9574904102857b 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a6bae9f044fe9ea86e11e92b6378e5fa 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8c75d228c89aa01a470e45e108bdce71 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d0864c9de07f0aedcb22b88f71392f95 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/i2i_image_denoise.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5c759a07cf3ed8d4212f151afbe676be 2500w" />

* **参考图像选择**：选择具有清晰主体和良好构图的图像通常能获得更好的结果。
* **提示词技巧**：在图生图模式中，提示词应该更多地关注你希望改变或增强的部分，而不需要描述已经存在于图像中的所有元素。

## 相关节点详解

你可查阅下面的文档了解对应节点的详细参数设置等

<Card title="Stability Stable Image Ultra 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/image/stability-ai/stability-ai-stable-image-ultra">
  Stability Stable Image Ultra 合作伙伴节点说明文档
</Card>
