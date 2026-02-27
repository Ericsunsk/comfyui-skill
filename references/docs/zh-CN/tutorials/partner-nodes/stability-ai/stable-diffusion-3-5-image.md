> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Stability AI Stable Diffusion 3.5 合作伙伴节点 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Stability AI Stable Diffusion 3.5 合作伙伴节点的文生图和图生图功能

[Stability AI Stable Diffusion 3.5 Image](/zh-CN/built-in-nodes/partner-node/image/stability-ai/stability-ai-stable-diffusion-3-5-image) 节点允许你使用 Stability AI 的 Stable Diffusion 3.5 模型，通过文本提示词或参考图像创建高质量、细节丰富的图像内容。

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

## Stability AI Stable Diffusion 3.5 文生图工作流

### 1. 工作流文件下载

下面的图片的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![Stability AI Stable Diffusion 3.5 文生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/stable_diffusion_3-5-t2i.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d56ae409c1f885bb54a8ca91144e3924" alt="Stability AI Stable Diffusion 3.5 文生图步骤图" data-og-width="2906" width="2906" data-og-height="1541" height="1541" data-path="images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3fc95a0f3863b12372071e30f7db967 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6385f4d8d5f053a9b608fe4d49917f28 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=71ea0bc7452504f29f729cfc08b9f607 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=48221dfbf9e9eb8728573fe7cb1a147f 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5192b0e55ad55767337260df769cc989 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_t2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f3dd577e99c20a7a81e1ddf5bbaa62e6 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. (可选)修改 `Stability AI Stable Diffusion 3.5 Image` 节点中的 `prompt` 参数，输入你想要生成的图像描述。提示词越详细，生成的图像质量往往越好。
2. (可选)选择 `model` 参数来选择使用的SD 3.5模型版本。
3. (可选)选择 `style_preset` 参数来控制图像的视觉风格。不同的预设风格会产生不同风格特点的图像，如"cinematic"（电影感）、"anime"（动漫风格）等。选择"None"则不应用任何特定风格。
4. (可选)编辑 `String(Multiline)` 来修改负向提示词，用于指定不希望在生成图像中出现的元素。
5. 点击 `Run（运行）` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图像的生成。
6. 等待 API 返回结果后，你可在 `Save Image` 节点中查看生成的图像，对应的图像也会被保存至 `ComfyUI/output/` 目录下。

### 3. 补充说明

* **提示词(Prompt)**：提示词是生成过程中最重要的参数之一，详细、清晰的描述会带来更好的效果。可以包含场景、主体、颜色、光照、风格等元素。
* **CFG Scale**：控制生成器对提示词的遵循程度，值越高生成的图像越接近提示词描述，但太高可能会导致过度饱和或不自然的结果。
* **风格预设(Style Preset)**：提供多种预设风格，能够快速定义图像的整体风格。
* **负面提示词(Negative Prompt)**：用于指定不希望在生成图像中出现的元素
* **Seed 参数**：可以用于复现或微调生成结果，对于创作过程中的迭代很有帮助。
* 当前 `Load Image` 节点为 "绕过（Bypass）" 模式，如需启用可以参考步骤图在对应节点上右键然后将"模式（Mode）"设置为"总是（Always）" 来启用输入,即可转为图生图模式。
* `image_denoise` 在没有输入图像时，该参数不起作用。

## Stability AI Stable Diffusion 3.5 图生图工作流

### 1. 工作流文件下载

下面的图片的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![Stability AI Stable Diffusion 3.5 图生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/sd3-5-i2i/stable_diffusion_3_5-i2i.png)

下载下面的图片我们将用于输入图片
![Stability AI Stable Diffusion 3.5 图生图工作流输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/stability_ai/sd3-5-i2i/input.jpg)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3f31575a609f91bd083cc22a99cf3991" alt="Stability AI Stable Diffusion 3.5 图生图步骤图" data-og-width="2436" width="2436" data-og-height="1446" height="1446" data-path="images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9f2daefb02ba44d89b0719d823a2d95f 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5e6ace02b6a2b117837959e9f2fe94fa 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e928b22ef9e3ef164f237c2031e74375 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=80a9cf25056d6eeb67f923d785a2467a 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e7fa6441ad2093f0130824c03077d4ff 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2c00041d1f7f670570580d8134180e18 2500w" />

你可参考图片中的序号来完成图生图工作流运行：

1. 通过 `Load Image` 节点加载一张参考图像，该图像将作为生成的基础。
2. (可选)修改 `Stability AI Stable Diffusion 3.5 Image` 节点中的 `prompt` 参数，描述你希望在参考图像基础上改变或增强的元素。
3. (可选)选择 `style_preset` 参数来控制图像的视觉风格，不同的预设风格会产生不同风格特点的图像。
4. (可选｜重要)调整 `image_denoise` 参数（范围0.0-1.0）来控制对原始图像的修改程度：
   * 值越接近0.0，生成的图像越接近输入的参考图像（当 0.0 时，基本和原始图像一致）
   * 值越接近1.0，生成的图像越接近纯文本生成的效果（当 1.0 时，相当于没有提供参考图像）
5. (可选)编辑 `String(Multiline)` 来修改负向提示词，用于指定不希望在生成图像中出现的元素。
6. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图像的生成。
7. 等待 API 返回结果后，你可在 `Save Image` 节点中查看生成的图像，对应的图像也会被保存至 `ComfyUI/output/` 目录下。

### 3. 补充说明

下图展示了使用相同参数设置下，有无输入图像的对比效果：

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=13d41c3d9718abe4d40321b5d9a85b70" alt="Stability AI Stable Diffusion 3.5 有无图像输入对比" data-og-width="1400" width="1400" data-og-height="700" height="700" data-path="images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b87317f78e02060552894bfe586bcb2c 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=67e2f9597c292ec17a3a9cb80b83c3cc 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d2a40aa65ca5f640fcb5229d6a3c1035 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=425f0b61b27ea3885160969ed294a1e9 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=657ee7666879076cbcd47d8aba120d41 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_compare.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=07bcc8bf00ade469352cbb56067c819d 2500w" />

**图像去噪强度(Image Denoise)**：这个参数决定了生成过程中保留原始图像特征的程度，是图生图模式中最关键的调节参数,下图是不同的去噪强度下生成的图像效果：

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=db7a75bbb9c6151f093fb9881f88a522" alt="Stability AI Stable Diffusion 3.5 图生图去噪强度说明" data-og-width="2100" width="2100" data-og-height="1400" height="1400" data-path="images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a3a2d76f4fed07b3016b5a53f43e26b9 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=530d2d1c0bcb789ec9b05f7e20286adf 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=52bd9d150069a3f81a0885a81d2b3590 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=da006a1ef9d06fc15e72d1151cfa7430 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=08a6c0ea76307d1733345b5238e588dd 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/stability_ai/stable_diffusion_3_5_image_i2i_image_denoise.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=98434f7a1c0823f4217bc3fb5d1d4f04 2500w" />

* **参考图像选择**：选择具有清晰主体和良好构图的图像通常能获得更好的结果。
* **提示词技巧**：在图生图模式中，提示词应该更多地关注你希望改变或增强的部分，而不需要描述已经存在于图像中的所有元素。
* **模式切换**：当提供输入图像时，节点会自动从文本到图像模式切换到图像到图像模式，并且会忽略宽高比参数设置。

## 相关节点详解

你可查阅下面的文档了解对应节点的详细参数设置等

<Card title="Stability Stable Diffusion 3.5 Image 节点文档" icon="book" href="/zh-CN/built-in-nodes/partner-node/image/stability-ai/stability-ai-stable-diffusion-3-5-image">
  Stability Stable Diffusion 3.5 Image 合作伙伴节点说明文档
</Card>
