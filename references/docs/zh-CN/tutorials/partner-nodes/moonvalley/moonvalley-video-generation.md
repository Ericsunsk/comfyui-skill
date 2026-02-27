> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Moonvalley 合作伙伴节点 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Moonvalley 合作伙伴节点的文生视频、图生视频、视频转绘等能力

<iframe className="w-full aspect-video rounded-xl" src="//player.bilibili.com/player.html?isOutside=true&aid=114817830488742&bvid=BV1ZQGHzgETo&cid=30922050121&p=1&autoplay=0" title="ComfyUI Selection Toolbox New Features" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Moonvalley Marey Realism v1.5 是专为影视级创作打造的 AI 视频生成模型，该模型 **完全使用商业授权内容训练**，确保 **版权无忧，商用安全**。

## 产品亮点

* 极强的提示词理解力: 精准还原复杂提示词指令;
* 原生 1080p 高清画质: 训练数据集基于 **1080P** 视频训练，输出画面细腻。
* 真实物理与动态表现: 对物理运动模型、自然动态进行精准模拟，带来专业级别的真实感。
* 复杂场景分层与高级光影效果: 支持复杂场景的前中后景分层，智能理解空间关系
* 动作迁移和姿态迁移等生产级控制功能: 自动生成复合场景的真实光照。

目前 Moonvalley 相关 合作伙伴节点，已在 ComfyUI 中原生支持，你可以在 ComfyUI 中使用 对应的 文生视频、图生视频、视频转绘等能力。

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

## Moonvalley 文生视频工作流

### 1. 工作流文件下载

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_text_to_video.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_text_to_video.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=75dc005efbab705ab95cea22b36f7a24" alt="文本生视频作流" data-og-width="3160" width="3160" data-og-height="2434" height="2434" data-path="images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=28c9273328f87a89dbd8471160792362 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3b69032638a7e8c21f48648587263ba 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=44a6909ce38a300f0fb289592229a7c1 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b1ace57a8eff4446f831b6348c37abd5 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=27e34daf102a1d0866aa937a2c6dd780 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=415c88b1d9a8b5bfbbefefa19e50bc2a 2500w" />

1. 输入正向提示词（想要出现在画面中的内容）
2. 输入负向提示词（不想要出现在画面中的内容）
3. 修改视频输出分辨率
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频的生成
5. 等待 API 返回结果后，你可在 `Save Video` 节点中查看生成的视频，对应的视频也会被保存至 `ComfyUI/output/` 目录下

## Moonvalley 图生视频工作流

### 1. 工作流文件下载

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的图片作为输入图片

![输入图片](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video_input.webp)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9467e0f19d709f9b77cc4778a97f04a8" alt="图生视频工作流" data-og-width="3966" width="3966" data-og-height="1350" height="1350" data-path="images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=15f722730ad8914c66953fd80343c68b 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=09c1e830f9a49d385496d720fa9cc2f8 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=75d4f6b4f7f6774e696c8c66b5b5fdaf 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f2835d3b2719b0738ef0fb005be0d919 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=467702de371d0a5f4f2069313bef68b2 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3e79e56ce7f9516a5ab105dfb47aa4c9 2500w" />

1. 在 `Load Image` 节点中加载输入图像
2. 输入正向提示词（想要出现在画面中的内容）
3. 输入负向提示词（不想要出现在画面中的内容）
4. 修改视频输出分辨率
5. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频的生成
6. 等待 API 返回结果后，你可在 `Save Video` 节点中查看生成的视频，对应的视频也会被保存至 `ComfyUI/output/` 目录下

## Moonvalley 视频转视频工作流

`Moonvalley Marey Video to Video` 节点将允许你输入一段参考视频来进行视频的重绘，你可以参考视频画面动态或者角色姿态动作来进行视频的绘制生成。

### 1. 工作流文件下载

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_video_to_video.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_video_to_video.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的视频作为输入视频：

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_video_to_video_input.mp4" />

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ee9e202bdc9a3b39c8dc6ba5b10577b5" alt="视频转绘工作流" data-og-width="3966" width="3966" data-og-height="1350" height="1350" data-path="images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cf6664f2196ff60462c2d1d28003eea5 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=77a0cd776ba0564f497915231d13f1cb 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0d6f58d692e5dcfc16703a678c3621dd 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=91f3ea51b33634ed0c54c1b1501bf7f0 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=99f1bfd447b88531d16c38c55b9aadeb 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=82f6b3a3c04808d4f5d5997b3dc53bc6 2500w" />

1. 在 `Load Video` 节点中加载参考视频，或者你自己的素材
   * 如最终视频时长为5s, 则输入视频要大于 5s
   * 如最终视频时长为 10s, 则输入视频要大于 10s
2. 输入正向提示词（想要出现在画面中的内容）
3. 输入负向提示词（不想要出现在画面中的内容）
4. 设置 `control_type` 参数，选择视频转绘的参考类型
   * `Motion Transfer` :  参考视频的画面动态进行生成
   * `Pose Transfer` :  参考视频中的角色姿态进行生成
5. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行视频的生成
6. 等待 API 返回结果后，你可在 `Save Video` 节点中查看生成的视频，对应的视频也会被保存至 `ComfyUI/output/` 目录下
