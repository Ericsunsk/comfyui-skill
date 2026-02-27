> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Stability AI Stable Diffusion 3.5 - ComfyUI Native Node Documentation

> A node that generates high-quality images using Stability AI Stable Diffusion 3.5 model

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-sd-3-5.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=535150f9957846dbd63d16c62e9de695" alt="ComfyUI Native Stability AI Stable Diffusion 3.5 Node" data-og-width="1731" width="1731" data-og-height="1332" height="1332" data-path="images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-sd-3-5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-sd-3-5.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d1a49ecbfa9f49b4ac66408422974a37 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-sd-3-5.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b2d60eba5c6ce54f51c96826505cab45 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-sd-3-5.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6e2616bd4d7d938526b450be1abfbcb8 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-sd-3-5.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=bf52f7b97c394cc9f29c3a3cc5be680f 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-sd-3-5.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=41c37aeb008c30367878026fe880eda2 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-sd-3-5.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b699433ce2e188c5101ea18b53f56d44 2500w" />

The Stability AI Stable Diffusion 3.5 Image node uses Stability AI's Stable Diffusion 3.5 API to generate high-quality images. It supports both text-to-image and image-to-image generation, capable of creating detailed visual content from text prompts.

## Parameters

### Required Parameters

| Parameter     | Type    | Default | Description                                                                                                                                       |
| ------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| prompt        | string  | ""      | What you want to see in the output image. Strong, descriptive prompts that clearly define elements, colors and themes will yield better results   |
| model         | select  | -       | Choose which Stability SD 3.5 model to use                                                                                                        |
| aspect\_ratio | select  | "1:1"   | Width to height ratio of generated image                                                                                                          |
| style\_preset | select  | "None"  | Optional preset style for the desired image                                                                                                       |
| cfg\_scale    | float   | 4.0     | How strictly the diffusion process adheres to the prompt text (higher values keep your image closer to your prompt). Range: 1.0 - 10.0, Step: 0.1 |
| seed          | integer | 0       | Random seed for noise generation (0-4294967294)                                                                                                   |

### Optional Parameters

| Parameter        | Type   | Default | Description                                                                                                                                                                             |
| ---------------- | ------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| image            | image  | -       | Input image. When provided, the node switches to image-to-image mode                                                                                                                    |
| negative\_prompt | string | ""      | Keywords of what you don't want to see in the output image. This is an advanced feature                                                                                                 |
| image\_denoise   | float  | 0.5     | Denoising strength for input image. 0.0 yields image identical to input, 1.0 is as if no image was provided at all. Range: 0.0 - 1.0, Step: 0.01. Only effective when image is provided |

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| IMAGE  | image | Generated image |

## Usage Example

<Card title="Stability AI Stable Diffusion 3.5 Image Workflow Example" icon="book" href="/tutorials/partner-nodes/stability-ai/stable-diffusion-3-5-image">
  Stability AI Stable Diffusion 3.5 Image Workflow Example
</Card>

## Notes

* When an input image is provided, the node switches from text-to-image mode to image-to-image mode
* In image-to-image mode, aspect ratio parameters are ignored
* Mode selection automatically switches based on whether an image is provided:
  * No image provided: text-to-image mode
  * Image provided: image-to-image mode
* If style\_preset is set to "None", no preset style will be applied

## Source Code

\[Node source code (Updated on 2025-05-07)]

```python  theme={null}
class StabilityStableImageSD_3_5Node:
    """
    Generates images synchronously based on prompt and resolution.
    """

    RETURN_TYPES = (IO.IMAGE,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/image/Stability AI"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "What you wish to see in the output image. A strong, descriptive prompt that clearly defines elements, colors, and subjects will lead to better results."
                    },
                ),
                "model": ([x.value for x in Stability_SD3_5_Model],),
                "aspect_ratio": ([x.value for x in StabilityAspectRatio],
                    {
                        "default": StabilityAspectRatio.ratio_1_1,
                        "tooltip": "Aspect ratio of generated image.",
                    },
                ),
                "style_preset": (get_stability_style_presets(),
                    {
                        "tooltip": "Optional desired style of generated image.",
                    },
                ),
                "cfg_scale": (
                    IO.FLOAT,
                    {
                        "default": 4.0,
                        "min": 1.0,
                        "max": 10.0,
                        "step": 0.1,
                        "tooltip": "How strictly the diffusion process adheres to the prompt text (higher values keep your image closer to your prompt)",
                    },
                ),
                "seed": (
                    IO.INT,
                    {
                        "default": 0,
                        "min": 0,
                        "max": 4294967294,
                        "control_after_generate": True,
                        "tooltip": "The random seed used for creating the noise.",
                    },
                ),
            },
            "optional": {
                "image": (IO.IMAGE,),
                "negative_prompt": (
                    IO.STRING,
                    {
                        "default": "",
                        "forceInput": True,
                        "tooltip": "Keywords of what you do not wish to see in the output image. This is an advanced feature."
                    },
                ),
                "image_denoise": (
                    IO.FLOAT,
                    {
                        "default": 0.5,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                        "tooltip": "Denoise of input image; 0.0 yields image identical to input, 1.0 is as if no image was provided at all.",
                    },
                ),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    def api_call(self, model: str, prompt: str, aspect_ratio: str, style_preset: str, seed: int, cfg_scale: float,
                 negative_prompt: str=None, image: torch.Tensor = None, image_denoise: float=None,
                 auth_token=None):
        validate_string(prompt, strip_whitespace=False)
        # prepare image binary if image present
        image_binary = None
        mode = Stability_SD3_5_GenerationMode.text_to_image
        if image is not None:
            image_binary = tensor_to_bytesio(image, total_pixels=1504*1504).read()
            mode = Stability_SD3_5_GenerationMode.image_to_image
            aspect_ratio = None
        else:
            image_denoise = None

        if not negative_prompt:
            negative_prompt = None
        if style_preset == "None":
            style_preset = None

        files = {
            "image": image_binary
        }

        operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path="/proxy/stability/v2beta/stable-image/generate/sd3",
                method=HttpMethod.POST,
                request_model=StabilityStable3_5Request,
                response_model=StabilityStableUltraResponse,
            ),
            request=StabilityStable3_5Request(
                prompt=prompt,
                negative_prompt=negative_prompt,
                aspect_ratio=aspect_ratio,
                seed=seed,
                strength=image_denoise,
                style_preset=style_preset,
                cfg_scale=cfg_scale,
                model=model,
                mode=mode,
            ),
            files=files,
            content_type="multipart/form-data",
            auth_token=auth_token,
        )
        response_api = operation.execute()

        if response_api.finish_reason != "SUCCESS":
            raise Exception(f"Stable Diffusion 3.5 Image generation failed: {response_api.finish_reason}.")

        image_data = base64.b64decode(response_api.image)
        returned_image = bytesio_to_image_tensor(BytesIO(image_data))

        return (returned_image,)
```
