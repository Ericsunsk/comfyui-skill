> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 节点

> 了解 ComfyUI 中节点的概念。

在 ComfyUI 中，节点是我们执行任务的单元，他们是构建好的一个个独立的模块，无论是 **Comfy Core** 还是 **自定义节点** ，每个节点都是一个独立的模块，有着自己独特的功能，节点之间通过连线连接，我们可以像搭乐高积木一样搭建起来复杂的功能。
可以说，不同的节点组合构建出了 ComfyUI 的无限可能。

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=aed5e1f863c37948107cfcb3458955b7" alt="Comfy Core K-Sampler 节点" data-og-width="854" width="854" data-og-height="767" height="767" data-path="images/comfy_core/sampling/k_sampler.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f891fb24b7fcbb6616bad811d797cd10 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d3597cfd9ef1b324ceb8b8e529246540 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e714d81c3a3214ef9fe1da89cdc2efd3 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5001918af1c739866639c03df51a3c19 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ff62cab54c0c1fa1432d98c69877706d 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=350b8494ce4c1e004ddd94f7977563d7 2500w" />

例如在 K-Sampler 节点中，你可以看到它有多个输入和输出，也同时包含多个参数设置，这些参数决定了节点执行的逻辑，它的背后是对应编写好的 Python 逻辑，从而可以让你不用去接触代码就可以实现对应的功能。

