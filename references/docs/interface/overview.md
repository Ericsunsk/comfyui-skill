> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Interface Overview

> In this article, we will briefly introduce the basic user interface of ComfyUI, familiarizing you with the various parts of the ComfyUI interface.

The visual interface is currently the way most users utilize ComfyUI to call the [ComfyUI Server](/development/comfyui-server/comms_overview) to generate corresponding media resources. It provides a visual interface for users to operate and organize workflows, debug workflows, and create amazing works.

Typically, when you start the ComfyUI server, you will see an interface like this:

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=034e80afc6ca940a6f0dbdf18fa1cd7a" alt="ComfyUI Basic Interface" data-og-width="2000" width="2000" data-og-height="1334" height="1334" data-path="images/interface/overview/comfyui_new_interface.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0beeca566a6bbab9eea4281073fcfd59 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=206017b2fdd64f404911be0ff3d9c614 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=33963cbf04870a8f23fb73b0256c711e 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d671b98279f44563d949793b1ce86897 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6e26d3c246a91a061789157046a672a3 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_new_interface.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=223f4f4514acb247db84ff9e42e65b02 2500w" />

If you are an earlier user, you may have seen the previous menu interface like this:

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=267da568996a69c02267d78196edece2" alt="ComfyUI Old Interface" data-og-width="2000" width="2000" data-og-height="1334" height="1334" data-path="images/interface/overview/comfyui_old_interface.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=fbf58825e4cd1829fea5ddc6a6789c2b 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c549131132fe63f05b5374cfe3cce891 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d446ac63ff6b27df9946cd038bafdaf4 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6b4692234bc0f0d860db61ac5611abd8 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=12557d1109eea53aba7edb85b02d047e 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui_old_interface.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4aab864badc28f87abcc0fd73fe42957 2500w" />

Currently, the [ComfyUI frontend](https://github.com/Comfy-Org/ComfyUI_frontend) is a separate project, released and maintained as an independent pip package. If you want to contribute, you can fork this [repository](https://github.com/Comfy-Org/ComfyUI_frontend) and submit a pull request.

## Localization Support

Currently, ComfyUI supports: English, Chinese, Russian, French, Japanese, and Korean.
If you need to switch the interface language to your preferred language, you can click the **Settings gear icon** and then select your desired language under `Comfy` --> `Locale`.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e5f9d37eb8ea17027846273e69bf292e" alt="ComfyUI Localization Support" data-og-width="1508" width="1508" data-og-height="936" height="936" data-path="images/interface/overview/locale.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=aa873b328567709a7cbfc9234a5b3caf 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d8405253fb460123648042ba60a6679e 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9b890f66294afa8110f84161be072420 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=694161d0af0a1d589e3a4eeec4bdc021 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=cd18d49dbc8ec8ef3d5cb53d480af73f 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/locale.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=490fd56e79b7e5bf5d6d4f31729697f3 2500w" />

## New Menu Interface

### Workspace Areas

Below are the main interface areas of ComfyUI and a brief introduction to each part.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-main.png?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=24c16f1242f71e5bcf11a965fc3307da" alt="ComfyUI Workspace" data-og-width="2660" width="2660" data-og-height="1580" height="1580" data-path="images/interface/overview/comfyui-new-interface-main.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-main.png?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b443b8ba0c23c22354a8f8b3827798e7 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-main.png?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=5bbbe4e81184a1002f058e40609cc8db 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-main.png?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=43b9ce574d162c68abfcd492f14ca2c1 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-main.png?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c74805970c2d260bd6a8d13354d64118 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-main.png?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=fa39aa2113f18310438364463f931153 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-main.png?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=04838786fff63d394f6e112c74d8e516 2500w" />

Currently, apart from the main workflow interface, the ComfyUI interface is mainly divided into the following parts:

1. Menu Bar: Provides workflow, editing, help menus, workflow execution, ComfyUI Manager entry, etc.
2. Sidebar Panel Switch Buttons: Used to switch between workflow history queue, node library, model library, local user workflow browsing, etc.
3. Theme Switch Button: Quickly switch between ComfyUI's default dark theme and light theme
4. Settings: Click to open the settings button
5. Canvas Menu: Provides zoom in, zoom out, and auto-fit operations for the ComfyUI canvas

### Menu Bar Functions

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-menu-bar.png?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=088e0a362fcda0b8e9eca48b6fa2763a" alt="ComfyUI Workspace" data-og-width="2734" width="2734" data-og-height="1126" height="1126" data-path="images/interface/overview/comfyui-new-interface-menu-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-menu-bar.png?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=010e6b3431cf3ba93f9a6ff2941b3dd3 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-menu-bar.png?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b605712908ff77c7cc66e8b7cdefe720 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-menu-bar.png?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=088c0aa9fafe9a616f4a35d88fbd0d04 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-menu-bar.png?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=5e916f438e9bf7267b9e10f4e8c186d1 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-menu-bar.png?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a48cb6dd9321beea5eeb47085329972f 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-new-interface-menu-bar.png?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6232de43916a0dc2903a6cf302092a49 2500w" />

The image above shows the corresponding functions of the top menu bar, including common features, which we will explain in detail in the specific function usage section.

### Sidebar Panel Buttons

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=138181422006bac20c5d092f729f00b3" alt="ComfyUI Sidebar Panel" data-og-width="1909" width="1909" data-og-height="1007" height="1007" data-path="images/interface/overview/side-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d155573e5ba3006af39d10523fc5ed3c 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f23e97db967f522b0609f262294c0fc7 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=40e1ecac4167eb739881c7a9db2edc53 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d7af26e3bb5bffcca92e68d0c9a73f15 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9921051b06c31e065979b569b4ec3dd5 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/side-panel.png?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=473efa4c4d5cb05cef2de7e51a06d8e1 2500w" />

In the current ComfyUI, we provide four side panels with the following functions:

1. Workflow History Queue (Queue): All queue information for ComfyUI executing media content generation
2. Node Library: All nodes in ComfyUI, including `Comfy Core` and your installed custom nodes, can be found here
3. Model Library: Models in your local `ComfyUI/models` directory can be found here
4. Local User Workflows (Workflows): Your locally saved workflows can be found here

## Old Menu Version

Currently, ComfyUI enables the new interface by default. If you prefer to use the old interface, you can click the **Settings gear icon** and then set `Use new menu` to `disabled` under `Comfy` --> `Menu` to switch to the old menu version.

<Note>
  The old menu interface only supports English.
</Note>

The function annotations for the old menu interface are explained below:

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-old-menu.png?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2f18e63bae1182c4a7a826d1f9385786" alt="ComfyUI Old Menu" data-og-width="928" width="928" data-og-height="1126" height="1126" data-path="images/interface/overview/comfyui-old-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-old-menu.png?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=338269cf53536041718a60f5acb77ad2 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-old-menu.png?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=72a8cef25664abc0f6c9329dc444e30b 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-old-menu.png?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=db4885dca2bacd1ba583c88227fc5bfc 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-old-menu.png?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2b8fa3683811237b47fe6f1815d3f4f0 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-old-menu.png?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4eb3611d79e1ecf3900c39cce8d3cbd2 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/overview/comfyui-old-menu.png?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bf8bac2b01c3bc8b57d29ad8154bae60 2500w" />
