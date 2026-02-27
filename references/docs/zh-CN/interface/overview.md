> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 界面概览

> 在本篇中，我们将简要介绍 ComfyUI 的基础用户界面，带你熟悉了解 ComfyUI 界面的各个部分，

可视化界面是目前绝大数用户使用 ComfyUI 来调用 [ComfyUI Server](/zh-CN/development/comfyui-server/comms_overview) 进行相应媒体资源生成的方式，它提供了一个可供用户操作和组织工作流的可视化界面，用于组织和调试工作流，并生成令人惊叹的作品。

在本篇我们将粗略介绍 ComfyUI 的界面以及各个部分的功能，在后续的章节中我们将详细介绍各个部分的功能和使用方法。

通常，当你当你启动 ComfyUI 后你可以看到下面这样的一个界面：

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=034e80afc6ca940a6f0dbdf18fa1cd7a" alt="ComfyUI 基础界面" data-og-width="2000" width="2000" data-og-height="1334" height="1334" data-path="images/interface/overview/comfyui_new_interface.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0beeca566a6bbab9eea4281073fcfd59 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=206017b2fdd64f404911be0ff3d9c614 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=33963cbf04870a8f23fb73b0256c711e 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d671b98279f44563d949793b1ce86897 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6e26d3c246a91a061789157046a672a3 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=223f4f4514acb247db84ff9e42e65b02 2500w" />

如果你是较为早期的用户，你应该还见过之前的这样的菜单界面：

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=267da568996a69c02267d78196edece2" alt="ComfyUI 旧界面" data-og-width="2000" width="2000" data-og-height="1334" height="1334" data-path="images/interface/overview/comfyui_old_interface.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=fbf58825e4cd1829fea5ddc6a6789c2b 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c549131132fe63f05b5374cfe3cce891 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d446ac63ff6b27df9946cd038bafdaf4 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6b4692234bc0f0d860db61ac5611abd8 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=12557d1109eea53aba7edb85b02d047e 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4aab864badc28f87abcc0fd73fe42957 2500w" />

这两个菜单界面可以通过设置进行切换，但随着 ComfyUI 的功能日益强大和复杂，我们建议你使用新版的菜单界面来获得更好的使用体验。