<Note>
  ComfyUI 正在持续开发中，文档中的部分内容可能已过时。如果你发现任何变化，欢迎[帮助我们更新文档](https://github.com/Comfy-Org/docs)。
</Note>

## 节点的的不同状态

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=150ab91575a7c9300b7ed20d8026e499" alt="节点状态" data-og-width="3167" width="3167" data-og-height="900" height="900" data-path="images/concepts/node/status.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=72ff0c9fc86e4de4abc041f54e9a76a4 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ec6264e55b41fe6f284bb32ccf7e09cb 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0964829012a38d6540d89773a163e5eb 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0b013434ced278f2029243136f80198d 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f4077f9da03b83ae9ee4a4d28cce19e7 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=68a03e96245d13250e0864a8951c2b7f 2500w" />

在 ComfyUI 中，节点有多种状态，下面是一些常见的节点状态：

1. **正常(Normal)状态**： 正常状态
2. **运行(Running)状态**： 运行中状态，通常在你开始运行工作流后，正在执行的节点会显示这个状态
3. **错误(Error)状态**： 节点错误，通常在运行工作流后，如果对应的节点输入存在问题，导致了错误会显示这个状态，并用红色标识对应出错的输入节点，你需要解决对应出错的输入来保证工作流正常运行
4. **丢失(Missing)状态**： 这个状态通常在你导入了一些工作流后会出现，存在两种可能
   * ComfyCore 原生节点丢失： 这通常是因为 ComfyUI 的版本更新了，而你当前使用的 ComfyUI 版本较旧，你需要更新 ComfyUI 来解决这个问题
   * 自定义节点丢失： 工作流中是用了第三方作者开发的自定义节点，而你的本地的 ComfyUI 版本没有安装对应的自定义节点，你可以使用 [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) 来查找丢失的自定义节点

## 节点之间的连接

在 ComfyUI 中，节点通过[连线](/zh-CN/development/core-concepts/links)连接，从而让相同的数据类型在不同的处理单元之间进行流转处理,从而获得最终的结果。

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=40a62b27aa2f44cb97eae917c8c1f8da" alt="ComfyUI 节点连线" data-og-width="2000" width="2000" data-og-height="1108" height="1108" data-path="images/concepts/node/inpaint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c90df520b2046575f0d0005253cf359e 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7850db8dad1f1096fe1e7870b47f772b 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=613be61533b2737be42795c6162d77b9 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4db8d8d46ec77ded6285a4939d8cb1cc 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=76228d5a4063d7923d02fb718938bd71 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=49f3f3318cf1e678bec7499f116c8065 2500w" />

每个节点都会接收一些输入内容，然后经过模块处理将他们转换为对应的输出，不同的节点链接之间，必须符合数据类型规定的要求，在 ComfyUI 中，我们使用不同的颜色来区分节点的数据类型,下面是一些基础的数据类型。

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5" alt="ComfyUI 节点数据类型" data-og-width="685" width="685" data-og-height="356" height="356" data-path="images/concepts/node/data_type.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3a128b7a0a1e6e93733f2fe649efd330 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=56df7925857870daf0995d69dcca1c24 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=69feb5a2bdde5813c9444c500710e1cb 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=087178033c73065ed5a521cb04f3f5cb 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=389aadb6b698921a58ffb6e3c65ce796 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9ee271b46d36d4ab90b1688dbcf80c5d 2500w" />

| 数据类型        | 颜色   |
| ----------- | ---- |
| 扩散模型        | 薰衣草色 |
| CLIP 模型     | 黄色   |
| VAE 模型      | 玫瑰色  |
| 条件化         | 橙色   |
| 潜在图像        | 粉色   |
| 像素图像        | 蓝色   |
| 蒙版          | 绿色   |
| 数字 (整数或浮点数) | 浅绿色  |
| 网格（Mesh）    | 亮绿色  |

随着 ComfyUI 的迭代，我们可能会拓展更多的数据类型，以符合更多场景的需求。

### 节点之间的连接和取消连接

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/link_nodes.gif?s=06359a20664f48e43763696313a063f9" alt="ComfyUI 节点连接" data-og-width="820" width="820" data-og-height="724" height="724" data-path="images/concepts/node/link_nodes.gif" data-optimize="true" data-opv="3" />

**连接**： 在上一个节点的输出点中拖拽到下一个节点相同颜色的输入中，即可连接
**取消连接**： 在被输入的端点，点击后鼠标左键拖拽输入，即可取消连接，或者通过连线的中点菜单来取消连接。

## 节点的外观

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=56f3531dfd593a0e01a80dd4c472dcc0" alt="节点外观" data-og-width="1261" width="1261" data-og-height="896" height="896" data-path="images/zh/core-concept/node/node.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4701f577ea39c832af15aa31f2ad872c 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=35389e98d34f2efc1c0793a6b465782c 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=14aa370e9612764e978a608d1a269fa4 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7449004397d162b9aec32ced64d33d51 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3c7cac8e156f31f8e3f1b32f94e89182 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7ec974980daaa9b95ffc87de59395087 2500w" />

我们为提供了多种样式设置，你可以根据你的需求来设置节点的外观:

* 修改样式
* 双击节点标题修改节点名称
* 通过拖拽节点任意角来缩放节点尺寸

<video controls className="w-full aspect-video" src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_appearance.mp4?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2fb1ff4aac3396cb3e4ecbebd8db7b14" data-path="images/concepts/node/node_appearance.mp4" />

### 节点标签 Badges

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1e22b62c50745c547e2b99c5f13df990" alt="节点标签" data-og-width="1207" width="1207" data-og-height="606" height="606" data-path="images/concepts/node/badge.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5725996ab758f6ca7476c8bc3c68b58a 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=dec77789c181bb56a23c8d8ede919ced 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=fc1a4671387cc7ffceb4ae130f543dac 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=cb938d3aebd43c9d9db64ec629d07781 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4dfa69ff4270496cacc3a9843d4fc841 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=17a8ec9f470311a50cbcd2c0bfa36ac1 2500w" />

我们提供了多个节点标签（Badges）的显示功能，比如：

* 节点ID
* 节点来源

目前 **Comfy Core 节点** 采用小狐狸的图标来展示，自定义节点则采用其名称，这样你可以快速了解到对应节点是来自哪个节点包。

你可以在菜单中设置对应的显示：

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/badge_setting.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e07d5c2dab21f3bf17b50d2828bee535" alt="标签设置" data-og-width="1500" width="1500" data-og-height="586" height="586" data-path="images/zh/core-concept/node/badge_setting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/badge_setting.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=067219a6d51aa354e81d97a77938f853 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/badge_setting.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=42c161a582832b3cdeb02479671c3024 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/badge_setting.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=9e3f79ee1249db9eb584bf4409359a87 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/badge_setting.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=805d98f98077b7b3c108b5477b9e2007 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/badge_setting.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1ec52007366c2ef49ec5e2d11e19f89d 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/badge_setting.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=658cfc718fbba2abb3b0c14df61a8a01 2500w" />

## 节点上下文菜单

节点的上下文菜单主要分为两种

* 针对节点本身的上下文菜单
* 针对输入 / 输出的上下文菜单

### 节点的上下文菜单

通过在节点上点击鼠标右键，你可以展开对应的节点上下文菜单，下面是对应的菜单截图：
<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/context_menus_1.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1771deeaece0fe19259c1ba75e53f63f" alt="节点上下文菜单" data-og-width="2000" width="2000" data-og-height="1930" height="1930" data-path="images/zh/core-concept/node/context_menus_1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/context_menus_1.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6b5dda61205eb12ac8508ed6946afd05 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/context_menus_1.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3618a67f0dec7f7fd998aadddb45a2c3 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/context_menus_1.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ac91c32254af024ecfdc4194045ce41c 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/context_menus_1.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=571503cede792fd33a4b0b62ebf86e99 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/context_menus_1.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3effb9b147e916171526b43d9f9bdefb 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/context_menus_1.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0681557d5f681c9ad9ccf02447acf46c 2500w" />

在节点的右键上下文菜单中你可以

* 调整节点的颜色样式
* 修改标题
* 克隆、复制、删除节点
* 设置节点的模式

在这个菜单中，除了外观相关的设置比较重要的是下面的菜单操作

* **模式（Mode）**： 设置节点的模式，Always、Never、绕过（Bypass）

#### 模式（Mode）

对于模式，你可能注意到目前我们提供了：Always、Never、On Event、On Trigger 四种模式，但实际上只有 **Always** 和 **Never** 是有效的，**On Event** 和 **On Trigger** 实际上是无效的，目前我们尚未完全实现这个功能，另外你可以把 **绕过（Bypass）** 也理解为一种模式，下面是对于几种可用模式的解释

* **Always**： 节点默认模式，当节点首次运行或者自上一次执行后，对应输入有变化对应节点都会执行
* **Never**： 节点在任何情况下都不会执行，就像节点被删除了，后续节点无法读取接收到任何来自它的数据
* **绕过（Bypass）**： 节点在任何情况下都不会执行，但是后续的节点仍旧可以试着获取到未经这个节点的处理的数据

下面是对于 `Never` 和 `Bypass` 模式的对比：

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7024037e0a22285a21484d102dae0f0c" alt="Never 和 Bypass 模式" data-og-width="3000" width="3000" data-og-height="1092" height="1092" data-path="images/concepts/node/never_vs_bypass.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=6344fa2d9cd016f427b02c74e1cf1740 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ea96796a2e23fef29363b065df5a16a9 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=aba3e1a0b57114dd729dc8c96e0adb05 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=fb4dd9dd8030ce2f4e789056955beaac 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=011c5d6f09f51e031c53488b0580db07 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5a6a4976bfd7ee42816e6d8b852c9274 2500w" />

在这个对比的例子中，你可以看到，两个工作流都是同时应用了两个 LoRA 模型，差异在于其中一个`Load LoRA` 节点被设置为 `Never` 模式而另一个被设置为`Bypass` 模式。

* 被设置为 `Never` 模式的节点，后续的节点由于接收不到任何的输入数据而出现了报错
* 被设置为 `Bypass` 模式的节点，后续的节点仍旧可以获取到未经这个节点处理的数据，从而加载了第一个`Load LoRA` 节点的输出数据，所以后续的工作流依旧可以正常运行

### 输入 / 输出的上下文菜单

这里上下文菜单主要和对应输入输出的数据类型相关

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2daf16654cdd151a6b9ace6ef9d9e530" alt="节点输入输出上下文菜单" data-og-width="1774" width="1774" data-og-height="910" height="910" data-path="images/concepts/node/context_menus_2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=21205850f45887caf0f440de0aef9e19 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a7037a646b1abadb3a8a03cf99b57f53 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0cfefc04ce317796d93a1d9c52f00d27 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0c92cbeef4b1beabd4105cd0872a3ae0 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=34f6d22e3d1dcb60697ccd4b811e3687 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ece7fca06a344e909a62444d253abfa2 2500w" />

在拖动节点的输入 / 输出的时候，当有连线出现，但你未连接到其它节点的输入或输出的时候，此时释放鼠标则会弹出针对输入 / 输出的上下文菜单，用于快速添加相关类型的节点。
你可以在设置中调整对应的节点建议的数量

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node_suggestions.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2faa8c0bf083a23ecefe93222c900c07" alt="节点建议数量" data-og-width="1000" width="1000" data-og-height="314" height="314" data-path="images/zh/core-concept/node/node_suggestions.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node_suggestions.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6cf828109015a55e8f114fa3d25e3e22 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node_suggestions.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=150ad0c9d9778e284b17c02e58ea76c2 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node_suggestions.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1844169f5e595a802f8d0d38bafe3118 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node_suggestions.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=29a52358f287ec4b72c09a89c9b69b5e 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node_suggestions.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5264b38cd663d65be29fad37de17375f 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/node_suggestions.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3ffd418d3b3e357dad0860d786b76d6d 2500w" />

## 节点选择工具箱

<video controls className="w-full aspect-video" src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/selection_toolbox.mp4?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f2a55de5682187a2e9e012120b968c95" data-path="images/concepts/node/selection_toolbox.mp4" />

**节点选择工具箱（Selection tool box）** 是一个为节点提供快速操作的一个浮层工具，当你选中一个节点的时候，它会悬浮在选中的节点上方，通过这个节点你可以：

* 修改节点的颜色
* 快速设置节点为 Bypass 模式(在运行时候不执行)
* 固定节点
* 删除节点

当然，这些功能在对应节点的右键菜单中也可以找到，节点选择工具箱只是提供了一个快捷操作，如果你想要关闭这个功能，可以在设置中关闭。

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/setting_selection_toolbox.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=cd6e45bb12ab11134bc13b6cc65187d3" alt="关闭节点选择工具箱" data-og-width="1067" width="1067" data-og-height="267" height="267" data-path="images/zh/core-concept/node/setting_selection_toolbox.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/setting_selection_toolbox.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=602ad9ea38f1163f9a1a639457766e2d 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/setting_selection_toolbox.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5c1c197181ee8e38299948407be0ee84 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/setting_selection_toolbox.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e5f8f45b8e9f394dc683eae069cfabdf 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/setting_selection_toolbox.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=52d708872206f82a247f36845412387a 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/setting_selection_toolbox.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e707305d4557a59486e73494e5f69a7b 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/core-concept/node/setting_selection_toolbox.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7fe3d8421282a5eebc82316e9dad76c5 2500w" />

## 节点组

在 ComfyUI 中，你可以将一个工具流的部分，同时选用，再使用右键菜单将它们合并成一个节点组，使得对应的部分可以成为一个可复用的模块，从而在你的 ComfyUI 中进行重复调用
