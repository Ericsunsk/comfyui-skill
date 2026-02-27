> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Ideogram V2 - ComfyUI Built-in Node Documentation

> Node for creating high-quality images and text rendering using Ideogram V2 API

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v2.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b9df9b148b7fdd0552ee35417c59a769" alt="ComfyUI Built-in Ideogram V2 Node" data-og-width="1731" width="1731" data-og-height="1549" height="1549" data-path="images/built-in-nodes/api_nodes/ideogram/ideogram-v2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v2.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=badf9dba828282b1c95733987eb72e16 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v2.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4dda2cc921e486f5365c3bdcd30698f0 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v2.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7dc5e5f0bd31dc7ecb91d23f8e32a310 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v2.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=db0be8dfbe7887459475e00c328ead6d 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v2.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=27768b2fd49e3b66c29911288e8b95c0 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v2.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4cc40653275b5e6b04fce642c4fa2993 2500w" />

The Ideogram V2 node allows you to generate more refined images using Ideogram's second-generation AI model, with significant improvements in text rendering, image quality, and overall aesthetics.

## Parameters

### Required Parameters

| Parameter | Type    | Default | Description                                                           |
| --------- | ------- | ------- | --------------------------------------------------------------------- |
| prompt    | string  | ""      | Text prompt describing the content to generate                        |
| turbo     | boolean | False   | Whether to use turbo mode (faster generation, possibly lower quality) |

### Optional Parameters

| Parameter             | Type     | Default | Description                                                                                                     |
| --------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| aspect\_ratio         | dropdown | "1:1"   | Image aspect ratio, effective when resolution is set to "Auto"                                                  |
| resolution            | dropdown | "Auto"  | Output image resolution, if not set to "Auto", it will override the aspect\_ratio setting                       |
| magic\_prompt\_option | dropdown | "AUTO"  | Determines whether to use MagicPrompt feature during generation, options are \["AUTO", "ON", "OFF"]             |
| seed                  | integer  | 0       | Random seed value, range 0-2147483647                                                                           |
| style\_type           | dropdown | "NONE"  | Generation style type (V2 only), options are \["AUTO", "GENERAL", "REALISTIC", "DESIGN", "RENDER\_3D", "ANIME"] |
| negative\_prompt      | string   | ""      | Specifies elements you don't want to appear in the image                                                        |
| num\_images           | integer  | 1       | Number of images to generate, range 1-8                                                                         |

### Output

| Output | Type  | Description        |
| ------ | ----- | ------------------ |
| IMAGE  | image | Generated image(s) |

## Source Code

\[Node Source Code (Updated on 2025-05-03)]

```python  theme={null}

class IdeogramV2(ComfyNodeABC):
    """
    Generates images synchronously using the Ideogram V2 model.

    Images links are available for a limited period of time; if you would like to keep the image, you must download it.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> InputTypeDict:
        return {
            "required": {
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Prompt for the image generation",
                    },
                ),
                "turbo": (
                    IO.BOOLEAN,
                    {
                        "default": False,
                        "tooltip": "Whether to use turbo mode (faster generation, potentially lower quality)",
                    }
                ),
            },
            "optional": {
                "aspect_ratio": (
                    IO.COMBO,
                    {
                        "options": list(V1_V2_RATIO_MAP.keys()),
                        "default": "1:1",
                        "tooltip": "The aspect ratio for image generation. Ignored if resolution is not set to AUTO.",
                    },
                ),
                "resolution": (
                    IO.COMBO,
                    {
                        "options": list(V1_V1_RES_MAP.keys()),
                        "default": "Auto",
                        "tooltip": "The resolution for image generation. If not set to AUTO, this overrides the aspect_ratio setting.",
                    },
                ),
                "magic_prompt_option": (
                    IO.COMBO,
                    {
                        "options": ["AUTO", "ON", "OFF"],
                        "default": "AUTO",
                        "tooltip": "Determine if MagicPrompt should be used in generation",
                    },
                ),
                "seed": (
                    IO.INT,
                    {
                        "default": 0,
                        "min": 0,
                        "max": 2147483647,
                        "step": 1,
                        "control_after_generate": True,
                        "display": "number",
                    },
                ),
                "style_type": (
                    IO.COMBO,
                    {
                        "options": ["AUTO", "GENERAL", "REALISTIC", "DESIGN", "RENDER_3D", "ANIME"],
                        "default": "NONE",
                        "tooltip": "Style type for generation (V2 only)",
                    },
                ),
                "negative_prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Description of what to exclude from the image",
                    },
                ),
                "num_images": (
                    IO.INT,
                    {"default": 1, "min": 1, "max": 8, "step": 1, "display": "number"},
                ),
                #"color_palette": (
                #    IO.STRING,
                #    {
                #        "multiline": False,
                #        "default": "",
                #        "tooltip": "Color palette preset name or hex colors with weights",
                #    },
                #),
            },
            "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
        }

    RETURN_TYPES = (IO.IMAGE,)
    FUNCTION = "api_call"
    CATEGORY = "api node/image/ideogram/v2"
    DESCRIPTION = cleandoc(__doc__ or "")
    API_NODE = True

    def api_call(
        self,
        prompt,
        turbo=False,
        aspect_ratio="1:1",
        resolution="Auto",
        magic_prompt_option="AUTO",
        seed=0,
        style_type="NONE",
        negative_prompt="",
        num_images=1,
        color_palette="",
        auth_token=None,
    ):
        aspect_ratio = V1_V2_RATIO_MAP.get(aspect_ratio, None)
        resolution = V1_V1_RES_MAP.get(resolution, None)
        # Determine the model based on turbo setting
        model = "V_2_TURBO" if turbo else "V_2"

        # Handle resolution vs aspect_ratio logic
        # If resolution is not AUTO, it overrides aspect_ratio
        final_resolution = None
        final_aspect_ratio = None

        if resolution != "AUTO":
            final_resolution = resolution
        else:
            final_aspect_ratio = aspect_ratio if aspect_ratio != "ASPECT_1_1" else None

        operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path="/proxy/ideogram/generate",
                method=HttpMethod.POST,
                request_model=IdeogramGenerateRequest,
                response_model=IdeogramGenerateResponse,
            ),
            request=IdeogramGenerateRequest(
                image_request=ImageRequest(
                    prompt=prompt,
                    model=model,
                    num_images=num_images,
                    seed=seed,
                    aspect_ratio=final_aspect_ratio,
                    resolution=final_resolution,
                    magic_prompt_option=(
                        magic_prompt_option if magic_prompt_option != "AUTO" else None
                    ),
                    style_type=style_type if style_type != "NONE" else None,
                    negative_prompt=negative_prompt if negative_prompt else None,
                    color_palette=color_palette if color_palette else None,
                )
            ),
            auth_token=auth_token,
        )

        response = operation.execute()

        if not response.data or len(response.data) == 0:
            raise Exception("No images were generated in the response")

        image_urls = [image_data.url for image_data in response.data if image_data.url]

        if not image_urls:
            raise Exception("No image URLs were generated in the response")

        return (download_and_process_images(image_urls),)

```
