> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Text to Image - ComfyUI Built-in Node Documentation

> A Recraft Partner node that generates high-quality images from text descriptions

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0cb81000a29e5fadef2c0e5e164ca60f" alt="ComfyUI Built-in Recraft Text to Image Node" data-og-width="1731" width="1731" data-og-height="1138" height="1138" data-path="images/built-in-nodes/api_nodes/recraft/recraft-text-to-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9f82afc139628c1a109950e976d0dea6 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d7661bde04e3af82c067e07706982a97 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4368ef74c90010ff2a46058bd0d08a58 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9564343bb32ef404cbc57fe069b3c06e 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=bf084b9a7ded85168483158941b471ed 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-text-to-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ac7bffe9d2d364da06aa6af84a75edad 2500w" />

The Recraft Text to Image node lets you generate high-quality images from text prompts by directly connecting to Recraft AI's image generation API to create images in various styles.

## Parameters

### Basic Parameters

| Parameter | Type   | Default   | Description                    |
| --------- | ------ | --------- | ------------------------------ |
| prompt    | string | ""        | Text description for the image |
| size      | select | 1024x1024 | Output image size              |
| n         | int    | 1         | Number of images (1-6)         |
| seed      | int    | 0         | Random seed value              |

### Optional Parameters

| Parameter         | Type             | Description                                       |
| ----------------- | ---------------- | ------------------------------------------------- |
| recraft\_style    | Recraft Style    | Image style setting, default is "realistic photo" |
| negative\_prompt  | string           | Elements to exclude from generation               |
| recraft\_controls | Recraft Controls | Additional control parameters (colors, etc.)      |

### Output

| Output | Type  | Description        |
| ------ | ----- | ------------------ |
| IMAGE  | image | Generated image(s) |

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}
class RecraftTextToImageNode:
    """
    Generates images synchronously based on prompt and resolution.
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
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Prompt for the image generation.",
                    },
                ),
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
        prompt: str,
        size: str,
        n: int,
        seed,
        recraft_style: RecraftStyle = None,
        negative_prompt: str = None,
        recraft_controls: RecraftControls = None,
        auth_token=None,
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
                style_id=recraft_style.style_id,
                controls=controls_api,
            ),
            auth_token=auth_token,
        )
        response: RecraftImageGenerationResponse = operation.execute()
        images = []
        for data in response.data:
            image = bytesio_to_image_tensor(
                download_url_to_bytesio(data.url, timeout=1024)
            )
            if len(image.shape) < 4:
                image = image.unsqueeze(0)
            images.append(image)
        output_image = torch.cat(images, dim=0)

        return (output_image,)
```
