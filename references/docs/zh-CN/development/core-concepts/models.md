> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 模型

## 模型是必不可少的

模型是媒体生成工作流程的核心组件。通过组合和混合，它们能够实现多样化的创意效果。

***模型*** 一词有多种含义。在这里，它指的是一种数据文件，包含节点图执行任务所需的信息。具体来说，它是一种数据结构，用于表示某种功能。作为动词，建模意味着对某物进行表示或提供示例。

在ComfyUI中，模型数据文件的典型示例是AI ***扩散模型***。它是一组庞大的数据集，表示文本与图像之间的复杂关系，从而实现文字与图片的相互转换。其他用于图像生成的常见模型示例包括多模态视觉和语言模型，如CLIP，以及图像放大模型，如RealESRGAN。

## 模型文件

模型文件是生成媒体制作的必需品。没有模型文件，工作流程将无法进行。ComfyUI安装包中不包含模型文件，但它通常可以自动下载并安装缺失的模型文件。许多模型可以通过**ComfyUI管理器**窗口下载和安装。模型还可以在以下网站获取：[huggingface.co](https://huggingface.co)、[civitai.green](https://civitai.green)和[github.com](https://github.com)。

### 在ComfyUI中使用模型

1. 下载并将其放置在ComfyUI程序目录中
   1. 在**models**文件夹中，您会找到各种类型模型的子文件夹，例如**checkpoints**
   2. **ComfyUI管理器**帮助自动化搜索、下载和安装的过程
   3. 如果ComfyUI正在运行，请重启它
2. 在您的工作流程中，创建适合模型类型的节点，例如**Load Checkpoints**、**Load LoRA**、**Load VAE**
3. 在加载节点中，选择您希望使用的模型
4. 将加载节点连接到工作流程中的其他节点

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

### 文件大小

相对于图像文件，模型文件可能非常大。一个典型的未压缩图像可能需要几MB的磁盘存储。生成的AI模型可能大到数万倍，单个模型可达数十GB。它们占用大量磁盘空间，并且在网络上传输需要很长时间。

## 模型训练和优化

生成式AI模型是通过在非常大的数据集上训练机器学习程序创建的，例如图像和文本描述的配对。AI模型并不明确存储训练数据，而是存储数据中隐含的相关性。

像Stability AI和Black Forest Labs这样的组织和公司发布“基础”模型，这些模型携带大量通用信息。这些是通用的生成AI模型。通常，基础模型需要进&#x884C;***优化***，以获得高质量的生成输出。一个专门的社区致力于优化基础模型。新的优化模型产生更好的输出，提供新的或不同的功能，并/或使用更少的资源。优化后的模型通常可以在计算能力和/或内存较少的系统上运行。

## 辅助模型

模型功能可以通过辅助模型进行扩展。例如，艺术指导文本到图像的工作流程以实现特定结果，单靠扩散模型可能会很困难或不可能。额外的模型可以在工作流程图中优化扩散模型，以产生所需的结果。示例包括**LoRA**（低秩适应），一个针对特定主题训练的小模型；**ControlNet**，一个使用引导图像帮助控制构图的模型；以及**Inpainting**，一个允许某些扩散模型在现有图像中生成新内容的模型。

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=0f49a29f61c23ccd32ec5a15207b8f9c" alt="辅助模型" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/concepts/core-concepts_auxiliary-model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d34ac90d5809aaff3437a6be6760c350 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d85c146bbf893f23854b57450b9df3f0 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d9211a61fb606b80819d1be2a9e212e9 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d390c38768b75c58e713aaef7a79551e 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7f515f04cbddc512b6713faffa3291cb 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_auxiliary-model.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f5d56a0a9add6dff1d1dcf2cb106c7ed 2500w" />

## 卸载模型

ComfyUI目前不支持通过前端界面卸载模型。如果您想要移除或卸载模型，需要手动删除系统中`ComfyUI/models/`目录下对应的模型文件。

## 常见问题

<AccordionGroup>
  <Accordion title="ComfyUI 支持 GGUF 格式的模型吗?">
    ComfyUI 原生并不支持 GGUF 格式,所以用户需要使用一些社区自定义节点来获取支持,如 [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)。
  </Accordion>

  <Accordion title="为什么找不到我的模型?">
    如果您已经安装了模型但在 ComfyUI 中找不到,请尝试以下步骤:

    * 验证模型是否在正确的位置:
      * 对于 **ComfyUI Desktop 桌面版**: 前往**帮助**菜单 → **打开文件夹** → **打开模型文件夹**来检查模型安装路径
      * 确保您的模型文件放置在正确的子文件夹中(例如 `checkpoints`、`loras`、`vae`)
    * 安装模型后点击快捷键 `r` 来刷新节点定义,以便 ComfyUI 可以检测到
    * 重启 ComfyUI
    * 确保在模型加载节点对应的模型有被选中
  </Accordion>
</AccordionGroup>
