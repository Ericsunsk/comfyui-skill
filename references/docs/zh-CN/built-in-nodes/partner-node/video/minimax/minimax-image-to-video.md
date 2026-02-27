> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Image to Video - ComfyUI 原生节点文档

> 使用 MiniMax AI将静态图像转换为动态视频的节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=20daea4b1e99477334f1a7be3d3cb4d3" alt="ComfyUI 原生 MiniMax Image to Video 节点" data-og-width="1731" width="1731" data-og-height="1360" height="1360" data-path="images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1bf0e97a0a4ba3d78b5bb31179834feb 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0e8b54168d3722db035c60ccd51eaa31 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=063762bc777a56217d88e984d85c07b9 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=848e10dd87fc30b16072f3ba41c23175 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=fbe894102020f7b8e27b5f15ebc250e2 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=34e4fda31f26d1e28a63c600a84d4145 2500w" />

MiniMax Image to Video 节点使用 MiniMax 的API，基于输入图像和提示词同步生成视频内容。

## 参数说明

### 必需参数

| 参数           | 类型  | 默认值      | 说明                                             |
| ------------ | --- | -------- | ---------------------------------------------- |
| image        | 图像  | -        | 用作视频生成第一帧的输入图像                                 |
| prompt\_text | 字符串 | ""       | 引导视频生成的文本提示词                                   |
| model        | 选择项 | "I2V-01" | 可选模型包括"I2V-01-Director"、"I2V-01"、"I2V-01-live" |

### 可选参数

| 参数   | 类型 | 说明           |
| ---- | -- | ------------ |
| seed | 整数 | 用于创建噪声的随机种子值 |

### 输出

| 输出    | 类型 | 说明      |
| ----- | -- | ------- |
| VIDEO | 视频 | 生成的视频结果 |

## 源码参考

\[节点源码 (更新于2025-05-03)]

```python  theme={null}

class MinimaxImageToVideoNode(MinimaxTextToVideoNode):
    """
    Generates videos synchronously based on an image and prompt, and optional parameters using Minimax's API.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": (
                    IO.IMAGE,
                    {
                        "tooltip": "Image to use as first frame of video generation"
                    },
                ),
                "prompt_text": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Text prompt to guide the video generation",
                    },
                ),
                "model": (
                    [
                        "I2V-01-Director",
                        "I2V-01",
                        "I2V-01-live",
                    ],
                    {
                        "default": "I2V-01",
                        "tooltip": "Model to use for video generation",
                    },
                ),
            },
            "optional": {
                "seed": (
                    IO.INT,
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "control_after_generate": True,
                        "tooltip": "The random seed used for creating the noise.",
                    },
                ),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    RETURN_TYPES = ("VIDEO",)
    DESCRIPTION = "Generates videos from an image and prompts using Minimax's API"
    FUNCTION = "generate_video"
    CATEGORY = "api node/video/Minimax"
    API_NODE = True
    OUTPUT_NODE = True
```
