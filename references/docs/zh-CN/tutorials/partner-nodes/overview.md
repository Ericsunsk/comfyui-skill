> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# API Nodes

> 在本篇中我们将介绍 ComfyUI 关于 API Nodes 的相关说明。

API Nodes 是 ComfyUI 新增的调用闭源模型的方式，通过 API 调用，这将为 ComfyUI 用户提供访问外部最先进 AI 模型的能力，而无需复杂的 API 密钥设置。

## 什么是 API Nodes？

API Nodes 是一组特殊的节点，它们能够连接到外部 API 服务，让您直接在 ComfyUI 工作流中使用闭源或第三方托管的 AI 模型。这些节点设计用于无缝集成外部模型的功能，同时保持 ComfyUI 核心的开源特性。

目前支持的模型包括：

* **Black Forest Labs**: Flux 1.1\[pro] Ultra, Flux .1\[pro], Flux .1 Kontext Pro, Flux .1 Kontext Max, Flux.1 Canny Control, Flux.1 Depth Control, Flux.1 Expand, Flux.1 Fill
* **Google**: Veo2, Veo 3.0, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini Image
* **Ideogram**: V3, V2, V1
* **Kling**: 2.0, 1.6, 1.5, v1, v2-1, v2-1-master, v2-maser & Various Effects
* **Luma**: Photon, Ray2, Ray1.6, Ray-flash-2, Photo-flash-1
* **MiniMax**: Text-to-Video, Image-to-Video, Hailuo-02, T2V-01, I2V-01
* **Moonvalley**: Image-to-Video, Text-to-Video, Video-to-Video
* **OpenAI**: o1, o1-pro, o3, o4-mini, gpt-4o, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-5, gpt-5-mini, gpt-5-nano, DALL·E 2, DALL·E 3, GPT-Image-1
* **PixVerse**: V4 & Effects
* **Pika**: 2.2
* **Recraft**: V3, V2 & Various Tools
* **Hunyuan 3D**: Text-to-3D, Image-to-3D, Multi-view-to-3D
* **Rodin**: 3D Generation
* **Runway**: Text-to-Image, First-Last-Frame to Video, Image to Video (Gen3a Turbo, Gen4 Turbo)
* **Stability AI**: Stable Image Ultra, Stable Diffusion 3.5 Large, Stable Diffusion 3.5 Medium, Image Upscale
* **Tripo**: v1-4, v2.0, v2.5
* **Vidu**: Image-to-Video, Reference Video, Start-End to Video, Text-to-Video

## 使用 API Nodes 的前提要求

要使用 API Nodes 节点，需要有以下节点要求

### 1. ComfyUI 版本要求

请更新你的 ComfyUI 到最新版本，由于我们后期可能会新增更多的 API 支持, 相应的节点也会进行更新, 所以请保持你的 ComfyUI 处于最新版本。

<Tip>
  请注意需要区分 nightly 版本和 release 版本，我们推荐使用 `nightly` 版本(也就是最新的代码 commit 提交)，因为 release 版本可能不会及时更新。
  也就是对应的开发版本和稳定版本，由于我们仍在快速地迭代中，此文档并不一定及时更新，所以请注意对应的版本差异。
</Tip>

### 2. 账号及账户余额要求

需要当前已经在 ComfyUI 中登录了 [Comfy账号](/zh-CN/interface/user)，并且账户[积分](/zh-CN/interface/credits)大于 0

在 `设置` -> `用户` 中进行登录：

<img src="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=156baae110c5223431a8692840481c27" alt="ComfyUI 用户界面" data-og-width="3358" width="3358" data-og-height="1828" height="1828" data-path="images/zh/interface/setting/user.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=280&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=599786bda9ebbaa358ec6e968249e733 280w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=560&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=931837dd5ad64512911fd24ea12400f8 560w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=840&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=ee58e29fb4c99d7cf6a99471589b364d 840w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=1100&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=c53f39f9677914ad476c33e574e83ace 1100w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=1650&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=fc990161f80fa5a5aca616209fda2f6d 1650w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=2500&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=0fbc5469bb6f9bf527ca70d9f32e2869 2500w" />

