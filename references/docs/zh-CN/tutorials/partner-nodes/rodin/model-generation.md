> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

#  Rodin 合作伙伴节点模型生成 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Rodin 节点的 API 来进行模型生成

Hyper3D Rodin (hyper3d.ai) 是一个专注于通过人工智能快速生成高质量、可直接用于生产环境的3D模型和材质的平台。
目前 ComfyUI 已原生集成了对应 Rodin 模型生成 API ，现在你可以在 ComfyUI 中便捷地使用相关节点来进行模型生成

目前 ComfyUI 的 合作伙伴节点中已经支持 Rodin 以下模型生成能力：

* 单视角模型生成
* 多视角模型生成
* 多种不同精度的模型生成

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

## 单视角模型生成工作流

### 1. 工作流文件下载

下载下面的文件，并拖入 ComfyUI 中加载对应工作流。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/rodin_image_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的图片作为输入图片

![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/doll.jpg)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ed79f1fb8546ed41a3d157cece818ee9" alt="ComfyUI Rodin Image to Model Step Guide" data-og-width="3184" width="3184" data-og-height="1966" height="1966" data-path="images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bb2b6e3ac6ed70eacf7eeac89fd00f52 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=19a1db47eea31a4666f42bb6607cb513 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=75cbf45620b8886b60a396330a9bb382 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c33ffd2c8306ea9d2d9ba27191374af7 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bf0689795ccfaa241823dcf6ae4bd2e3 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=03f0404c646e21eaac437e9d2959c174 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在  `Load Image` 节点中加载提供的输入图片
2. (可选)在  `Rodin 3D Generate - Regular Generate` 调整对应参数
   * polygon\_count: 可以设置不同的面数, 越大模型越平滑越精细
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行模型的生成，工作流完成后对应的模型会自动保存至 `ComfyUI/output/Rodin` 目录下
4. 在 `Preview 3D` 节点中点击展开菜单
5. 选择`Export` 可以直接将对应模型导出

## 多视角模型生成工作流

对应的 `Rodin 3D Generate - Regular Generate` 最多允许5张图像输入

### 1. 工作流文件下载

你可以将单视角部分的工作流修改为多视角工作流，或者直接下载下面的工作流文件

下载下面的文件，并拖入 ComfyUI 中加载对应工作流。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/api_rodin_multiview_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的图片作为输入图片

![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/front.jpg)
![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/back.jpg)
![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/left.jpg)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6241527775e83bd480811631ef4d88ed" alt="ComfyUI Rodin Image to Model Step Guide" data-og-width="3062" width="3062" data-og-height="1862" height="1862" data-path="images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3bdf978dce46f6db8ab13a0437f8af6 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a867df65f89c9cfd6bb6ce6d84de998f 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4a64175900800ea8ed9c10834b1a659a 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=85a75906989c2303477a70a57bc2a749 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=24ca3f810e13d8e7eab70ceb2ec96dfd 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c82bea8ae4fbf55442bdc61abfd3dc8c 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在  `Load Image` 节点中加载提供的输入图片
2. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行模型的生成，工作流完成后对应的模型会自动保存至 `ComfyUI/output/Rodin` 目录下
3. 在 `Preview 3D` 节点中点击展开菜单
4. 选择`Export` 可以直接将对应模型导出

## 其它相关节点

目前在 ComfyUI 中， Rodin 提供了不同类型的模型生成节点，由于对应输入条件与本文介绍的工作流相同，你可以按需启用，另外在对应模板中，我们提供了对应的节点，你也可以按需修改对应节点模式来启用

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7caf60a6b994156e71476564c856fc15" alt="Rodin 其它相关节点" data-og-width="975" width="975" data-og-height="1170" height="1170" data-path="images/tutorial/api_nodes/rodin/other_nodes.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=37c61a8000c0d3bfd5db85417a4ef98a 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ed2d06928db9041c249ab44b780c0127 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d4faca003f5b868e16be6f45b03d8a8f 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=52067d9b1de876f176083b6b2c0cc8f5 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=86fffeaf114a2532b28a95a75d5f5df7 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=945fdf363130d1e3bad049c2062dd231 2500w" />
