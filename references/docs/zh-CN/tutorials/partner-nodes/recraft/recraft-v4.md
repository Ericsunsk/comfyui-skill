> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft V4 图像与矢量生成教程

> 在 ComfyUI 中使用 Recraft V4 生成专业图像和可用于生产的矢量图

Recraft V4 是一款专为专业设计工作打造的全新图像生成模型。它与设计师合作开发，针对构图、光线、色彩关系和材质真实感进行了优化。

<Tip>
  使用 API 节点需要保证你已经正常登录，并在受许可的网络环境下使用，请参考[API 节点总览](/zh-CN/tutorials/partner-nodes/overview)部分文档来了解使用 API 节点的具体使用要求。
</Tip>

<Tip>
  <Tabs>
    <Tab title="便携版或手动安装用户">
      请确保你的 ComfyUI 已经更新。

      * [ComfyUI 下载](https://www.comfy.org/download)
      * [ComfyUI 更新教程](/zh-CN/installation/update_comfyui)

      本指南里的工作流可以在 ComfyUI 的[工作流模板](/zh-CN/interface/features/template)中找到。如果找不到，可能是 ComfyUI 没有更新。

      如果加载工作流时有节点缺失，可能原因有：

      1. 你用的不是最新开发版（nightly）。
      2. 你用的是稳定版或桌面版（没有包含最新的更新）。
      3. 启动时有些节点导入失败。
    </Tab>

    <Tab title="桌面版或云端用户">
      * 桌面版是基于 ComfyUI 稳定版本构建的，它会在有新的桌面稳定版本发布时自动更新。
      * [Cloud](https://cloud.comfy.org) 会在 ComfyUI 稳定版本发布后更新，我们会同步更新 Cloud。

      所以，如果你发现本教程中有任何核心节点缺失，那是因为对应的节点支持还在开发中没有发布正式的稳定版，请等待下一个稳定版本发布。
    </Tab>
  </Tabs>
</Tip>

## V4 新特性

* **光栅 + 矢量一体化模型** — 同一模型可生成逼真照片、风格化插画和可用于生产的 SVG
* **更好的细节** — 更清晰的纹理、更准确的光线、更紧凑的几何结构，在复杂场景中表现出色
* **人脸和人体结构精准** — 可靠的比例和表情，即使在多主体或动作姿势中也能保持
* **文本渲染** — 可生成清晰可读的文字，适用于标牌、包装、信息图表，能很好地处理短句和中长句
* **SVG 输出** — 可编辑的矢量图形，线条清晰，色彩分割合理。这是生产级质量的矢量输出
* **提示词准确性** — 严格遵循详细的创意指导，包括空间关系、材质和反射
* **V4 Pro** — 相同模型，更高分辨率。输出 2048×2048，适用于印刷和大幅面作品

## Recraft V4 文本到图像工作流

<CardGroup cols={2}>
  <Card title="在 Comfy Cloud 运行" icon="cloud" href="https://cloud.comfy.org/?template=api_recraft_v4_t2i&utm_source=docs&utm_medium=referral&utm_campaign=recraft_v4">
    在 Comfy Cloud 中打开
  </Card>

  <Card title="下载工作流" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_v4_t2i.json">
    下载 JSON 或在模板库中搜索 "Recraft V4 Text to Image"
  </Card>
</CardGroup>

### 运行工作流步骤

1. (可选) 修改 `Recraft Style` 节点来控制图像的视觉风格
2. (可选) 修改 `Recraft Text to Image` 节点中的 `prompt` 参数
3. (可选) 修改 `size` 参数来改变输出尺寸
4. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图像的生成
5. 等待 API 返回结果后，你可在 `Save Image` 节点中查看生成的图像

### 图像展示

![街拍示例](https://substack-post-media.s3.amazonaws.com/public/images/9fe39ca3-b0ba-4f26-aa26-b3eaa11185de_1792x1024.png)
*全身街拍编辑照片，一位年轻人穿着超大号复古 Fear of God 法兰绒，内搭褪色的 Pyrex Vision 连帽衫，破洞阔腿牛仔裤，原版 Just Don 蟒蛇皮帽檐棒球帽，以及破旧的 Nike Dunk Lows。在布鲁克林粗犷的人行道上拍摄，黄金时段，35mm 胶片颗粒。*

![潮流编辑风格](https://substack-post-media.s3.amazonaws.com/public/images/9fd968f1-f5f9-42a9-973d-74bd163babde_2560x1664.png)
*全身穿搭照：电光蓝和珊瑚色迷彩连帽衫，配套迷彩慢跑裤，白色 G-Shock 手表，哑光黑科技风斜挎背心包，以及奶油色 New Balance 550。混凝土停车场背景，头顶刺眼的荧光灯投下锐利的阴影。*

![动作镜头](https://substack-post-media.s3.amazonaws.com/public/images/a8643f80-8cc4-4246-a95a-bed1f9ee10f1_2560x1664.png)
*鱼眼镜头，从空泳池内部拍摄——一个穿着羊毛夹克和透明 PVC 外壳的人正在泳池边沿上方做踢翻板动作，滑板与脚分离，他的层叠穿搭随风展开，露出里面的冰球球衣。*

## Recraft V4 文本到矢量工作流

Recraft V4 可以直接生成可用于生产的 SVG 矢量输出。这对于 Logo、图标、品牌资产或任何需要缩放的内容非常有用。SVG 输出与 Illustrator、Figma 和 Sketch 兼容。

<CardGroup cols={2}>
  <Card title="在 Comfy Cloud 运行" icon="cloud" href="https://cloud.comfy.org/?template=api_recraft_v4_text_to_vector&utm_source=docs&utm_medium=referral&utm_campaign=recraft_v4">
    在 Comfy Cloud 中打开
  </Card>

  <Card title="下载工作流" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_v4_text_to_vector.json">
    下载 JSON 或在模板库中搜索 "Recraft V4 Text to Vector"
  </Card>
</CardGroup>

### 矢量展示

![屋顶插画](https://substack-post-media.s3.amazonaws.com/public/images/571c5214-5c7f-43f9-81c4-80cad1e5578b_1792x1024.png)
*一群朋友在日落时分躺在屋顶上，头顶是串灯，一个人在照料小烧烤架，另一个人在弹尤克里里，一只狗在冷藏箱旁的毯子上打盹——温暖、放松、复古的生活方式插画*

![音箱插画](https://substack-post-media.s3.amazonaws.com/public/images/748f04c7-50b9-433d-93cb-c619984c8e89_1792x1024.png)
*一个巨大的霓虹音箱正在播放音乐，闪电和声波从扬声器中爆发出来，融化的磁带在周围旋转，一副超大号耳机搭在上面——大胆、混乱、充满电力*

![小猫贴纸](https://substack-post-media.s3.amazonaws.com/public/images/3ddce7b4-8f37-4256-bd93-2e5796dfacca_1024x1024.png)
*可爱的小猫贴纸，小猫正在一台小小的笔记本电脑上使用 ComfyUI*

## 补充说明

* **Recraft Style**：提供多种预设风格，如真实照片、数字插画、Logo 设计等
* **Seed 参数**：仅用于确定节点是否应重新运行，实际生成结果与种子值无关
