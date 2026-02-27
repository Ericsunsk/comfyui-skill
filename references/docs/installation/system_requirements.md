> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# System Requirements

> This guide introduces some system requirements for ComfyUI, including hardware and software requirements

In this guide, we will introduce the system requirements for installing ComfyUI. Due to frequent updates of ComfyUI, this document may not be updated in a timely manner. Please refer to the relevant instructions in [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

Regardless of which version of ComfyUI you use, it runs in a separate Python environment.

### System Requirements

Currently, we support the following operating systems:

* Windows
* Linux
* macOS (supports Apple Silicon, such as the M series)

You can refer to the following sections to learn about the installation methods for different systems and versions of ComfyUI. In the installation of different versions, we have simply described the system requirements.

<AccordionGroup>
  <Accordion title="ComfyUI Desktop">
    ComfyUI Desktop currently supports standalone installation for **Windows and MacOS (ARM)**, currently in Beta

    * Code is open source on [Github](https://github.com/Comfy-Org/desktop)

    <Tip>
      Because Desktop is always built based on the **stable release**, so the latest updates may take some time to experience for Desktop, if you want to always experience the latest version, please use the portable version or manual installation
    </Tip>

    You can choose the appropriate installation for your system and hardware below

    <Tabs>
      <Tab title="Windows">
        <Card title="ComfyUI Desktop (Windows) Installation Guide" icon="link" href="/installation/desktop/windows">
          Suitable for **Windows** version with **Nvidia** GPU
        </Card>
      </Tab>

      <Tab title="MacOS(Apple Silicon)">
        <Card title="ComfyUI Desktop (MacOS) Installation Guide" icon="link" href="/installation/desktop/macos">
          Suitable for MacOS with **Apple Silicon**
        </Card>
      </Tab>

      <Tab title="Linux">
        <Note>ComfyUI Desktop **currently has no Linux prebuilds**, please visit the [Manual Installation](/installation/manual_install) section to install ComfyUI</Note>
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="ComfyUI Portable (Windows)">
    Portable version is a ComfyUI version that integrates an independent embedded Python environment, using the portable version you can experience the latest features, currently only supports **Windows** system

    <Card title="ComfyUI Portable (Windows) Installation Guide" icon="link" href="/installation/comfyui_portable_windows">
      Supports **Windows** ComfyUI version running on **Nvidia GPUs** or **CPU-only**, always use the latest commits and completely portable.
    </Card>
  </Accordion>

  <Accordion title="Manual Installation">
    <Card title="ComfyUI Manual Installation Guide" icon="link" href="/installation/manual_install">
      Supports all system types and GPU types (Nvidia, AMD, Intel, Apple Silicon, Ascend NPU, Cambricon MLU)
    </Card>
  </Accordion>
</AccordionGroup>

### Python Version

* **Python 3.13** is very well supported and recommended
* Python 3.14 works but some custom nodes may have issues. The free threaded variant works but some dependencies will enable the GIL so it's not fully supported
* Python 3.12 is a good fallback if you have trouble with some custom node dependencies on 3.13

### Browser Requirements

For the best experience, use **Google Chrome version 143 or later**. Earlier versions of Chrome (142 and below) have known issues that can cause visual glitches and performance problems in ComfyUI.

### Supported Hardware

* **NVIDIA GPU** - Install stable pytorch with CUDA 13.0: `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130`
* **AMD GPU (Linux)** - ROCm 6.4 stable or ROCm 7.1 nightly
* **AMD GPU (Windows/Linux, RDNA 3/3.5/4 only)** - Experimental support for RX 7000 series (RDNA 3), Strix Halo/Ryzen AI Max+ 365 (RDNA 3.5), and RX 9000 series (RDNA 4)
* **Intel GPU** - Arc series with native PyTorch torch.xpu support
* **Apple Silicon** - M1/M2/M3/M4 series with Metal acceleration
* **Ascend NPU** - Via torch\_npu extension
* **Cambricon MLU** - Via torch\_mlu extension
* **Iluvatar Corex** - Via Iluvatar Extension for PyTorch
* **CPU** - Use the `--cpu` parameter (slower)

Please refer to the [ComfyUI Windows and Linux manual installation section](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#manual-install-windows-linux) for detailed installation steps.

<Note>
  PyTorch 2.4 and above is supported, but some features and optimizations might only work on newer versions. We generally recommend using the latest major version of PyTorch with the latest CUDA version unless it is less than 2 weeks old.

  The Windows portable build currently comes with Python 3.13 and PyTorch CUDA 13.0. Update your Nvidia drivers if it doesn't start.
</Note>

### Dependencies

* Install PyTorch (version specific to your hardware)
* Install all dependencies in the requirements.txt of ComfyUI: `pip install -r requirements.txt`

<Card title="Manual Installation" icon="book" href="/installation/manual_install">
  Please refer to the manual installation section for detailed installation steps.
</Card>
