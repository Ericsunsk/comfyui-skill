> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 开始 ComfyUI 的 AI 绘图之旅

> 本部分教程将会带你完成首次 ComfyUI 的图片生成，了解并熟悉 ComfyUI 中的一些界面基础操作，如工作流加载、模型安装、图片生成等

本篇的主要目的是带你初步了解 ComfyUI 熟悉 ComfyUI 的一些基础操作，并引导你首次的图片生成

1. 加载示例工作流
   * 从 ComfyUI 加载`Workflows template`中的`Text to Image`工作流
   * 使用带有`metadata` 的图片中加载工作流
2. 指导你完成模型
   * 自动安装模型
   * 手动安装模型
   * 使用 **ComfyUI Manager** 的模型管理功能安装模型
3. 进行一次文本到图片的生成

## 关于文生图的说明

**文生图（Text to Image）**，是 AI 绘图的基础，通过输入文本描述来生成对应的图片，是 AI 绘图最常用的功能之一，你可以理解成你把你的**绘图要求(正向提示词、负向提示词)**告诉一个**画家(绘图模型)**，画家会根据你的要求，画出你想要的内容，由于本篇教程主要是为了引导你开始 ComfyUI 的使用，对于文生图的详细说明，我们将在[文生图](/zh-CN/tutorials/basic/image-to-image)章节进行详细讲解

## ComfyUI 文生图工作流教程讲解

### 1. 启动 ComfyUI

请确定你已经按照[安装指南](/zh-CN/installation/system_requirements)完成了 ComfyUI 的启动，并可以成功打开 ComfyUI 的页面。或者，你也可以使用 [Comfy Cloud](/zh-CN/get_started/cloud) 在云端使用 ComfyUI，无需安装。

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8d74bbaaf16e92f0e41fbf446bce8655" alt="ComfyUI界面" data-og-width="1068" width="1068" data-og-height="819" height="819" data-path="images/interface/comfyui-boot-screen.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5cb9199e3321fff7ad0f3d05b98b5fb0 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d8079eb6460f02357a19daf916789cca 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8f430035873b1af54fbefe18ccb7f89f 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=901fc46444d049a7c309f3d3dde04168 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=74ef473885ed787270cdba6b753ec96b 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=eb273ff76ed49bc91d290de3db733468 2500w" />

如果你还未安装 ComfyUI 请根据你的设备情况选择一个合适的版本进行安装

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

### 2. 加载默认文生图工作流

正常情况下，打开 ComfyUI 后是会自动加载默认的文生图工作流的, 不过你仍旧可以尝试以下不同方式加载工作流来熟悉 ComfyUI 的一些基础操作

<Tabs>
  <Tab title="从 Workflow Template 加载">
    <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9d27e08e27b8eb3d201b83f9e310fcf1" alt="ComfyUI 界面" data-og-width="973" width="973" data-og-height="696" height="696" data-path="images/tutorial/gettingstarted/first-image-generation-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b8fcf7b9cf036e830c80d5c7d08277eb 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=024bfa97dcc43a5544614536571f6cfa 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=bbf0c3c26374de9f92be8dcf2c010623 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=135c10c9218d1e205c7d14a0648e20ab 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=04b75e491e8734279e7e595b8ad8557f 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8a40678cb2b4ceb856ddc3d2e867b372 2500w" />
    请对照图片中序号所对应的顺序进行操作

    1. 点击 ComfyUI 界面右下角的**Fit View**按钮，防止已加载工作流是在视图外导致不可见
    2. 点击侧边栏的**文件夹图标（workflows）**
    3. 点击 工作流（Workflows）面板顶部的**浏览工作流示例（Browse example workflows）** 按钮

    下图继续

        <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=95604069c95b98aaaecfac6141eadadc" alt="加载工作流" data-og-width="972" width="972" data-og-height="692" height="692" data-path="images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0eb0a67fc3fe9e9cb951fd92fa871e7e 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d6180ba2452c01eda59a52e8f1af7446 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=493e05c8c000d4d44b963afa6c6b968c 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fe206a76045f658b209d05463f414363 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=99d1dd62a0ef8e5296477f8cbecb47e6 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6f939111ff708e666db1c331f608c22f 2500w" />

    4. 选择默认的第一个工作流 **Image Generation** 以加载图标

    或者你也可以从`workflow`菜单中选择**Browse workflow templates** 浏览工作流模板
    <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=bbc70cd0f990a2674b9db9d6f080e026" alt="ComfyUI 菜单 - 浏览工作流模板" data-og-width="612" width="612" data-og-height="536" height="536" data-path="images/tutorial/gettingstarted/first-image-generation-1-menu.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=08dbdd225603ece1d7d92b70c4ca5bd6 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=94951273209435d7e744f8354364f51d 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=cae53710d2bcbb862a75bdd5218cfb44 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=692cf88d6cf8868d898c2d7450e90cf6 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8368d39fd5611a52749df6d66260c766 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ced69fca7e53b06aa1b36d1067aa75a0 2500w" />
  </Tab>

  <Tab title="从带有 metadata 的图片中加载">
    所有用 ComfyUI 生成的图片，都会带有 metadata 信息，这些信息会包含图片的 workflow 信息，你可以通过这些信息来加载对应的 workflow。

    现在，让我们尝试一下，请保存下面的工作流图片，然后直接拖入 ComfyUI 的界面中，或者使用菜单 **工作流（Workflows）** -> **打开（Open）** 打开这个图片以加载对应的 workflow

    ![ComfyUI-文生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/text-to-image-workflow.png)
  </Tab>

  <Tab title="从 workflow.json 文件中加载">
    ComfyUI 工作流还可以 json 格式存储，当我们完成一个工作流后，可以使用菜单 **工作流（Workflows）** -> **导出（Export）** 导出，这样对应的工作流就可以被保存为 json 文件中加载

    现在，让我们尝试一下，点击下面的按钮，前往 Github 下载对应的 text-to-image.json 文件

    <a className="prose" href="https://github.com/Comfy-Org/docs/blob/main/public/text-to-image.json" download style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
      <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>前往下载 text-to-image.json 文件</p>
    </a>

    下载完成后，请使用菜单 **工作流（Workflows）** -> **打开（Open）** 打开这个 json 文件以加载对应的 workflow
  </Tab>
