> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# TrimVideoLatent 节点

> 裁剪潜在空间中的视频帧

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=87bf02eabffeba90db7e9409ddf48dd1" alt="ComfyUI TrimVideoLatent 节点" data-og-width="1608" width="1608" data-og-height="762" height="762" data-path="images/built-in-nodes/latent/video/trim-video-latent.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8cabf59929e83251d9c4faced9f4559f 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=51e4b50bfc4f860f1118006743c72add 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=50cbec822d7d2788a5130da31b75e5c2 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c654433a8b05804a967cf79eaf9d30b4 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e2aacbe2d5b4822bb66da6e5e0a47fd7 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=90e007a0181c33d3d285eaefccd5fba3 2500w" />

TrimVideoLatent 节点用于在潜在空间（LATENT）中裁剪视频帧。常用于处理视频潜变量序列时，去除前面不需要的帧，实现视频的“前向裁剪”。

基本用法：将需要裁剪的视频潜变量输入到 samples，设置 trim\_amount 为要裁剪的帧数。节点会从视频的开头裁剪掉指定数量的帧，输出剩余的潜变量序列。
典型场景：用于视频生成、视频编辑等场景下，去除不需要的前置帧，或配合其他节点实现视频片段的拼接与处理。

## 参数说明

### 输入参数

| 参数名          | 类型     | 是否必填 | 默认值 | 说明               |
| ------------ | ------ | ---- | --- | ---------------- |
| samples      | LATENT | 是    | 无   | 输入的潜在视频数据        |
| trim\_amount | INT    | 是    | 0   | 需要裁剪掉的帧数（从前往后裁剪） |

### 输出参数

| 参数名     | 类型     | 说明        |
| ------- | ------ | --------- |
| samples | LATENT | 裁剪后的视频潜变量 |

## 使用示例

<Card title="Wan2.1 VACE 视频生成工作流示例" icon="book" href="/zh-CN/tutorials/video/wan/vace">
  Wan2.1 VACE 视频生成工作流示例
</Card>

### 源码

```python  theme={null}
class TrimVideoLatent:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "samples": ("LATENT",),
                              "trim_amount": ("INT", {"default": 0, "min": 0, "max": 99999}),
                             }}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "op"

    CATEGORY = "latent/video"

    EXPERIMENTAL = True

    def op(self, samples, trim_amount):
        samples_out = samples.copy()

        s1 = samples["samples"]
        samples_out["samples"] = s1[:, :, trim_amount:]
        return (samples_out,)

```
