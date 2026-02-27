> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria FIBO Edit API 节点 ComfyUI 官方示例

> 了解如何在 ComfyUI 中使用 Bria FIBO Edit 合作伙伴节点进行精准图像编辑

FIBO Edit 是 Bria AI 的 JSON 原生图像编辑模型，现已通过合作伙伴节点在 ComfyUI 中提供。它允许您将图像与结构化 JSON 提示词结合，进行精确、有针对性的编辑——无需猜测提示词，不会对图像其他部分造成不必要的更改。

## 关于 FIBO Edit

**主要特性：**

* **精准编辑**：更改特定属性（光照、颜色、纹理、材质）而不破坏场景的其他部分
* **背景替换和对象修改**：对目标区域进行精确控制
* **可复现、可审计的编辑**：结构化 JSON 输入确保一致的结果
* **100% 授权数据**：完整的治理和法律清晰度，适用于商业用途
* **强大的提示词遵循能力**：经过 PRISM 风格评估验证

<Tip>
  To use the API nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [API Nodes Overview](/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the API nodes.
</Tip>

<Tip>
  <Tabs>
    <Tab title="Portable or self deployed users">
      Make sure your ComfyUI is updated.

      * [Download ComfyUI](https://www.comfy.org/download)
      * [Update Guide](/installation/update_comfyui)

      Workflows in this guide can be found in the [Workflow Templates](/interface/features/template).
      If you can't find them in the template, your ComfyUI may be outdated. (Desktop version's update will delay sometime)

      If nodes are missing when loading a workflow, possible reasons:

      1. You are not using the latest ComfyUI version (Nightly version)
      2. Some nodes failed to import at startup
    </Tab>

    <Tab title="Desktop or Cloud users">
      * The Desktop is base on ComfyUI stable release, it will auto-update when there is a new Desktop stable release available.
      * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

      So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.
    </Tab>
  </Tabs>
</Tip>

## FIBO Edit 工作流

<CardGroup cols={2}>
  <Card title="图像编辑工作流" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_image_edit.json">
    下载 Bria FIBO 图像编辑工作流。
  </Card>

  <Card title="图像扩展工作流" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_image_outpainting.json">
    下载 Bria FIBO 图像扩展工作流。
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="在云端运行图像编辑" icon="cloud" href="https://cloud.comfy.org/?template=api_bria_image_edit&utm_source=docs">
    在 Comfy Cloud 上即时体验图像编辑工作流。
  </Card>

  <Card title="在云端运行图像扩展" icon="cloud" href="https://cloud.comfy.org/?template=api_bria_image_outpainting&utm_source=docs">
    在 Comfy Cloud 上即时体验图像扩展工作流。
  </Card>
</CardGroup>

## 示例输出

FIBO Edit 擅长各种编辑任务：

* **时间变换**：重新打光场景或更改一天中的时间
* **材质和纹理替换**：尝试不同的颜色、材质、面料和服装
* **对象材质替换**：替换特定对象上的材质
* **蒙版区域编辑**：遮罩特定区域进行精确编辑
* **文字调整**：调整图像中的文字
* **艺术风格转换**：以不同的艺术风格重新想象您的图像