</Tabs>

### 3. 安装绘图模型

通常在 ComfyUI 的初始安装中，并不会包含任何的绘图模型，但是模型是我们运行图片生成必不可少的部分。

在你完成第二步，工作流的加载后，如果你的电脑上没有安装[v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) 这个模型文件时，一般会出现下图的提示

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=631b68f7fd227245f032c1837b6e44e7" alt="模型缺失" data-og-width="972" width="972" data-og-height="696" height="696" data-path="images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=bf07d8fa6107520f408460032a331d0a 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=04d7ecb43ff2b94040742a31b9dc621b 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=103f5bf2c1bfaf50c9b4084d84a8e9a7 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=005a3b038883b9c372080cfa0bb770fc 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=11adbcce9945ab8aac33ad7b8c509417 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c0ec6fab2f0449810fef6a376da685e0 2500w" />

你可以直接选择点击 `Download` 按钮，让 ComfyUI 自动完成对应的模型的下载，但由于在有些地区不能够顺利访问对应模型的下载源，所以在这个步骤中，我将说明几种不同的模型安装方法。

无论使用哪种方法，模型都会被保存到 `<你的 ComfyUI 安装位置>/ComfyUI/models/` 文件夹下，你可以在你的电脑上尝试找到这个文件夹位置，你可以看到许多文件夹比如 `checkpoints`、`embeddings`、`vae`、`lora`、`upscale_model` 等，这些都是不同的模型保存的文件夹，通常以文件夹名称区分，ComfyUI 在启动时会检测这些文件夹下的模型文件，以及`extra_model_paths.yaml` 文件中配置的文件路径

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9715b090919f665331e3500712d5e9e7" alt="ComfyUI 模型文件夹" data-og-width="1564" width="1564" data-og-height="1228" height="1228" data-path="images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=657fd94230a1a7796906339c48b8c3b0 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7d884de0fc538ab8ef00c14da507b9a8 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=31938fcc781769c8fabc60ddef58363a 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b005cfc130ac988cf28f8ceb7315596b 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=dc0ae8e2a2f2ffaf7c63c57316b6fde1 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d0ee5cb2437d9ea25cab05dca82d81d0 2500w" />

被检测到的不同的文件夹里的模型将可以在 ComfyUI 的不同 **模型加载节点** 里使用，下面让我们开始了解不同模型的安装方式：

