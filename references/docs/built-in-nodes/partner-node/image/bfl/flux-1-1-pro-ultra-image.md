> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux 1.1 [pro] Ultra Image - ComfyUI Native Node Documentation

> Create images using Black Forest Labs' high-resolution image generation API

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=51f4ad7b93c0df61bcc855eac5324802" alt="ComfyUI Native Flux 1.1 [pro] Ultra Image node" data-og-width="1731" width="1731" data-og-height="1163" height="1163" data-path="images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=2d5e0d3353e130ce452dc6d3748fe40b 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b5594a0b49f78853bb09550ac0500d51 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=174b45e936d2349e977e7d0a68b995b8 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=fe883d69f481734a08e3ec34a9df487a 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=39dc4540e3af081e5eeddfc476ce0a9d 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=904755f3be6c655e228912f05b684ec0 2500w" />

The Flux 1.1 \[pro] Ultra Image node allows you to generate ultra-high-resolution images through text prompts, directly connecting to Black Forest Labs' latest image generation API.

This node supports two main usage modes:

1. **Text-to-Image**: Generate high-quality images from text prompts (when no image input is used)
2. **Image-to-Image**: Combine existing images with prompts to create new images that blend features from both (Remix mode)

This node supports Ultra mode through API calls, capable of generating images at 4 times the resolution of standard Flux 1.1 \[pro] (up to 4MP), without sacrificing prompt adherence, and maintaining super-fast generation times of just 10 seconds. Compared to other high-resolution models, it's more than 2.5 times faster.

## Parameter Description

### Basic Parameters

| Parameter          | Type    | Default | Description                                                                                                                                                                                                                      |
| ------------------ | ------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| prompt             | String  | ""      | Text description for generating the image                                                                                                                                                                                        |
| prompt\_upsampling | Boolean | False   | Whether to use prompt upsampling technique to enhance details. When enabled, automatically modifies prompts for more creative generation, but results become non-deterministic (same seed won't produce exactly the same result) |
| seed               | Integer | 0       | Random seed value, controls generation randomness                                                                                                                                                                                |
| aspect\_ratio      | String  | "16:9"  | Width-to-height ratio of the image, must be between 1:4 and 4:1                                                                                                                                                                  |
| raw                | Boolean | False   | When set to True, generates less processed, more natural-looking images                                                                                                                                                          |

### Optional Parameters

| Parameter               | Type  | Default | Description                                                                                                                                               |
| ----------------------- | ----- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| image\_prompt           | Image | None    | Optional input, used for Image-to-Image (Remix) mode                                                                                                      |
| image\_prompt\_strength | Float | 0.1     | Active when `image_prompt` is input, adjusts the blend between prompt and image prompt. Higher values make output closer to input image, range is 0.0-1.0 |

### Output

| Output | Type  | Description                            |
| ------ | ----- | -------------------------------------- |
| IMAGE  | Image | Generated high-resolution image result |

## Usage Examples

Please visit the tutorial below to see corresponding usage examples

* [Flux 1.1 Pro Ultra Image API Node ComfyUI Official Example Workflow](/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image)

## How It Works

Flux 1.1 \[pro] Ultra mode uses optimized deep learning architecture and efficient GPU acceleration technology to achieve high-resolution image generation without sacrificing speed. When a request is sent to the API, the system parses the prompt, applies appropriate parameters, then computes the image in parallel, finally generating and returning the high-resolution result.

Compared to regular models, Ultra mode particularly focuses on detail preservation and consistency at large scales, ensuring impressive quality even at 4MP high resolution.

## Source Code

\[Node Source Code (Updated on 2025-05-03)]

```python  theme={null}
class FluxProUltraImageNode(ComfyNodeABC):
    """
    Generates images synchronously based on prompt and resolution.
    """

    MINIMUM_RATIO = 1 / 4
    MAXIMUM_RATIO = 4 / 1
    MINIMUM_RATIO_STR = "1:4"
    MAXIMUM_RATIO_STR = "4:1"

    @classmethod
    def INPUT_TYPES(s):
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
                "prompt_upsampling": (
                    IO.BOOLEAN,
                    {
                        "default": False,
                        "tooltip": "Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation, but results are nondeterministic (same seed will not produce exactly the same result).",
                    },
                ),
                "seed": (
                    IO.INT,
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "control_after_generate": True,
                        "tooltip": "The random seed used for creating the noise.",
                    },
                ),
                "aspect_ratio": (
                    IO.STRING,
                    {
                        "default": "16:9",
                        "tooltip": "Aspect ratio of image; must be between 1:4 and 4:1.",
                    },
                ),
                "raw": (
                    IO.BOOLEAN,
                    {
                        "default": False,
                        "tooltip": "When True, generate less processed, more natural-looking images.",
                    },
                ),
            },
            "optional": {
                "image_prompt": (IO.IMAGE,),
                "image_prompt_strength": (
                    IO.FLOAT,
                    {
                        "default": 0.1,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                        "tooltip": "Blend between the prompt and the image prompt.",
                    },
                ),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    @classmethod
    def VALIDATE_INPUTS(cls, aspect_ratio: str):
        try:
            validate_aspect_ratio(
                aspect_ratio,
                minimum_ratio=cls.MINIMUM_RATIO,
                maximum_ratio=cls.MAXIMUM_RATIO,
                minimum_ratio_str=cls.MINIMUM_RATIO_STR,
                maximum_ratio_str=cls.MAXIMUM_RATIO_STR,
            )
        except Exception as e:
            return str(e)
        return True

    RETURN_TYPES = (IO.IMAGE,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/image/bfl"

    def api_call(
        self,
        prompt: str,
        aspect_ratio: str,
        prompt_upsampling=False,
        raw=False,
        seed=0,
        image_prompt=None,
        image_prompt_strength=0.1,
        auth_token=None,
        **kwargs,
    ):
        operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path="/proxy/bfl/flux-pro-1.1-ultra/generate",
                method=HttpMethod.POST,
                request_model=BFLFluxProUltraGenerateRequest,
                response_model=BFLFluxProGenerateResponse,
            ),
            request=BFLFluxProUltraGenerateRequest(
                prompt=prompt,
                prompt_upsampling=prompt_upsampling,
                seed=seed,
                aspect_ratio=validate_aspect_ratio(
                    aspect_ratio,
                    minimum_ratio=self.MINIMUM_RATIO,
                    maximum_ratio=self.MAXIMUM_RATIO,
                    minimum_ratio_str=self.MINIMUM_RATIO_STR,
                    maximum_ratio_str=self.MAXIMUM_RATIO_STR,
                ),
                raw=raw,
                image_prompt=(
                    image_prompt
                    if image_prompt is None
                    else convert_image_to_base64(image_prompt)
                ),
                image_prompt_strength=(
                    None if image_prompt is None else round(image_prompt_strength, 2)
                ),
            ),
            auth_token=auth_token,
        )
        output_image = handle_bfl_synchronous_operation(operation)
        return (output_image,)
```
