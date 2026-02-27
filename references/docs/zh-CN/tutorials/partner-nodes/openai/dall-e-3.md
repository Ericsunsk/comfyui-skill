> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI DALL·E 3 节点

> 了解如何在 ComfyUI 中使用 OpenAI DALL·E 3 合作伙伴节点生成图像

OpenAI DALL·E 3 是 ComfyUI 合作伙伴节点系列中的一员，它允许用户通过 OpenAI 的 **DALL·E 3** 模型生成图像。此节点支持文本到图像的生成功能。

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-3.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8a8a46d4c0db57ee3967cc8c2f80d638" alt="OpenAI DALL·E 2 节点截图" data-og-width="1576" width="1576" data-og-height="966" height="966" data-path="images/comfy_core/api_nodes/openai-dall-e-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-3.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=027370cede633de4e243cfe640143df6 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-3.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d36da818966d16faf6590c202ba8e158 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-3.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=bafb97521291b836b6872e687e906a9f 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-3.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7e92f584de4ef7d6094a7871d28c71c5 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-3.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1e7bf24044c7cafc947b3d7d532218b1 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/api_nodes/openai-dall-e-3.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=25cf4f53ca7a507474c38dc890136375 2500w" />

## 节点概述

DALL·E 3 是 OpenAI 的最新图像生成模型，能够根据文本提示创建详细且高质量的图像。通过 ComfyUI 中的这个节点，您可以直接访问 DALL·E 3 的生成能力，无需离开 ComfyUI 界面。

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

## 参数详解

### 必需参数

| 参数名    | 类型 | 描述                                   |
| ------ | -- | ------------------------------------ |
| prompt | 文本 | 用于生成图像的文本提示。支持多行输入，可以详细描述您想要生成的图像内容。 |

### widget 参数

| 参数名     | 类型 | 可选值                             | 默认值       | 描述                                                   |
| ------- | -- | ------------------------------- | --------- | ---------------------------------------------------- |
| seed    | 整数 | 0-2147483647                    | 0         | 用于控制生成结果的随机种子                                        |
| quality | 选项 | standard, hd                    | standard  | 图像质量设置。"hd"选项生成更高质量的图像，但可能需要更多计算资源                   |
| style   | 选项 | natural, vivid                  | natural   | 图像风格。"vivid"倾向于生成超真实和戏剧性的图像，"natural"则产生更自然、不那么夸张的图像 |
| size    | 选项 | 1024x1024, 1024x1792, 1792x1024 | 1024x1024 | 生成图像的尺寸。可以选择方形或不同方向的矩形图像                             |

## 使用示例

你可以下载下面的图片，并拖入 ComfyUI 以加载对应的工作流
![ComfyUI openai-dall-e-3工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-3/text2image.png)

由于对应工作流非常简单，你也可以直接在 ComfyUI 中添加 **OpenAI DALL·E 3** 节点，并输入您想要生成的图像描述，然后运行工作流即可

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=29cd1bbda083d98eb24196d554586c43" alt="ComfyUI openai-dall-e-3 工作流" data-og-width="2308" width="2308" data-og-height="1059" height="1059" data-path="images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=80240ed5377b1c5215e92795dd950b86 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=2b522272027cc91a93db758416496694 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66c4318cfa7a4b18b34a18122cd34116 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=398e16e036cc013d9774512302038da7 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8df52f2b31d8d1c39306f259007c5659 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai-dall-e-3/text2image.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=401dc6e74fc88045c42dbf90557fd82f 2500w" />

1. 在 ComfyUI 中添加 **OpenAI DALL·E 3** 节点
2. 在提示文本框中输入您想要生成的图像描述
3. 根据需要调整可选参数（质量、风格、尺寸等）
4. 运行工作流程生成图像

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
