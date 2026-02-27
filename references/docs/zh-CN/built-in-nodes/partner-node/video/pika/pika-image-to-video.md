> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Pika 2.2 Image to Video - ComfyUI 原生节点文档

> 使用Pika的AI技术将静态图像转换为动态视频的节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4d84ed0f286826f853aeb820bf01c473" alt="ComfyUI 原生 Pika 2.2 Image to Video 节点" data-og-width="1731" width="1731" data-og-height="1610" height="1610" data-path="images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6231adab3c17f6b259419ea1ca56851b 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f68712438d1dc3b57282825a276e55b1 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=414c952553bf355df8f624badafa6651 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1e9d7bf229f464467877a9e3545f6fdb 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=24a0c522a83a0f2034931f7b4fb86dd7 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3c88a91bbb2117ae69e7724b3a70ad24 2500w" />

Pika 2.2 Image to Video 节点通过连接Pika最新的2.2版本API，将静态图像转变为动态视频。该节点能够保留原始图像的视觉特征，同时根据文本提示词添加自然的动态效果。

## 参数说明

### 必需参数

| 参数               | 类型  | 默认值     | 说明              |
| ---------------- | --- | ------- | --------------- |
| image            | 图像  | -       | 要转换为视频的输入图像     |
| prompt\_text     | 字符串 | ""      | 描述视频动作和内容的文本提示词 |
| negative\_prompt | 字符串 | ""      | 指定不希望在视频中出现的元素  |
| seed             | 整数  | 0       | 生成过程的随机种子       |
| resolution       | 选择项 | "1080p" | 生成视频的分辨率        |
| duration         | 选择项 | "5s"    | 生成视频的持续时间       |

### 输出

| 输出    | 类型 | 说明      |
| ----- | -- | ------- |
| VIDEO | 视频 | 生成的视频结果 |

## 工作流程

节点将输入图像和相关参数（提示词、分辨率、持续时间等）通过多部分表单数据发送到Pika的API服务器。API处理后返回生成的视频结果。用户可以通过调整提示词、负面提示词、随机种子等参数来控制生成效果。

## 源码参考

\[节点源码 (更新于2025-05-05)]

```python  theme={null}

class PikaImageToVideoV2_2(PikaNodeBase):
    """Pika 2.2 Image to Video Node."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": (
                    IO.IMAGE,
                    {"tooltip": "The image to convert to video"},
                ),
                **cls.get_base_inputs_types(PikaBodyGenerate22I2vGenerate22I2vPost),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    DESCRIPTION = "Sends an image and prompt to the Pika API v2.2 to generate a video."
    RETURN_TYPES = ("VIDEO",)

    def api_call(
        self,
        image: torch.Tensor,
        prompt_text: str,
        negative_prompt: str,
        seed: int,
        resolution: str,
        duration: int,
        auth_token: Optional[str] = None,
    ) -> tuple[VideoFromFile]:
        """API call for Pika 2.2 Image to Video."""
        # Convert image to BytesIO
        image_bytes_io = tensor_to_bytesio(image)
        image_bytes_io.seek(0)  # Reset stream position

        # Prepare file data for multipart upload
        pika_files = {"image": ("image.png", image_bytes_io, "image/png")}

        # Prepare non-file data using the Pydantic model
        pika_request_data = PikaBodyGenerate22I2vGenerate22I2vPost(
            promptText=prompt_text,
            negativePrompt=negative_prompt,
            seed=seed,
            resolution=resolution,
            duration=duration,
        )

        initial_operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path=PATH_IMAGE_TO_VIDEO,
                method=HttpMethod.POST,
                request_model=PikaBodyGenerate22I2vGenerate22I2vPost,
                response_model=PikaGenerateResponse,
            ),
            request=pika_request_data,
            files=pika_files,
            content_type="multipart/form-data",
            auth_token=auth_token,
        )

        return self.execute_task(initial_operation, auth_token)

```
