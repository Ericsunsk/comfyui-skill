> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI DALL·E 2 - ComfyUI Native Node Documentation

> Node for generating images using OpenAI's DALL·E 2 model

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-2.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=2a1ad9dab55bb9b02c4551dbf05078ff" alt="ComfyUI Native Stability AI Stable Image Ultra Node" data-og-width="1576" width="1576" data-og-height="954" height="954" data-path="images/built-in-nodes/api_nodes/openai/openai-dall-e-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-2.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=53b28734e20336b812c35ffea924981b 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-2.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b30dbe9ccd774fe3571a3906a17bda65 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-2.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=be84d3151baae3d9ac80a9bccdacad6f 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-2.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b941cec97ff07c2d88f89dee636cea5e 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-2.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a4665033990c3947974a9befb8293466 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/openai/openai-dall-e-2.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c727c2192f64c414a57ad745fc6faccf 2500w" />

The OpenAI DALL·E 2 node allows you to use OpenAI's DALL·E 2 API to generate creative images from text descriptions.

## Parameters

### Basic Parameters

| Parameter | Type    | Default     | Description                                                                                          |
| --------- | ------- | ----------- | ---------------------------------------------------------------------------------------------------- |
| prompt    | string  | ""          | Text prompt for DALL·E to generate images, supports multi-line input                                 |
| seed      | integer | 0           | The result is not actually related to the seed, this parameter only determines whether to re-execute |
| size      | select  | "1024x1024" | Output image size, options: 256x256, 512x512, 1024x1024                                              |
| n         | integer | 1           | Number of images to generate, range 1-8                                                              |

### Optional Parameters

| Parameter | Type  | Default | Description                                                 |
| --------- | ----- | ------- | ----------------------------------------------------------- |
| image     | image | None    | Optional reference image for image editing                  |
| mask      | mask  | None    | Optional mask for inpainting (white areas will be replaced) |

### Output

| Output | Type  | Description        |
| ------ | ----- | ------------------ |
| IMAGE  | image | Generated image(s) |

## Features

* Basic function: Generate images from text prompts
* Image editing: When both image and mask parameters are provided, performs image editing (white masked areas will be replaced)

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}

class OpenAIDalle2(ComfyNodeABC):
    """
    Generates images synchronously via OpenAI's DALL·E 2 endpoint.

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
                "size": (
                    IO.COMBO,
                    {
                        "options": ["256x256", "512x512", "1024x1024"],
                        "default": "1024x1024",
                        "tooltip": "Image size",
                    },
                ),
                "n": (
                    IO.INT,
                    {
                        "default": 1,
                        "min": 1,
                        "max": 8,
                        "step": 1,
                        "display": "number",
                        "tooltip": "How many images to generate",
                    },
                ),
                "image": (
                    IO.IMAGE,
                    {
                        "default": None,
                        "tooltip": "Optional reference image for image editing.",
                    },
                ),
                "mask": (
                    IO.MASK,
                    {
                        "default": None,
                        "tooltip": "Optional mask for inpainting (white areas will be replaced)",
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
        image=None,
        mask=None,
        n=1,
        size="1024x1024",
        auth_token=None,
    ):
        model = "dall-e-2"
        path = "/proxy/openai/images/generations"
        content_type = "application/json"
        request_class = OpenAIImageGenerationRequest
        img_binary = None

        if image is not None and mask is not None:
            path = "/proxy/openai/images/edits"
            content_type = "multipart/form-data"
            request_class = OpenAIImageEditRequest

            input_tensor = image.squeeze().cpu()
            height, width, channels = input_tensor.shape
            rgba_tensor = torch.ones(height, width, 4, device="cpu")
            rgba_tensor[:, :, :channels] = input_tensor

            if mask.shape[1:] != image.shape[1:-1]:
                raise Exception("Mask and Image must be the same size")
            rgba_tensor[:, :, 3] = 1 - mask.squeeze().cpu()

            rgba_tensor = downscale_image_tensor(rgba_tensor.unsqueeze(0)).squeeze()

            image_np = (rgba_tensor.numpy() * 255).astype(np.uint8)
            img = Image.fromarray(image_np)
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format="PNG")
            img_byte_arr.seek(0)
            img_binary = img_byte_arr  # .getvalue()
            img_binary.name = "image.png"
        elif image is not None or mask is not None:
            raise Exception("Dall-E 2 image editing requires an image AND a mask")

        # Build the operation
        operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path=path,
                method=HttpMethod.POST,
                request_model=request_class,
                response_model=OpenAIImageGenerationResponse,
            ),
            request=request_class(
                model=model,
                prompt=prompt,
                n=n,
                size=size,
                seed=seed,
            ),
            files=(
                {
                    "image": img_binary,
                }
                if img_binary
                else None
            ),
            content_type=content_type,
            auth_token=auth_token,
        )

        response = operation.execute()

        img_tensor = validate_and_cast_response(response)
        return (img_tensor,)
```
