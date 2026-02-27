> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Ideogram V1 - ComfyUI Native Node Documentation

> Node for creating precise text rendering images using Ideogram API

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v1.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=10b0ea0f9a0ddb9c1184540f977e2cef" alt="ComfyUI Native Ideogram V1 Node" data-og-width="1731" width="1731" data-og-height="1374" height="1374" data-path="images/built-in-nodes/api_nodes/ideogram/ideogram-v1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v1.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=95b9ab3556b117e6dcededef89df7f05 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v1.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c1d4b0ff22e2e42f5aa598680e5aaa93 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v1.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1c00cda4beee6d743b5f85d4ea399bda 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v1.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e06aba34eb0a3ddc3f84c59486c5b7f3 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v1.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=29e030418b7b97ad941342ea49904c11 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/ideogram/ideogram-v1.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9acea2d45fbcc54c7c52a522adc6777f 2500w" />

The Ideogram V1 node allows you to generate images with high-quality text rendering capabilities using Ideogram's text-to-image API.

## Parameter Description

### Required Parameters

| Parameter             | Type    | Default | Description                                                                 |
| --------------------- | ------- | ------- | --------------------------------------------------------------------------- |
| prompt                | string  | ""      | Text prompt describing the content to generate                              |
| turbo                 | boolean | False   | Whether to use turbo mode (faster but possibly lower quality)               |
| aspect\_ratio         | select  | "1:1"   | Image aspect ratio                                                          |
| magic\_prompt\_option | select  | "AUTO"  | Determines whether to use MagicPrompt in generation, options: AUTO, ON, OFF |
| seed                  | integer | 0       | Random seed value (0-2147483647)                                            |
| negative\_prompt      | string  | ""      | Specifies elements you don't want in the image                              |
| num\_images           | integer | 1       | Number of images to generate (1-8)                                          |

### Output

| Output | Type  | Description            |
| ------ | ----- | ---------------------- |
| IMAGE  | image | Generated image result |

## Source Code

\[Node Source Code (Updated on 2025-05-03)]

```python  theme={null}
class IdeogramV1(ComfyNodeABC):
    """
    Generates images synchronously using the Ideogram V1 model.

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
                        "tooltip": "The aspect ratio for image generation.",
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
            },
            "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
        }

    RETURN_TYPES = (IO.IMAGE,)
    FUNCTION = "api_call"
    CATEGORY = "api node/image/ideogram/v1"
    DESCRIPTION = cleandoc(__doc__ or "")
    API_NODE = True

    def api_call(
        self,
        prompt,
        turbo=False,
        aspect_ratio="1:1",
        magic_prompt_option="AUTO",
        seed=0,
        negative_prompt="",
        num_images=1,
        auth_token=None,
    ):
        # Determine the model based on turbo setting
        aspect_ratio = V1_V2_RATIO_MAP.get(aspect_ratio, None)
        model = "V_1_TURBO" if turbo else "V_1"

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
                    aspect_ratio=aspect_ratio if aspect_ratio != "ASPECT_1_1" else None,
                    magic_prompt_option=(
                        magic_prompt_option if magic_prompt_option != "AUTO" else None
                    ),
                    negative_prompt=negative_prompt if negative_prompt else None,
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
