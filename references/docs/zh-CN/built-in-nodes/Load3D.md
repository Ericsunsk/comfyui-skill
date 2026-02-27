> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 加载3D - ComfyUI内置节点文档

> Load3D 节点是 ComfyUI 中用于加载和预览多种 3D 模型文件的核心节点，支持多格式导入与丰富的三维视图操作。

Load3D 节点用于加载和处理 3D 模型文件的核心节点，在加载节点时会自动获取  ` ComfyUI/input/3d/`  可用的 3D 资源，你也可以通过上传功能将受支持的 3D 文件上传然后进行预览。

**支持格式**
目前该节点支持多种 3D 文件格式，包括 `.gltf`、`.glb`、`.obj`、`.fbx` 和 `.stl`。

**3D 节点预设**
3D 节点的一些相关偏好设置可以在 ComfyUI 的设置菜单中进行设置，请参考下面的文档了解对应的设置
[设置菜单 - 3D](/zh-CN/interface/settings/3d)

除了常规的节点输出之外， Load3D 有许多相关的 3D 视图相关操作是位于预览区域菜单, 3D 节点

## 输入

| 参数名  | 类型   | 描述                                              | 默认值  | 范围      |
| ---- | ---- | ----------------------------------------------- | ---- | ------- |
| 模型文件 | 文件选择 | 3D 模型文件路径，支持上传，默认读取 ` ComfyUI/input/3d/` 下的模型文件 | -    | 受支持格式文件 |
| 宽度   | INT  | 画布渲染宽度                                          | 1024 | 1-4096  |
| 高度   | INT  | 画布渲染高度                                          | 1024 | 1-4096  |

## 输出

| 参数名称             | 数据类型           | 说明                                         |
| ---------------- | -------------- | ------------------------------------------ |
| image            | IMAGE          | 画布渲染渲染图像                                   |
| mask             | MASK           | 包含当前模型位置的遮罩                                |
| mesh\_path       | STRING         | 模型文件路径在`ComfyUI/input` 文件夹下的路径             |
| normal           | IMAGE          | 法线贴图                                       |
| lineart          | IMAGE          | 线稿图像输出，对应的 `edge_threshold` 可在画布的模型菜单中进行调节 |
| camera\_info     | LOAD3D\_CAMERA | 相机信息                                       |
| recording\_video | VIDEO          | 录制视频（仅当有录制视频存在时）                           |

对应所有的输出预览如下：
<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a8b0622a7e96c8085692046f539218fa" alt="视图操作演示" data-og-width="2594" width="2594" data-og-height="1272" height="1272" data-path="images/comfy_core/load3d/load3d_outputs.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4bb4a98f81496ee779d5b2610198fc93 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7919d0d4724666101b4110eabab747e7 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ced77b204c999954bb4b5d560eddd86c 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cee88e3a213c56013ba08f5e1966fc9c 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=34658b0f24f5935e241bda5f43b3bc6c 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=59c9883857d9fda02988144a7585ac57 2500w" />

## 模型画布(Canvas)区说明

Load 3D 节点的 Canvas 区域包含了诸多的视图操作，包括：

* 预览视图设置（网格、背景色、预览视图）
* 相机控制: 控制FOV、相机类型
* 全局光照强度: 调节光照强度
* 视频录制: 录制视频并导出视频
* 模型导出: 支持`GLB`、`OBJ`、`STL` 格式
* 等

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=79fb8f464bc62086be17f0082625d0b8" alt="Load 3D 节点UI" data-og-width="2025" width="2025" data-og-height="1696" height="1696" data-path="images/comfy_core/load3d/load3d_ui.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=880997a87fa95cf38bdb5cf6be494bb5 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f558829882997fb902ee37cd7f3f7887 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e1d5bee3c3c31905fd034e4622da5513 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7cc603401811185c9af72d869a3fe4ea 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=53532669e02277f4b94c1ceab595e8e0 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=82c8743cc193239ab5de05254cb345a7 2500w" />

1. 包含了 Load 3D 节点的多个菜单以及隐藏菜单
2. 重新`缩放预览窗口大小`以及进行`画布视频录制`菜单
3. 3D 视图操作轴
4. 预览缩略图
5. 预览尺寸设置，通过设置尺寸然后再缩放窗口大小来缩放预览视图显示

### 1. 视图操作

<video controls muted loop playsInline className="w-full aspect-video rounded-xl" src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/view_operations.mp4?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=651f1cf60f5868704e03b4fb0c773761" data-path="images/comfy_core/load3d/view_operations.mp4" />

视图控制操作：

* 鼠标左键点击 + 拖拽： 视图旋转控制
* 鼠标右键 + 拖拽： 平移视图
* 鼠标中键： 缩放控制
* 坐标轴： 切换视图

### 2. 左侧菜单功能

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f6e11c260b9c3f3aad82e82eded36030" alt="Menu" data-og-width="1184" width="1184" data-og-height="1582" height="1582" data-path="images/comfy_core/load3d/menu.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8c0168da03202fbb8a053c03343d1941 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b9b245f4cd95892cbb1ffeea5563e918 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7d8c70ed6b986745ce20c3507d61e8c8 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5a70ad2f39ea37f90a6eb1848e15b4e8 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=07c6fc74935556b0db9e8bfdc2caa932 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=71d2e2694e536e89e585e2c567841588 2500w" />

