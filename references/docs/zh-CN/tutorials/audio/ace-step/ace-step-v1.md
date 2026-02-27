> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI ACE-Step 原生示例

> 本文将引导你在 ComfyUI 中使用 ACE-Step 模型来创造灵动音乐

ACE-Step是由中国团队阶跃星辰（StepFun）与ACE Studio联合开发的​​开源音乐生成基础大模型​​，旨在为音乐创作者提供高效、灵活且高质量的音乐生成与编辑工具。

该模型采用[Apache-2.0](https://github.com/ace-step/ACE-Step?tab=readme-ov-file#-license)许可证发布，可免费商用。

ACE-Step 作为一个强大的音乐生成基座，提供了丰富的扩展能力。通过 LoRA、ControlNet 等微调技术，开发者可以根据实际需求对模型进行定制化训练。
无论是音频编辑、歌声合成、伴奏制作、声音克隆还是风格转换等应用场景，ACE-Step 都能提供稳定可靠的技术支持。
这种灵活的架构设计大大简化了音乐 AI 应用的开发流程，让更多创作者能够快速将 AI 技术应用到音乐创作中。

目前 ACE-Step 已经发布相关的训练代码，包括 LoRA 模型训练等，对应 ControlNet 的训练代码也将在未来陆续发布，你可以访问他们的[Github](https://github.com/ace-step/ACE-Step?tab=readme-ov-file#-roadmap) 来了解更多详情。

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

## ACE-Step ComfyUI 文本到音频生成工作流示例

### 1. 工作流及相关模型下载

点击下面的按钮下载对应的工作流文件，拖入 ComfyUI 中即可加载对应的工作流信息，对应工作流已包含模型下载信息。

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/audio/ace-step/ace_step_1_t2m.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

你也可以手动下载[ace\_step\_v1\_3.5b.safetensors](https://huggingface.co/Comfy-Org/ACE-Step_ComfyUI_repackaged/blob/main/all_in_one/ace_step_v1_3.5b.safetensors) 后保存到 `ComfyUI/models/checkpoints` 文件夹下

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_t2a_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=236a3db013af8dda09a7730916f24da0" alt="步骤图" data-og-width="2583" width="2583" data-og-height="1328" height="1328" data-path="images/tutorial/audio/ace_step/ace_step_1_t2a_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_t2a_step_guide.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=309a437f463a28efba4d8ea61aa7500b 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_t2a_step_guide.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=7468bdcde82ab2597c0d16e05d0e9b22 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_t2a_step_guide.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=90a7d7daa9ac44f9e0c88c3cb3c696a4 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_t2a_step_guide.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=695d947ba36f923d9532ade671ad36c2 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_t2a_step_guide.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=67c9b001e188d03dad95100b7d0d6b6c 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_t2a_step_guide.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f6fd4bbb8a6a9b41b5943059ac984efb 2500w" />

1. 确保 `Load Checkpoints` 节点加载了 `ace_step_v1_3.5b.safetensors` 模型
2. （可选）在 `EmptyAceStepLatentAudio` 节点上你可以设置生成音乐的时长
3. （可选）在 `LatentOperationTonemapReinhard` 节点，你可以调整 `multiplier` 来调整人声的音量大小（数字越大，人声音量越明显）
4. （可选）在 `TextEncodeAceStepAudio` 的 `tags` 输入对应的音乐风格等等
5. （可选）在 `TextEncodeAceStepAudio` 的 `lyrics` 中输入对应的歌词，如果你不知道该输入哪些歌词
6. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行音频的生成。
7. 工作流完成后，你可在 `Save Audio` 节点中查看生成的音频，你可以点击播放试听，对应的音频也会被保存至 `ComfyUI/output/audio` （由`Save Audio`节点决定子目录名称）。

## ACE-Step ComfyUI 音频到音频工作流

你可以像图生图工作流一样，输入一段音乐，使用下面的工作流来达到重新对音乐采样生成，同样，你也可以通过控制 `Ksampler`  的 `denoise` 来调整和原始音频的区别程度。

通过这样的流程，可以实现对音乐的重新编辑，来达到你想要的效果。

### 1. 工作流文件下载

点击下面的按钮下载对应的工作流文件，拖入 ComfyUI 中即可加载对应的工作流信息

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/audio/ace-step/ace_step_1_m2m_editing.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载 Json 格式工作流文件</p>
</a>

下载下面的音频作为输入音频

<a className="prose" target="_blank" href="https://github.com/Comfy-Org/example_workflows/raw/refs/heads/main/audio/ace-step/input.mp3" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff!important', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>下载示例音频文件用于输入</p>
</a>

### 2. 按步骤完成工作流的运行

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_m2m_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=74b041e1a727b4d4bfa22f6ae446d611" alt="ACE-Step 步骤图" data-og-width="2393" width="2393" data-og-height="1241" height="1241" data-path="images/tutorial/audio/ace_step/ace_step_1_m2m_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_m2m_step_guide.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=183515127facdc31a45ecbffba2ee44f 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_m2m_step_guide.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=0049a0613a2d5d52b2e17aa0680c184d 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_m2m_step_guide.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5b51994f52cc17a92bffac03fd3ddc36 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_m2m_step_guide.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a1e40f3dabde3aba980466e77d3a9b43 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_m2m_step_guide.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=adacf1b3ec4887c5eee671ec5c26d40e 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_m2m_step_guide.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=8696e5f924054ca98d687f3f8a08f9b8 2500w" />

1. 确保 `Load Checkpoints` 节点加载了 `ace_step_v1_3.5b.safetensors` 模型
2. 在 `LoadAudio` 节点中上传提供的音频文件
3. （可选）在 `TextEncodeAceStepAudio` 的 `tags` 和 `lyrics` 中输入对应的音乐风格歌词等，提供歌词对于音频编辑来说非常重要
4. （可选）修改 `Ksampler` 节点的 `denoise` 参数，来调整采样过程中添加的噪声来调整与原始音频的相似程度，（越小与原始音频越相似，如果设置为 `1.00`则可以近似认为没有音频输入）
5. 点击 `Run` 按钮，或者使用快捷键 `Ctrl(cmd) + Enter(回车)` 来执行音频的生成。
6. 工作流完成后，你可在 `Save Audio` 节点中查看生成的音频，你可以点击播放试听，对应的音频也会被保存至 `ComfyUI/output/audio` （由`Save Audio`节点决定子目录名称）。

### 3. 工作流补充说明

1. 在  `TextEncodeAceStepAudio` 的 `tags` 中示例工作流中，将原本男声的 `tags` 修改为 `female voice` 来生成女声的音频
2. 在 `TextEncodeAceStepAudio` 的 `lyrics` 中示例工作流中，中对原本的歌词进行了调整修改，具体编辑你可以参考 ACE-Step 项目页面中的示例来了解如何完成修改

## ACE-Step 提示词指南

ACE 的提示词目前使用的有两个，一个是 `tags` 一个是 `lyrics`。

* `tags`： 主要用来描述音乐的风格、场景等, 和我们平常其它生成的 prompt 类似，主要描述音频整体的风格和要求，使用英文逗号分隔
* `lyrics`： 主要用来描述歌词，支持歌词结构标签，如 \[verse]（主歌）、\[chorus]（副歌）和 \[bridge]（过渡段）来区分歌词的不同部分，也可以在纯音乐情况下输入乐器名称

对应的 `tags` 和 `lyrics` 在 [ACE-Step 模型主页](https://ace-step.github.io/) 中可以找到丰富的示例,你可以参考对应示例来尝试对应的提示词，本文档的提示词指南基于项目做了一些整理，以便让你能够快速尝试组合，来达到最想要的效果

### tags标签(prompt)

#### 主流音乐风格

使用简短标签组合，来生成特定风格的音乐

* electronic（电子音乐）
* rock（摇滚）
* pop（流行）
* funk（放克）
* soul（灵魂乐）
* cyberpunk（赛博朋克）
* Acid jazz（酸爵士）
* electro（电子）
* em（电子音乐）
* soft electric drums（软电鼓）
* melodic（旋律）

#### 场景类型

结合具体使用场景和氛围，生成符合对应氛围的音乐

* background music for parties（派对背景音乐）
* radio broadcasts（电台广播音乐）
* workout playlists（健身播放列表音乐）

#### 乐器元素

* saxophone,
* azz（萨克斯风、爵士）
* piano, violin（钢琴、小提琴）

#### 人声类型

* female voice（女声）
* male voice（男声）
* clean vocals（纯净人声）

#### 专业用语

使用音乐中常用的一些专业的用词，来精准控制音乐效果

* 110 bpm（每分钟节拍数为110）

* fast tempo（快节奏）

* slow tempo（慢节奏）

* loops（循环片段）

* fills（填充音）

* acoustic guitar（木吉他）

* electric bass（电贝斯）

{/* - 歌词编辑：
  - edit lyrics: 'When I was young' -> 'When you were kid'（编辑歌词示例） */}

### 歌词（lyrics）

#### 歌词结构标签

* \[intro] (前奏)
* \[verse] (主歌)
* \[pre-chorus] (导歌)
* \[chorus] (副歌/合唱)
* \[bridge] (过渡段/桥段)
* \[outro] (尾声)
* \[hook] (钩子/主题旋律)
* \[refrain] (重复段落)
* \[interlude] (间奏)
* \[breakdown] (分解段)
* \[ad-lib] (即兴段落)

#### 多语言支持

* ACE-Step V1 是支持多语言的，实际使用的时候 ACE-Step 会获取到对应的不同语言转换后的英文字母，然后进行音乐生成。
* 在 ComfyUI 中我们并没有完全实现全部多语言到英文字母的转换，目前仅实现了[日语平假名和片假名字符](https://github.com/comfyanonymous/ComfyUI/commit/5d3cc85e13833aeb6ef9242cdae243083e30c6fc)
  所以如果你需要使用多语言来进行相关的音乐生成，你需要首先将对应的语言转换成英文字母，然后在对应 `lyrics` 开头输入对应语言代码的缩写，比如中文`[zh]`  韩语 `[ko]` 等

比如：

```
[verse]

[zh]wo3zou3guo4shen1ye4de5jie1dao4
[zh]leng3feng1chui1luan4si1nian4de5piao4liang4wai4tao4
[zh]ni3de5wei1xiao4xiang4xing1guang1hen3xuan4yao4
[zh]zhao4liang4le5wo3gu1du2de5mei3fen1mei3miao3

[chorus]

[verse]​
[ko]hamkke si-kkeuleo-un sesang-ui sodong-eul pihae​
[ko]honja ogsang-eseo dalbich-ui eolyeompus-ileul balaboda​
[ko]niga salang-eun lideum-i ganghan eum-ag gatdago malhaess-eo​
[ko]han ta han tamada ma-eum-ui ondoga eolmana heojeonhanji ijge hae

[bridge]
[es]cantar mi anhelo por ti sin ocultar
[es]como poesía y pintura, lleno de anhelo indescifrable
[es]tu sombra es tan terca como el viento, inborrable
[es]persiguiéndote en vuelo, brilla como cruzar una mar de nubes

[chorus]
[fr]que tu sois le vent qui souffle sur ma main
[fr]un contact chaud comme la douce pluie printanière
[fr]que tu sois le vent qui s'entoure de mon corps
[fr]un amour profond qui ne s'éloignera jamais
```

目前 ACE-Step 支持了 19 种语言，但下面十种语言的支持会更好一些：

* English
* Chinese: \[zh]
* Russian: \[ru]
* Spanish: \[es]
* Japanese: \[ja]
* German: \[de]
* French: \[fr]
* Portuguese: \[pt]
* Italian: \[it]
* Korean: \[ko]

<Note>
  上面的语言标签在撰写文档时并没有经过完全测试，如果对应语言标签不正确，请[提交 issue 到我们的文档的仓库](https://github.com/Comfy-Org/docs/issues) 我们会进行及时修改
</Note>

## ACE-Step 相关资源

* [项目主页](https://ace-step.github.io/)
* [Hugging Face 模型](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B)
* [GitHub 仓库](https://github.com/ace-step/ACE-Step)
* [训练脚本](https://github.com/ace-step/ACE-Step?tab=readme-ov-file#-train)
