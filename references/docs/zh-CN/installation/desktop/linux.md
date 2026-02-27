> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux桌面版

> 本文将介绍 ComfyUI Desktop MacOS 版本的下载以及安装使用

<Warning>Linux预建包尚不可用。请尝试[手动安装](/zh-CN/installation/manual_install)。 </Warning>

当Linux预建包可用时，你可以配置外部模型路径：

## 添加外部模型路径

如果你在计算机上的 ComfyUI 安装目录之外的其他位置存储了模型，可以通过配置 `extra_model_paths.yaml` 文件将它们添加到 ComfyUI 中。

对于 ComfyUI 桌面版，对应文件路径为：

* Windows：`C:\Users\<你的用户名>\AppData\Roaming\ComfyUI\extra_model_paths.yaml`
* macOS：`~/Library/Application Support/ComfyUI/extra_model_paths.yaml`
* Linux：`~/.config/ComfyUI/extra_model_paths.yaml`

详细说明请参见[模型文档](/zh-CN/development/core-concepts/models#adding-external-model-paths)
