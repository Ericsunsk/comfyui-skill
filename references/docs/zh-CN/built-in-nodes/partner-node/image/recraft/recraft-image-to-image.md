> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Image to Image - ComfyUI 原生节点文档

> 通过文本描述和参考图像生成新图像的 Recraft 合作伙伴节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-to-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=80e1a35d96e8943dee2cd18151db2db4" alt="ComfyUI 原生Recraft Image to Image节点" data-og-width="1731" width="1731" data-og-height="1208" height="1208" data-path="images/built-in-nodes/api_nodes/recraft/recraft-image-to-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-to-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4ee37ccf9a9b15ccb7877da37ba6f7be 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-to-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6551c1942eb8dc2ac83446307092cfa5 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-to-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=364f5d3e4f8dc1027cb8893861b6670f 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-to-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3d872985bb0b4d5c4625c527de14bce5 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-to-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f8e2b5a9a6ed620b1b169f13b0eecabe 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-to-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f53e962ba4484ebbd775d60a3306756c 2500w" />

Recraft Image to Image 节点通过 Recraft 的 API 将参考图像和文本提示词生成新的图像。

## 参数说明

### 基本参数

| 参数     | 类型  | 默认值 | 说明          |
| ------ | --- | --- | ----------- |
| image  | 图像  | -   | 作为参考的输入图像   |
| prompt | 字符串 | ""  | 生成图像的文本描述   |
| n      | 整数  | 1   | 生成图像数量(1-6) |
| seed   | 整数  | 0   | 随机种子值       |

### 可选参数

| 参数                | 类型               | 说明          |
| ----------------- | ---------------- | ----------- |
| recraft\_style    | Recraft Style    | 设置生成图像的风格   |
| negative\_prompt  | 字符串              | 指定不希望出现的元素  |
| recraft\_controls | Recraft Controls | 附加控制参数(颜色等) |

### 输出

| 输出    | 类型 | 说明      |
| ----- | -- | ------- |
| IMAGE | 图像 | 生成的图像结果 |

## 源码参考

\[节点源码 (更新于2025-05-03)]

```python  theme={null}

class RecraftImageToImageNode:
    """
    Modify image based on prompt and strength.
    """

    RETURN_TYPES = (IO.IMAGE,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/image/Recraft"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": (IO.IMAGE, ),
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Prompt for the image generation.",
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
                "strength": (
                    IO.FLOAT,
                    {
                        "default": 0.5,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                        "tooltip": "Defines the difference with the original image, should lie in [0, 1], where 0 means almost identical, and 1 means miserable similarity."
                    }
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
                "recraft_style": (RecraftIO.STYLEV3,),
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
        image: torch.Tensor,
        prompt: str,
        n: int,
        strength: float,
        seed,
        auth_token=None,
        recraft_style: RecraftStyle = None,
        negative_prompt: str = None,
        recraft_controls: RecraftControls = None,
        **kwargs,
    ):
        default_style = RecraftStyle(RecraftStyleV3.realistic_image)
        if recraft_style is None:
            recraft_style = default_style

        controls_api = None
        if recraft_controls:
            controls_api = recraft_controls.create_api_model()

        if not negative_prompt:
            negative_prompt = None

        request = RecraftImageGenerationRequest(
            prompt=prompt,
            negative_prompt=negative_prompt,
            model=RecraftModel.recraftv3,
            n=n,
            strength=round(strength, 2),
            style=recraft_style.style,
            substyle=recraft_style.substyle,
            style_id=recraft_style.style_id,
            controls=controls_api,
            random_seed=seed,
        )

        images = []
        total = image.shape[0]
        pbar = ProgressBar(total)
        for i in range(total):
            sub_bytes = handle_recraft_file_request(
                image=image[i],
                path="/proxy/recraft/images/imageToImage",
                request=request,
                auth_token=auth_token,
            )
            images.append(torch.cat([bytesio_to_image_tensor(x) for x in sub_bytes], dim=0))
            pbar.update(1)

        images_tensor = torch.cat(images, dim=0)
        return (images_tensor, )
```