并在 `设置` -> `积分` 中购买积分：

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5c862444d78a8887b8f8fd500bf1b1fd" alt="ComfyUI 积分界面" data-og-width="3358" width="3358" data-og-height="1820" height="1820" data-path="images/zh/interface/setting/menu-credits.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0078ad8fca746d13e7e37b7af88bc21a 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=be7a88754951017d38429846baff9550 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=48a3c32781b4e56cc5b8d3e22bfe616e 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2e62b1f074c32757a1811ecacc0076b3 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4bf7e88f24f09823f4f38eba62bdc9d0 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=505c573620b6b2f0af75aaf0ea33d89f 2500w" />

请参考对应的账号及积分部分的文档来确保这一要求：

* [Comfy账号](/zh-CN/interface/user): 在设置菜单中找到`用户`部分，进行登录
* [积分](/zh-CN/interface/credits): 登录后设置界面会出现积分菜单，您可以在`设置` → `积分`中购买积分，我们使用预付费，不会有意外的费用

### 3. 网络环境要求

* 本地网络仅允许 `127.0.0.1` 或者 `localhost` 访问可以直接使用登录功能
* 如果是局域网或者非白名单网站访问请使用 API Key 登录，请参考[使用 API Key 进行登录](/zh-CN/interface/user#使用-api-key-进行登录)
* 能够正常访问我们的 API 服务（在某些地区可能需要使用代理服务）
* 要求在 `https` 环境下访问，保证请求的安全性

<Note>
  不安全的上下文访问会有巨大的风险可能会有以下后果：

  1. 身份认证被窃取，从而造成你的账号信息泄露
  2. 账号被恶意使用，造成经济损失

  就算是后期我们开放了这一限制，我们依然强烈建议你不要通过不安全的网络请求访问 API 服务，因为这一风险极大.
</Note>

### 4. 使用对应节点

**添加到工作流**：将 API 节点添加到您的工作流中，就像使用其他节点一样
**运行**：设置好参数后运行工作流

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=91c9219b9648e55c19a95359060eeb56" alt="API Nodes" data-og-width="784" width="784" data-og-height="773" height="773" data-path="images/tutorial/api_nodes/sidebar.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7179545b60c6a046bd0d309914a0000f 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f92ab198e88fa7e15fd03ec421214ac9 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b3384e5b0bd6a825865c30d169abcea0 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c41b83cf96aea58cef7d0191e35ec278 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f3f4d2d7183c91491b8ba7672906950f 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4485b5b141edfc6f27a421e9d91f6eeb 2500w" />

## 使用 API Key 在非白名单网站登录 ComfyUI 账户来使用 API Nodes

目前我们设置有白名单来限制可以登录ComfyUI 账户的网站，如果需要在一些非白名单网站登录 ComfyUI 账户，请参考账号管理相关的部分了解如何使用 API Key 来进行登录，在这种情况下不需要对应的网站在我们的白名单中。

<Card title="账户管理" icon="book" href="/zh-CN/interface/user#使用-api-key-进行登录">
  查看如何使用 ComfyUI API Key 登录
</Card>

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdb8d99a4bd52a6cc1de1b3453e8cfda" alt="Select Comfy API Key Login" data-og-width="3450" width="3450" data-og-height="1914" height="1914" data-path="images/interface/setting/user/user-login-api-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=84683bcf8e9b1f53885f54175cd83b87 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ae30f89ae6d9a7b97e41f69d3ae0e9f6 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=4dce9815e1729742abd819ce400429ad 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=148e2ee529690c7985999f64841f8fcd 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=dca8a17b4e613ba65ee0d1dca67f4b28 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=0d1ab01184bd504d62531abfb88abb57 2500w" />

## 使用 ComfyUI 账户 API Key 集成来调用付费模型 合作伙伴节点

目前我们支持通过 ComfyUI 账户 API Key 集成来访问我们的服务来调用付费模型 合作伙伴节点，请参考 API Key 集成章节了解如何使用 API Key 集成来调用付费模型 合作伙伴节点

<Note>
  **重要提示:** 此处讨论的 API 密钥是您的 **ComfyUI 账户 API Key**(用于在工作流中访问付费 合作伙伴节点)。这与开发者用于将自定义节点发布到注册表的 **注册表发布 API Key** **不同**。如果您想发布自定义节点,请参阅[发布节点](/zh-CN/registry/publishing)。
</Note>

<Card title="API Key 集成" icon="link" href="/zh-CN/development/comfyui-server/api-key-integration">
  请参考 API Key 集成章节了解如何使用 API Key 集成来调用付费模型 合作伙伴节点
</Card>

## API Nodes 的优势

API Nodes 为 ComfyUI 用户提供了几个重要优势：

* **访问闭源模型**：使用最先进的 AI 模型，无需自行部署
* **无缝集成**：合作伙伴节点与其他 ComfyUI 节点完全兼容，可以组合创建复杂工作流
* **简化的体验**：无需管理 API 密钥或处理复杂的 API 请求
* **可控的成本**：预付费系统确保您完全控制支出，没有意外费用

## 计费方式

<Card title="合作伙伴节点计费" icon="coin" href="/zh-CN/tutorials/partner-nodes/pricing">
  请参考定价页面了解对应的 API 定价
</Card>

<img src="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user/user-login-api-1.jpg?fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=5c9e09c007bb0a36d4c21970e4219460" alt="选择 Comfy API Key 登录" data-og-width="3354" width="3354" data-og-height="1850" height="1850" data-path="images/zh/interface/setting/user/user-login-api-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user/user-login-api-1.jpg?w=280&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=3ebcef96e903b67b82a6067c4a3b012e 280w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user/user-login-api-1.jpg?w=560&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=7c5183e36835936f701a4a9c3b90cdeb 560w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user/user-login-api-1.jpg?w=840&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=a6246e498dee4b5752d1dae86377c0fb 840w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user/user-login-api-1.jpg?w=1100&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=fbd4929cc290f6c805d2cb05f42a1b01 1100w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user/user-login-api-1.jpg?w=1650&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=f87e2240cc94fb6d4957dd0ad33f4e36 1650w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user/user-login-api-1.jpg?w=2500&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=9a9957003b49e67c66698c54e4e50f97 2500w" />

## 关于开源和选择加入

重要的是要注意，**API Nodes 是完全可选的**。ComfyUI 将始终保持完全开源，并对本地用户免费。合作伙伴节点设计为"选择加入"功能，为那些想要访问外部 SOTA（最先进）模型的用户提供便利。

## 如何完全禁用合作伙伴节点

您可以添加 `--disable-api-nodes` 启动参数来禁用 ComfyUI 中的所有合作伙伴节点。此参数还将阻止前端与互联网通信。

**手动安装用户：**

```bash  theme={null}
python main.py --disable-api-nodes
```

**便携版用户 (Windows)：**

更新您的 `run_xxx.bat` 文件：

```batch  theme={null}
.\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build --disable-api-nodes
pause
```

## 如何使用 API Nodes

API Nodes 的一个强大应用是将外部模型的输出与本地节点结合。例如：

* 使用 [GPT-Image-1](/zh-CN/tutorials/partner-nodes/openai/gpt-image-1) 生成基础图像，然后通过本地 `WanImageToVideo` 节点转换为视频
* 结合外部生成的图像与本地的上采样或风格转换节点
* 创建混合工作流，充分利用闭源和开源模型的优势

这种灵活性使 ComfyUI 成为真正的通用生成式 AI 入口，将各种不同的 AI 功能整合到一个统一的工作流中，带来了更多可能性

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
