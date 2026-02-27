> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Comfy Cloud

> 开始使用 Comfy Cloud 在云端运行 ComfyUI 工作流，无需本地安装

<Card title="访问 Comfy Cloud" icon="cloud" href="https://comfy.org/cloud">
  点击此处直接访问 ComfyUI Cloud
</Card>

## 什么是 Comfy Cloud？

ComfyUI Cloud 是 ComfyUI 的云端版本，具有与本地版本相同的功能。一切都已预装并可立即使用。

### 主要特性

<CardGroup cols={2}>
  <Card title="零配置" icon="bolt">
    无需安装。所有模型和自定义节点都已预装并可立即使用
  </Card>

  <Card title="强大的 GPU" icon="microchip">
    在我们强大的服务器 GPU 上快速运行工作流，无需自己的硬件
  </Card>

  <Card title="始终保持最新" icon="arrows-rotate">
    自动保持最新的 ComfyUI 版本和功能
  </Card>

  <Card title="随处访问" icon="globe">
    从任何有互联网连接的设备使用 ComfyUI - 无需本地安装
  </Card>
</CardGroup>

## 云端版本 vs 本地版本

目前 ComfyUI 有官方的云端版本 [Comfy Cloud](https://comfy.org/cloud)，同时也有开源的本地部署版本。如果你有足够强劲的 GPU，那么在本地部署并使用 ComfyUI 是一个不错的选择；而 Comfy Cloud 则是一个开箱即用的在线应用，无需部署，只要打开对应的 URL 即可开始使用。

| 类别        | Comfy Cloud                                                | 自托管（本地 ComfyUI）                                         |
| --------- | ---------------------------------------------------------- | ------------------------------------------------------- |
| **成本**    | 月度订阅                                                       | 免费                                                      |
| **GPU**   | 强大的 Blackwell RTX 6000 Pro                                 | 使用你自己的 GPU                                              |
| **技术知识**  | 无需技术知识。                                                    | 虽然桌面版和便携版为你提供了简单的入门方式，但你需要解决自定义节点安装和本地安装问题。             |
| **自定义节点** | 使用预装的自定义节点，永远不用担心兼容性问题。                                    | 安装任何你想要的自定义节点，但你需要自己管理。                                 |
| **模型**    | 使用预装模型。支持从 Civitai 导入 LoRA 模型。支持从 Hugging Face 导入模型（即将推出）。 | 使用任何你想要的模型，但你需要先下载它们。                                   |
| **显著差异**  | 易于入门                                                       | 离线工作，无限可定制                                              |
| **开始使用**  | [运行 ComfyUI Cloud](https://comfy.org/cloud)                | [本地安装 ComfyUI](/zh-CN/installation/system_requirements) |

## 定价与订阅

<Card title="查看定价" icon="tag" href="https://www.comfy.org/zh-cn/cloud/pricing">
  查看 Comfy Cloud 的定价和订阅选项
</Card>

## 如何使用 ComfyUI Cloud

使用 ComfyUI Cloud 基本和你的本地 ComfyUI 使用方式相同，如果你是第一次使用 ComfyUI，这里有一些快速入门提示：

<Steps>
  <Step title="选择一个模板">
    点击左侧边栏的模板图标以浏览可用的工作流。
    <img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a32875bb4e6d1c92ea4f893831aff925" alt="打开工作流模板" data-og-width="2048" width="2048" data-og-height="1128" height="1128" data-path="images/cloud/open_template.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b75636f8fdf033185ad180f9b51b5ec2 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=acb56caaddbd17845f65266d0d3a8e17 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=d0c30a7b485b6d96dc64c32b6d70b7f2 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=9aea324f8357077c9f0b64919e9172e4 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=9c44447bb6c57690bf49b1a2f5d258ae 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f3cf92bb13bc5f400effe170ec118bbc 2500w" />
  </Step>

  <Step title="选择你要运行的工作流">
    点击你想要运行的模板
    <img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b16043c4ad9372834eb7fe49c1180eee" alt="选择工作流模板" data-og-width="2048" width="2048" data-og-height="1136" height="1136" data-path="images/cloud/template_library.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a398d81d88d88f5cd9ebae8919f925e0 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=ca97b03eeb15e84605e74d7716724be4 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=75accea5eb08cd6e8dd56d7c8df473f6 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=837933b6b1a09f75fbb28b2483173898 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=bb02cd10b5a2212349830369205e56c7 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=66050ae24580d3190d340aa3a38021bd 2500w" />
  </Step>

  <Step title="更新模板的输入">
    1. 在加载的工作流中，由于在云端版本中我们已经预置了所有的模型，所有模板都是加载后即可使用点击运行。
    2. 如果需要更新，你只需要提供图像输入或文本提示词部分，检查 `Load Image` 节点或 `CLIP Text Encode` 节点。
       <img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=56ca79d24c79e666146c927263c96e99" alt="检查输入" data-og-width="2048" width="2048" data-og-height="1128" height="1128" data-path="images/cloud/workflow_input_or_loader.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=127cf8e3644b55f1849aeac06f1b1400 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=458b4a5311110ba33ae6006f7dd8ac94 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=69e518f7eb1fd1370ce3059420e823b1 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=32d8e4f15f1e6e9c39692b09ad2e8c16 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=1c916d45a5280a5b682fef62adefc8dd 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=8550b03cc2fdf3f2bde1b922e31d248e 2500w" />
  </Step>

  <Step title="运行你的工作流">
    如果一切正确，点击 "Run" 图标或使用快捷键 "Ctrl + Enter" 运行工作流。
    <img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=546f1e0003941deba2006a36d8f9ed34" alt="运行工作流" data-og-width="2048" width="2048" data-og-height="1441" height="1441" data-path="images/cloud/workflow_run_workflow.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b10e443657cecde2e6ccd70e5ffd55fc 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=17fd7d78a06d27eed5ba9a7a2bc703e1 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=6e35df195b3167470f2cf9baa63ea9a5 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=5d9cee59ce80d28cddbe56b6dcfc999a 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=fde6f5f8ea2f5dc7d9d12ee8c1092855 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=511cfe76f48a42ab357d5fec2a327b54 2500w" />
  </Step>

  <Step title="查看输出">
    点击运行后，我们的服务会开始为你的工作流分配机器，你可以在队列面板中查看该工作流的执行状态。
    <img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=4ac366407cf13fa84e55ef7948cff36e" alt="查看队列" data-og-width="1812" width="1812" data-og-height="1246" height="1246" data-path="images/cloud/workflow_check_queue.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=8b15c9935fbbc177171cccf5f9b34153 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f263581788c40988b061499eff933dc3 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=1f4c89d2d7d2b329080ad9e7a63fec03 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=57df498441c1f8a8cd04981740e9429e 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=395585423ef0ad04a17c905f5747582f 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=67aba03e595f9badd10b3e3dfbd2d2f9 2500w" />
  </Step>

  <Step title="保存内容到本地">
    在工作流执行完成后，你可以将生成的内容保存到本地。根据不同的素材类型，保存方式如下：

    <Tabs>
      <Tab title="保存图片">
        在队列面板或者保存图像节点上使用右键点击生成的图片，选择"保存图片"即可将图片保存到本地。

                <img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a15e70a3649537fb8c6adc50689dfbe7" alt="保存图片素材" data-og-width="2444" width="2444" data-og-height="1176" height="1176" data-path="images/cloud/download_image_assets.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=3d38181af7c253a663272638ceb88fd3 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=55ebb3096557f7f6f7a15608d970f536 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=afc78f0861b8fbfadb2a38a6ed06152a 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a7a7674d618a5dad86d174024ad3d5b0 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=7ec781932bde423f3b6933b29c2c4b6e 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=da0cdccadf8614d70fa2c77dbedbd33d 2500w" />
      </Tab>

      <Tab title="保存视频">
        在队列面板或者保存视频节点上：

        1. 点击浏览器播放组件的三个点，点击打开菜单
        2. 选择"下载"即可将视频保存到本地。

                <img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=2c987025c1c25e954a3065775ef5223d" alt="保存视频素材" data-og-width="2404" width="2404" data-og-height="1306" height="1306" data-path="images/cloud/download_video_assets.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=33b5d524c89458932e4eb812fb79b45e 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f772e685ed03b0de2933c7efc40a4a39 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=54c85dee44a6dcaa1e97e2a027948c11 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=0740c5be44110eb871a002f774877369 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=6139c2dad232b504cb1a3a98dd24cd48 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=e0c7c0e5e330a2295c92991214d67b91 2500w" />
      </Tab>

      <Tab title="保存音频">
        在队列面板或者保存音频节点上：

        1. 点击浏览器播放组件的三个点，点击打开菜单
        2. 选择"下载"即可将音频保存到本地。\
           <img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=8d876d9c3b89b2ae9f1e84ba8b3e9887" alt="保存音频素材" data-og-width="2416" width="2416" data-og-height="1308" height="1308" data-path="images/cloud/download_audio_assets.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=813ddfd43e25c7636c586e220e60d342 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b32f5d499050c6551579a63c1f9924d8 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=bb56a92a4e287f40a707a6b3f8c75eb4 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=1fd00394970dcff4d7a2aa6e965a93a1 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=ca02dfe4f3af5aadff45be0405973564 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=1f884d11d52e14f721189989af4bc467 2500w" />
      </Tab>

      <Tab title="保存3D素材">
        在 3D 浏览器节点的菜单中选择 “Export” 选项，选择你想要保存的格式即可将3D文件保存到本地。

                <img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=5e121107826658a3e1725b8d9840d94b" alt="保存3D素材" data-og-width="4392" width="4392" data-og-height="2752" height="2752" data-path="images/cloud/download_3d_assets.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=e4c87feee21051d4628a277017a47447 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=6dd17940bde85a544e06f9ce26eacebe 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=c6fd15ca374ae15f02dac542da09d54d 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=29d653a4188a9d6f1c4e9164f21acb1c 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=cc994df8c991db973ff8d1f1a7fb3a00 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=75841e7056186b759422dbb281036c16 2500w" />
      </Tab>
    </Tabs>
  </Step>
</Steps>

## 反馈

如果你有任何想法、建议或遇到任何问题，只需点击"反馈"图标。这将直接将你的反馈发送到我们。

<img src="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f1306e3587e441fc9964ffc0f9e4cc73" alt="反馈" data-og-width="1844" width="1844" data-og-height="1340" height="1340" data-path="images/cloud/feedback.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?w=280&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=7f1e8d9591e347e7cd75af2ea6e0804c 280w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?w=560&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=19d86ae7c41ed6b8fdf1b1fb44834d9f 560w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?w=840&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=36aa74fc89209a6413af918b956d505c 840w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?w=1100&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=ece35a7b92f63b9074848cf1b01e6180 1100w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?w=1650&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=5d37a906c10197a952f114dda1e2b689 1650w, https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?w=2500&fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=740b8fd5f788a3522d33d57b047e9497 2500w" />

## 常见问题

<Card title="查看常见问题" icon="circle-question" href="https://comfy.org/cloud">
  查看有关 Comfy Cloud 的常见问题和解答，包括定价、功能、限制等详细信息
</Card>

## 下一步

<CardGroup cols={2}>
  <Card title="Cloud API" icon="code" href="/zh-CN/development/cloud/overview">
    通过 Cloud API 以编程方式运行工作流
  </Card>

  <Card title="教程" icon="book" href="/zh-CN/tutorials/basic/text-to-image">
    探索教程以学习 ComfyUI 工作流
  </Card>

  <Card title="支持" icon="life-ring" href="https://discord.com/invite/comfyorg">
    加入我们的 Discord 社区获取帮助
  </Card>
</CardGroup>