<Tabs>
  <Tab title="自动下载模型">
    在你点击 **Download** 按钮后，ComfyUI 将会执行下载,根据你使用的版本不同，将会执行不同的行为

    <Tabs>
      <Tab title="ComfyUI 桌面版">
        桌面版将自动完成模型的下载并保存到 `<你的 ComfyUI 安装位置>/ComfyUI/models/checkpoints` 目录下
        你可以等待安装完成或者在侧边栏的模型面板里查看安装进度

                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=850acf678de82f1358fd230347f41a86" alt="模型下载进度" data-og-width="974" width="974" data-og-height="697" height="697" data-path="images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=54a28a5d0739ccec1b41f6def3f88ddb 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5f210d81700174972dacef081a56659d 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c4b78e4ac1b98ebc33d5f3e6285f10bb 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2b3167deb99fcd5ba3b01dfb25b9ff69 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9718f43183df17023ccccb41a6fb8ffa 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6084de5bb78eb5956a497389383512f0 2500w" />

        如果一切顺利，模型应该可以自动下载到本地，如果长时间未下载成功，请尝试其它安装方法
      </Tab>

      <Tab title="ComfyUI 便携版">
        浏览器将会执行文件下载，请在下载完成后，将文件保存到的 `<你的 ComfyUI 安装位置>/ComfyUI_windows_portable/ComfyUI/models/checkpoints` 目录下
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="使用 ComfyUI Manager 安装模型">
    [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) 是由 [ltdrdata](https://github.com/ltdrdata) 开发的用于扩展和管理自定义节点、模型及插件的工具，目前 ComfyUI 的安装过程会自动完成 ComfyUI Manager 的安装，下面的步骤将会引导你使用 ComfyUI Manager 安装模型

    <Steps>
      <Step title="打开 ComfyUI Manager">
                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=63bea93b65f4aa69499343eaa8f8fa3d" alt="ComfyUI Manager 安装" data-og-width="492" width="492" data-og-height="124" height="124" data-path="images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3960c57be9777c85e7704ed7d838f389 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=cf45c060e2e6e2d9c7ac9de6071b3004 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0fbccad434fdbadf7951372cf2e674db 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2ca5b357da7a0163b274c3eadddd04d8 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fd74e46709d4bd2e573aa79ea66e0daf 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=4238a1c13094c4e16f7f976a1375d1bb 2500w" />

        如图，点击对应的 `Manager` 按钮，即可打开 ComfyUI Manager 的界面
      </Step>

      <Step title="打开模型管理界面（Model Manager）">
                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f263705f288d59e181c4fbd5d2ce8077" alt="ComfyUI Manager 模型管理" data-og-width="1200" width="1200" data-og-height="723" height="723" data-path="images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=1ba12adec58d6664a2222b80db97254b 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d6d2feadaf68a0fcca57333e1dc4cfe2 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a3eae65d43bf4d9e1dc1827f3611fafd 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3d54457cd8213afd45d728a38d665d57 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=443471cc0f938f916d96aa1213db34e9 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6e3e020446ebe6a348aec7239811d4e4 2500w" />

        如图，点击对应的 `Model Manager` 按钮，即可打开模型管理界面
      </Step>

      <Step title="搜索模型并安装模型">
                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3af1349a1b3a91b680030d3511a53695" alt="ComfyUI Manager 模型下载" data-og-width="1200" width="1200" data-og-height="723" height="723" data-path="images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7963c563d6ac8d95b2c043623dd21660 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fa757c67c6889c30975d0611159a9151 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d5f1855f2d8dd89899b781fe4116d3c0 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=397a777a3c91325e5c9ec95a5d268271 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=18ade34b5f43a854f7296f6a90ed4b65 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f209b1b10e09c634cd1d5ffe45ce7cfa 2500w" />

        1. 请在搜索框输入`v1-5-pruned-emaonly.ckpt`
        2. 在搜索结果里，点击对应的 `install` 按钮，即可下载模型

        不过由于目前各类模型的更新迭代速度较快，你不一定可以在这里找到所有的模型，另外在某些地区因为无法正常访问 ComfyUI Manager 的模型下载源，所以会存在下载不成功的情况，如果长时间无法下载成功，请尝试手动安装
      </Step>
    </Steps>
  </Tab>

  <Tab title="手动完成模型的安装">
    请访问模型地址：[前往下载 v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors)
    参考下面图片完成对应模型的下载

        <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=15c2560c44e7e4276b6a351809f7bf9f" alt="Hugging Face 模型下载" data-og-width="769" width="769" data-og-height="727" height="727" data-path="images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8a0a11ce09344e6137d0318c4b3b9719 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8089b1a5012ff008f26ebec351eab046 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c7d903b4cfd6ac8e1104f577d865f8b1 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e712597b7d24bbb7564c0b50e7a073de 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a96dc866b2123b98a2addbe33920543b 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=31971d485c7495f4f71baf350f1b83cc 2500w" />

    下载完成后，请将对应的**v1-5-pruned-emaonly-fp16.safetensors** 文件保存到以下位置

    <Tabs>
      <Tab title="ComfyUI 桌面版">
        请找到你在安装过程中设置的 ComfyUI 安装位置，将对应模型文件保存到以下文件夹位置 `<你的 ComfyUI 安装位置>/ComfyUI/models/checkpoints`

                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=275add7233b1f048455cff0f162847b9" alt="ComfyUI 桌面版模型保存位置" data-og-width="911" width="911" data-og-height="710" height="710" data-path="images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9bde4750c8ff36b3c64bc610ebb05b57 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e3340ae124d7239717afe84315d6079d 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=27da936e2e5be7f615411a89244732bc 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=cd6a3d90f78767506c30deb0c36e8170 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=390a871fda8ffe2debbe8da45f6d93ab 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fe78a0f9c474924a916a57c8a02348e7 2500w" />
      </Tab>

      <Tab title="ComfyUI便携版本">
        找到你解压后的便携版的文件夹，在**ComfyUI\_windows\_portable/ComfyUI/models/checkpoints** 文件夹下完成模型的保存
        <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=48976b87bcfdba962b119d901c43b286" alt="ComfyUI 便携版模型保存位置" data-og-width="1081" width="1081" data-og-height="709" height="709" data-path="images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e24f9a271a0aea30a444c519a4991c48 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d2a219d501d98acbc88eb4ef0a3da736 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c49908bc31bf6c82e47138199558e74e 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b66628ad620d7ba1a77d824804d68660 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e41817dee653258bf714a83e29edcede 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=49379cc7f2f8c0c359a6e97a93d091ad 2500w" />
      </Tab>

      <Tab title="其它版本">
        请参考 桌面版和便携版部分的说明查找 **ComfyUI/models/checkpoints**文件夹位置
      </Tab>
    </Tabs>

    完成对应保存操作后，请刷新或者重启 ComfyUI 保证对应模型可以被 ComfyUI 检测
  </Tab>
</Tabs>

### 4. 加载模型，并进行第一次图片生成

在完成了对应的绘图模型安装后，请参考下图步骤加载对应的模型，并进行第一次图片的生成

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e0c8f5d7af48afa25076309392f02129" alt="图片生成" data-og-width="2640" width="2640" data-og-height="1384" height="1384" data-path="images/tutorial/gettingstarted/first-image-generation-7-queue.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a2c75afbbad046faedacdc0d49847785 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=51baad1b8a08a3d07956f62cf18b11b5 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b414fc5ca9f56a55bc317bfc9a6bc445 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=16fff107aa1c88d7772c01adae99430f 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3e6a2c94b9760ea8e4ca615a4d2be760 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d8b83b791ae3a2cc979326454d6cc654 2500w" />
请对应图片序号，完成下面操作

1. 请在 **Load Checkpoint** 节点使用箭头或者点击文本区域确保 **v1-5-pruned-emaonly-fp16.safetensors** 被选中，且左右切换箭头不会出现 **null** 的文本
2. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl + enter(回车)` 来执行图片生成

等待对应流程执行完成后，你应该可以在界面的 **保存图像(Save Image)** 节点中看到对应的图片结果，可以在上面右键保存到本地

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=92b100190dd8f91abb37b01cc2e09a59" alt="ComfyUI 首次图片生成结果" data-og-width="2642" width="2642" data-og-height="1390" height="1390" data-path="images/tutorial/gettingstarted/first-image-generation-8-result.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f0c2219d45e70c2f21ebd64032fddb50 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9391713ee886380f8302e396975a94aa 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ace21872a174725c45788b7ce5ce8a34 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a579037cd0b65cd2115280f8eee6e80b 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8dba16d2de187f3f6356af67ee1040ef 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=adfc35ce5d546ca79f140b45dee3fe2d 2500w" />

对于文生图的详细说明，下面的指南中会有详细的说明和指导

<Card title="ComfyUI 文生图工作流示例说明" icon="link" href="/zh-CN/tutorials/basic/text-to-image">
  点击这里查看文生图工作流的详细说明
</Card>

## 故障排除

### 模型加载问题

如果 `Load Checkpoint` 节点没有任何模型可以选择，或者显示为 **null**，请先确认你的模型安装位置正确，或者尝试 **刷新** 或者 **重启 ComfyUI** 使得对应文件夹下的模型可以被检测到
