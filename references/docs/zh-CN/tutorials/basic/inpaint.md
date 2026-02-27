> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 局部重绘工作流

> 本篇指南将带你了解 ComfyUI 中的局部重绘工作流，并带你完成一个局部重绘的示例，以及遮罩编辑器的使用等

本篇将引导了解 AI 绘图中，局部重绘的概念，并在 ComfyUI 中完成局部重绘工作流生成，我们将接触以下内容：

* 使用局部重绘工作流完成画面的修改
* 了解并使用 ComfyUI 中遮罩编辑器
* 了解相关节点 VAE Encoder (for Inpainting)

## 关于局部重绘

在 AI 图像生成过程中，我们常会遇到生成的画面整体较为满意，但是画面中存在一些不希望出现或者错误的元素，但是重新生成可能会生成另外一张完全不同的图片，所以这时候利用局部重绘来修复这部分的元素就非常有必要了。

这就像让 **画家(AI 绘图模型)** 画了一幅画，但是总是会有稍微有 **局部区域需要调整**，我们需要向画家说明**需要调整的区域(遮罩)**，然后让画家会根据我们的要求进行 **重新绘制(重绘)**。

局部重绘的场景包括：

* **瑕疵修复：** 消除照片中多余物体、错误的AI生成的画面的肢体等
* **细节优化：** 精准调整局部元素（如修改服装纹理、调整面部表情）
* 等其它场景

## ComfyUI 局部重绘工作流示例讲解

### 模型及相关素材准备

#### 1. 模型安装

下载下面的模型文件，并保存到`ComfyUI/models/checkpoints`目录下

