> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Image Inpainting - ComfyUI 原生节点文档

> 使用Recraft API选择性地修改图像区域

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-inpainting.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ce37045a2a53e129f5bec3e425f0002b" alt="ComfyUI 原生Recraft Image Inpainting节点" data-og-width="1731" width="1731" data-og-height="1109" height="1109" data-path="images/built-in-nodes/api_nodes/recraft/recraft-image-inpainting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-inpainting.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d07ac3bf1ac8adc554c7e5501ade97c0 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-inpainting.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1bf04240ed1b57ef3d29e7237bd80200 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-inpainting.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7bd6ae3d2278cae4bd26590dc97fce31 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-inpainting.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=bebca092cdfa569d08e73fcab712541a 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-inpainting.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=02ea2f2c6ffead1cb6631a256e00176b 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-image-inpainting.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c913e6fc3844208d68cfca9745c1fa7b 2500w" />

Recraft Image Inpainting 节点允许你选择性地修改图像的特定区域，保持其余部分不变。通过提供图像、蒙版和文本提示词，可以精确地生成新内容填充指定区域。

## 参数说明

### 基本参数

| 参数     | 类型  | 默认值 | 说明            |
| ------ | --- | --- | ------------- |
| image  | 图像  | -   | 需要修改的输入图像     |
| mask   | 蒙版  | -   | 定义要修改区域的黑白蒙版  |
| prompt | 字符串 | ""  | 描述要在蒙版区域生成的内容 |
| n      | 整数  | 1   | 生成结果的数量(1-6)  |
| seed   | 整数  | 0   | 随机种子值         |

### 可选参数

| 参数                | 类型               | 说明               |
| ----------------- | ---------------- | ---------------- |
| recraft\_style    | Recraft Style    | 设置生成内容的风格        |
| negative\_prompt  | 字符串              | 指定不希望在生成内容中出现的元素 |
| recraft\_controls | Recraft Controls | 附加控制参数(颜色等)      |

### 输出

| 输出    | 类型 | 说明       |
| ----- | -- | -------- |
| IMAGE | 图像 | 修改后的图像结果 |

## 源码参考

\[节点源码 (更新于2025-05-03)]

```python  theme={null}
class RecraftImageInpaintingNode:
    """
    Modify image based on prompt and mask.
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
                "mask": (IO.MASK, ),
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
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    def api_call(
        self,
        image: torch.Tensor,
        mask: torch.Tensor,
        prompt: str,
        n: int,
        seed,
        auth_token=None,
        recraft_style: RecraftStyle = None,
        negative_prompt: str = None,
        **kwargs,
    ):
        default_style = RecraftStyle(RecraftStyleV3.realistic_image)
        if recraft_style is None:
            recraft_style = default_style

        if not negative_prompt:
            negative_prompt = None

        request = RecraftImageGenerationRequest(
            prompt=prompt,
            negative_prompt=negative_prompt,
            model=RecraftModel.recraftv3,
            n=n,
            style=recraft_style.style,
            substyle=recraft_style.substyle,
            style_id=recraft_style.style_id,
            random_seed=seed,
        )

        # prepare mask tensor
        _, H, W, _ = image.shape
        mask = mask.unsqueeze(-1)
        mask = mask.movedim(-1,1)
        mask = common_upscale(mask, width=W, height=H, upscale_method="nearest-exact", crop="disabled")
        mask = mask.movedim(1,-1)
        mask = (mask > 0.5).float()

        images = []
        total = image.shape[0]
        pbar = ProgressBar(total)
        for i in range(total):
            sub_bytes = handle_recraft_file_request(
                image=image[i],
                mask=mask[i:i+1],
                path="/proxy/recraft/images/inpaint",
                request=request,
                auth_token=auth_token,
            )
            images.append(torch.cat([bytesio_to_image_tensor(x) for x in sub_bytes], dim=0))
            pbar.update(1)

        images_tensor = torch.cat(images, dim=0)
        return (images_tensor, )
```
