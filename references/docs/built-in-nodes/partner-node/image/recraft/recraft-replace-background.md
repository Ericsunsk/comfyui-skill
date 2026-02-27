> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Replace Background - ComfyUI Native Node Documentation

> A Recraft Partner node that automatically detects foreground subjects and replaces backgrounds

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-replace-background.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=798d76cef5bcc224546b066e8a9b2db2" alt="ComfyUI Native Recraft Replace Background Node" data-og-width="1625" width="1625" data-og-height="1158" height="1158" data-path="images/built-in-nodes/api_nodes/recraft/recraft-replace-background.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-replace-background.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=517a4b80ea434c8d62f20b0d1ff48a5d 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-replace-background.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=085a235f7d2f230c840e6458685ce85d 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-replace-background.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=49a62e636876eba8670f60e71f9e129c 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-replace-background.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=66af47ca9c4dad461dbce9ff2ab93702 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-replace-background.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=564fe13233e518e89815e6393296f423 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-replace-background.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c0ea9a57f6f4e7efea60820441a4291b 2500w" />

The Recraft Replace Background node uses Recraft's API to intelligently detect subjects in images and generate new backgrounds based on text prompts.

## Parameters

### Basic Parameters

| Parameter | Type    | Default | Description                           |
| --------- | ------- | ------- | ------------------------------------- |
| image     | image   | -       | Input image with subject to preserve  |
| prompt    | string  | ""      | Text prompt for background generation |
| n         | integer | 1       | Number of images to generate (1-6)    |
| seed      | integer | 0       | Random seed value for node re-runs    |

### Optional Parameters

| Parameter        | Type          | Description                              |
| ---------------- | ------------- | ---------------------------------------- |
| recraft\_style   | Recraft Style | Style settings for background generation |
| negative\_prompt | string        | Text describing elements to avoid        |

### Output

| Output | Type  | Description                          |
| ------ | ----- | ------------------------------------ |
| IMAGE  | image | Final image with replaced background |

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}

class RecraftReplaceBackgroundNode:
    """
    Replace background on image, based on provided prompt.
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
        )

        images = []
        total = image.shape[0]
        pbar = ProgressBar(total)
        for i in range(total):
            sub_bytes = handle_recraft_file_request(
                image=image[i],
                path="/proxy/recraft/images/replaceBackground",
                request=request,
                auth_token=auth_token,
            )
            images.append(torch.cat([bytesio_to_image_tensor(x) for x in sub_bytes], dim=0))
            pbar.update(1)

        images_tensor = torch.cat(images, dim=0)
        return (images_tensor, )

```