* [512-inpainting-ema.safetensors](https://huggingface.co/Comfy-Org/stable_diffusion_2.1_repackaged/resolve/main/512-inpainting-ema.safetensors)

#### 2. 局部重绘素材

请下载下面的图片，我们将在这个示例中使用这个图片作为输入使用

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a6557da482429ba4feff636d36f1bb54" alt="ComfyUI局部重绘输入图片" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/basic/inpaint/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ab6da5c62e779df51cab0462652ae03b 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=89b7bba32e0e50aa5e0b14a1780f9f81 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c8a4c7369adda8b0e594c36c1253ad69 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a5e3e567978c89496e6b301e17889a40 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3f207a73f6d035e655d204467aa9a97f 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/input.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ff19842492f61b33b7c7b6bb7fe8a791 2500w" />

<Note>这张照片已经包含了 alpha 透明通道，所以并不需要你手动绘制蒙版，在本篇教程也会涉及如何使用遮罩编辑器来绘制蒙版的部分，我们会引导你一步步来完成整个局部重绘的过程</Note>

#### 3. 局部重绘工作流

下面这张图的 metadata 包含的对应的json工作流，请将其下载后 **拖入** ComfyUI 界面或者使用菜单 **工作流(Workflow)** --> **打开工作流(Open,快捷键 `Ctrl + O`)** 来加载这个局部重绘工作流

![ComfyUI局部重绘工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/sd1.5_inpaint.png)

### ComfyUI 局部重绘工作流示例讲解

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=eec79976ea5771763a00668de7c15bc3" alt="ComfyUI 局部重绘工作流" data-og-width="2000" width="2000" data-og-height="1108" height="1108" data-path="images/tutorial/basic/inpaint/inpaint_workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a6fdc071447c0798d9beb2ad963249c1 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=483c6cc059ba949df3d3ae302e904dfc 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=dae548fecc00b515bbf698f15457f760 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e4e471b6cd770836162c82a14c31590f 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=937ae7a877e2ad00b161f1489d599207 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_workflow.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=551b69ce8a2eb8e4f52ca448abb87366 2500w" />

请参照图片序号对照下面的提示完下操作：

1. 请确保已经加载了你所下载使用的模型
2. 请在在 `Load Image` 节点中加载局部重绘的素材
3. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl + Enter(回车)` 来执行图片生成

此外我们在这里可以对比一下，下图是使用[v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) 模型来进行 inpainting 的结果。

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=36916904f9884b5bc3c62f6b60ec17e8" alt="ComfyUI 局部重绘工作流 - SD1.5" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=793ae8991e483962785f4a1ebdc66931 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5f36ef651544636822ef6b910cf93a45 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b8f76ae73e41564f61668de75dd3784f 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e04c184d8e04180645be207d60754f2b 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b725d2042a4228df0f14498cfbb742a7 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_sd1.5_pruned_emaonly.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=07e4eaecd7725da7adb146d9a06e37d6 2500w" />

你会发现 [512-inpainting-ema.safetensors](https://huggingface.co/Comfy-Org/stable_diffusion_2.1_repackaged/resolve/main/512-inpainting-ema.safetensors) 模型生成的结果局部重绘的效果更好过渡更自然。
这因为这个模型是专为 inpainting 设计的模型，它可以帮助我们更好地控制生成区域，从而获得更好的局部重绘效果。

记得我们一直用的比喻吗？不同的模型就像能力不同的画家一样，但每个画家都有自己能力的上限，选择合适的模型可以让你的生成效果更好。

你可以进行下面的尝试来让画面达到你想要的效果:

1. 修改正向 、负向提示词，使用更具体的描述
2. 尝试多次运行，让 `KSampler` 使用不同的种子，从而带来不同的生成效果
3. 在了解本篇遮罩编辑器使用的部分后，对于生成的结果再次进行重绘以获得满意的结果。

接下来我们将简单了解如何使用 **遮罩编辑器(Mask Editor)** ，因为之前提供的输入图片中是已经包含了`alpha`透明通道（也就是我们希望在绘图过程中进行编辑的区域），所以并不需要你手动绘制，但在日常使用中我们会更经常使用 **遮罩编辑器(Mask Editor)** 来绘制 蒙版(Mask)

### 使用遮罩编辑器(Mask Editor) 绘制蒙版

首先在上一步工作流中的`Save Image` 节点上右键，你可以在右键菜单中看到`复制(Clipspace)` 选项，点击后会复制当前图片到剪贴板

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7d1bfea21723437c4ca09bba34edd1ed" alt="ComfyUI 局部重绘 - 复制图片" data-og-width="751" width="751" data-og-height="1112" height="1112" data-path="images/tutorial/basic/inpaint/inpaint_copy_clipspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=471161782a68a4a1c9b6b93f90c359bf 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=19e42850cde5a3165aa297c9839a9262 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ecc873dc3f9a633fee9cb2f030aec515 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3e31c622dd7630f5eb12bed77beffb1a 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=232b22932471ab2713a99b4c9dbd9ad0 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_copy_clipspace.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=587e879f30a86eb915838ef2aba36ddd 2500w" />

然后在 **加载图像(Load Image)** 节点上右键，你可以在右键菜单中看到`Paste(Clipspace)` 选项，点击后会从剪贴板中粘贴图片

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=42c942d88b97c696f6f2ed59f7ff9bc8" alt="ComfyUI 局部重绘 - 粘贴图片" data-og-width="750" width="750" data-og-height="947" height="947" data-path="images/tutorial/basic/inpaint/inpaint_paste_clipspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=947f8a2ba53d5e91da74d83cbe7de177 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=aa0df4dd3f7700f2c817fdfeb6af7db8 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7ec2cdd378a38fa9baab14823b4089b3 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3ca8dc639d673d4c6094d48bb1112491 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3ee5a66e68a9f6b2f3c72621986f5f6e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_paste_clipspace.png?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=547532ec78c09b89905cf4a1efa28175 2500w" />

然后在 **加载图像(Load Image)** 节点上右键，你可以在右键菜单中看到`在遮罩编辑器中打开(Open in MaskEditor)` 选项，点击后会打开遮罩编辑器

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=682a66f54e0f61366c42e553d50f4e76" alt="打开遮罩编辑器" data-og-width="894" width="894" data-og-height="1000" height="1000" data-path="images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8aec5f48665275dbe971f1e6b06a8689 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=0d5c93b36e0bdb80bdd09329e4ae1f3a 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e1eda1fc545857dbd5f5d7544c0562f8 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=fcf26f11d3563e21c4f6c1a821b98ce5 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3fe4854c50fe874a310e8b08efa118e8 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint_open_in_maskeditor.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=4c0739d96a8d0b998a8be453bdeca656 2500w" />

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/inpaint/inpaint-maskeditor.gif?s=217f481d8cd4e22183c0dd1551f3e831" alt="遮罩编辑器" data-og-width="960" width="960" data-og-height="720" height="720" data-path="images/tutorial/basic/inpaint/inpaint-maskeditor.gif" data-optimize="true" data-opv="3" />

1. 你可以右侧编辑相关参数，比如调整画笔大小、透明度等等
2. 绘制错误区域可以使用橡皮檫来擦除
3. 绘制完成后点击 `Save` 按钮保存蒙版

这样绘制完成的内容就会作为 遮罩(Mask) 输入到 VAE Encoder (for Inpainting) 节点中一起进行编码

然后试着调整提示词，再次进行生成，直到你可以完成满意的生成结果。

## 局部重绘制相关节点

通过[文生图](/zh-CN/tutorials/basic/text-to-image)、[图生图](/zh-CN/tutorials/basic/image-to-image) 和本篇的工作流对比，我想你应该可以看到这几个工作流主要的差异都在于 VAE 部分这部分的条件输入,
在这个工作流中我们使用到的是 **VAE 内部编码器** 节点，这个节点是专门用于局部重绘的节点，它可以帮助我们更好地控制生成区域，从而获得更好的生成效果。

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2eeecee7cf23a0e1ab7b1a996256278f" alt="VAE Encoder (for Inpainting) 节点" data-og-width="854" width="854" data-og-height="440" height="440" data-path="images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a4dab6ea6ede77a88491abcca4486b12 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=504884ff3853ee9e623e077c85092b5c 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=93307ae96b3c05fc271dd06af325a6c9 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=120a4315d7eaeaacf754647e55f620d4 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=267f53b6551eeac2952cea05913f6ff3 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/latent/inpaint/vae_encode_for_inpainting.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a27dd641b206b80d3e6e79154b5b16f5 2500w" />

**输入类型**

| 参数名称           | 作用                                                     |
| -------------- | ------------------------------------------------------ |
| `pixels`       | 需要编码到潜空间的输入图像。                                         |
| `vae`          | 用于将图片从像素空间编码到潜在空间的 VAE 模型。                             |
| `mask`         | 图片遮罩，用来具体指明哪个区域需要进行修改。                                 |
| `grow_mask_by` | 在原有的遮罩基础上，向外扩展的像素值，保证在遮罩区域外围有一定的过度区域，避免重绘区域与原图存在生硬的过渡。 |

**输出类型**

| 参数名称     | 作用                |
| -------- | ----------------- |
| `latent` | 经过 VAE 编码后的潜空间图像。 |
