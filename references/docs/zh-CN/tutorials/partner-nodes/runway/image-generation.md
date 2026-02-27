> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

#  Runway 合作伙伴节点 图像生成 ComfyUI 官方示例

> 本文将介绍如何在 ComfyUI 中使用 Runway 节点进行文生图和参考生图功能

Runway 是一家专注于生成式AI的科技公司，提供强大的图像生成功能。其模型支持风格迁移、图像扩展和细节控制等特性。目前 ComfyUI 已集成 Runway API，你可以直接在 ComfyUI 中使用相关节点进行图像生成。

本篇指南中，我们将引导你完成下面的工作流:

* 文生图
* 参考生图

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

## Runway Image 文生图 工作流

### 1. 工作流文件下载

下面的图片的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![ComfyUI Runway Image Text to Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/text_to_image.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66f4bf5de975a5f0302d930e352605ff" alt="ComfyUI Runway Image Text to Image Step Guide" data-og-width="2842" width="2842" data-og-height="1260" height="1260" data-path="images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=126eb9ab59ac3fa69464dcca17d562c9 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4a77fa7bbaf5dc855339285e728bc27a 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=73094b95981662d3901cd4510050449b 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a604909a3fa461af35535f68ead78758 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4951668dc502679fe8d2c0e229330b28 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1c41ecbce818d39424610c0a5ee21efa 2500w" />

你可参考图片中的序号来完成最基础的文生图工作流运行：

1. 在 `Runway Text to Image` 的 `prompt` 中输入提示词
2. (可选) 设置调整 `ratio` 来设置不同的输出比例
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图像的生成。
4. 等待 API 返回结果后，你可在 `Save Image` 节点中查看生成的图像（右键可以保存），对应的图像也会被保存至 `ComfyUI/output/` 目录下。

## Runway Image 参考生图 工作流

### 1. 工作流及输入图像下载

下面的图片的`metadata`中已经包含工作流信息，请下载并拖入 ComfyUI 中加载对应工作流。

![ComfyUI Runway Image Reference to Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/reference_to_image/runway_reference_to_image.png)

下载下面的图像用于输入

![ComfyUI Runway Image Reference to Image Input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/reference_to_image/input.png)

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f0ce702cc2a6a03d887072416d78c241" alt="ComfyUI Runway Image Reference to Image Step Guide" data-og-width="2842" width="2842" data-og-height="1260" height="1260" data-path="images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=696ef8ecc46427bd46c7830c11b24f49 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1956bc38e424e3e757f63ee07fa88957 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8d03e7a6eca51b29251bf9606b86e351 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=894ba54fbd13795bac0e847936fed65c 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=423127ac47ecb8310a3a451a35b4e522 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c97748843c91858030259f11b2ad526e 2500w" />

你可参考图片中的序号来完成最基础的参考生图工作流运行：

1. 在 `Load Image` 节点中加载提供的输入图像
2. 在 `Runway Text to Image` 的 `prompt` 中输入提示词及进行尺寸调整
3. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图像的生成。
4. 等待 API 返回结果后，你可在 `Save Image` 节点中查看生成的图像（右键可以保存），对应的图像也会被保存至 `ComfyUI/output/` 目录下。
