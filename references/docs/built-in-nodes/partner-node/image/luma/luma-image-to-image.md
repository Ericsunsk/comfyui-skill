> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Image to Image - ComfyUI Built-in Node Documentation

> Node for modifying images using Luma AI

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-image-to-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c59f5ee7cefc230c298f9e3d8a24e507" alt="ComfyUI Built-in Luma Image to Image Node" data-og-width="1731" width="1731" data-og-height="1036" height="1036" data-path="images/built-in-nodes/api_nodes/luma/luma-image-to-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-image-to-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ecac3f917e86aabc2b1dc029063303f2 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-image-to-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3f9ca15c8600b37f9d25e8f2de7cfae6 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-image-to-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e5479916063e4ed86cd0283710d6512d 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-image-to-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=66aff37c622c3eca50e97e354636e206 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-image-to-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9144938fd44937e50a07c27df37809e6 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-image-to-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1628ad1fc847ab42536547a448ebc192 2500w" />

The Luma Image to Image node allows you to modify existing images using Luma AI technology based on text prompts, while preserving certain features and structure of the original image.

## Node Function

This node connects to Luma AI's text-to-image API, enabling users to generate images through detailed text prompts. Luma AI is known for its excellent realism and detail, particularly excelling at generating photorealistic content and artistic style images.

## Parameters

### Basic Parameters

| Parameter            | Type    | Default | Description                                                                             |
| -------------------- | ------- | ------- | --------------------------------------------------------------------------------------- |
| prompt               | string  | ""      | Text prompt describing the content to generate                                          |
| model                | select  | -       | Select which generation model to use                                                    |
| aspect\_ratio        | select  | 16:9    | Set the aspect ratio of the output image                                                |
| seed                 | integer | 0       | Seed value to determine if node should rerun, but actual results don't depend on seed   |
| style\_image\_weight | float   | 1.0     | Weight of the style image, range 0.02-1.0, only effective when style\_image is provided |

### Optional Parameters

Without the following parameter inputs, the node functions in text-to-image mode

| Parameter        | Type      | Description                                                                                                               |
| ---------------- | --------- | ------------------------------------------------------------------------------------------------------------------------- |
| image\_luma\_ref | LUMA\_REF | Luma reference node connection, influences generation results through input images, can consider up to 4 images           |
| style\_image     | image     | Style reference image, uses only 1 image, influences the style of generated images, adjusted through `style_image_weight` |
| character\_image | image     | Adds character features to the generated results, can be a batch of multiple images, up to 4 images                       |

### Output

| Output | Type  | Description         |
| ------ | ----- | ------------------- |
| IMAGE  | image | The generated image |

## Usage Examples

## How It Works

The Luma Image to Image node analyzes the input image and combines it with text prompts to guide the modification process. It uses Luma AI's generation models to make creative changes to images based on prompts.

Node process:

1. First uploads the input image to ComfyAPI
2. Then sends the image URL with the prompt to Luma API
3. Waits for Luma AI to complete processing
4. Downloads and returns the generated image

The image\_weight parameter controls the degree of influence from the original image - values closer to 0 will preserve more of the original image features, while values closer to 1 allow for more substantial modifications.

## Source Code

\[Node Source Code (Updated on 2025-05-05)]

```python  theme={null}

class LumaImageModifyNode(ComfyNodeABC):
    """
    Modifies images synchronously based on prompt and aspect ratio.
    """

    RETURN_TYPES = (IO.IMAGE,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/image/Luma"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": (IO.IMAGE,),
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Prompt for the image generation",
                    },
                ),
                "image_weight": (
                    IO.FLOAT,
                    {
                        "default": 1.0,
                        "min": 0.02,
                        "max": 1.0,
                        "step": 0.01,
                        "tooltip": "Weight of the image; the closer to 0.0, the less the image will be modified.",
                    },
                ),
                "model": ([model.value for model in LumaImageModel],),
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
            "optional": {},
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    def api_call(
        self,
        prompt: str,
        model: str,
        image: torch.Tensor,
        image_weight: float,
        seed,
        auth_token=None,
        **kwargs,
    ):
        # first, upload image
        download_urls = upload_images_to_comfyapi(
            image, max_images=1, auth_token=auth_token
        )
        image_url = download_urls[0]
        # next, make Luma call with download url provided
        operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path="/proxy/luma/generations/image",
                method=HttpMethod.POST,
                request_model=LumaImageGenerationRequest,
                response_model=LumaGeneration,
            ),
            request=LumaImageGenerationRequest(
                prompt=prompt,
                model=model,
                modify_image_ref=LumaModifyImageRef(
                    url=image_url, weight=round(image_weight, 2)
                ),
            ),
            auth_token=auth_token,
        )
        response_api: LumaGeneration = operation.execute()

        operation = PollingOperation(
            poll_endpoint=ApiEndpoint(
                path=f"/proxy/luma/generations/{response_api.id}",
                method=HttpMethod.GET,
                request_model=EmptyRequest,
                response_model=LumaGeneration,
            ),
            completed_statuses=[LumaState.completed],
            failed_statuses=[LumaState.failed],
            status_extractor=lambda x: x.state,
            auth_token=auth_token,
        )
        response_poll = operation.execute()

        img_response = requests.get(response_poll.assets.image)
        img = process_image_response(img_response)
        return (img,)

```
