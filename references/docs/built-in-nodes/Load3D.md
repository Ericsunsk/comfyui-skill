> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Load3D - ComfyUI Built-in Node Documentation

> The Load3D node is a core node in ComfyUI for loading and previewing various 3D model files, supporting multi-format import and rich three-dimensional view operations.

The Load3D node is a core node for loading and processing 3D model files. When loading the node, it automatically retrieves available 3D resources from `ComfyUI/input/3d/`. You can also upload supported 3D files for preview using the upload function.

**Supported Formats**
Currently, this node supports multiple 3D file formats, including `.gltf`, `.glb`, `.obj`, `.fbx`, and `.stl`.

**3D Node Preferences**
Some related preferences for 3D nodes can be configured in ComfyUI's settings menu. Please refer to the following documentation for corresponding settings:

[Settings Menu - 3D](/interface/settings/3d)

Besides regular node outputs, Load3D has lots of 3D view-related settings in the canvas menu.

## Inputs

| Parameter Name | Type           | Description                                                                                   | Default | Range             |
| -------------- | -------------- | --------------------------------------------------------------------------------------------- | ------- | ----------------- |
| model\_file    | File Selection | 3D model file path, supports upload, defaults to reading model files from `ComfyUI/input/3d/` | -       | Supported formats |
| width          | INT            | Canvas rendering width                                                                        | 1024    | 1-4096            |
| height         | INT            | Canvas rendering height                                                                       | 1024    | 1-4096            |

## Outputs

| Parameter Name   | Data Type      | Description                                                                                    |
| ---------------- | -------------- | ---------------------------------------------------------------------------------------------- |
| image            | IMAGE          | Canvas rendered image                                                                          |
| mask             | MASK           | Mask containing current model position                                                         |
| mesh\_path       | STRING         | Model file path                                                                                |
| normal           | IMAGE          | Normal map                                                                                     |
| lineart          | IMAGE          | Line art image output, corresponding `edge_threshold` can be adjusted in the canvas model menu |
| camera\_info     | LOAD3D\_CAMERA | Camera information                                                                             |
| recording\_video | VIDEO          | Recorded video (only when recording exists)                                                    |

All corresponding outputs preview
<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a8b0622a7e96c8085692046f539218fa" alt="View Operation Demo" data-og-width="2594" width="2594" data-og-height="1272" height="1272" data-path="images/comfy_core/load3d/load3d_outputs.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4bb4a98f81496ee779d5b2610198fc93 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7919d0d4724666101b4110eabab747e7 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ced77b204c999954bb4b5d560eddd86c 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cee88e3a213c56013ba08f5e1966fc9c 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=34658b0f24f5935e241bda5f43b3bc6c 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_outputs.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=59c9883857d9fda02988144a7585ac57 2500w" />

## Canvas Area Description

The Load3D node's Canvas area contains numerous view operations, including:

* Preview view settings (grid, background color, preview view)
* Camera control: Control FOV, camera type
* Global illumination intensity: Adjust lighting intensity
* Video recording: Record and export videos
* Model export: Supports `GLB`, `OBJ`, `STL` formats
* And more

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=79fb8f464bc62086be17f0082625d0b8" alt="Load 3D Node UI" data-og-width="2025" width="2025" data-og-height="1696" height="1696" data-path="images/comfy_core/load3d/load3d_ui.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=880997a87fa95cf38bdb5cf6be494bb5 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f558829882997fb902ee37cd7f3f7887 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e1d5bee3c3c31905fd034e4622da5513 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7cc603401811185c9af72d869a3fe4ea 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=53532669e02277f4b94c1ceab595e8e0 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/load3d_ui.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=82c8743cc193239ab5de05254cb345a7 2500w" />

1. Contains multiple menus and hidden menus of the Load 3D node
2. Menu for `resizing preview window` and `canvas video recording`
3. 3D view operation axis
4. Preview thumbnail
5. Preview size settings, scale preview view display by setting dimensions and then resizing window

### 1. View Operations

<video controls muted loop playsInline className="w-full aspect-video rounded-xl" src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/view_operations.mp4?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=651f1cf60f5868704e03b4fb0c773761" data-path="images/comfy_core/load3d/view_operations.mp4" />

View control operations:

* Left-click + drag: Rotate the view
* Right-click + drag: Pan the view
* Middle wheel scroll or middle-click + drag: Zoom in/out
* Coordinate axis: Switch views

### 2. Left Menu Functions

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f6e11c260b9c3f3aad82e82eded36030" alt="Menu" data-og-width="1184" width="1184" data-og-height="1582" height="1582" data-path="images/comfy_core/load3d/menu.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8c0168da03202fbb8a053c03343d1941 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b9b245f4cd95892cbb1ffeea5563e918 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7d8c70ed6b986745ce20c3507d61e8c8 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5a70ad2f39ea37f90a6eb1848e15b4e8 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=07c6fc74935556b0db9e8bfdc2caa932 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=71d2e2694e536e89e585e2c567841588 2500w" />

