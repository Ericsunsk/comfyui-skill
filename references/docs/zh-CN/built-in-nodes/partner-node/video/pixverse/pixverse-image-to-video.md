> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# PixVerse Image to Video - ComfyUI 原生节点文档

> 使用PixVerse的AI技术将静态图像转换为动态视频的节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=5dad32a76df9845caf721b255b39df09" alt="ComfyUI 原生 PixVerse Image to Video 节点" data-og-width="1731" width="1731" data-og-height="1659" height="1659" data-path="images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3155afe1969bafa8920123e9917e54e0 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6a8e5c91f4d608ef3dde687fc9c43541 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=03241f98cc99bc9b3bd6a41e361a1a73 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a2ebe2cb1fb508cf2b1d2c3c1d5b2c1b 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1035165aa7732d5e36faa262d6ede118 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=951bf8ba9400bbb5c25471ef63ff0fa4 2500w" />

PixVerse Image to Video 节点通过 PixVerse 的API服务，可以将静态图像转换为动态视频。它能保留原始图像的视觉特征，同时根据文本提示词添加自然的动态效果。

## 参数说明

### 必需参数

| 参数               | 类型  | 默认值          | 说明              |
| ---------------- | --- | ------------ | --------------- |
| image            | 图像  | -            | 要转换为视频的输入图像     |
| prompt           | 字符串 | ""           | 描述视频动作和内容的文本提示词 |
| negative\_prompt | 字符串 | ""           | 指定不希望在视频中出现的元素  |
| seed             | 整数  | -1           | 生成过程的随机种子，-1为随机 |
| quality          | 选择项 | "high"       | 生成视频的质量级别       |
| aspect\_ratio    | 选择项 | "r16\_9"     | 输出视频的宽高比        |
| duration         | 选择项 | "seconds\_4" | 生成视频的持续时间       |
| motion\_mode     | 选择项 | "standard"   | 视频的动作模式         |

### 可选参数

| 参数                 | 类型                 | 默认值  | 说明              |
| ------------------ | ------------------ | ---- | --------------- |
| pixverse\_template | PIXVERSE\_TEMPLATE | None | 可选的PixVerse模板配置 |

### 输出

| 输出    | 类型 | 说明      |
| ----- | -- | ------- |
| VIDEO | 视频 | 生成的视频结果 |

## 源码参考

\[节点源码 (更新于2025-05-05)]

```python  theme={null}
class PixverseImageToVideoNode(ComfyNodeABC):
    """
    Pixverse Image to Video

    Generates videos from an image and prompts.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "prompt": ("STRING", {"multiline": True, "default": ""}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 0xffffffffffffffff}),
                "quality": (list(PixverseQuality.__members__.keys()), {"default": "high"}),
                "aspect_ratio": (list(PixverseAspectRatio.__members__.keys()), {"default": "r16_9"}),
                "duration": (list(PixverseDuration.__members__.keys()), {"default": "seconds_4"}),
                "motion_mode": (list(PixverseMotionMode.__members__.keys()), {"default": "standard"}),
            },
            "optional": {
                "pixverse_template": ("PIXVERSE_TEMPLATE",),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    RETURN_TYPES = ("VIDEO",)
    DESCRIPTION = "Generates videos from an image and prompts using Pixverse's API"
    FUNCTION = "generate_video"
    CATEGORY = "api node/video/Pixverse"
    API_NODE = True
    OUTPUT_NODE = True
```
