> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI GPT-Image-1 节点

> 了解如何在 ComfyUI 中使用 OpenAI GPT-Image-1 合作伙伴节点生成图像

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=243b4200a707b55f1c4fd88d4edf51a9" alt="OpenAI GPT-Image-1 节点截图" data-og-width="1576" width="1576" data-og-height="1123" height="1123" data-path="images/comfy_core/api_nodes/openai-gpt-image-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2d4ad0d8fdf6ac49815d5de1f21c0df7 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=868f4b2403c8ce07803227285cd6f2fc 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ab08d31d2151a589f569d13cc10692ce 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5993067ce1d818c9bcfd5147537ae256 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f2e101e964fad443efd7374c2f9ce37b 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-gpt-image-1.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=44cf580b967693bfdc2c49a6cc25aeb7 2500w" />

OpenAI GPT-Image-1 是 ComfyUI 合作伙伴节点系列中的一员，它允许用户通过 OpenAI 的 **GPT-Image-1** 模型生成图像。这是与 ChatGPT 4o 图像生成相同的模型。

这个节点支持:

* 文本到图像的生成
* 图像编辑功能（通过蒙版进行修复绘制）

## 节点概述

**OpenAI GPT-Image-1** 节点通过 OpenAI 的图像生成 API 同步生成图像。它接收文本提示并返回符合描述的图像。GPT-Image-1 是目前 OpenAI 最先进的图像生成模型，能够创建高度详细和逼真的图像。

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

## 参数说明

### 必填参数

| 参数名      | 类型 | 说明                |
| -------- | -- | ----------------- |
| `prompt` | 文本 | 描述您想要生成的图像内容的文本提示 |

### Widget 参数

| 参数名          | 类型 | 选项                                    | 默认值    | 说明               |
| ------------ | -- | ------------------------------------- | ------ | ---------------- |
| `seed`       | 整数 | 0-2147483647                          | 0      | 用于控制生成结果的随机种子    |
| `quality`    | 选项 | low, medium, high                     | low    | 图像质量设置，影响成本和生成时间 |
| `background` | 选项 | opaque, transparent                   | opaque | 返回的图像是否带有背景      |
| `size`       | 选项 | auto, 1024x1024, 1024x1536, 1536x1024 | auto   | 生成图像的尺寸          |
| `n`          | 整数 | 1-8                                   | 1      | 生成的图像数量          |

### 可选参数

| 参数名     | 类型 | 选项     | 默认值 | 说明                     |
| ------- | -- | ------ | --- | ---------------------- |
| `image` | 图像 | 任何图像输入 | 无   | 可选的参考图像，用于图像编辑         |
| `mask`  | 蒙版 | 蒙版输入   | 无   | 可选的蒙版，用于局部重绘（白色区域将被替换） |

## 使用示例

### 文生图像（Text to Image）示例

下面的图片包含了一个简单的文生图像工作流，请下载对应的图像，并拖入 ComfyUI 以加载对应的工作流
![ComfyUI openai-gpt-image-1工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/text2image.png)

对应的工作流非常简单：
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e7308997e027153d914a61418a9c0058" alt="ComfyUI openai-gpt-image-1 工作流示例" data-og-width="3580" width="3580" data-og-height="1956" height="1956" data-path="images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e21f0cd8c845d34ed3fd4016bce71fd5 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e06c844a22bd4bf1e2fca9ef2052f720 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=34f42055304ee347d962051da6a00102 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3ad0d9e30f20fe8c535d4238e331a5bc 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=24830df172d325f9593696d59c0aedcf 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/text2image.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a3b050cf1382fb378f45aac540259d0c 2500w" />

你只需要加载 `OpenAI GPT-Image-1` 节点，在 `prompt` 节点中输入你想要生成的图像的描述，连接一个 `保存图像（Save Image）` 节点，然后运行工作流即可。

### 图生图（Image to Image）示例

下面的图片包含了一个简单的图生图工作流，请下载对应的图像，并拖入 ComfyUI 以加载对应的工作流
![ComfyUI openai-gpt-image-1工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/image2image.png)

我们将使用下面的图片作为输入：
![ComfyUI openai-gpt-image-1 工作流 input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/input.webp)

这个工作流中，我们使用 `OpenAI GPT-Image-1` 节点生成图像，并使用 `加载图像（Load Image）` 节点加载输入的图像，然后连接到 `OpenAI GPT-Image-1` 节点的 `image` 输入中。

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=05cab30de9ab5bc2e0865c0a367f82fc" alt="ComfyUI openai-gpt-image-1 工作流示例" data-og-width="3180" width="3180" data-og-height="1114" height="1114" data-path="images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=419c2f8470d671c9f9876ba8d2b64379 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=402654cfaf0701617b2e0d6c2b47414e 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1916ef7321e796d7e31b3d05462d64ce 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b5b6d1a301172a877855fb42c896e978 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=08ea4d43044625afecb002b0cedd6aaf 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/image2image.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c7a65d6109ebd439564cb1830c93db00 2500w" />

### 多张图片输入示例

请下载下面的图片并拖入 ComfyUI 来加载对应的工作流

![多张图片输入示例](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/multiple_image_input.png)

使用下面的帽子作为额外的输入图片
![帽子](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/hat.webp)

对应工作流如下图所示：
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=125236ed762b17ae1e711fa702663f74" alt="多张图片输入示例" data-og-width="1432" width="1432" data-og-height="748" height="748" data-path="images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a51e55f0d4de107f42cdc2f576d798f9 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7ffbaa360a6a18c11e1c37c4cb93de6a 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c95bf1edf0e7c09b269693788d856149 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c0fad9f36754684b3fa540c2f4e5575a 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cd3e53553401ddbdf57db68659c30be7 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/multi_images_input.png?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=07213db91090f513a00548170a21c346 2500w" />

