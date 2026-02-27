> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI DALL·E 3 - ComfyUI Native Node Documentation

> Node for generating high-quality images using OpenAI's DALL·E 3 model

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1d4da35db8baddcd1321ef98365e26d0" alt="ComfyUI Native OpenAI DALL·E 3 Node" data-og-width="1576" width="1576" data-og-height="966" height="966" data-path="images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c4991a2a05a37c4f63b9251cc4f5cb66 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=bdb4fb6d52ed938a4a6f3dfb830e79f2 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f4de073cc71e3209f66be6eb0f45a575 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e525c1ca97e0ee9bd5e0b812e812530d 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d50bd7dabc5e9e5adca0683bc6777de4 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-3.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b1867a36a2203ad0a1b2fba9117a42ec 2500w" />

This node connects to OpenAI's DALL·E 3 API, allowing users to generate high-quality images through detailed text prompts. DALL·E 3 is OpenAI's image generation model that offers significantly improved image quality, more accurate prompt understanding, and better detail rendering compared to previous versions.

## Parameters

### Input Parameters

| Parameter | Type      | Default     | Description                                                                                                                                                                         |
| --------- | --------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| prompt    | string    | ""          | Detailed text prompt describing what to generate                                                                                                                                    |
| seed      | integer   | 0           | Final result is not related to seed, this parameter only determines whether to re-execute                                                                                           |
| quality   | selection | "standard"  | Image quality, options: "standard" or "hd"                                                                                                                                          |
| style     | selection | "natural"   | Visual style, options: "natural" or "vivid". "Vivid" makes the model tend to create more surreal and dramatic images, while "natural" generates more realistic, less surreal images |
| size      | selection | "1024x1024" | Output image size, options: "1024x1024", "1024x1792", or "1792x1024"                                                                                                                |

### Output Parameters

| Output | Type  | Description                |
| ------ | ----- | -------------------------- |
| IMAGE  | image | The generated image result |

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}

class OpenAIDalle3(ComfyNodeABC):
    """
    Generates images synchronously via OpenAI's DALL·E 3 endpoint.

    Uses the proxy at /proxy/openai/images/generations. Returned URLs are short‑lived,
    so download or cache results if you need to keep them.
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
                        "tooltip": "Text prompt for DALL·E",
                    },
                ),
            },
            "optional": {
                "seed": (
                    IO.INT,
                    {
                        "default": 0,
                        "min": 0,
                        "max": 2**31 - 1,
                        "step": 1,
                        "display": "number",
                        "control_after_generate": True,
                        "tooltip": "not implemented yet in backend",
                    },
                ),
                "quality": (
                    IO.COMBO,
                    {
                        "options": ["standard", "hd"],
                        "default": "standard",
                        "tooltip": "Image quality",
                    },
                ),
                "style": (
                    IO.COMBO,
                    {
                        "options": ["natural", "vivid"],
                        "default": "natural",
                        "tooltip": "Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images.",
                    },
                ),
                "size": (
                    IO.COMBO,
                    {
                        "options": ["1024x1024", "1024x1792", "1792x1024"],
                        "default": "1024x1024",
                        "tooltip": "Image size",
                    },
                ),
            },
            "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
        }

    RETURN_TYPES = (IO.IMAGE,)
    FUNCTION = "api_call"
    CATEGORY = "api node/image/openai"
    DESCRIPTION = cleandoc(__doc__ or "")
    API_NODE = True

    def api_call(
        self,
        prompt,
        seed=0,
        style="natural",
        quality="standard",
        size="1024x1024",
        auth_token=None,
    ):
        model = "dall-e-3"

        # build the operation
        operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path="/proxy/openai/images/generations",
                method=HttpMethod.POST,
                request_model=OpenAIImageGenerationRequest,
                response_model=OpenAIImageGenerationResponse,
            ),
            request=OpenAIImageGenerationRequest(
                model=model,
                prompt=prompt,
                quality=quality,
                size=size,
                style=style,
                seed=seed,
            ),
            auth_token=auth_token,
        )

        response = operation.execute()

        img_tensor = validate_and_cast_response(response)
        return (img_tensor,)
```
