> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux Desktop Version

> This article introduces how to download, install and use ComfyUI Desktop for Linux

<Warning>Linux pre-built packages are not yet available. Please try [manual installation.](/installation/manual_install)</Warning>

When Linux desktop packages become available, you can configure external model paths:

## Adding External Model Paths

If you have models stored in other locations on your computer outside the ComfyUI installation directory, you can add them to ComfyUI by configuring the `extra_models_config.yaml` file.

For ComfyUI Desktop, this file is located at:

* On Windows: `C:\Users\<YOUR_USERNAME>\AppData\Roaming\ComfyUI\extra_models_config.yaml`
* On macOS: `~/Library/Application Support/ComfyUI/extra_models_config.yaml`
* On Linux: `~/.config/ComfyUI/extra_models_config.yaml`

For detailed instructions, see [Models documentation](/development/core-concepts/models#adding-external-model-paths)
