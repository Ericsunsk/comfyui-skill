> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Text to Vector - ComfyUI 原生节点文档

> 通过文本描述生成可缩放矢量图像的 Recraft 合作伙伴节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-vector.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=868aafbbe8b41edf218df85bd0f17fa0" alt="ComfyUI 原生Recraft Text to Vector节点" data-og-width="1731" width="1731" data-og-height="1148" height="1148" data-path="images/built-in-nodes/api_nodes/recraft/recraft-text-to-vector.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-vector.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e3d6ec2992615565923dbbb36f60a251 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-vector.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=df217a184ae2c7a423de51f13a2b2086 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-vector.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=83e13573fcb5bcbb12d95c720535f17e 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-vector.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=99c07d85409f33603a5c68e946adff98 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-vector.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=824ddf41c71681d5b59fd05b2e8e72b3 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-vector.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e8903d5001d3eca5eb633173e514390c 2500w" />

Recraft Text to Vector 节点允许你通过文本描述通过 Recraft 的 API 生成高质量的矢量图形(SVG格式)，适用于创建标志、图标和可无限缩放的插图。

## 参数说明

### 基本参数

| 参数       | 类型  | 默认值       | 说明           |
| -------- | --- | --------- | ------------ |
| prompt   | 字符串 | ""        | 描述要生成的矢量图形   |
| substyle | 选择项 | -         | 矢量风格的子类型     |
| size     | 选择项 | 1024x1024 | 输出矢量图的画布尺寸   |
| n        | 整数  | 1         | 生成结果的数量(1-6) |
| seed     | 整数  | 0         | 随机种子值        |

### 可选参数

| 参数                | 类型               | 说明          |
| ----------------- | ---------------- | ----------- |
| negative\_prompt  | 字符串              | 指定不希望出现的元素  |
| recraft\_controls | Recraft Controls | 附加控制参数(颜色等) |

### 输出

| 输出  | 类型  | 说明                         |
| --- | --- | -------------------------- |
| SVG | 矢量图 | 生成的SVG矢量图形，需连接到SaveSVG节点保存 |

## 源码参考

\[节点源码 (更新于2025-05-03)]

```python  theme={null}

class RecraftTextToVectorNode:
    """
    Generates SVG synchronously based on prompt and resolution.
    """

    RETURN_TYPES = (RecraftIO.SVG,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/image/Recraft"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Prompt for the image generation.",
                    },
                ),
                "substyle": (get_v3_substyles(RecraftStyleV3.vector_illustration),),
                "size": (
                    [res.value for res in RecraftImageSize],
                    {
                        "default": RecraftImageSize.res_1024x1024,
                        "tooltip": "The size of the generated image.",
                    },
                ),
                "n": (
                    IO.INT,
                    {
                        "default": 1,
                        "min": 1,
                        "max": 6,
                        "tooltip": "The number of images to generate.",
                    },
                ),
                "seed": (
                    IO.INT,
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "control_after_generate": True,
                        "tooltip": "Seed to determine if node should re-run; actual results are nondeterministic regardless of seed.",
                    },
                ),
            },
            "optional": {
                "negative_prompt": (
                    IO.STRING,
                    {
                        "default": "",
                        "forceInput": True,
                        "tooltip": "An optional text description of undesired elements on an image.",
                    },
                ),
                "recraft_controls": (
                    RecraftIO.CONTROLS,
                    {
                        "tooltip": "Optional additional controls over the generation via the Recraft Controls node."
                    },
                ),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    def api_call(
        self,
        prompt: str,
        substyle: str,
        size: str,
        n: int,
        seed,
        negative_prompt: str = None,
        recraft_controls: RecraftControls = None,
        auth_token=None,
        **kwargs,
    ):
        # create RecraftStyle so strings will be formatted properly (i.e. "None" will become None)
        recraft_style = RecraftStyle(RecraftStyleV3.vector_illustration, substyle=substyle)

        controls_api = None
        if recraft_controls:
            controls_api = recraft_controls.create_api_model()

        if not negative_prompt:
            negative_prompt = None

        operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path="/proxy/recraft/image_generation",
                method=HttpMethod.POST,
                request_model=RecraftImageGenerationRequest,
                response_model=RecraftImageGenerationResponse,
            ),
            request=RecraftImageGenerationRequest(
                prompt=prompt,
                negative_prompt=negative_prompt,
                model=RecraftModel.recraftv3,
                size=size,
                n=n,
                style=recraft_style.style,
                substyle=recraft_style.substyle,
                controls=controls_api,
            ),
            auth_token=auth_token,
        )
        response: RecraftImageGenerationResponse = operation.execute()
        svg_data = []
        for data in response.data:
            svg_data.append(download_url_to_bytesio(data.url, timeout=1024))

        return (SVG(svg_data),)
```
