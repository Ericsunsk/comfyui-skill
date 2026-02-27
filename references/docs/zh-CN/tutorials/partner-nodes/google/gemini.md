> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

#  Google Gemini 合作伙伴节点 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Google Gemini 合作伙伴节点来完成对话功能

Google Gemini 是 Google 推出的一款强大的 AI 模型，支持对话、文本生成等多种功能。目前 ComfyUI 已集成 Google Gemini API，你可以直接在 ComfyUI 中使用相关节点来完成对话功能。

本篇指南中，我们将引导你完成对应对话功能。

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

## Google Gemini Chat 工作流

### 1. 工作流文件下载

请下载下面的 Json 文件并拖入 ComfyUI 中加载对应工作流。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/google/api_google_gemini.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/google/tripo_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f5069d4edbc353783cf79fc1898df568" alt="OpenAI Chat Step Guide" data-og-width="3940" width="3940" data-og-height="2092" height="2092" data-path="images/tutorial/api_nodes/google/tripo_image_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/google/tripo_image_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=297f9266b6fe23c3e06053f4a605d9f5 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/google/tripo_image_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=65af09f4006c2aefb634da623430bdde 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/google/tripo_image_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0581bfd8f5e1fd73a08ee9d6cfe45381 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/google/tripo_image_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5e22076889c086e5c5568d7b87fc94da 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/google/tripo_image_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=df4f5e9bf6f0d1e312f0d0a77319be93 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/google/tripo_image_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8048fad10d4849720aac37264af222d2 2500w" />

<Note>
  在对应模板中我们构建了一个用于分析提示词生成的角色的提示词，用于将你的图像解读成对应的绘图提示词
</Note>

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在 `Load Image` 节点中加载你需要 AI 的解读图片
2. (可选) 如果需要你可以修改`Google Gemini` 中的提示词，从而让 AI 来执行特定任务
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行对话。
4. 等待 API 返回结果后，你可在 `Preview Any` 节点中查看对应 AI 返回的内容。

### 3. 补充说明

* 目前文件输入节点 `Gemini Input Files` 需要先将文件上传至`ComfyUI/input/` 目录下， 此节点正在改进，我们会在更新后修改模板
* 工作流中提供了使用 `Batch Images` 来输入的示例，如果你有多张图片需要 AI 解读，可参考步骤图在使用右键来将对应的节点模式设置为 `总是（always）` 来启用
