> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 概述

自定义节点允许你实现新功能并与更广泛的社区分享。

自定义节点就像任何 Comfy 节点一样：它接收输入，对其进行处理，然后产生输出。
虽然有些自定义节点执行非常复杂的任务，但许多节点只做一件事。下面是一个简单节点的例子，它接收一张图片并进行反色处理。

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=8088073e29e8af1bc700937ecb3b77e9" alt="唯一图片节点" data-og-width="564" width="564" data-og-height="279" height="279" data-path="images/invert_image_node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6fa9f912f38ec608ee43f4e456cedf42 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=aeae6dd8bc6393935ebabe3de4b8ed85 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3dbe92afa58705aca5f218df9f5c5a52 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=dfda0a7b67616219ac9b7ec9742cb0d4 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a3b84be0acf1b9248b9ac0086a49bd53 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=2113625a7743f680050980330f4f928d 2500w" />

示例节点代码：

* [cookiecutter-comfy-extension](https://github.com/Comfy-Org/cookiecutter-comfy-extension)
* [ComfyUI-React-Extension-Template](https://github.com/Comfy-Org/ComfyUI-React-Extension-Template)
* [ComfyUI\_frontend\_vue\_basic](https://github.com/jtydhr88/ComfyUI_frontend_vue_basic)

## 客户端-服务器模型

Comfy 运行在客户端-服务器模型下。服务器端由 Python 编写，负责所有实际工作：数据处理、模型、图像扩散等。客户端由 Javascript 编写，负责用户界面。

Comfy 也可以以 API 模式使用，在该模式下，工作流由非 Comfy 客户端（如其他 UI 或命令行脚本）发送到服务器。

自定义节点可以分为以下四类：

### 仅服务器端

大多数自定义节点仅在服务器端运行，通过定义一个 Python 类来指定输入和输出类型，并提供一个可调用的函数来处理输入并生成输出。

### 仅客户端

少数自定义节点仅对客户端 UI 进行修改，但不添加核心功能。尽管名字如此，它们甚至可能不会向系统添加新节点。

### 客户端与服务器端独立

自定义节点可以同时提供额外的服务器功能和额外（相关的）UI 功能（例如用于新数据类型的新小部件）。在大多数情况下，客户端和服务器之间的通信可以通过 Comfy 的数据流控制来处理。

### 客户端与服务器端联动

在少数情况下，UI 功能和服务器需要直接相互通信。

<Warning>任何需要客户端-服务器通信的节点都无法通过 API 使用。</Warning>
