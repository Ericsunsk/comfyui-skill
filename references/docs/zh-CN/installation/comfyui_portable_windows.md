> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 便携版(Windows)

> 本篇教程将指导你如何下载和开始使用 ComfyUI Portable(便携版) 并运行对应的程序

**ComfyUI Portable(便携版)** 是一个独立封装完整的 ComfyUI Windows 版本，内部已经整合了 ComfyUI 运行所需的独立的 **Python(python\_embeded)**,只需要解压即可使用,目前便携版本支持通过 **Nvidia** 显卡或者 **CPU** 运行。

本部分指南将引导你完成对应的安装。

## 下载 ComfyUI Portable(便携版)

您可通过点击下面的链接来获取最新的 **ComfyUI Portable(便携版)** 下载链接

<CardGroup cols={2}>
  <Card title="Nvidia 显卡标准版" icon="download" href="https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia.7z" />

  <Card title="AMD 显卡实验版" icon="microchip" href="https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_amd.7z" />
</CardGroup>

### 其他 Nvidia 显卡下载选项

<CardGroup cols={2}>
  <Card title="Portable with pytorch cuda 12.8 and python 3.12" icon="download" href="https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia_cu128.7z" />

  <Card title="Portable with pytorch cuda 12.6 and python 3.12" icon="download" href="https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia_cu126.7z">
    支持 Nvidia 10 系列及更早的显卡
  </Card>
</CardGroup>

### 其他下载选项

* [AMD 显卡实验版](https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_amd.7z)
* [PyTorch CUDA 12.8 + Python 3.12 版本](https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia_cu128.7z)
* [PyTorch CUDA 12.6 + Python 3.12 版本](https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia_cu126.7z)（支持 Nvidia 10 系列及更早的显卡）

