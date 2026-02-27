> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 自定义节点 CI/CD

## 简介

在对自定义节点进行更改时，在 Comfy 或其他自定义节点中出现问题并不罕见。在每种操作系统和不同的 Pytorch 配置上进行测试通常是不现实的。

### 使用 Github Actions 运行 Comfy 工作流

[Comfy-Action](https://github.com/Comfy-Org/comfy-action) 允许您在 Github Actions 上运行 Comfy workflow\.json 文件。它支持下载模型、自定义节点，并可在 Linux/Mac/Windows 上运行。

### 结果

输出文件会上传到 [CI/CD 仪表板](https://ci.comfy.org/)，可以在提交新更改或发布自定义节点的新版本之前作为最后一步查看。

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=443608968123247168b89b026ed2ae0e" alt="ComfyCI" data-og-width="2526" width="2526" data-og-height="1722" height="1722" data-path="images/comfyci.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=bf00166a6e417a12b3afce2a3b70caac 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8e6a0bfe6492622ae7c3b61c2946fb01 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4381e7cb42aa617fdfaf2f0f51abd09c 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=64dd33fa30c0810d93e6c4415e847d6d 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ac6ecc93ae6dfc064445e7ca61e8351c 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c458db2f48fa97f12f368c2adcd3de76 2500w" />
