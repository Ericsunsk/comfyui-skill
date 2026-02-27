> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

#  Tripo 合作伙伴节点模型生成 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Tripo 节点的 API 来进行模型生成

Tripo AI 是一家专注于生成式 AI 3D 建模的公司，它提供用户友好的平台和 API 服务，能够快速地将文本提示或2D图像（单张或多张）转换成高质量的3D模型。
目前 ComfyUI 已原生集成了对应 Tripo API ,现在你可以在 ComfyUI 中便捷地使用相关节点来进行模型生成

目前 ComfyUI 的 合作伙伴节点中已经支持 Tripo 以下模型生成能力：

* 文生模型
* 图生模型
* 多视图模型生成
* 骨骼绑定
* 骨骼动画

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

## 文生模型工作流

### 1. 工作流文件下载

下载下面的文件，并拖入 ComfyUI 中加载对应工作流。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/api_tripo_text_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b25199fbdd5c00f3fd8a1b587586bbed" alt="ComfyUI Tripo Text to Model Step Guide" data-og-width="2318" width="2318" data-og-height="1564" height="1564" data-path="images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=808ef38a541ba42c3b620b3e55ff56f3 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ca327bac2f1d7a11cc6d8433607e85ed 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=432f2214d0abbb7709ec85850f76b9c9 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f34d08594b7a1720ae80afa4c91b3142 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a68421325e3a559a58e8a1a84395cf17 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1c434abf6d478d1f86f1385614cc29a8 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在  `Tripo: Text to Model` 节点的 `prompt` 中输入提示词
   * model： 可以选择不同的模型，目前仅 v1.4 模型支持 `Tripo: Refine Draft model` 的后续优化
   * style: 中可以设置不同的风格
   * texture\_quality: 可以设置不同的纹理质量
2. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行模型的生成，工作流完成后对应的模型会自动保存至 `ComfyUI/output/` 目录下
3. 在 `Preview 3D` 节点中点击展开菜单
4. 选择`Export` 可以直接将对应模型导出

## 图生模型工作流

### 1. 工作流文件下载

下载下面的文件，并拖入 ComfyUI 中加载对应工作流。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/image_to_model/api_tripo_image_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的图片作为输入图片

![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/image_to_model/panda.jpg)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=302a46095bbb73ea478f441fa489b763" alt="ComfyUI Tripo Text to Model Step Guide" data-og-width="2242" width="2242" data-og-height="2610" height="2610" data-path="images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d8e92cb71153fceb6c2f0dbb4c1274f3 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0a94c80971b9c0af74607418869d99e5 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c52fda410d968df9b53b62282bd0af75 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f38d19355d3a8bdb3f1c7d9754f2e186 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e2d4f2d0e7592eddc65143626053ebe4 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=88b1cbf8fce76b0e1810bf6ec9aa2a6c 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在 `Load Image` 节点中加载提供的输入图片
2. 在  `Tripo: Image to Model` 节点中修改对应的参数设置
   * model： 可以选择不同的模型，目前仅 v1.4 模型支持 `Tripo: Refine Draft model` 的后续优化
   * style: 中可以设置不同的风格
   * texture\_quality: 可以设置不同的纹理质量
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行模型的生成，工作流完成后对应的模型会自动保存至 `ComfyUI/output/` 目录下
4. 模型下载请参考文生图部分的说明

## 多视图模型生成工作流

### 1. 工作流文件下载

下载下面的文件，并拖入 ComfyUI 中加载对应工作流。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/api_tripo_multiview_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的图片作为输入图片

![前视图](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/front.jpg)
![背视图](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/back.jpg)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5c4abf93f36e2ea96202c7cdb92d9917" alt="ComfyUI Tripo Text to Model Step Guide" data-og-width="4474" width="4474" data-og-height="2210" height="2210" data-path="images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1652f6fdc87287b6740f8ba562ffe58d 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=dc97a91541029fac8049a1b9d8b54d8b 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f2ff33370148a64dcf2aa4866a3f5e19 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e377ddfcb814d22fb8f6254725a9d806 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c8ac321431fb9f399eed6cad35629cd9 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=701f03c24907864e48309ac5fa5eed11 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在 `Load Image` 节点中分别加载提供的输入图片
2. 在  `Tripo: Image to Model` 节点中修改对应的参数设置
   * model： 可以选择不同的模型，目前仅 v1.4 模型支持 `Tripo: Refine Draft model` 的后续优化
   * style: 中可以设置不同的风格
   * texture\_quality: 可以设置不同的纹理质量
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行模型的生成，工作流完成后对应的模型会自动保存至 `ComfyUI/output/` 目录下
4. 其它视图输入可以参考步骤图中的示意将对应节点的模式设置为 `总是（always）` 来启用
5. 模型下载请参考文生图部分的说明

## 对应任务的后续任务处理

Tripo 的对应节点提供了对于同一任务的后续处理，只需要在相关节点中输入对应的`model_task_id` 即可,我们在相关模板中也已提供了对应的节点，你也可以按需通过修改对应节点模式来启用

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ad7966d458e1d327c98d2b21eccdd7a4" alt="Tripo 任务处理" data-og-width="904" width="904" data-og-height="696" height="696" data-path="images/tutorial/api_nodes/tripo/other_nodes.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=de8dda0c9a610962374d6d45ef9ef81b 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=aa635a07bf3de940c377e07e9bb9b323 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=853f4de5683d2adaf09fc590ee0afda1 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b673f11e9724c3bb397d3a13b71fcc47 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=58e9b87b84f3d2edcdda3ce067e52aa1 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=57cc00957d0d65bf950a8ffcf014fc6a 2500w" />

<Error>
  其中 `Tripo: Refine Draft model` 节点只对 V1.4 模型支持，其它模型不支持
</Error>
