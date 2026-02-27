> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Stability AI Stable Audio 2.5 合作伙伴节点 ComfyUI 官方工作流示例

> 本文将介绍如何在 ComfyUI 中使用 Stability AI Stable Audio 2.5 合作伙伴节点的文本转音频、音频转音频和音频修复功能

Stability AI Stable Audio 2.5 合作伙伴节点允许你使用 Stability AI 最新的音频生成模型，通过文本提示、音频转换和音频修复功能来创建高质量音乐。

Stable Audio 2.5 专为企业使用而设计，具有改进的音乐结构、更好的提示遵循能力，以及能够在几秒钟内生成长达数分钟的作品。该模型提供三种主要工作流：**文本转音频**用于从描述生成音乐，**音频转音频**用于将现有音频转换为新作品，**音频修复**用于完成或扩展现有音轨。

Stable Audio 2.5 完全基于授权音频训练，商业安全，非常适合需要专业级音频生成且具有企业级可靠性的广告商、游戏工作室和内容创作者。

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

## 文本转音频工作流

对于文本转音频，你可以通过文本提示生成音频。你需要描述想要生成的音乐。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/api_stability_ai_text_to_audio.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 工作流</p>
</a>

<img src="https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_text_to_audio.jpg?fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=7e369b21bd7a974f40ed38bcbc4c8afe" alt="workflow" data-og-width="2170" width="2170" data-og-height="1130" height="1130" data-path="images/tutorial/api_nodes/stability_ai/api_stability_ai_text_to_audio.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_text_to_audio.jpg?w=280&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=f933d31a488d96c95c717ae3630f1cbe 280w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_text_to_audio.jpg?w=560&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=f7fed196827182261976aea32e522c2a 560w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_text_to_audio.jpg?w=840&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=078a21a78fabbe870444a21d12a003ae 840w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_text_to_audio.jpg?w=1100&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=6eccc85d2feab74797b7e9d3fb16f42d 1100w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_text_to_audio.jpg?w=1650&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=4dd0da78dd4a6efe6f7a0ff3117dce60 1650w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_text_to_audio.jpg?w=2500&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=a9b327a847b32dbe99750e9bf217baf2 2500w" />

1. 修改文本提示。你应该使用关键词来描述想要生成的音乐。
2. （可选）修改 `duration` 参数。默认为 `190`。
3. 点击 `Run` 按钮或使用快捷键 `Ctrl(cmd) + Enter` 来执行音频生成。音频将保存到 `ComfyUI/output/audio` 目录。

## 音频转音频工作流

音频转音频基本上是音乐重采样。你可以使用它从给定的音乐片段生成新音乐，或者你可以哼唱一段旋律，然后模型将基于输入音频生成新音乐。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/api_stability_ai_audio_to_audio.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 工作流</p>
</a>

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/stability_ai/stable_audio/beatbox.mp3" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载输入音频</p>
</a>

<img src="https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_to_audio.jpg?fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=e3fb5f33fd60d42d65544874a574a483" alt="workflow" data-og-width="2366" width="2366" data-og-height="890" height="890" data-path="images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_to_audio.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_to_audio.jpg?w=280&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=0986fd5d755ae5a1dd16d1c918d83cf4 280w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_to_audio.jpg?w=560&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=5edbd9254f46138721015beea5669b2d 560w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_to_audio.jpg?w=840&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=957beac2b40d48517c68396b8dcdfa72 840w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_to_audio.jpg?w=1100&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=00b8997207fae2c4aa18c7e86de428a2 1100w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_to_audio.jpg?w=1650&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=de12e64a619cebb83ea44e55928bfe27 1650w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_to_audio.jpg?w=2500&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=147ead09b14ab884e5fbafc851e0b129 2500w" />

1. 在此工作流中，我们提供了两个节点来输入你想要编辑的音频（至少 6 秒）：
   * 1.1 `Record Audio` 节点：你可以使用它录制任何音乐想法，例如哼唱的旋律。
   * 1.2 `LoadAudio` 节点：你可以使用它上传要在此工作流中使用的音频。
2. 修改文本提示。你应该使用关键词来描述想要生成的音乐。
3. `strength` 参数用于控制与原始音频的差异。值越低，生成的音频与原始音频越相似。
4. 点击 `Run` 按钮或使用快捷键 `Ctrl(cmd) + Enter` 来执行音频生成。音频将保存到 `ComfyUI/output/audio` 目录。

## 音频修复工作流

音频修复用于完成或扩展现有音轨。你可以使用它来完成音乐的缺失部分，或将音乐扩展到更长的时长。

你需要设置想要开始和结束修复的位置。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/api_stability_ai_audio_inpaint.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 JSON 工作流</p>
</a>

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/stability_ai/stable_audio/audio_input.wav" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载输入音频</p>
</a>

<img src="https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_inpaint.jpg?fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=733ebe929fe884c94701a36e38549c58" alt="workflow" data-og-width="2358" width="2358" data-og-height="848" height="848" data-path="images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_inpaint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_inpaint.jpg?w=280&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=b1e3d149cbf62cab22b311663b54da1e 280w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_inpaint.jpg?w=560&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=01606a6efb0c05c8ec39917c2f03afd6 560w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_inpaint.jpg?w=840&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=2dc4160b3619080eaa29e0a576e2aeb5 840w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_inpaint.jpg?w=1100&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=dd812ab64f8939469a5226e14faf3fa9 1100w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_inpaint.jpg?w=1650&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=ad241c5858411f087968e400833197a7 1650w, https://mintcdn.com/dripart/odc_rZSmR0RrwUYs/images/tutorial/api_nodes/stability_ai/api_stability_ai_audio_inpaint.jpg?w=2500&fit=max&auto=format&n=odc_rZSmR0RrwUYs&q=85&s=6f851ac856dced5b14f7236112e9eb08 2500w" />

1. 将音频上传到 `LoadAudio` 节点。
2. 修改文本提示。你应该使用关键词来描述想要生成的音乐。
3. （可选）修改 `duration` 参数。默认为 `190`。
4. （重要）修改 `mask_start` 和 `mask_end` 参数。你需要设置想要开始和结束修复的位置。
5. 点击 `Run` 按钮或使用快捷键 `Ctrl(cmd) + Enter` 来执行音频生成。音频将保存到 `ComfyUI/output/audio` 目录。