在预览区域，有些视图操作相关的菜单被隐藏在了菜单里，点击菜单按钮可以展开对应不同的菜单

* 1. 场景（Scene）: 包含预览窗口网格、背景色、缩略图设置
* 2. 模型（Model）: 模型渲染模式、纹理材质、上方向设置
* 3. 摄像机（Camera）: 轴测视图和透视视图切换、透视视角大小设置
* 4. 灯光（Light）: 场景全局光照强度
* 5. 导出（Export）: 导出模型为其它格式（GLB、OBJ、STL）

#### 场景（Scene）

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=065dcbc017397af3fc9393cf07d45735" alt="scene menu" data-og-width="1671" width="1671" data-og-height="1106" height="1106" data-path="images/comfy_core/load3d/menu_scene.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a870f6f996d5a2845ebd501b3c174a4f 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=01c5802e199086069ecedeb52128f490 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f4c68255bc6da4f5ccab382848cb5c09 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6219802420efaa01fc709bea116d7d3c 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e434ccef5e3756ccb614a45e42c2c6ca 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=838be02caf4d19fda9e1384ad51dab86 2500w" />

场景菜单提供了对场景的一些基础设置功能

1. 显示 / 隐藏网格
2. 设置背景色
3. 点击上传设置背景图片
4. 隐藏预览图

#### 模型(Model)

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5abbf34a279bffcb89bccaaeec4dc0d5" alt="Menu_Scene" data-og-width="3605" width="3605" data-og-height="1911" height="1911" data-path="images/comfy_core/load3d/menu_model.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b6958b73e23adbdf99f588b5671f0c4f 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=79541430c16eec94141e3256beb4c3c9 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c49e84eab6fe15c0f761442981ef4290 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=163d7d04d19ff8b7388d4fb60151cbc5 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=74443cf59c5cc8147b41ac9713e6a6e9 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a2654354b3c42b4c99f0781becfefe34 2500w" />

模型菜单提供了一些模型的相关功能

1. **上方向(Up direction)**: 确定模型的哪个轴为上方向
2. **渲染模式（Material mode）**: 模型渲染模式切换 原始（Original）、法线(Normal)、线框(Wireframe)、线稿(Lineart)

#### 摄像机（Camera）

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=41698c4ccc2a711dcd1d6b78788c2f57" alt="menu_modelmenu_camera" data-og-width="1729" width="1729" data-og-height="1434" height="1434" data-path="images/comfy_core/load3d/menu_camera.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5bb365052ce2cf4bc79092371649e34c 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=46c0ec016c2e6525a57ba95036e0908a 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c4286312edf6752b6e99f84fbbb95350 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=32427a62fd4f48503cb03a7b652277c4 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=31ea7b4e7e32afd99768fee63d544108 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=65e8d80228a737f616b1a75a6da49e48 2500w" />

该菜单提供了轴测视图和透视视图切换、透视视角大小设置

1. **相机（Camera）**: 在轴测视图和正交视图之间快速切换
2. **视场角(FOV)**: 调整 FOV 视角角度

#### 灯光（Light）

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ffd6bd85f4dd12d35626e2d2799b7944" alt="menu_modelmenu_camera" data-og-width="1729" width="1729" data-og-height="740" height="740" data-path="images/comfy_core/load3d/menu_light.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e6435fd6a500cf11f8e65e4aa59ef91b 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=198ef3ba79e99d7a7f377af1b62547ba 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=32984b4552fa350394b2cf03eda60b7c 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e6211fa0ed56e3b79974892ff47403be 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ee103a6ae3351eac002024aea2d7ecc3 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3d3a86bd5e2f40ab36741d90afe421b0 2500w" />

通过该菜单可以快速调节模型场景的全局光照强度

#### 导出（Export）

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=fc2488b6681e8269f7d9eac8ce8123b5" alt="menu_export" data-og-width="1729" width="1729" data-og-height="740" height="740" data-path="images/comfy_core/load3d/menu_export.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e275701e81e42ed77d1aec794db7bb3b 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7d36035e06c25b62ef319738c92ab670 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1ef633b32843162d27464b90cecc7682 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=336cf22bbd01b35c6df1206f9a0ce230 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ad9838e8a2b1ed8422980ffd6416ce29 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=264cdfde8395392952100e468536a12d 2500w" />

该菜单提供了一个快速转换模型格式并导出的能力

### 3. 右侧菜单功能

<video controls muted loop playsInline className="w-full aspect-video rounded-xl" src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/recording.mp4?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4a5ed3f8ebba73beb99e7f86bd35c71e" data-path="images/comfy_core/load3d/recording.mp4" />

右侧菜单的两个主要功能为：

1. **重设视图比例**： 点击按钮后视图将根据设定好的宽高按比例调整画布渲染区域比例
2. **视频录制**： 允许你将当前的 3D 视图操作录制为视频，允许导入，并可以作为 `recording_video` 输出给后续节点
