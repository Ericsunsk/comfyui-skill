> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 图像放大工作流

> 本篇将引导了解 AI 绘图中，放大图片的概念，并在 ComfyUI 中完成放大图片工作流生成

## 什么是图像放大

图像放大（Image Upscaling）是通过算法将低分辨率图像转换为高分辨率图像的过程。与传统插值放大不同，AI 放大模型（如 ESRGAN）能智能重建细节，保持图像质量。
比如默认通过 SD1.5 模型对于大尺寸的图片生成表现不佳，如果需要高分辨率，我们通常会先生成小尺寸的图像，然后使用图像放大来提升图片的分辨率。

当然本文介绍的只是诸多 ComfyUI 中图像放大方法中的一种，在这篇讲解中，我们将带你完成以下内容：

* 下载并安装放大模型
* 使用放大模型进行一次简单的放大
* 结合文生图工作流，完成图像的放大

<Note>
  想了解更多高级放大选项？请查看我们的综合[图像放大指南](/zh-CN/tutorials/utility/image-upscale)，涵盖各种模型和使用场景，包括人像增强、产品摄影等。
</Note>

## 下载并安装放大模型

额外需要下载 ESRGAN 等放大模型（必须）：

<Steps>
  <Step title="访问 OpenModelDB">
    访问 [OpenModelDB](https://openmodeldb.info/) 搜索下载需要的放大模型（如 RealESRGAN）

        <img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e5a63a5efe9b72af78d7331179cef6ba" alt="openmodeldb" data-og-width="1200" width="1200" data-og-height="1209" height="1209" data-path="images/tutorial/basic/upscale/upscale_OpenModelDB.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ed2e223f6fdf3841a3268e3925c214ca 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e5a012d3e1827c0033d192b40e2657a7 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f0a8e3b96e3812e0bc4382fe006e04ff 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f04936c9b6c0215a784cb29d11e68b3d 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b9220bb51a7b9f2fc281b3ec66a6777a 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_OpenModelDB.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=afc0f1083e090bf02b462353ff7f3f64 2500w" />

    如图所示：

    1. 你可以在筛选处根据你的图像类型选来过滤对应的模型类型
    2. 对应模型右上角会有标注具体放大的倍数，比如在我们提供的截图里，对应的这个模型是将图像放大2倍的模型

    本篇教程中我们将使用 [4x-ESRGAN](https://openmodeldb.info/models/4x-ESRGAN) 模型，点击进入详情页，点击 `Download` 下载模型

    ![OpenModelDB\_download](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/upscale_workflow.png)
  </Step>

  <Step title="将模型文件放入指定目录">
    将模型文件（.pth）放入 `ComfyUI\models\upscale_models` 目录
  </Step>
</Steps>

## 简单放大工作流

### 1. 工作流及素材

请下载下面的图片，并拖入到 ComfyUI 中，加载简单版本放大工作流
![放大工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/upscale_workflow.png)

请下载下面这张小尺寸的图片作为输入
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ce8c5f3cd94c0cbde5ded50f09204d5b" alt="Upscale-input" data-og-width="512" width="512" data-og-height="512" height="512" data-path="images/tutorial/basic/upscale/upscale-input.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1babcd7fcdcb1f3b2cc953c79f237753 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6d8772a8c139cb4aa8f8554855552b1e 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a331ba6e2e35bef944d672990a9f39ce 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=af8cd385a69e8c69d4a9166cfb0056c9 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=2c79e1219e9af3bed8c72cc5a79caca6 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale-input.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6ec8647f560daf3c2fe61670edc8fbca 2500w" />

### 2. 工作流讲解

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=632d1202982e8e7c59974a4152304967" alt="放大工作流" data-og-width="2136" width="2136" data-og-height="1192" height="1192" data-path="images/tutorial/basic/upscale/upscale_simple_workflow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=90de763eac7f4f322269592af72d6328 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=edd7e70f7b9f80178b08b3984b7c3eec 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3c3000421314917ba8de3b74b754b15d 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6f53afad6d2ed56c155aa57d5ea9083e 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=252e00d8d5f0b8f48554c4f9bf3a8b5b 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/upscale_simple_workflow.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f48238be1a23ac57b5f766cdadf8dcd2 2500w" />

1. 在`加载放大模型(Load Upscale Model)`节点中选择我们之前下载的放大模型
2. 在`加载图片(Load Image)`节点中选择我们之前准备的输入图片
3. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl + Enter(回车)` 来执行图片生成

通过以上步骤，我们就可以完成一个图片的放大，你可以看到在这个工作流中，核心主要在于 `Load Upscale Model` 和 `Upscale Image(Using Model)` 的组合，他们通过接收一个图像的输入，然后使用放大模型将图像放大。

## 结合文生图的放大工作流

在完成了简单的放大工作流后，我们就可以尝试结合[文生图](/zh-CN/tutorials/basic/text-to-image)的工作流来完成一个完整放大工作的流程，关于文生图的基础部分及相关模型要求，请参考[文生图](/zh-CN/tutorials/basic/text-to-image)的部分的说明完成。

请将下面的图片下载并保存后拖入到 ComfyUI 中，加载结合文生图的放大工作流
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=98c8d536f0a76025092f8fec157002f8" alt="结合文生图的放大工作流" data-og-width="2533" width="2533" data-og-height="941" height="941" data-path="images/tutorial/basic/upscale/esrgan_example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=13fc9ef8db862b4c5b60289c5fe256ef 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4b8d819e10d503a630e98b092944c1f5 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b2dff912bcc2413b84f9d43fe88c1093 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=99dae3b712b3ad7b1b9cfa7d71db947d 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f128f8649d0fc1d8f9bbd6e36fb49a3e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/upscale/esrgan_example.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=6f130e45a1bcd061fe4e4bc21301e1dc 2500w" />

你可以看到在这个工作流里，就是在文生图工作流之后把对应的图片输入到放大工作流中完成了对应图片的放大。

## 其它相关补充

<Tip>
  不同放大模型特性：

  * **RealESRGAN**: 通用型放大，适合大多数场景
  * **BSRGAN**: 擅长处理文字和锐利边缘
  * **SwinIR**: 保持自然纹理，适合风景照片
</Tip>

1. **链式放大**：对于需要超高倍率放大的情况，可以串联多个放大节点（如先2x再4x）
2. **混合放大**：在生成工作流后接放大节点，实现"生成+增强"一体化流程
3. **对比测试**：不同模型对特定类型图片效果差异较大，建议同时测试多个模型
