> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 自定义节点

> 了解 ComfyUI 中自定义节点的安装、依赖启用、更新、禁用、卸载

## 关于自定义节点

当你在安装了 ComfyUI 后，你将会发现 ComfyUI 中已经包含了许多节点，这些原生的节点称为 **Comfy Core** 节点，这些节点都是由 ComfyUI 官方维护的。

此外还有许多来自 ComfyUI 社区的众多作者带来的各种各样的 [**自定义节点**](https://registry.comfy.org)，这些自定义节点为 ComfyUI 带来了诸多的扩展功能，大大扩展了 ComfyUI 的功能和能力边界。

在本指南中，我们将介绍如何自定义节点相关的一些操作，包括安装、更新、禁用、卸载、依赖安装等。

每个人都可以开发自己的自定义的扩展功能到 ComfyUI 中，并分享给其他人使用，你可以在[这里](https://registry.comfy.org)找到许多来自社区的自定义节点，如果你想要开发自己的自定义节点请访问下面的部分开始：

<Card title="开始开发自定义节点" icon="link" href="/zh-CN/custom-nodes/overview">
  了解如何开始开发一个自定义节点
</Card>

## 自定义节点管理

在这个部分我们将讲解：

* 安装自定义节点
* 安装节点依赖
* 自定义节点版本控制
* 卸载自定义节点
* 临时禁用自定义节点
* 处理自定义节点依赖冲突

### 1. 安装自定义节点

目前 ComfyUI 支持通过多种方式安装自定义节点，包括：

* \[通过 ComfyUI Manager 安装（推荐）]\(#通过 ComfyUI Manager 安装)
* 通过 Git 安装
* 手动安装

我们推荐通过 **ComfyUI Manager** 来安装自定义节点，这是一个在 ComfyUI 自定义节点生态中具有非常重要意义的一个工具，它使得自定义节点管理（如搜索、安装、更新、禁用和卸载）变得简单，你只需要在 ComfyUI Manager 中搜索你想要安装的节点，然后点击安装即可。

但由于目前所有的自定义节点都是存储在 GitHub 上，所以在本篇针对于某些无法正常访问 GitHub 的的地区，我们在本篇撰写了详尽的不同的自定义节点的安装方式。

另外由于我们推荐使用 **ComfyUI Manager** 进行对应的插件管理，我们推荐使用这一工具来进行插件的管理，你可以在[这里](https://github.com/Comfy-Org/ComfyUI-Manager)找到它的源码。
所以在本篇文档中，我们将会使用安装 ComfyUI Manager 作为自定义节点安装示例，并在本篇的相关介绍部分补充如何使用它来进行节点的管理。

<Tabs>
  <Tab title="通过 ComfyUI Manager 安装">
    由于 ComfyUI Manager 的功能非常丰富，所在在这里我们将对应的通过 ComfyUI Manager 章节单独使用一篇文档来介绍，请访问下面的链接来了解如何使用 ComfyUI Manager 来安装自定义节点。

    <Card title="ComfyUI Manager 安装自定义节点" icon="link" href="/zh-CN/installation/install_custom_node#方法一:comfyui-manager（推荐）">
      了解如何使用 ComfyUI Manager 安装自定义节点
    </Card>
  </Tab>

  <Tab title="通过 Git 安装">
    <Steps>
      <Step title="确保 Git 已经安装">
        首先你需要确保在你的系统中已经安装了 Git，你可以在对应的系统终端(terminal)中输入下面的命令来检查是否已经安装了 Git。

        ```bash  theme={null}
        git --version
        ```

        如果已经安装了 Git，你将会看到类似如下的输出：

                <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c0e90164d3a1c8f9ed0f54164b16443b" alt="Windows 终端" data-og-width="1114" width="1114" data-og-height="228" height="228" data-path="images/concepts/custom_nodes/win_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a357e53c048002cce88022038c5bf828 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9cb6790f16ae6e6f63235f1e959600d5 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=271a0c821c923b7b2fdc3d5746dfeaa8 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bc288cf2488e869ae3d2f6a8a56063ed 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2af5489655f4e5cb48890bf017a7b647 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=808b660d6e7116094aadda28a1dfb2d6 2500w" />

        如果还没有安装，请访问 [git-scm.com](https://git-scm.com/) 下载对应的安装包进行安装, linux 用户请参考 [git-scm.com/downloads/linux](https://git-scm.com/downloads/linux) 这个部分来完成对应的安装。

        <Tip>
          对于 ComfyUI Desktop 版本,你可以参考下面的方式使用 Desktop 的终端来完成对应的安装。
          <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=946b0d382dc99eba1b7c33072ed1bce2" alt="ComfyUI Desktop 终端" data-og-width="1800" width="1800" data-og-height="1403" height="1403" data-path="images/concepts/custom_nodes/desktop_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4ce6791b7ace89fa5a1e7fd8438b8dc0 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6e9fcf09190d3cfa4ee6ef730d6b9fe6 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=fc1b03b1b9b43062a5c4bd31dbea62d9 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=216afbc5d75842f85ebc8f1b76b2d5be 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cce1b33c7a01b016a61baa10339c97df 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1216d21a3cc886305cc67a8c22edfb91 2500w" />
        </Tip>
      </Step>

      <Step title="克隆自定义节点代码到对应目录">
        在完成 Git 的安装后，我们需要对应的自定义节点的仓库地址，在这里我们使用 ComfyUI-Manager 的仓库地址作为示例:

        ```bash  theme={null}
        https://github.com/Comfy-Org/ComfyUI-Manager
        ```

        <Tip>对于无法顺利访问 GitHub 的地区，可以尝试使用其它的代码托管服务网站来 fork 对应的仓库，然后使用对应的仓库地址来完成对应的节点安装，比如 gitee 等。</Tip>

        我们首先需要进入到 ComfyUI 的自定义节点的相关目录，以 ComfyUI 便携版为例，如果对应文件夹位置为`D:\ComfyUI_windows_portable`，那么你应该可以找到对应自定义节点的文件夹为`D:\ComfyUI_windows_portable\ComfyUI\custom_nodes`，首先我们需要使用 `cd` 命令进入到对应的目录

        ```bash  theme={null}
        cd D:\ComfyUI_windows_portable\ComfyUI\custom_nodes
        ```

        然后我们使用 `git clone` 命令来完成对应的节点安装。

        ```bash  theme={null}
        git clone https://github.com/Comfy-Org/ComfyUI-Manager
        ```

        如果一切顺利，你将会看到类似如下的输出：

                <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=80409dceca35c9d58c42dde48c4c53a5" alt="通过 Git 安装自定义节点" data-og-width="1116" width="1116" data-og-height="317" height="317" data-path="images/concepts/custom_nodes/install_custom_nodes_by_git.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=11856e33ebf16d403fc1bfd7dea88fa7 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3fe94004114027d4c921c43f3d42a9d9 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ac2c83634737859345407522169a2777 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b1a5d9aecc3d51fcf9cd8a254797f565 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=dd666e0e9c82d0929c1c4e0430003571 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=205985da6950ff470816f40f5fc51500 2500w" />

        这意味着你已经成功克隆了对应的自定义节点的代码，接下来我们需要进行对应依赖的安装。
      </Step>

      <Step title="安装依赖">
        请参考[安装节点依赖](#安装节点依赖)章节中的说明进行对应的依赖安装。
      </Step>
    </Steps>
  </Tab>

  <Tab title="手动安装">
    手动安装虽然不是推荐的安装方式，但在你无法使用 git 顺利安装的情况下，这不失为一个备用的方案。

    <Warning>
      使用这种方式安装的插件，将丢失对应的 git 版本历史信息，将无法很便利地进行后续的版本管理
    </Warning>

    <Steps>
      <Step title="下载自定义节点代码 zip 包">
        使用手动安装我们需要首先下载对应的节点代码，然后解压到对应的目录。

                <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=34fa06cf4580152428c5d2b55b192911" alt="下载节点代码" data-og-width="1011" width="1011" data-og-height="618" height="618" data-path="images/concepts/custom_nodes/download_zip.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=abe163da0d4486c9ac953740efa53132 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=938e6e59ac49b2f6f4d5a6ab8e3fc34b 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4d2b335af8cf590678abf746ad2faad0 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=40a958844a5808923eb70f12ecdca784 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ea0a46e7137e32594e7d3525b679865c 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b8980eb0deed06232f1081ceb18ed528 2500w" />

        访问对应自定义节点的仓库界面

        1. 点击 `Code` 按钮
        2. 然后点击 `Download ZIP` 按钮，下载对应的 zip 包。
        3. 解压对应的 zip 包
      </Step>

      <Step title="复制文件到 ComfyUI 自定义节点目录">
        将上面步骤解压后的代码复制到 ComfyUI 自定义节点目录，以 ComfyUI 便携版为例，如果对应文件夹位置为`D:\ComfyUI_windows_portable`，那么你应该可以找到对应自定义节点的文件夹为`D:\ComfyUI_windows_portable\ComfyUI\custom_nodes`，将上面步骤解压后的代码复制到对应的目录。
      </Step>

      <Step title="安装依赖">
        请参考[安装节点依赖](#安装节点依赖)章节中的说明进行对应的依赖安装。
      </Step>
    </Steps>
  </Tab>
</Tabs>

### 2. 安装节点依赖

自定义节点都需要进行相关的依赖的安装，比如对于 ComfyUI-Manager 来说，你可以访问[requirements.txt](https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/requirements.txt) 文件来查看对应的依赖包的要求,

在之前的步骤中，我们仅仅是把对应的自定义节点代码克隆到了本地，并没有安装对应的依赖，所以接下来我们需要安装对应的依赖。

<Note>
  实际上，如果你使用的是 ComfyUI-Manager 来安装插件的话，ComfyUI Manager 会自动帮你完成对应的依赖安装，你只需要在安装插件后，重启 ComfyUI 即可，这也是为什么我们极力推荐使用 ComfyUI Manager 来安装自定义节点。

  但也许你会在某些情况下无法顺利使用 ComfyUI Manager 来安装自定义节点，所以我们提供了这部分较为详细的依赖安装说明。
</Note>

在关于[依赖关系](/zh-CN/development/core-concepts/dependencies)章节中，我们介绍了 ComfyUI 中依赖关系的相关内容，ComfyUI 是一个基于 **Python** 的项目，我们构建了一个用于运行 ComfyUI 的独立 **Python** 运行环境，所有的相关依赖都需要被安装在在这个独立的 **Python** 运行环境中。

如果你直接在系统级的终端运行 `pip install -r requirements.txt`，对应的依赖可能会被安装到了系统级的 **Python** 环境中，会导致对应的自定义节点在 ComfyUI 的环境中依赖还是丢失的，导致对应自定义节点无法正常运行。

所以接下来我们需要使用 ComfyUI 的独立 Python 运行环境来完成对应的依赖安装。

依据不同的 ComfyUI 版本我们将使用不同的方式来进行对应的依赖安装，

<Tabs>
  <Tab title="ComfyUI 便携版（Portable）">
    对于 ComfyUI 便携版（Portable）来说，它使用的是一个嵌入式的 Python ，对应 Python 位于 `\ComfyUI_windows_portable\python_embeded` 目录下, 我们需要使用对应的 Python 来完成对应的依赖安装。

    首先先在便携版的目录下启动 terminal 或者启动 terminal 后使用 `cd` 命令进入到 `\ComfyUI_windows_portable\` 目录下

        <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ee4569d27b4ef901c5f67d8f795b448c" alt="启动 terminal" data-og-width="1822" width="1822" data-og-height="1187" height="1187" data-path="images/concepts/custom_nodes/open_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6e1589dff5dd380e4484e6ae44172df4 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=107a3e8c8020ddc46b1473004a2e8394 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9eb529d60d9cfb939bed1014c0895939 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f17cb8cb8a0f24461baaa909482591e0 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=649ce090ec9804a49662f81b20e192c9 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=26d70d0642ffe52424f940463d770a2b 2500w" />

    确保对应终端的目录为 `\ComfyUI_windows_portable\` 目录下，如下图为 `D:\ComfyUI_windows_portable\`

        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f6da2e8c4eef1016e6fde84ee5527ce0" alt="终端" data-og-width="2400" width="2400" data-og-height="1147" height="1147" data-path="images/concepts/custom_nodes/terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d4c3e07411aed9823f7b52287e8c4d95 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5dd7ecf31d1183f950d31c9b9b4b97c9 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0bc86f9512c81d0045ec3cc8e3067846 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e54eab41295a7fb58c69bca2b1310f73 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=eef8a3bad5e20eb6bf0b14c756cdef1b 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b91b3d6f97318bcae7aa99c6613e42ee 2500w" />

    然后使用 `python_embeded\python.exe` 来完成对应的依赖安装。

    ```bash  theme={null}
    python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-Manager\requirements.txt
    ```

    当然你可以把对应的 ComfyUI-Manager 替换为你实际安装的自定义节点名称，但需要确保对应节点目录下的确存在 `requirements.txt` 文件。
  </Tab>

  <Tab title="ComfyUI 桌面版">
    <Tip>
      由于 ComfyUI 桌面版在安装过程中已经安装了 ComfyUI-Manager 及对应依赖，但本文是以 ComfyUI Manager 作为自定义节点安装为示例讲解的，实际上你并不需要再在桌面版中执行 ComfyUI Manager 的依赖安装。
      如果没有意外情况，我们建议使用 ComfyUI Manager 来安装自定义节点，这样你就不需要手动安装依赖了。
    </Tip>

        <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=946b0d382dc99eba1b7c33072ed1bce2" alt="ComfyUI Desktop 终端" data-og-width="1800" width="1800" data-og-height="1403" height="1403" data-path="images/concepts/custom_nodes/desktop_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4ce6791b7ace89fa5a1e7fd8438b8dc0 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6e9fcf09190d3cfa4ee6ef730d6b9fe6 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=fc1b03b1b9b43062a5c4bd31dbea62d9 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=216afbc5d75842f85ebc8f1b76b2d5be 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cce1b33c7a01b016a61baa10339c97df 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1216d21a3cc886305cc67a8c22edfb91 2500w" />

    然后使用下面的命令来安装对应插件的依赖

    ```bash  theme={null}
    pip install -r .\custom_nodes\<对应自定义节点名称>\requirements.txt
    ```

    如下图，是对应 ComfyUI-Hunyuan3Dwrapper 的依赖安装。

        <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=23366292f947d238ea260f07d8529502" alt="ComfyUI Desktop 依赖安装" data-og-width="2038" width="2038" data-og-height="1472" height="1472" data-path="images/concepts/custom_nodes/install_dependencies.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8849616b5cbe36efa5096e396ab83795 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=32c343240d23faf1f40d94ba43f9c747 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=859ffceb951a83654e3c363a489c3c7a 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=376dd9c1750dbff7a9a796285ce1704e 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=26af3d5f53099c4b5ebb4c51c13053d8 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=34db9db7e172a2cd0af03eb08ee1265a 2500w" />
  </Tab>

  <Tab title="自定义 Python 环境的用户">
    对于自定义 Python 环境的用户，我们建议使用 `pip install -r requirements.txt` 来完成对应的依赖安装。
  </Tab>
</Tabs>

### 自定义节点版本控制

自定义节点的版本控制，实际上是基于 Git 的版本控制来进行的，你可以通过 Git 来进行对应的节点版本管理，但实际上在 ComfyUI Manager 中已经很好地集成了这一版本管理功能，非常感谢 [@Dr.Lt.Data](https://github.com/ltdrdata) 为我们带来如此便捷的工具。

在这个部分我们依旧会为你讲解这两种不同插件版本管理的方法，但如果你是使用 zip 压缩包进行手动安装的，那么对应的 git 版本历史信息会丢失，会导致你无法进行对应的版本管理。

<Tabs>
  <Tab title="使用 ComfyUI Manager 进行版本管理">
    <Tip>由于我们正在对 ComfyUI Manager 进行迭代，实际最新的界面和步骤可能会有较大的改变</Tip>

    <Steps>
      <Step title="进入节点管理界面">
        如图进行对应的操作，进入 ComfyUI Manager 的对应界面
      </Step>

      <Step title="找到对应自定义节点包">
        可以使用对应的筛选过滤来过滤出已安装的节点包，然后再进行对应的节点管理
      </Step>

      <Step title="进行版本切换">
        切换到对应的版本，Manager 会帮助你完成对应的依赖更新和安装，通常切换完版本之后你需要重启 ComfyUI 以使更改生效。
      </Step>
    </Steps>
  </Tab>

  <Tab title="使用 Git 进行版本管理">
    <Steps>
      <Step title="使用命令行工具进入所在目录">
        找到你对应节点所在的目录文件夹如`ComfyUI/custom_nodes/ComfyUI-Manager`
        使用 `cd` 命令来进入对应的文件夹

        ```bash  theme={null}
        cd <你的安装目录>/ComfyUI/custom_nodes/ComfyUI-Manager
        ```
      </Step>

      <Step title="使用 git 命令来查看版本">
        可以使用以下命令查看所有可用的 tag 和 release：

        ```bash  theme={null}
        git tag
        ```

        这将列出所有的版本标签，你可以选择你想要切换到的版本。
      </Step>

      <Step title="切换到指定版本">
        使用以下命令切换到指定的 tag 或 release：

        ```bash  theme={null}
        git checkout <tag_name>
        ```

        将 `<tag_name>` 替换为你想要切换到的具体版本标签。
      </Step>

      <Step title="切换到特定 commit 版本">
        如果你想要切换到特定的 commit 版本，可以使用以下命令：

        ```bash  theme={null}
        git checkout <commit_hash>
        ```

        将 `<commit_hash>` 替换为你想要切换到的具体 commit 的哈希值。
      </Step>

      <Step title="进行依赖安装">
        由于进行版本切换后，对应的自定义节点包的依赖可能会有所改变，所以你需要重新进行对应节点的依赖的安装，请参考[安装节点依赖](#2.安装节点依赖)部分的说明进入对应的环境进行安装
      </Step>
    </Steps>
  </Tab>
</Tabs>

### 卸载自定义节点

待更新

### 临时禁用自定义节点

待更新

### 自定义节点依赖冲突

待更新

## ComfyUI Manager

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cea0de500828224b23b64cef84a31936" alt="ComfyUI 管理器界面" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/concepts/core-concepts_nodes_manager.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b66fffe074ba15068c2868e5e127cc41 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=951aa7941493ea56018c7aa77d1bc143 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=93e156a11636d64258510480fe1c28c2 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=352d680f30f32e457031be3c6de987d9 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a034b1663b608f4d64c6a690ea652b88 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4ca79e9090f1ed2513db42fa9838af40 2500w" />

目前在 [Desktop 版本](/zh-CN/installation/desktop/windows) 中已默认包含该工具,而在[便携（Portable）版](/zh-CN/installation/comfyui_portable_windows)中，你需要参考本文档中[安装管理器](#安装自定义节点)章节中的说明进行安装。

<Note>
  由于随着 ComfyUI 的发展，ComfyUI Manager 在 ComfyUI 中的角色也愈加重要，目前 ComfyUI-Manager 已经正式加入 Comfy Org 组织，正式成为 ComfyUI 核心依赖的一部分，并且由原作者[Dr.Lt.Data](https://github.com/ltdrdata)继续维护，你可以查看[这篇博客](https://blog.comfy.org/p/comfyui-manager-joins-comfy-org)了解更多信息。
  并且在未来迭代中，我们会大大优化 ComfyUI Manager 的使用，所以本文的中使用说明文档的界面，可能会与最新版本的 ComfyUI Manager 界面有所不同。
</Note>

### 安装管理器

如果您正在运行 ComfyUI 服务器应用程序，则需要安装管理器。如果 ComfyUI 正在运行，请在继续之前将其关闭。

第一步是安装 Git，这是一个用于软件版本控制的命令行应用程序。Git 将从 [github.com](https://github.com) 下载 ComfyUI 管理器。从 [git-scm.com](https://git-scm.com/) 下载并安装 Git。

安装 Git 后，导航到 ComfyUI 服务器程序目录，进入标记为 **custom\_nodes** 的文件夹。打开命令窗口或终端。确保命令行显示当前目录路径为 **custom\_nodes**。输入以下命令。这将下载管理器。从技术上讲，这被称为 *克隆 Git 仓库*。

### 检测缺失的节点

在安装管理器后，你可以在管理器中检测到缺失的节点。

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cea0de500828224b23b64cef84a31936" alt="ComfyUI 管理器界面" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/concepts/core-concepts_nodes_manager.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b66fffe074ba15068c2868e5e127cc41 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=951aa7941493ea56018c7aa77d1bc143 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=93e156a11636d64258510480fe1c28c2 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=352d680f30f32e457031be3c6de987d9 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a034b1663b608f4d64c6a690ea652b88 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4ca79e9090f1ed2513db42fa9838af40 2500w" />

## 开发一个自定义节点

如果你具有一定的开发能力，请从下面的文档开始以了解如何开始开发一个自定义节点。

<Card title="开始开发自定义节点" icon="link" href="/zh-CN/custom-nodes/overview">
  了解如何开始开发一个自定义节点
</Card>
