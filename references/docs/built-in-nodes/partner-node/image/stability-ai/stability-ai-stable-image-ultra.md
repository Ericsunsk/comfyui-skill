> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Stability Stable Image Ultra - ComfyUI Native Node Documentation

> A node that generates high-quality images using Stability AI's ultra stable diffusion model

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-ultra.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9e4876faeb241e65b347da9ec53420b6" alt="ComfyUI Native Stability Stable Image Ultra Node" data-og-width="1731" width="1731" data-og-height="1499" height="1499" data-path="images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-ultra.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-ultra.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=bd79cfb4090cde78bd5ad5388c36c9b3 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-ultra.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=077579812d5c8c643eedf8a23f04d968 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-ultra.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6fe6deae28ddf0195d504fa88b827e96 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-ultra.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a6005153737e4859d10dc8de41beed75 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-ultra.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c08475f82b9c7fce6ff0f84d38543cdb 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/api_nodes/stability-ai/stability-ai-stable-image-ultra.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ea0703fd121790af89fd74fb1cb7ed64 2500w" />

The Stability Stable Image Ultra node uses Stability AI's Stable Diffusion Ultra API to generate high-quality images. It supports both text-to-image and image-to-image generation, creating detailed and artistic visuals from text prompts.

## Parameters

### Required Parameters

| Parameter     | Type    | Default | Description                                                                                                                                                                                                                                                                                                               |
| ------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| prompt        | string  | ""      | Text description of what you want to generate. Better results come from clear, descriptive prompts that specify elements, colors and themes. You can control word importance using `(word:weight)` format, where weight is 0-1. For example: `The sky was (blue:0.3) and (green:0.8)` makes the sky more green than blue. |
| aspect\_ratio | select  | "1:1"   | Width to height ratio of output image                                                                                                                                                                                                                                                                                     |
| style\_preset | select  | "None"  | Optional preset style for generated image                                                                                                                                                                                                                                                                                 |
| seed          | integer | 0       | Random seed for noise generation (0-4294967294)                                                                                                                                                                                                                                                                           |

### Optional Parameters

| Parameter        | Type   | Default | Description                                                                                                      |
| ---------------- | ------ | ------- | ---------------------------------------------------------------------------------------------------------------- |
| image            | image  | -       | Input image for image-to-image generation                                                                        |
| negative\_prompt | string | ""      | Describes what you don't want in the output image. This is an advanced feature                                   |
| image\_denoise   | float  | 0.5     | Denoising strength for input image (0.0-1.0). 0.0 keeps input image unchanged, 1.0 is like having no input image |

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| IMAGE  | image | Generated image |

## Notes

* image\_denoise has no effect when no input image is provided
* No preset style is applied when style\_preset is "None"
* For image-to-image, input images are converted to the proper format before API submission

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}

class StabilityStableImageUltraNode:
    """
    Generates images synchronously based on prompt and resolution.
    """

    RETURN_TYPES = (IO.IMAGE,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/image/stability"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "What you wish to see in the output image. A strong, descriptive prompt that clearly defines" +
                                    "What you wish to see in the output image. A strong, descriptive prompt that clearly defines" +
                                    "elements, colors, and subjects will lead to better results. " +
                                    "To control the weight of a given word use the format `(word:weight)`," +
                                    "where `word` is the word you'd like to control the weight of and `weight`" +
                                    "is a value between 0 and 1. For example: `The sky was a crisp (blue:0.3) and (green:0.8)`" +
                                    "would convey a sky that was blue and green, but more green than blue."
                    },
                ),
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
                        "tooltip": "A blurb of text describing what you do not wish to see in the output image. This is an advanced feature."
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

    def api_call(self, prompt: str, aspect_ratio: str, style_preset: str, seed: int,
                 negative_prompt: str=None, image: torch.Tensor = None, image_denoise: float=None,
                 auth_token=None):
        # prepare image binary if image present
        image_binary = None
        if image is not None:
            image_binary = tensor_to_bytesio(image, 1504 * 1504).read()
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
                path="/proxy/stability/v2beta/stable-image/generate/ultra",
                method=HttpMethod.POST,
                request_model=StabilityStableUltraRequest,
                response_model=StabilityStableUltraResponse,
            ),
            request=StabilityStableUltraRequest(
                prompt=prompt,
                negative_prompt=negative_prompt,
                aspect_ratio=aspect_ratio,
                seed=seed,
                strength=image_denoise,
                style_preset=style_preset,
            ),
            files=files,
            content_type="multipart/form-data",
            auth_token=auth_token,
        )
        response_api = operation.execute()

        if response_api.finish_reason != "SUCCESS":
            raise Exception(f"Stable Image Ultra generation failed: {response_api.finish_reason}.")

        image_data = base64.b64decode(response_api.image)
        returned_image = bytesio_to_image_tensor(BytesIO(image_data))

        return (returned_image,)


```
