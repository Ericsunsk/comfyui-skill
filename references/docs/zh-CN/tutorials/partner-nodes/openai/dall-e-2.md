> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI DALL·E 2 节点

> 了解如何在 ComfyUI 中使用 OpenAI DALL·E 2 合作伙伴节点生成图像

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=42a0b800a337494eebec116cfea8d71a" alt="OpenAI DALL·E 2 节点截图" data-og-width="1576" width="1576" data-og-height="954" height="954" data-path="images/comfy_core/api_nodes/openai-dall-e-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6ecf05f49bca8201e70d91bf6c39e2c5 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5d03fc5dc0289a0219f278b0747bf2b4 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9d8742d23f44e4a6f2752bd0126f6fd0 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=41023d403a268fed8120a91446837843 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=41fd9ca39c2d652fcaed9889c2ed3b59 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-2.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8434b4a8a25e5b2d86286d44d31a778a 2500w" />

OpenAI DALL·E 2 是 ComfyUI 合作伙伴节点系列中的一员，它允许用户通过 OpenAI 的 **DALL·E 2** 模型生成图像。

这个节点支持:

* 文本到图像的生成
* 图像编辑功能（通过蒙版进行修复绘制）

## 节点概述

**OpenAI DALL·E 2** 节点通过 OpenAI 的图像生成 API 同步生成图像。它接收文本提示并返回符合描述的图像。

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

| 参数名      | 说明                |
| -------- | ----------------- |
| `prompt` | 文本提示，描述你想要生成的图像内容 |

### Widget 参数

| 参数名    | 说明                 | 选项/范围                             | 默认值         |
| ------ | ------------------ | --------------------------------- | ----------- |
| `seed` | 生成图像的种子值（目前在后端未实现） | 0 到 2^31-1                        | 0           |
| `size` | 输出图像的尺寸            | "256x256", "512x512", "1024x1024" | "1024x1024" |
| `n`    | 生成的图像数量            | 1 到 8                             | 1           |

### 可选参数

| 参数名     | 说明             | 选项/范围  | 默认值 |
| ------- | -------------- | ------ | --- |
| `image` | 可选的参考图像，用于图像编辑 | 任何图像输入 | 无   |
| `mask`  | 可选的蒙版，用于局部重绘   | 蒙版输入   | 无   |

## 使用方法

## 工作流示例

目前该合作伙伴节点支持两种工作流，分别是：

* 文生图像（Text to Image）
* 局部重绘（Inpainting）

<Note>
  不支持图生图（Image to Image）工作流
</Note>

### 文生图像（Text to Image）示例

下面的图片包含了一个简单的文生图像工作流，请下载对应的图像，并拖入 ComfyUI 以加载对应的工作流
![ComfyUI openai-dall-e-2工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-2/text2image.png)

对应的示例非常简单
<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cd0262919a3be35855c9891b6de8c9c0" alt="ComfyUI openai-dall-e-2 工作流示例" data-og-width="3086" width="3086" data-og-height="1423" height="1423" data-path="images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=766a95093f1ef90769a2e02718dd27a8 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=315f7cb9d4b49293c18476e725869615 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1f52369d732c2040e395861d57fca2ba 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=60d125ab1c8f9759cda7a14a81fbedd1 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=dd64dbeec33bba7c9329dcb56746cf41 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/text2image.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=135961dddf3f7b28a431a5a92899db51 2500w" />

你只需要在加载 `OpenAI DALL·E 2` 节点后，在 `prompt` 节点中输入你想要生成的图像的描述，并连接一个 `保存图像（Save Image）` 节点，然后运行工作流即可

### 局部重绘（Inpainting）工作流

DALL·E 2 支持图像编辑功能，允许您使用蒙版指定要替换的区域，下面是一个简单的局部重绘工作流示例：

#### 1. 工作流文件下载

下载下面的图片，并拖入 ComfyUI 以加载对应的工作流

![ComfyUI openai-dall-e-2工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-2/inpainting.png)

我们将使用下面的图片作为输入：
![ComfyUI openai-dall-e-2 工作流 input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-2/input.jpg)

#### 2. 工作流文件使用说明

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=29719686459aadec1d533f8fe26e0370" alt="ComfyUI openai-dall-e-2 工作流示例" data-og-width="3609" width="3609" data-og-height="1425" height="1425" data-path="images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bb303fab72131dd5d985117514275fea 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cb22d377322c4e1db0d9866ee9c46843 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1eb5f9818cfc708f620a4e8861b64b83 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=719e8e5bd24b645cbae7c36aee1ee03e 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f4a7e78a2c9be90d26800628267ab236 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-2/inpainting.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0aaad83a58eb9bd3beed8ee0afa5b959 2500w" />

由于此工作流较为简单，如果你想要自己手动实现对应的工作流，可以按照下面的步骤完成对应的工作流

1. 使用`加载图像（Load Image）`节点加载图像
2. 在加载图像节点中右键，选择 `遮罩编辑器（MaskEditor）`
3. 在遮罩编辑器中，使用画笔绘制你想要重绘的区域
4. 在**OpenAI DALL·E 2** 节点 `image` 输入中连接加载的图像
5. **OpenAI DALL·E 2** 节点 `mask` 输入中连接蒙版
6. 编辑 `prompt` 节点的提示词
7. 运行工作流

**注意事项**

* 如果您想使用图像编辑功能，必须同时提供图像和蒙版（缺一不可）
* 蒙版和图像必须大小相同
* 当输入大尺寸图片时，节点会自动将图像缩小到合适的尺寸
* API 返回的 URL 是短期有效的，请确保及时保存需要的结果
* 每次生成都会消耗积分，根据图像大小和数量收费

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
