> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 图生图工作流

> 本篇将引导了解并完成图生图工作流

## 什么是图生图

图生图（Image to Image）是 ComfyUI 中的一种工作流，它允许用户将一张图像作为输入，并生成一张新的图像。

图生图可以使用在以下场景中：

* 原始图像风格的转换，如把写实照片转为艺术风格
* 将线稿图像转换为写实图像
* 图像的修复
* 老照片着色
* ... 等其它场景

用一个比喻来讲解的话，大概是这样：
你需要画家根据你的参考图片，画出符合你要求特定效果的作品。

如果你仔细比对本篇教程和[文生图](/zh-CN/tutorials/basic/text-to-image)教程，你会发现图生图的流程和文生图的流程非常相似，只是多了个输入的参考图片作为输入条件，也就是在文生图中，我们是让画家（绘图模型）根据我们的提示词生成自由发挥，而在图生图中，我们是让画家（绘图模型）根据我们的参考图片和提示词生成图片。

## ComfyUI 图生图工作流示例讲解

### 1. 模型安装

请确保你已经在 `ComfyUI/models/checkpoints` 文件夹至少有一个 SD1.5 的模型文件，如果你还不了解如何安装模型，请参[开始 ComfyUI 的 AI 绘图之旅](/zh-CN/get_started/first_generation#3-安装绘图模型)章节中关于模型安装的部分说明。

你可以使用下面的这些模型：

* [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors)
* [Dreamshaper 8](https://civitai.com/models/4384?modelVersionId=128713)
* [Anything V5](https://civitai.com/models/9409?modelVersionId=30163)

### 2. 图生图工作流相关文件

保存并下载下面的图片到本地，然后 **拖拽或使用 ComfyUI 打开** 它，就会加载对应的工作流

![图生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image_to_image/workflow.png)

或在 ComfyUI 的 **workflow template** 中加载 **image to image** 工作流
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/image-to-image-01-template.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a664948a124db94816228b64456459db" alt="ComfyUI 工作流模板 - 图生图" data-og-width="972" width="972" data-og-height="662" height="662" data-path="images/tutorial/basic/image-to-image-01-template.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/image-to-image-01-template.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ce2bc6bfbe2812cc3a54938b45325c44 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/image-to-image-01-template.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=514e66bb85e8d50eee2b773e000d0276 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/image-to-image-01-template.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a43ac8bf80d8e95389b3960c9835724e 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/image-to-image-01-template.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=52a599f1da47d09621e51bfad86e6244 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/image-to-image-01-template.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=cd5082883a5b71fdef4f8dc1371df030 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/image-to-image-01-template.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=68627cef449d33714b353e3e37fe6dc7 2500w" />

下载下面的图片作为使用示例，我们会在后面的步骤中使用它
<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f8d1c4f2afa4a80f07a6ad862506c832" alt="图片示例" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/basic/img2img/input.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=2cf62d99d9595053f961e18bbae104fa 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=25ee69405b3bb78b8ad9fffa930324ec 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=96d0a0acd6f76c4b3d547f5911dd2888 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=54694dfd7f86ad5d13363b8123ed95cb 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7dcb3f779c1a36505bde2f7f50828ea3 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/input.jpeg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=fa0782cbc1a84bc318679384cbbb0873 2500w" />

### 3. 开始图生图工作流

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=dd85418c3e8070eb5c3f491a89fd29b3" alt="ComfyUI 图生图工作流 - 步骤" data-og-width="1197" width="1197" data-og-height="779" height="779" data-path="images/tutorial/basic/img2img/image-to-image-02-guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1b0cc094853876eb09edcd81575f3171 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4630801bea3f11270b97b29cfcc77bea 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4935b3f629d63f2bf0c8a79fa864eb16 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ba9c51655e26715be1b316c307c3a761 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=90406adf554c73a31ffe9b86cfea06ed 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/img2img/image-to-image-02-guide.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=d813a71613511b97258f4b01317f565a 2500w" />

在加载图生图工作流后，请对照图片，按照序号完成以下操作，完成示例工作流的生成

1. 在 **Load Checkpoint** 节点中加载好你本地的绘图模型
2. 在 **Load Image** 节点点击 `upload` 按钮，上传准备步骤中提供的图片
3. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl + Enter(回车)` 来执行图片生成

## 开始你自己的尝试

1. 试着修改 **KSampler** 节点中的 `denoise` 参数，逐渐从 1 到 0 变化，观察生成图片的变化
2. 更换你自己的提示词和参考图片，生成属于你自己的图片效果

## 图生图工作流核心要点

图生图工作流的核心在于在于 `KSampler` 节点中的 `denoise` 参数要是 **小于 1**

如果你调整过 `denoise` 参数，进行生成后会发现：

* `denoise` 越小，生成图片和参考图片的差异就会越小，
* `denoise` 越大，生成图片和参考图片的差异就会越大。

因为 `denoise` 决定了对应图片转换为潜空间图像后，向潜在空间图像添加的噪声强度，如果 `denoise` 为 1，对应潜空间图像就会变成一个完全随机的噪声，那这样就和`empty latent image`节点生成的潜在空间一样了，就会丢失参考图片的所有特征。

对应原理可以参考[文生图](/zh-CN/tutorials/basic/text-to-image)教程中的原理讲解。
