> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# LTX-Video

> 快速生成可控视频

<Tip>
  将任意视频直接拖入 ComfyUI 即可开始使用
</Tip>

## 快速入门

[LTX-Video](https://huggingface.co/Lightricks/LTX-Video) 是 Lightricks 开发的高效视频生成模型。

使用该模型的关键是提供详细的长描述提示词。

请下载 [ltx-video-2b-v0.9.5.safetensors](https://huggingface.co/Lightricks/LTX-Video/resolve/main/ltx-video-2b-v0.9.5.safetensors?download=true) 文件并放入 `ComfyUI/models/checkpoints` 目录。

若尚未下载 [t5xxl\_fp16.safetensors](https://huggingface.co/Comfy-Org/mochi_preview_repackaged/resolve/main/split_files/text_encoders/t5xxl_fp16.safetensors?download=true) 文件，请将其放入 `ComfyUI/models/text_encoders` 目录。

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

## 多帧控制

通过系列图像控制视频生成。可下载输入图像：[起始帧](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/house1.png) 和 [结束帧](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/house2.png)。

<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/workflow.webp" alt="LTX-Video 多帧控制工作流" />

## 图生视频

通过首帧图像控制视频生成：[示例首帧](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/i2v/girl1.png)。

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=ltxv_image_to_video&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28A745', color: '#FFFFFF', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/i2v/workflow.webp" alt="LTX-Video 图生视频工作流" />

## 文生视频

<img src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/t2v.webp" alt="LTX-Video 文生视频工作流" />
