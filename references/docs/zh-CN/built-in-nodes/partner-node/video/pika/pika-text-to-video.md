> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Pika 2.2 Text to Video - ComfyUI 原生节点文档

> 使用Pika的AI技术将文本描述转换为视频的节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3eea0be5229f14d73d79d17a1b9872ea" alt="ComfyUI 原生 Pika 2.2 Text to Video 节点" data-og-width="1731" width="1731" data-og-height="1712" height="1712" data-path="images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d12e35717b758b3fe6edee67ea6bf3f1 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=01e926f28ab200aa7ecd60eeed6bb791 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ceaced8c4a6712925c5506eac3fc00af 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b62485e36320061e636d7b34ee9747a4 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9c1bd0cd3ab168fd6f92de1d3dc0a9ab 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=03cd041ab170254cc97f90fed682169b 2500w" />

Pika 2.2 Text to Video 节点允许你使用Pika的2.2版本API，通过文本描述创建视频内容。此节点连接到Pika的文本到视频API，让用户能够通过文本提示词生成视频，并提供多种参数控制生成效果。

## 参数说明

### 必需参数

| 参数               | 类型  | 默认值                | 说明                         |
| ---------------- | --- | ------------------ | -------------------------- |
| prompt\_text     | 字符串 | ""                 | 描述要生成视频内容的文本提示词            |
| negative\_prompt | 字符串 | ""                 | 指定不希望在视频中出现的元素             |
| seed             | 整数  | 0                  | 生成过程的随机种子                  |
| resolution       | 选择项 | "1080p"            | 生成视频的分辨率                   |
| duration         | 选择项 | "5s"               | 生成视频的持续时间                  |
| aspect\_ratio    | 浮点数 | 1.7777777777777777 | 输出视频的宽高比，范围0.4-2.5，步长0.001 |

### 输出参数

| 输出    | 类型 | 说明      |
| ----- | -- | ------- |
| VIDEO | 视频 | 生成的视频结果 |

## 源码参考

\[节点源码 (更新于2025-05-05)]

```python  theme={null}

class PikaTextToVideoNodeV2_2(PikaNodeBase):
    """Pika 2.2 Text to Video Node."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_base_inputs_types(PikaBodyGenerate22T2vGenerate22T2vPost),
                "aspect_ratio": model_field_to_node_input(
                    IO.FLOAT,
                    PikaBodyGenerate22T2vGenerate22T2vPost,
                    "aspectRatio",
                    step=0.001,
                    min=0.4,
                    max=2.5,
                    default=1.7777777777777777,
                ),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    RETURN_TYPES = ("VIDEO",)
    DESCRIPTION = "Sends a text prompt to the Pika API v2.2 to generate a video."

    def api_call(
        self,
        prompt_text: str,
        negative_prompt: str,
        seed: int,
        resolution: str,
        duration: int,
        aspect_ratio: float,
        auth_token: Optional[str] = None,
    ) -> tuple[VideoFromFile]:
        """API call for Pika 2.2 Text to Video."""
        initial_operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path=PATH_TEXT_TO_VIDEO,
                method=HttpMethod.POST,
                request_model=PikaBodyGenerate22T2vGenerate22T2vPost,
                response_model=PikaGenerateResponse,
            ),
            request=PikaBodyGenerate22T2vGenerate22T2vPost(
                promptText=prompt_text,
                negativePrompt=negative_prompt,
                seed=seed,
                resolution=resolution,
                duration=duration,
                aspectRatio=aspect_ratio,
            ),
            auth_token=auth_token,
            content_type="application/x-www-form-urlencoded",
        )

        return self.execute_task(initial_operation, auth_token)


```