目前 ComfyUI前端是一个独立的项目，作为一个独立的 ComfyUI 依赖进行进行发布和更新维护，如果你想要参与贡献，可以 fork 这个[仓库](https://github.com/Comfy-Org/ComfyUI_frontend)，并进行 pull request。

## 本地化支持

目前 ComfyUI 支持：包括英文、中文、俄罗斯语、法语、日文、韩文。
如果你需要切换界面语言到你需要的语言可以点击 **设置齿轮图标** 然后在 `Comfy` --> `Locale` 中选择你需要的语言。

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e5f9d37eb8ea17027846273e69bf292e" alt="ComfyUI 本地化支持" data-og-width="1508" width="1508" data-og-height="936" height="936" data-path="images/interface/overview/locale.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=aa873b328567709a7cbfc9234a5b3caf 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d8405253fb460123648042ba60a6679e 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9b890f66294afa8110f84161be072420 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=694161d0af0a1d589e3a4eeec4bdc021 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=cd18d49dbc8ec8ef3d5cb53d480af73f 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=490fd56e79b7e5bf5d6d4f31729697f3 2500w" />

## 新版菜单界面

### 界面分区（Workspace）

下面是主要的 ComfyUI 的界面分区以及各部分的简要介绍。

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-main.png?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f2222384edaabb19b348da360bcf95bd" alt="ComfyUI 工作区" data-og-width="2582" width="2582" data-og-height="1624" height="1624" data-path="images/zh/interface/comfyui-new-interface-main.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-main.png?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7e98803d24a5a1a0d56f994b96c9729b 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-main.png?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e1e0d933b30386b331a4582230f7f847 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-main.png?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=96c4d963d6e7ab6870e64ccf82f1e641 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-main.png?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a4449118199c2191f604b7395fb5adc4 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-main.png?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=cab59621f7b9f2e3d0b5bc32b10891b1 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-main.png?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a47de64b34591bded52722938569e10e 2500w" />

目前 ComfyUI 的界面除开主要的工作流界面，主要分为以下几个部分：

1. 菜单栏：提供工作流、编辑、帮助菜单，工作流执行、ComfyUI Manager入口等等
2. 侧边栏面板切换按钮：用于切换工作流历史队列、节点库、模型库、本地用户工作流浏览等
3. 切换主题按钮： 在 ComfyUI 默认的暗色主题和亮色主题之间进行快速切换
4. 设置：点击后可打开设置按钮
5. 画布菜单： 提供了ComfyUI 画布的视图放大、缩小、自适应操作等

### 菜单栏功能

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-menu-bar.png?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f28fc727fb1489d74cc76ced846f0e2b" alt="ComfyUI 工作区" data-og-width="2734" width="2734" data-og-height="1126" height="1126" data-path="images/zh/interface/comfyui-new-interface-menu-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-menu-bar.png?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c192d11d55617d56985293819402da01 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-menu-bar.png?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=bd52ff14a2c39af37dcc27b388e31623 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-menu-bar.png?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d6440aa44ab6e80abf86e069973c630f 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-menu-bar.png?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=688eb18f6c4471d93b79e2103c869680 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-menu-bar.png?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f68d0a553ca950c203485df0cc3032f7 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-new-interface-menu-bar.png?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a1817cdbdb395803080266920bb3d116 2500w" />

上图是顶部菜单栏的对应功能，包含的常见的功能，我们会在具体的功能使用部分再详细介绍对应的功能

### 侧边栏面板按钮

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=138181422006bac20c5d092f729f00b3" alt="ComfyUI 侧边栏面板" data-og-width="1909" width="1909" data-og-height="1007" height="1007" data-path="images/interface/overview/side-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d155573e5ba3006af39d10523fc5ed3c 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f23e97db967f522b0609f262294c0fc7 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=40e1ecac4167eb739881c7a9db2edc53 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d7af26e3bb5bffcca92e68d0c9a73f15 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9921051b06c31e065979b569b4ec3dd5 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=473efa4c4d5cb05cef2de7e51a06d8e1 2500w" />

在目前的 ComfyUI 中，我们提供了四个侧边面板包含了以下功能：

1. 工作流历史队列(Queue)： 所有 ComfyUI 执行媒体内容生成的队列信息
2. 节点库(Node Library)： 所有 ComfyUI 中的节点包括`Comfy Core` 和你安装的自定义节点都会可以在这里进行查找
3. 模型库(Model Library)： 你本地的`ComfyUI/models` 目录下的模型可以在这里被查找到
4. 本地用户工作流(Workflows)： 你本地保存的工作流可以在这里被查找到

## 旧版菜单

目前 ComfyUI 默认启用新版界面，如果你更偏好使用旧版界面，可以点击 **设置齿轮图标** 然后在 `Comfy` --> `菜单(Menu)` 将 `使用新菜单(Use new menu)` 设置为 `disabled` 即可切换到旧版本的菜单。

<Note>
  旧版菜单界面仅支持英文。
</Note>

旧版本菜单界面功能标注说明如下：

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-old-menu.png?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=01c840da5ea420dea500a0e0160e1f1b" alt="ComfyUI 旧版菜单" data-og-width="884" width="884" data-og-height="1126" height="1126" data-path="images/zh/interface/comfyui-old-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-old-menu.png?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f4c7c810e0935d24be791875139ce800 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-old-menu.png?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2772bed82e23d9be9c03f104d8053c37 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-old-menu.png?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1bbea8f6856fdc6a24a1ca0f0b088f29 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-old-menu.png?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=76db8ae8130ee3681f23fff2d2a81c34 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-old-menu.png?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2ebc52c604d678e5be89c2356ec1987c 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/comfyui-old-menu.png?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6fbd56a449bb948f6d6b5c38e54513ec 2500w" />
