> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何在不同系统上手动安装 ComfyUI

> 本部分将指导你完成在 Windows、MacOS 以及 Linux 的手动安装过程

对于 ComfyUI 的安装， 主要分为几个步骤

1. 创建一个虚拟环境(避免污染系统级 Python 环境)
2. 克隆 ComfyUI 代码仓库
3. 安装依赖
4. 启动 ComfyUI

你也可以参考 [ComfyUI CLI](/zh-CN/comfy-cli/getting-started) 来安装 ComfyUI, 它是一个命令行工具，可以方便地安装 ComfyUI 并管理其依赖。

## （可选）创建虚拟环境

<Tip>
  独立的虚拟环境是必要的，因为 ComfyUI 的依赖可能会与系统上的其他依赖冲突，也可以避免对系统级 Python 环境的污染。
</Tip>

[Install Miniconda](https://docs.anaconda.com/free/miniconda/index.html#latest-miniconda-installer-links). 这将帮助您安装 ComfyUI 所需的正确版本的 Python 和其他库。

使用 Conda 创建一个环境。

```
conda create -n comfyenv
conda activate comfyenv
```

## 克隆代码仓库

你需要保证你的系统上已经安装了 [Git](https://git-scm.com/downloads), 首先你需要打开终端（命令行）,然后克隆代码仓库。

<Tabs>
  <Tab title="Windows">
    <Warning>如果你还没有安装 Microsoft Visual C++ Redistributable，请在[这里安装](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)</Warning>
  </Tab>

  <Tab title="Linux">
    打开终端应用程序。
  </Tab>

  <Tab title="MacOS">
    打开[终端应用程序](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac)。
  </Tab>
</Tabs>

```bash  theme={null}
git clone git@github.com:comfyanonymous/ComfyUI.git
```

## 安装GPU 及 ComfyUI 依赖

<Steps>
  <Step title="安装 GPU 依赖">
    安装 GPU 依赖

    <Accordion title="Nvidia">
      ```
      conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
      ```

      或者，您可以安装 PyTorch 的夜间版本。

      <Accordion title="Install Nightly">
        <Warning>安装夜间版本（可能风险更大）</Warning>

        ```
        conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch-nightly -c nvidia
        ```
      </Accordion>
    </Accordion>

    <Accordion title="AMD">
      ```
      pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0
      ```

      或者，您可以安装 PyTorch 的夜间版本。

      <Accordion title="Install Nightly">
        <Warning>安装夜间版本（可能风险更大）</Warning>

        ```
        pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.0
        ```
      </Accordion>
    </Accordion>

    <Accordion title="Mac ARM Silicon">
      ```bash  theme={null}
      conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly
      ```
    </Accordion>
  </Step>

  <Step title="安装 ComfyUI 依赖">
    ```bash  theme={null}
    cd ComfyUI
    pip install -r requirements.txt
    ```
  </Step>

  <Step title="启动 ComfyUI">
    启动 ComfyUI

    ```
    cd ComfyUI
    python main.py
    ```
  </Step>
</Steps>

## 如何更新 ComfyUI

<Steps>
  <Step title="拉取最新代码">
    使用命令行进入 ComfyUI 的安装路径，然后拉取最新代码。

    ```bash  theme={null}
    cd <安装路径>/ComfyUI
    git pull
    ```
  </Step>

  <Step title="安装依赖">
    使用命令行进入 ComfyUI 的安装路径，然后安装依赖。

    <Warning>
      你需要确保当前的 Python 环境是 ComfyUI 的虚拟环境，否则依赖会安装到系统级 Python 环境，污染系统级 Python 环境。
    </Warning>

    ```bash  theme={null}
        pip install -r requirements.txt
    ```
  </Step>
</Steps>

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