使用了`Batch Images` 节点来将多张图像加载到 `OpenAI GPT-Image-1` 节点 中

### 局部重绘（Inpainting）工作流

GPT-Image-1 也支持图像编辑功能，允许您使用蒙版指定要替换的区域，下面是一个简单的局部重绘工作流示例：

下载下面的图片，并拖入 ComfyUI 以加载对应的工作流，我们将继续使用 图生图工作流部分的输入图片。

![ComfyUI openai-gpt-image-1工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/GPT-Image-1/inpaint.png)

对应工作流入图所示
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=12d74944bf8905025606740b820918a8" alt="ComfyUI openai-gpt-image-1 工作流示例" data-og-width="3154" width="3154" data-og-height="1156" height="1156" data-path="images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6fef6c79f60a91ae564e84f8361dd5a7 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1cf77f379b0f0326bdc4165f445c87b4 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d23e66dde56fcab9ea4cf500151848ec 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=fa900de7686e8c71a858c4e0e24c7687 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=60618c269a1433faf14fa72fb7da0a97 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/gpt-image-1/inpaint.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=937496ea2ab4f3b6bda82b20bd43db80 2500w" />

与图生图工作流相比，我们在`Load Image`中通过右键菜单使用 蒙版编辑器（MaskEditor） 并绘制蒙版，然后连接到 `OpenAI GPT-Image-1` 节点的 `mask` 输入中，来完成对应工作流。

**注意事项**

* 蒙版和图像必须大小相同
* 当输入大尺寸图片时，节点会自动将图像缩小到合适的尺寸

## 常见问题

<AccordionGroup>
  <Accordion title="为什么我找不到 API 节点？">
    请更新你的 ComfyUI 到最新版本（最新的 commit,或者最新的[桌面版](https://www.comfy.org/download)），由于我们后期可能会新增更多的 API 支持, 相应的节点也会进行更新, 所以请保持你的 ComfyUI 处于最新版本。

    <Tip>
      请注意需要区分 nightly 版本和 release 版本，有些情况下 `nightly` 版本(也就是最新的代码 commit 提交)才会包含最新的节点，因为 release 版本可能不会及时更新。

      由于我们仍在快速地迭代中，所以当你无法找到对应节点时请确保你使用的是最新的版本。
    </Tip>
  </Accordion>

  <Accordion title="为什么我无法使用 / 登录 API Nodes 节点？">
    API 访问需要你当前的请求是基于安全的网络环境，目前对 API 访问的网络环境要求如下:

    * 本地网络仅允许 `127.0.0.1` 或者 `localhost` 访问, 这可能意味着，你无法在局域网环境下使用带有`--listen` 参数启动的 ComfyUI 服务中中使用 API Nodes 节点
    * 能够正常访问我们的 API 服务（在某些地区可能需要使用代理服务）
    * 你的账号没有足够的[积分](/zh-CN/interface/credits)
  </Accordion>

  <Accordion title="为什么登录了还是无法使用或在使用时还会继续要求我登录？">
    * 目前仅支持 `127.0.0.1` 或者 `localhost` 访问,
    * 确保你的账户有足够余额
  </Accordion>

  <Accordion title="API Nodes 节点可以免费使用吗？">
    API Nodes 节点由于需要通过 API 调用闭源模型，所以需要使用积分，不支持免费使用
  </Accordion>

  <Accordion title="要如何购买积分？">
    请参考下面的文档：

    1. [Comfy账号](/zh-CN/interface/user): 在设置菜单中找到`用户`部分，进行登录
    2. [积分](/zh-CN/interface/credits): 登录后设置界面会出现积分菜单，您可以在`设置` → `积分`中购买积分，我们使用预付费，不会有意外的费用
    3. 通过 Stripe 完成付款
    4. 查看积分是否更新，如果没有试着重启或者刷新页面
  </Accordion>

  <Accordion title="未用完的积分支持退款吗？">
    目前我们不支持对积分进行退款。
    如果你觉得是因为技术问题出现了错误而存在未使用的余额，请[联系支持](mailto:support@comfy.org)
  </Accordion>

  <Accordion title="积分可以出现负数吗？">
    积分不应作为负余额或信用额度使用。但是，由于合作伙伴节点在执行前并不总是能报告成本，存在竞态条件，单次执行可能会消耗超过剩余余额的积分，导致完成后暂时出现负余额。当余额为负时，您将无法运行合作伙伴节点，直到充值恢复正余额。请在进行 API 调用前确保您有足够的积分。
  </Accordion>

  <Accordion title="我可以在哪里查看使用量和花费？">
    请在登录后访问[积分](/zh-CN/interface/credits) 菜单，查看相应的积分。
  </Accordion>

  <Accordion title="支持使用自己的 API Key 吗？">
    目前 API Nodes 节点仍在测试阶段，目前暂不支持，我们已经把这个功能纳入考虑中了。。
  </Accordion>

  <Accordion title="积分会过期吗？">
    不你的积分不会过期。
  </Accordion>

  <Accordion title="积分可以转让或者共享吗？">
    不，你的积分不能转让给其他用户，也只限制于当前登录账户使用，但是我们并不限制登录设备的数量
  </Accordion>

  <Accordion title="我可以在不同设备间使用同一个账户吗？">
    我们不限制登录的设备数量，你可以在你想要的任何地方使用你的账号？
  </Accordion>

  <Accordion title="我该如何请求删除我的账户或信息？">
    请发送请求邮件至 [support@comfy.org](mailto:support@comfy.org)，我们将删除您的信息。
  </Accordion>
</AccordionGroup>
