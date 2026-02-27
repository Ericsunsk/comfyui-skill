> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Flux 文生图工作示例

> 本文将简要介绍 Flux 绘图模型，并指导使用 Flux 模型进行文生图的示例包括原始完整版本和 FP8 Checkpoint 版本。

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=199a3f0f9e2381586b482029d246f4bb" alt="Flux" data-og-width="2048" width="2048" data-og-height="1171" height="1171" data-path="images/tutorial/flux/flux_example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=809f1427a04668bc20fde161f79f8e8c 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=51679c65a29520e2eae4d5e529eb9d22 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2b562246e400efca7612f7fd228beb60 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=142b51a1bc19a56ef5264c3ccd6beb61 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f5dab39f12ef469b89729d99a3c2eb63 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d9ced5a2d86b6ba2613c57ec43339ed9 2500w" />
Flux 是目前最大的开源AI绘画模型之一，拥有 12B 参数，原始文件大小约为23GB。它由 [Black Forest Labs](https://blackforestlabs.ai/) 开发，该团队由前 Stable Diffusion 团队成员创立。
Flux 以其卓越的画面质量和灵活性而闻名，能够生成高质量、多样化的图像。

目前 Flux.1  模型主要有以下几个版本：

* **Flux.1 Pro：** 效果最佳模型，闭源模型，仅支持通过 API 调用。
* **[Flux.1 \[dev\]：](https://huggingface.co/black-forest-labs/FLUX.1-dev)** 开源但仅限非商业使用，从 Pro 版本蒸馏而来，效果接近Pro版。
* \*\*[Flux.1 \[schnell\]：](https://huggingface.co/black-forest-labs/FLUX.1-schnell)\*\*采用 Apache2.0 许可，仅需4步即可生成图像，适合低配置硬件。

**Flux.1 模型特点**

* **混合架构：** 结合了 Transformer 网络和扩散模型的优势，有效整合文本与图像信息，提升生成图像与提示词的对齐精度，对复杂的提示词依旧有非常好的还原能力。
* **参数规模：** Flux 拥有 12B 参数，可捕捉更复杂的模式关系，生成更逼真、多样化的图像。
* **支持多种风格：** 支持多样化的风格，对各种类型的图像都有非常好的表现能力。

在本篇示例中，我们将介绍使用 Flux.1 Dev 和 Flux.1 Schnell 两个版本进行文生图的示例，包括原始完整版模型和 FP8 Checkpoint 简化版本。

* **Flux 完整版本：** 效果最佳，但需要较大的显存资源（推荐16GB以上），需要安装多个模型文件。
* **Flux FP8 Checkpoint：** 仅需一个 fp8 版本的模型，但是质量相对完整版会有所降低。

<Tip>
  本篇示例中的所有工作流图片的 Metadata 中已包含对应模型下载信息，使用以下方式来加载工作流：

  * 直接拖入 ComfyUI
  * 或使用菜单 `Workflows` -> `Open（ctrl+o）`

  如果你使用的不是 Desktop 版本或者部分模型无法顺利下载，请参考手动安装部分保存模型文件到对应的文件夹。
  请在开始之前确保你的 ComfyUI 已更新到最新版本。
</Tip>

## Flux.1 原始版本模型文生图示例

<Note>
  请注意如果你无法下载 [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) 中的模型，请确保你已登录 Huggingface 并同意了对应 Repo 的协议。
  <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7171d72127bc5b3d6943996a9ef06970" alt="Flux Agreement" data-og-width="3330" width="3330" data-og-height="1854" height="1854" data-path="images/tutorial/flux/flux_agreement.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5fed306c4f611f1edaef827dc6e0d8b6 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8d2968fdc71af13b4993583d9bd77c6d 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6d731ba033d2044414a352f927521f4c 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=205f214d986b9eee863b1ac7b644adf5 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f03cb20f999349c5c6d8bfde63b817e2 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0e6f751cb15e267efa77287ebee79f35 2500w" />
</Note>

### Flux.1 Dev 完整版本工作流

#### 1. 工作流文件

请下载下面的图片，并拖入 ComfyUI 中加载工作流。
![Flux Dev 原始版本工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/text-to-image/flux_dev_t5fp16.png)

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_dev_checkpoint_example&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>在 Comfy Cloud 上运行</p>
</a>

#### 2. 手动安装模型

<Note>
  * `flux1-dev.safetensors` 文件需要同意 [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) 的协议后才能使用浏览器进行下载。
  * 如果你的显存较低，可以尝试使用 [t5xxl\_fp8\_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors?download=true) 来替换 `t5xxl_fp16.safetensors` 文件。
</Note>

请下载下面的模型文件：

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) 当你的显存大于 32GB 时推荐使用。
* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)
* [flux1-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors)

文件保存位置：

```
ComfyUI/
├── models/
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── t5xxl_fp16.safetensors
│   ├── vae/
│   │   └── ae.safetensors
│   └── diffusion_models/
│       └── flux1-dev.safetensors
```

#### 3. 按步骤检查确保工作流可以正常运行

请参照下面的图片，确保各个模型文件都已经加载完成

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fbdc3a3b3b795328425b4ab854b77f13" alt="ComfyUI Flux Dev工作流" data-og-width="3000" width="3000" data-og-height="1564" height="1564" data-path="images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=62b855e6dc0a2c7009437c4c405e2e08 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=980bc0272a2045ad438bed17c14d169b 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8716a037e0507c3299e61752ec61cd1e 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=1d329ee0b53c6148550d31521dbd0d5b 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a4d8ce8f0c9a1266bef3e52f91883bd7 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8b49df11330394e528d2c476d30a7cfc 2500w" />

1. 确保在`DualCLIPLoader`节点中下面的模型已加载：
   * clip\_name1: t5xxl\_fp16.safetensors
   * clip\_name2: clip\_l.safetensors
2. 确保在`Load Diffusion Model`节点加载了`flux1-dev.safetensors`
3. 确保在`Load VAE`节点中加载了`ae.safetensors`
4. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

<Tip>
  得益于 Flux 良好的提示词遵循能力，我们并不需要任何的负向提示词
</Tip>

### Flux.1 Schnell 完整版本工作流

#### 1. 工作流文件

请下载下面的图片，并拖入 ComfyUI 中加载工作流。

![Flux Schnell 版本工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/text-to-image/flux_schnell_t5fp8.png)

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_schnell&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>在 Comfy Cloud 上运行</p>
</a>

#### 2. 手动安装模型

<Note>
  在这个工作流中，只有两个模型文件与 Flux1 Dev 版本的工作流不同,对于 t5xxl 你仍可使用 fp16 版本来获得更好的效果。

  * **t5xxl\_fp16.safetensors** -> **t5xxl\_fp8.safetensors**
  * **flux1-dev.safetensors** -> **flux1-schnell.safetensors**
</Note>

完整模型文件列表：

* [clip\_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true)
* [t5xxl\_fp8\_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors?download=true)
* [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true)
* [flux1-schnell.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/flux1-schnell.safetensors)

文件保存位置：

```
ComfyUI/
├── models/
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └── t5xxl_fp8_e4m3fn.safetensors
│   ├── vae/
│   │   └── ae.safetensors
│   └── diffusion_models/
│       └── flux1-schnell.safetensors
```

#### 3. 按步骤检查确保工作流可以正常运行

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6ce852c65510f40dde8069dc6370869d" alt="Flux Schnell 版本工作流" data-og-width="4000" width="4000" data-og-height="1599" height="1599" data-path="images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a693b1cabe10e1403554d980e3235789 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a5df5a560d6209426506c18a01592596 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f6f054bd91ee1e4c652c8131893f7346 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8c7918768349130fe0b64d0d631758a1 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0d8a64ea9b06142e8bb38c00487a2153 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d64840834a702aae0a8d3b0697ed8d27 2500w" />

1. 确保在`DualCLIPLoader`节点中下面的模型已加载：
   * clip\_name1: t5xxl\_fp8\_e4m3fn.safetensors
   * clip\_name2: clip\_l.safetensors
2. 确保在`Load Diffusion Model`节点加载了`flux1-schnell.safetensors`
3. 确保在`Load VAE`节点中加载了`ae.safetensors`
4. 点击 `Queue` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来运行工作流

## Fp8 Checkpoint 版文生图示例

fp8 版本是对 flux1 原版 fp16 版本的量化版本，在一定程度上这个版本的质量会低于 fp16 版本，但同时它需要的显存也会更少，而且你仅需要安装一个模型文件即可尝试运行。

### Flux.1 Dev fp8 Checkpoint 版工作流

请下载下面的图片，并拖入 ComfyUI 中加载工作流。

![Flux Dev fp8 Checkpoint 版本工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/text-to-image/flux_dev_fp8.png)

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=flux_dev_full_text_to_image&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>在 Comfy Cloud 上运行</p>
</a>

请下载 [flux1-dev-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors?download=true)并保存至 `ComfyUI/models/Checkpoints/` 目录下。

确保对应的 `Load Checkpoint` 节点加载了 `flux1-dev-fp8.safetensors`，即可测试运行。

### Flux.1 Schnell fp8 Checkpoint 版工作流

请下载下面的图片，并拖入 ComfyUI 中加载工作流。

![Flux Schnell fp8 Checkpoint 版本工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/text-to-image/flux_schnell_fp8.png)

请下载[flux1-schnell-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-schnell/resolve/main/flux1-schnell-fp8.safetensors?download=true)并保存至 `ComfyUI/models/Checkpoints/` 目录下。

确保对应的 `Load Checkpoint` 节点加载了 `flux1-schnell-fp8.safetensors`，即可测试运行。