下载后你可以使用类似解压软件如 [7-ZIP](https://7-zip.org/) 对压缩包进行解压

便携版解压后对应的文件结构及说明如下：

```
ComfyUI_windows_portable
├── 📂ComfyUI                   // ComfyUI 程序主体
├── 📂python_embeded            // 独立的 Python 环境
├── 📂update                    // 用于升级便携版安装包的批处理脚本
├── README_VERY_IMPORTANT.txt   // 英文版本的 ComfyUI 便携版使用说明
├── run_cpu.bat                 // 双击启动 ComfyUI（仅支持 CPU）
└── run_nvidia_gpu.bat          // 双击启动 ComfyUI（仅支持 Nvidia 显卡）
```

## 如何启动 ComfyUI

根据你的电脑情况双击 `run_nvidia_gpu.bat ` 或者 `run_cpu.bat` 来启动 ComfyUI，你会看到对应下图所示的命令的运行

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyui-portable-cmd.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=27ead27f4bf5f09cabffc238e5a5890a" alt="ComfyUI便携版运行命令提示符" data-og-width="1145" width="1145" data-og-height="648" height="648" data-path="images/comfyui-portable-cmd.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyui-portable-cmd.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2ee9a9bb89a49939af0aa62a3e5d9621 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyui-portable-cmd.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=69bfce9759f4de69fb6382e873a9ad16 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyui-portable-cmd.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=929494225b52b341b9f68b3042120963 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyui-portable-cmd.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e568e501c7bce40d696f07861b56f6f2 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyui-portable-cmd.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=fa7adcdf557b4c7d398f386cf8f6cf23 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyui-portable-cmd.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c44563098a54d52ee935b219284e9014 2500w" />

当你看到类似图片中的

```
To see the GUI go to: http://127.0.0.1:8188
```

此时你的 ComfyUI 服务已经启动，正常情况下 ComfyUI 会自动打开你的默认浏览器并访问 `http://127.0.0.1:8188` 地址，如果没有自动打开，请手动打开浏览器并访问该地址。

<Note>使用过程中请不要关闭对应的命令行窗口，否则 ComfyUI 将会停止运行</Note>

## 添加外部模型路径

如果你想要在 `ComfyUI/models` 之外管理你的模型文件，可能出于以下原因:

* 你有多个 ComfyUI 实例，你想要让这些实例共享模型文件，从而减少磁盘占用
* 你有多个不同的类型的 GUI 程序，如：WebUI, 你想要他们共用模型文件
* 模型文件无法被识别或读取到

我们提供了通过 `extra_model_paths.yaml` 配置文件来添加额外模型搜索路径的方法。

### 不同 ComfyUI 版本配置文件位置

<Tabs>
  <Tab title="Portable 及自部署">
    对于[便携版](/zh-CN/installation/comfyui_portable_windows)和[手动安装](/zh-CN/installation/manual_install)的 ComfyUI版本，你可以在 ComfyUI 的根目录下找到 `extra_model_paths.yaml.example` 的示例文件

    ```
    ComfyUI/extra_model_paths.yaml.example
    ```

    复制并重命名为 `extra_model_paths.yaml` 来使用, 并保持在 ComfyUI 的根目录下, 路径应该是 `ComfyUI/extra_model_paths.yaml`

    你也可以在 [这里](https://github.com/comfyanonymous/ComfyUI/blob/master/extra_model_paths.yaml.example) 找到配置示例文件
  </Tab>

  <Tab title="ComfyUI Desktop">
    如果你使用的是 ComfyUI 桌面应用程序，你可以参考下图打开额外模型的配置文件：

        <img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ec4e05559876366ea1e85dba00e98a4b" alt="Open Config File" data-og-width="1072" width="1072" data-og-height="1166" height="1166" data-path="images/zh/desktop/extra_model_paths.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=672b0f4991bd3c0f5e0c50226523f334 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5a1910a0040b6d56f89b56fc1c8c9c57 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=140c5f4a117bc5b8ddbf8c5de4c04b4f 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4980ad35aa2d388a5b4cbdd65cf846f5 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0d6280f2267d23062b6d04bbfba63f39 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a4c79b52db5bf34c616e39f8db0dce4c 2500w" />

    或者通过下面的位置打开：

    <Tabs>
      <Tab title="Windows">
        ```
        C:\Users\YourUsername\AppData\Roaming\ComfyUI\extra_models_config.yaml
        ```
      </Tab>

      <Tab title="macOS">
        ```
        ~/Library/Application Support/ComfyUI/extra_models_config.yaml
        ```
      </Tab>
    </Tabs>

    对应的配置文件不应该被改变
  </Tab>
</Tabs>

### 配置示例

比如，你需要额外让 ComfyUI 识别的模型文件位于下面的文件夹:

```
📁 YOUR_PATH/
  ├── 📁models/
  |   ├── 📁 loras/
  |   │   └── xxxxx.safetensors
  |   ├── 📁 checkpoints/
  |   │   └── xxxxx.safetensors
  |   ├── 📁 vae/
  |   │   └── xxxxx.safetensors
  |   └── 📁 controlnet/
  |       └── xxxxx.safetensors
```

那么你可以进行如下的配置来让 ComfyUI 识别到你设备上的模型路径

```
my_custom_config:
    base_path: YOUR_PATH
    loras: models/loras/
    checkpoints: models/checkpoints/
    vae: models/vae/
    controlnet: models/controlnet/
```

或者使用

```
my_custom_config:
    base_path: YOUR_PATH/models/
    loras: loras
    checkpoints: checkpoints
    vae: vae
    controlnet: controlnet
```

<Warning>
  对于桌面版，请在原有配置路径下新增配置，而不覆盖掉安装过程中自动生成的路径配置，请在修改前备份对应的文件，这样在你配置错误时可以及时恢复
</Warning>

或者你也可以参考默认的 [extra\_model\_paths.yaml.example](https://github.com/comfyanonymous/ComfyUI/blob/master/extra_model_paths.yaml.example) 来配置，保存之后， 需要 **重启 ComfyUI** 才能生效。

下面是完整的原始的配置配置示例:

```yaml  theme={null}
#Rename this to extra_model_paths.yaml and ComfyUI will load it


#config for a1111 ui
#all you have to do is change the base_path to where yours is installed
a111:
    base_path: path/to/stable-diffusion-webui/

    checkpoints: models/Stable-diffusion
    configs: models/Stable-diffusion
    vae: models/VAE
    loras: |
         models/Lora
         models/LyCORIS
    upscale_models: |
                  models/ESRGAN
                  models/RealESRGAN
                  models/SwinIR
    embeddings: embeddings
    hypernetworks: models/hypernetworks
    controlnet: models/ControlNet

#config for comfyui
#your base path should be either an existing comfy install or a central folder where you store all of your models, loras, etc.

#comfyui:
#     base_path: path/to/comfyui/
#     # You can use is_default to mark that these folders should be listed first, and used as the default dirs for eg downloads
#     #is_default: true
#     checkpoints: models/checkpoints/
#     clip: models/clip/
#     clip_vision: models/clip_vision/
#     configs: models/configs/
#     controlnet: models/controlnet/
#     diffusion_models: |
#                  models/diffusion_models
#                  models/unet
#     embeddings: models/embeddings/
#     loras: models/loras/
#     upscale_models: models/upscale_models/
#     vae: models/vae/

#other_ui:
#    base_path: path/to/ui
#    checkpoints: models/checkpoints
#    gligen: models/gligen
#    custom_nodes: path/custom_nodes

```

### 添加额外自定义节点路径

除了添加外部模型之外，你同样可以添加不在 ComfyUI 默认路径下的自定义节点路径

<Tip>
  请注意，这并不会改变自定义节点的默认安装路径，只是在启动 ComfyUI 时会增加额外的路径搜索，你仍旧需要在对应的环境中完成自定义节点的依赖的安装，来保证其运行环境的完整性。
</Tip>

下面是一个简单的配置示例（Mac 系统），请根据你的实际情况进行修改，并新增到对应的配置文件中，保存后需要 **重启 ComfyUI** 才能生效:

```yaml  theme={null}
my_custom_nodes:
  custom_nodes: /Users/your_username/Documents/extra_custom_nodes
```

## 进行第一次图片生成

安装成功后，你可以参考访问下面的章节，开始你的 ComfyUI 之路。

<Card title="进行第一次图片生成" icon="link" href="/zh-CN/get_started/first_generation">
  本教程将引导你完成第一次的模型安装以及对应的文本到图片的生成
</Card>

## 社区分发版本

在中国早期有社区作者 [@秋葉aaaki](https://space.bilibili.com/12566101) 制作过独立分发的版本-秋叶整合包，有被广泛使用。

如果你是在中国使用，这个版本更改了 Github 的源地址，并配置了 Pypi 地址为为中国国内镜像地址，这可以让你在开始上手 ComfyUI 时可以避免一些因为网络导致的依赖和更新问题。

<Card title="秋叶 ComfyUI 整合包" icon="link" href="https://www.bilibili.com/video/BV1Ew411776J">
  访问秋叶整合包原始发布地址
</Card>

<Tip>
  这个社区分发版本并不是由 ComfyUI 官方维护更新
</Tip>

## 其它 ComfyUI 便携版相关说明

### 1. ComfyUI 便携版升级

你可以使用 **update** 文件夹下的相关批处理命令完成 ComfyUI 便携版的升级

```
ComfyUI_windows_portable
└─ 📂update
   ├── update.py
   ├── update_comfyui.bat            // 更新 ComfyUI 到最新的 Commit 版本
   ├── update_comfyui_and_python_dependencies.bat  // 请仅在你的运行环境存在问题时使用
   └── update_comfyui_stable.bat       // 更新 ComfyUI 为最新的 stable 版本
```

### 2. ComfyUI 便携版设置局域网访问

如果你的 ComfyUI 运行在局域网内，想要其它的设备也可以访问到 ComfyUI，你可以通过记事本修改 `run_nvidia_gpu.bat` 或者 `run_cpu.bat` 文件来完成配置，主要通过添加`--listen`来添加监听地址
下面的示例是添加了 `--listen` 参数的 `run_nvidia_gpu.bat` 文件命令

```bat  theme={null}
.\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build
pause
```

当启用 ComfyUI 后您会发现最后的运行地址会变为

```
Starting server

To see the GUI go to: http://0.0.0.0:8188
To see the GUI go to: http://[::]:8188
```

你可以通过 `WIN + R` 输入`cmd` 打开命令行，输入 `ipconfig` 来查看你的局域网 IP 地址，然后在其它设备上输入 `http://你的局域网IP:8188` 来访问 ComfyUI