In the canvas, some settings are hidden in the menu. Click the menu button to expand different menus

* 1. Scene: Contains preview window grid, background color, preview settings
* 2. Model: Model rendering mode, texture materials, up direction settings
* 3. Camera: Switch between orthographic and perspective views, and set the perspective angle size
* 4. Light: Scene global illumination intensity
* 5. Export: Export model to other formats (GLB, OBJ, STL)

#### Scene

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=065dcbc017397af3fc9393cf07d45735" alt="scene menu" data-og-width="1671" width="1671" data-og-height="1106" height="1106" data-path="images/comfy_core/load3d/menu_scene.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a870f6f996d5a2845ebd501b3c174a4f 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=01c5802e199086069ecedeb52128f490 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f4c68255bc6da4f5ccab382848cb5c09 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6219802420efaa01fc709bea116d7d3c 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e434ccef5e3756ccb614a45e42c2c6ca 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_scene.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=838be02caf4d19fda9e1384ad51dab86 2500w" />

The Scene menu provides some basic scene setting functions

1. Show/Hide grid
2. Set background color
3. Click to upload a background image
4. Hide the preview

#### Model

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5abbf34a279bffcb89bccaaeec4dc0d5" alt="Menu_Scene" data-og-width="3605" width="3605" data-og-height="1911" height="1911" data-path="images/comfy_core/load3d/menu_model.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b6958b73e23adbdf99f588b5671f0c4f 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=79541430c16eec94141e3256beb4c3c9 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c49e84eab6fe15c0f761442981ef4290 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=163d7d04d19ff8b7388d4fb60151cbc5 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=74443cf59c5cc8147b41ac9713e6a6e9 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_model.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a2654354b3c42b4c99f0781becfefe34 2500w" />

The Model menu provides some model-related functions

1. **Up direction**: Determine which axis is the up direction for the model
2. **Material mode**: Switch model rendering modes - Original, Normal, Wireframe, Lineart

#### Camera

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=41698c4ccc2a711dcd1d6b78788c2f57" alt="menu_modelmenu_camera" data-og-width="1729" width="1729" data-og-height="1434" height="1434" data-path="images/comfy_core/load3d/menu_camera.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5bb365052ce2cf4bc79092371649e34c 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=46c0ec016c2e6525a57ba95036e0908a 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c4286312edf6752b6e99f84fbbb95350 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=32427a62fd4f48503cb03a7b652277c4 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=31ea7b4e7e32afd99768fee63d544108 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_camera.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=65e8d80228a737f616b1a75a6da49e48 2500w" />

This menu provides switching between orthographic and perspective views, and perspective angle size settings

1. **Camera**: Quickly switch between orthographic and orthographic views
2. **FOV**: Adjust FOV angle

#### Light

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ffd6bd85f4dd12d35626e2d2799b7944" alt="menu_modelmenu_camera" data-og-width="1729" width="1729" data-og-height="740" height="740" data-path="images/comfy_core/load3d/menu_light.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e6435fd6a500cf11f8e65e4aa59ef91b 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=198ef3ba79e99d7a7f377af1b62547ba 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=32984b4552fa350394b2cf03eda60b7c 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e6211fa0ed56e3b79974892ff47403be 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ee103a6ae3351eac002024aea2d7ecc3 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_light.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3d3a86bd5e2f40ab36741d90afe421b0 2500w" />

Through this menu, you can quickly adjust the scene's global illumination intensity

#### Export

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=fc2488b6681e8269f7d9eac8ce8123b5" alt="menu_export" data-og-width="1729" width="1729" data-og-height="740" height="740" data-path="images/comfy_core/load3d/menu_export.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e275701e81e42ed77d1aec794db7bb3b 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=7d36035e06c25b62ef319738c92ab670 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1ef633b32843162d27464b90cecc7682 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=336cf22bbd01b35c6df1206f9a0ce230 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ad9838e8a2b1ed8422980ffd6416ce29 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/menu_export.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=264cdfde8395392952100e468536a12d 2500w" />

This menu provides the ability to quickly convert and export model formats

### 3. Right Menu Functions

<video controls muted loop playsInline className="w-full aspect-video rounded-xl" src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/load3d/recording.mp4?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4a5ed3f8ebba73beb99e7f86bd35c71e" data-path="images/comfy_core/load3d/recording.mp4" />

The right menu has two main functions:

1. **Reset view ratio**: After clicking the button, the view will adjust the canvas rendering area ratio according to the set width and height
2. **Video recording**: Allows you to record current 3D view operations as video, allows import, and can be output as `recording_video` to subsequent nodes
