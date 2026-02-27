> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

#  Runway 合作伙伴节点 视频生成 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Runway 节点进行视频生成的相关工作流

Runway 是一家专注于生成式 AI 的科技公司，提供强大的视频生成功能。目前 ComfyUI 已集成 Runway API，你可以直接在 ComfyUI 中使用相关节点进行视频生成。

目前 ComfyUI 中原生集成了 Runway 的以下视频生成模型：

* Runway Gen3a turbo
* Runway Gen4 turbo
* Runway First Last Frame to video

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

## Gen3a turbo 图生视频工作流

### 1. 工作流文件下载

下面的视频的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen3a_turbo_image_to_video/runway_image_to_video_gen3a_turbo.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen3a_turbo_image_to_video/runway_image_to_video_gen3a_turbo.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的图片作为输入图片

![ComfyUI Runway gen3a turbo image to video Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen3a_turbo_image_to_video/steampunk.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c173269c427a4c3fcc08f5b0ead4ffab" alt="ComfyUI Runway gen3a turbo image to video Step Guide" data-og-width="2202" width="2202" data-og-height="1188" height="1188" data-path="images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0a59187c4a18d53b4568d662092f12de 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=23df8ac507adbadca3e4e49883e7ce8b 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5c511ccab9bbfdde11116edfe184999b 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=770b47e6170450ce300b163f8ed77ccc 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=58f31be12e93ece370302cae526092a9 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3ced3310fde20979a1159def906fa388 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在 `Load Image` 节点中加载提供的输入图片
2. 在 `Runway Gen3a turbo` 节点中设置 `prompt` 描述视频内容，修改 `duration` 参数来设置视频时长, 修改 `ratio` 参数来设置视频宽高比
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频的生成。
4. 等待 API 返回结果后，你可在 `Save Video` 节点中查看生成的视频（右键菜单可以保存），对应的视频也会被保存至 `ComfyUI/output/` 目录下。

## Gen4 turbo 图生视频工作流

### 1. 工作流文件下载

下面的视频的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/runway_gen4_turo_image_to_video.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/runway_gen4_turo_image_to_video.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的图片作为输入图片

![ComfyUI Runway gen4 turbo image to video Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/godfather.jpg)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1c2df6f00cd1a0fc221a058621cd1449" alt="ComfyUI Runway gen4 turbo image to video Step Guide" data-og-width="2202" width="2202" data-og-height="1152" height="1152" data-path="images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=676ee2e7986565c3e482f153871858de 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=49184313bdcc3931cfdf6aec01fd7170 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=11dc5ed72c9e578e83484ff3a24ed8f3 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ada028966a71fed3c695a5fafc5ba08b 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9344d3b599961ce42bd43e7f5a9dd23f 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=81a52c64571c1a3c61410e63f9183a72 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在 `Load Image` 节点中加载提供的输入图片
2. 在 `Runway Gen4 turbo` 节点中设置 `prompt` 描述视频内容，修改 `duration` 参数来设置视频时长, 修改 `ratio` 参数来设置视频宽高比
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频的生成。
4. 等待 API 返回结果后，你可在 `Save Video` 节点中查看生成的视频（右键菜单可以保存），对应的视频也会被保存至 `ComfyUI/output/` 目录下。

## 首尾帧视频生成工作流

### 1. 工作流文件下载

下面的视频的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/first_last_frame_to_video/runway_first_last_frame.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/first_last_frame_to_video/runway_first_last_frame.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的图片作为输入图片

![ComfyUI Runway gen4 turbo image to video Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/first_last_frame_to_video/first.jpg)
![ComfyUI Runway gen4 turbo image to video Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/first_last_frame_to_video/last.jpg)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4cf592284e4ef7d48a1780e10483f03c" alt="ComfyUI Runway gen4 turbo image to video Step Guide" data-og-width="2082" width="2082" data-og-height="1154" height="1154" data-path="images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d39249726e6ff98915ca48dbd010c81e 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ad3e00b1647cfa32b12682f69ecc004d 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0570bf102ba92d8b823caf6cf604126f 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d969338e625f09c6e54a07eb5c6f1ce1 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bcd44d0a555ee1c9893d5ddb154f1266 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cb6a1b59c2f2904f1c7d7e0fdcde23d0 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在 `Load Image` 节点中加载起始帧
2. 在 `Load Image` 节点中加载结束帧
3. 在 `Runway First-Last-Frame to Video` 节点中设置 `prompt` 描述视频内容，修改 `duration` 参数来设置视频时长, 修改 `ratio` 参数来设置视频宽高比
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频的生成。
5. 等待 API 返回结果后，你可在 `Save Video` 节点中查看生成的视频（右键菜单可以保存），对应的视频也会被保存至 `ComfyUI/output/` 目录下。
