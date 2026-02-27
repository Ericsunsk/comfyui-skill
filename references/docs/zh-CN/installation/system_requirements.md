> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 系统要求

> 本文将介绍 ComfyUI 目前的一些系统要求，包括硬件及软件要求

在本篇我们将介绍安装 ComfyUI 的系统要求, 由于 ComfyUI 的更新频繁，本篇文档未必能够及时更新，请参考[ComfyUI](https://github.com/comfyanonymous/ComfyUI)中的相关说明。

无论是哪个版本的 ComfyUI，都是运行在一个独立的 Python 环境中。

### 操作系统要求

目前我们支持以下操作系统：

* Windows
* Linux
* macOS（支持 Apple 芯片，如 M 系列）

请参考[ComfyUI Windows 和 Linux 手动安装章节](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#manual-install-windows-linux)了解详细的安装步骤。

你可以参考下面的章节来了解不同系统和版本 ComfyUI 的安装方式，在不同版本的安装中我们简单对安装的系统要求进行了说明。

<AccordionGroup>
  <Accordion title="ComfyUI 桌面版">
    ComfyUI 桌面版目前支持 **Windows 及 MacOS(Apple Silicon)** 的独立安装，目前仍在 Beta 版本

    * 代码开源在 [Github](https://github.com/Comfy-Org/desktop)

    <Tip>
      由于 Desktop 总是基于稳定版本发布构建，所以我们最新的一些更新，对于 Desktop 来说可能需要等待一段时间才能体验到，如果你想要总是体验最新版本，请使用便携版或者手动安装
    </Tip>

    你可以从下面选择适合你的系统和硬件开始安装 ComfyUI

    <Tabs>
      <Tab title="Windows">
        <Card title="ComfyUI桌面版(Windows)安装指南" icon="link" href="/zh-CN/installation/desktop/windows">
          适合带有 **Nvdia** 显卡 **Windows** 版本的 ComfyUI 桌面版
        </Card>
      </Tab>

      <Tab title="MacOS(Apple Silicon)">
        <Card title="ComfyUI桌面版(MacOS)安装指南" icon="link" href="/zh-CN/installation/desktop/macos">
          适合带有 **Apple Silicon** 的 MacOS ComfyUI 桌面版
        </Card>
      </Tab>

      <Tab title="Linux">
        <Note>ComfyUI桌面版，**暂时没有 Linux 的预构建**，请访问[手动安装](/zh-CN/installation/manual_install)部分进行 ComfyUI 的安装</Note>
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="ComfyUI 便携版(Windows)">
    便携版是一个集成了独立的嵌入式 Python 环境的 ComfyUI 版本，使用便携版你可以体验到最新的功能，目前仅支持 **Windows** 系统

    <Card title="ComfyUI桌面版(Windows)安装指南" icon="link" href="/zh-CN/installation/comfyui_portable_windows">
      支持 **Navida 显卡** 和在 **CPU** 运行的 **Windows** ComfyUI 版本，始终使用最新 commit 的代码
    </Card>
  </Accordion>

  <Accordion title="手动安装 ComfyUI">
    <Card title="ComfyUI 手动安装教程" icon="link" href="/zh-CN/installation/manual_install">
      支持所有的系统类型和 GPU 类型（Nvidia、AMD、Intel、Apple Silicon、Ascend NPU、寒武纪 MLU）的用户都可以尝试使用手动安装 ComfyUI
    </Card>
  </Accordion>
</AccordionGroup>

### Python 版本

* **Python 3.13** 支持良好，推荐使用
* Python 3.14 可用，但部分自定义节点可能存在问题。自由线程版本可以运行，但某些依赖会启用 GIL，因此尚未完全支持
* 如果某些自定义节点在 3.13 上有依赖问题，Python 3.12 是一个不错的备选

### 浏览器要求

为获得最佳体验，请使用 **Google Chrome 143 或更高版本**。Chrome 142 及更早版本存在已知问题，可能导致 ComfyUI 出现视觉故障和性能问题。

### 支持的硬件

* **NVIDIA 显卡** - 安装稳定版 PyTorch（CUDA 13.0）：`pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130`
* **AMD 显卡（Linux）** - ROCm 6.4 稳定版或 ROCm 7.1 nightly 版
* **AMD 显卡（Windows/Linux，仅 RDNA 3/3.5/4）** - 实验性支持 RX 7000 系列（RDNA 3）、Strix Halo/Ryzen AI Max+ 365（RDNA 3.5）和 RX 9000 系列（RDNA 4）
* **Intel 显卡** - Arc 系列，原生支持 PyTorch torch.xpu
* **Apple Silicon** - M1/M2/M3/M4 系列，支持 Metal 加速
* **Ascend NPU** - 通过 torch\_npu 扩展
* **Cambricon MLU** - 通过 torch\_mlu 扩展
* **Iluvatar Corex** - 通过 Iluvatar Extension for PyTorch
* **CPU** - 使用 `--cpu` 参数（速度较慢）

请参考[ComfyUI Windows 和 Linux 手动安装章节](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#manual-install-windows-linux)了解详细的安装步骤。

<Note>
  支持 PyTorch 2.4 及以上版本，但某些功能和优化可能仅在较新版本上可用。我们通常建议使用最新主要版本的 PyTorch 和最新 CUDA 版本，除非发布时间不足两周。

  Windows 便携版目前附带 Python 3.13 和 PyTorch CUDA 13.0。如果无法启动，请更新您的 Nvidia 驱动程序。
</Note>

### 依赖

* 安装 PyTorch（根据您的硬件选择对应版本）
* 安装 ComfyUI 的 requirements.txt 中所有依赖：`pip install -r requirements.txt`

<Card title="Manual Installation" icon="book" href="/zh-CN/installation/manual_install">
  请参考手动安装章节了解详细的安装步骤。
</Card>
