> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 原生版本 HiDream-I1 文生图工作流示例

> 本篇将引导了解并完成 ComfyUI 原生版本 HiDream-I1 文生图工作流实例

![HiDream-I1 演示](https://raw.githubusercontent.com/HiDream-ai/HiDream-I1/main/assets/demo.jpg)

HiDream-I1 是智象未来(HiDream-ai)于2025年4月7日正式开源的文生图模型。该模型拥有17B参数规模，采用 [MIT 许可证](https://github.com/HiDream-ai/HiDream-I1/blob/main/LICENSE) 发布，支持用于个人项目、科学研究以及商用，目前在多项基准测试中该模型表现优异。

## 模型特点

**混合架构设计**
采用​​扩散模型（DiT）​​与​​混合专家系统（MoE）​​的结合架构：

* 主体基于Diffusion Transformer（DiT），通过双流MMDiT模块处理多模态信息，单流DiT模块优化全局一致性。
* 动态路由机制灵活分配计算资源，提升复杂场景处理能力，在色彩还原、边缘处理等细节上表现优异。

**多模态文本编码器集成**
整合四个文本编码器：

* OpenCLIP ViT-bigG、OpenAI CLIP ViT-L（视觉语义对齐）
* T5-XXL（长文本解析）
* Llama-3.1-8B-Instruct（指令理解）
  这一组合使其在颜色、数量、空间关系等复杂语义解析上达到SOTA水平，中文提示词支持显著优于同类开源模型。

**原始模型版本**

智象未来(HiDream-ai)提供了三个版本的 HiDream-I1 模型，以满足不同场景的需求，下面是原始的模型仓库链接：

* 完整版本：[🤗 HiDream-I1-Full](https://huggingface.co/HiDream-ai/HiDream-I1-Full) 推理步数为 50
* 蒸馏开发版本：[🤗 HiDream-I1-Dev](https://huggingface.co/HiDream-ai/HiDream-I1-Dev) 推理步数为 28
* 蒸馏快速版本：[🤗 HiDream-I1-Fast](https://huggingface.co/HiDream-ai/HiDream-I1-Fast) 推理步数为 16

## 关于本篇工作流示例

我们将在本篇示例中使用 ComfyOrg 的 repackaged 的版本，你可以在 [HiDream-I1\_ComfyUI](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/) 仓库中找到我们将在本篇示例中使用的所有模型文件。

<Tip>
  在开始前请更新你的 ComfyUI 版本，至少保证在这个[提交](https://github.com/comfyanonymous/ComfyUI/commit/9ad792f92706e2179c58b2e5348164acafa69288) 之后才能确保你的 ComfyUI 有 HiDream 的原生支持
</Tip>

## HiDream-I1 工作流

对应不同 ComfyUI 原生版本 HiDream-I1 工作流的模型要求基本上是相同的，只有使用过的 [diffusion models](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files/diffusion_models) 文件不同。

如果你不知道如何选择合适的版本，请参考以下建议：

* **HiDream-I1-Full** 可以生成质量最高的图像
* **HiDream-I1-Dev** 在生成较高质量的图像的同时，又兼顾速度
* **HiDream-I1-Fast** 只需要 16 步就可以生成图像，适合需要实时迭代的场景

对于 **dev** 和 **fast** 版本并不需要负向提示词，所以请在采样时设置`cfg` 参数为 `1.0`，我们对应参数设置已在相关工作流中备注。

<Tip>
  以上三个版本的完整版本对显存要求较高，你可能需要 27GB 以上的显存才能顺利运行。在对应版本的工作流教程中，我们将会使用 **fp8** 版本作为示例演示，以保证大多用户都可以顺利运行，不过我们仍会在对应示例中提供不同版本的模型下载链接，你可以根据你的显存情况来选择合适的文件。
</Tip>

### 模型安装

下面的模型文件是我们会共用的模型文件，请点击对应的链接进行下载，并参照模型文件保存位置进行保存，对应的 **diffusion models** 模型我们会在对应工作流中引导你进行下载。

**text\_encoders**：

* [clip\_l\_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_l_hidream.safetensors)
* [clip\_g\_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_g_hidream.safetensors)
* [t5xxl\_fp8\_e4m3fn\_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors) 这个模型在许多的工作流中都有使用过，你可能已经下载了这个文件。
* [llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/llama_3.1_8b_instruct_fp8_scaled.safetensors)

**VAE**

* [ae.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/vae/ae.safetensors) 这个是 Flux 的 VAE 模型，如果你之前使用过 Flux 的工作流，你可能已经下载了这个文件。

**diffusion models**
这部分我们将在对应工作流中具体引导下载对应的模型文件。

模型文件保存位置

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├─── clip_l_hidream.safetensors
│   │   ├─── clip_g_hidream.safetensors
│   │   ├─── t5xxl_fp8_e4m3fn_scaled.safetensors
│   │   └─── llama_3.1_8b_instruct_fp8_scaled.safetensors
│   └── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 diffusion_models/
│       └── ...               # 将在对应版本的工作流中引导你进行安装            
```

### HiDream-I1 full 版本工作流

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=hidream_i1_full&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

#### 1. 模型文件下载

请根据你的硬件情况选择合适的版本，点击链接并下载对应的模型文件保存到 `ComfyUI/models/diffusion_models/` 文件夹下。

* FP8 版本：[hidream\_i1\_full\_fp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_full_fp8.safetensors?download=true) 需要 16GB 以上的显存
* 完整版本：[hidream\_i1\_full\_f16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_full_fp16.safetensors?download=true) 需要 27GB 以上的显存

#### 2. 工作流文件下载

请下载下面的图片，并拖入 ComfyUI 中以加载对应的工作流
![HiDream-I1 full 版本工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hidream_i1/hidream_i1_full.png)

#### 3. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=d7cd0444bdb290b4724bf01b80e5b1dd" alt="HiDream-I1 full 版本步骤图" data-og-width="3000" width="3000" data-og-height="1620" height="1620" data-path="images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=57444e4459fbac669797acf7075bd544 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e83e9e59c0847b984af3ad6b178e9494 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=0af3aba1e4b43d3aeadf08304dc004c6 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=b57f0178ad0cf8c1fa5f0490ebfdfcfc 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=fce43e17a4779f1757f9a95948e24858 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_full_flow_diagram.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6cae50583dbd7b6f091d7e28df1a64e8 2500w" />

按步骤完成工作流的运行

1. 确保`Load Diffusion Model` 节点中使用的是 `hidream_i1_full_fp8.safetensors` 文件
2. 确保`QuadrupleCLIPLoader` 中四个对应的 text encoder 被正确加载
   * clip\_l\_hidream.safetensors
   * clip\_g\_hidream.safetensors
   * t5xxl\_fp8\_e4m3fn\_scaled.safetensors
   * llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors
3. 确保`Load VAE` 节点中使用的是 `ae.safetensors` 文件
4. 对于 **full** 版本你需要设置 `ModelSamplingSD3` 中的 `shift` 参数为 `3.0`
5. 对于 `Ksampler` 节点，你需要进行以下设置
   * `steps` 设置为 `50`
   * `cfg` 设置为 `5.0`
   * (可选) `sampler` 设置为 `lcm`
   * (可选) `scheduler` 设置为 `normal`
6. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片生成

### HiDream-I1 dev 版本工作流

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=hidream_i1_dev&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

#### 1. 模型文件下载

请根据你的硬件情况选择合适的版本，点击链接并下载对应的模型文件保存到 `ComfyUI/models/diffusion_models/` 文件夹下。

* FP8 版本：[hidream\_i1\_dev\_fp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_dev_fp8.safetensors?download=true) 需要 16GB 以上的显存
* 完整版本：[hidream\_i1\_dev\_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_dev_bf16.safetensors?download=true) 需要 27GB 以上的显存

#### 2. 工作流文件下载

请下载下面的图片，并拖入 ComfyUI 中以加载对应的工作流

![HiDream-I1 dev 版本工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hidream_i1/hidream_i1_dev.png)

#### 3. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ec40487c298368e902ddac3549a23f09" alt="HiDream-I1 dev 版本步骤图" data-og-width="3000" width="3000" data-og-height="1620" height="1620" data-path="images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=60089a16b296f7931777fe5f516c75c5 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c9a5c339380b2cda2c81ffc22c107ce2 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=68a3b8434c000845e1a3d21d60c2c295 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=572ccba5e3ae07b49d4afd76bebfd633 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=83780daf5a04294791d7209439e2eb04 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_dev_flow_diagram.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=19149609d7810003a767599a3845c702 2500w" />
按步骤完成工作流的运行

1. 确保`Load Diffusion Model` 节点中使用的是 `hidream_i1_dev_fp8.safetensors` 文件
2. 确保`QuadrupleCLIPLoader` 中四个对应的 text encoder 被正确加载
   * clip\_l\_hidream.safetensors
   * clip\_g\_hidream.safetensors
   * t5xxl\_fp8\_e4m3fn\_scaled.safetensors
   * llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors
3. 确保`Load VAE` 节点中使用的是 `ae.safetensors` 文件
4. 对于 **dev** 版本你需要设置 `ModelSamplingSD3` 中的 `shift` 参数为 `6.0`
5. 对于 `Ksampler` 节点，你需要进行以下设置
   * `steps` 设置为 `28`
   * (重要) `cfg` 设置为 `1.0`
   * (可选) `sampler` 设置为 `lcm`
   * (可选) `scheduler` 设置为 `normal`
6. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片生成

### HiDream-I1 fast 版本工作流

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=hidream_i1_fast&utm_source=docs" style={{ display: 'inline-block', backgroundColor: '#28a745', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Run on Comfy Cloud</p>
</a>

#### 1. 模型文件下载

请根据你的硬件情况选择合适的版本，点击链接并下载对应的模型文件保存到 `ComfyUI/models/diffusion_models/` 文件夹下。

* FP8 版本：[hidream\_i1\_fast\_fp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_fast_fp8.safetensors?download=true) 需要 16GB 以上的显存
* 完整版本：[hidream\_i1\_fast\_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_fast_bf16.safetensors?download=true) 需要 27GB 以上的显存

#### 2. 工作流文件下载

请下载下面的图片，并拖入 ComfyUI 中以加载对应的工作流

![HiDream-I1 fast 版本工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hidream_i1/hidream_i1_fast.png)

#### 3. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=8969d355742543b20158bbefa4705bfe" alt="HiDream-I1 fast 版本步骤图" data-og-width="3000" width="3000" data-og-height="1620" height="1620" data-path="images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=225090529328f08cae2a900e783a52f7 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=68c6898820435105c79bfbe3cd581f98 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=5029a867eafc2f0dc3ed3ea1947078cd 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=16ac4c99632a3eff8e3c270f5e5ae54c 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=44f8f8b29411aaefc3ce3b903f380abc 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hidream/hidream_i1_fast_flow_diagram.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=d49f08328c107693e3d1c6e85e6f9a0d 2500w" />

按步骤完成工作流的运行

1. 确保`Load Diffusion Model` 节点中使用的是 `hidream_i1_fast_fp8.safetensors` 文件
2. 确保`QuadrupleCLIPLoader` 中四个对应的 text encoder 被正确加载
   * clip\_l\_hidream.safetensors
   * clip\_g\_hidream.safetensors
   * t5xxl\_fp8\_e4m3fn\_scaled.safetensors
   * llama\_3.1\_8b\_instruct\_fp8\_scaled.safetensors
3. 确保`Load VAE` 节点中使用的是 `ae.safetensors` 文件
4. 对于 **fast** 版本你需要设置 `ModelSamplingSD3` 中的 `shift` 参数为 `3.0`
5. 对于 `Ksampler` 节点，你需要进行以下设置
   * `steps` 设置为 `16`
   * (重要) `cfg` 设置为 `1.0`
   * (可选) `sampler` 设置为 `lcm`
   * (可选) `scheduler` 设置为 `normal`
6. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行图片生成

## 使用建议

* 虽然 HiDream-I1 支持中文提示词，但建议还是优先使用英文提示词来保证准确性
* 你可以使用 fast 版本来快速生成示例验证，然后再用完整版本的模型来生成较高质量的图像

## 其它相关资源

### GGUF 版本模型

* [HiDream-I1-Full-gguf](https://huggingface.co/city96/HiDream-I1-Full-gguf)
* [HiDream-I1-Dev-gguf](https://huggingface.co/city96/HiDream-I1-Dev-gguf)

你需要使用 City96 的 [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)  中的 `Unet Loader (GGUF)`节点替换掉 `Load Diffusion Model` 节点来使用 GGUF 版本模型。

* [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)

### NF4 版本模型

* [HiDream-I1-nf4](https://github.com/hykilpikonna/HiDream-I1-nf4)
* 使用 [ComfyUI-HiDream-Sampler](https://github.com/SanDiegoDude/ComfyUI-HiDream-Sampler) 节点来使用 NF4 版本模型。
