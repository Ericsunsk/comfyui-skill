> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Text to Image - ComfyUI Native Node Documentation

> A node that converts text descriptions into high-quality images using Luma AI

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-text-to-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=19025e6d9d71bde0458f444404afe2b6" alt="ComfyUI Native Luma Text to Image Node" data-og-width="1731" width="1731" data-og-height="1218" height="1218" data-path="images/built-in-nodes/api_nodes/luma/luma-text-to-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-text-to-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=04dac25d3b0df7c78a1c577f6817b188 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-text-to-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e2296dbd807aee153a2cdba84c4103e1 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-text-to-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4ddb5c76d0e154abef23ff8cb3024e21 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-text-to-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1fc029fcc7147dd529a51420daf96f13 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-text-to-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=00b4e5db96d95cfc23c0ff093899a7c2 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-text-to-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f19f237fc7b4d0f130d51296c2bc8f2b 2500w" />

The Luma Text to Image node allows you to create highly realistic and artistic images from text descriptions using Luma AI's advanced image generation capabilities.

## Node Function

This node connects to Luma AI's text-to-image API, enabling users to generate images through detailed text prompts. Luma AI is known for its excellent realism and detail representation, particularly excelling at producing photorealistic content and artistic style images.

## Parameters

### Basic Parameters

| Parameter            | Type    | Default | Description                                                                                                          |
| -------------------- | ------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| prompt               | String  | ""      | Text prompt describing the content to generate                                                                       |
| model                | Select  | -       | Choose which generation model to use                                                                                 |
| aspect\_ratio        | Select  | 16:9    | Set the output image's aspect ratio                                                                                  |
| seed                 | Integer | 0       | Seed value to determine if the node should re-run, but actual results are independent of the seed                    |
| style\_image\_weight | Float   | 1.0     | Style image weight, range 0.0-1.0, only applies when style\_image is provided, higher means stronger style reference |

### Optional Parameters

| Parameter        | Type      | Description                                                                              |
| ---------------- | --------- | ---------------------------------------------------------------------------------------- |
| image\_luma\_ref | LUMA\_REF | Luma reference node connection to influence generation with input images; up to 4 images |
| style\_image     | Image     | Style reference image; only 1 image will be used                                         |
| character\_image | Image     | Character reference images; can be a batch of multiple, up to 4 images                   |

### Output

| Output | Type  | Description            |
| ------ | ----- | ---------------------- |
| IMAGE  | Image | Generated image result |

## Usage Example

<Card title="Luma Text to Image Usage Example" icon="book" href="/tutorials/partner-nodes/luma/luma-text-to-image">
  Detailed guide for Luma Text to Image workflow
</Card>

## How It Works

The Luma Text to Image node analyzes the text prompt provided by the user and creates corresponding images through Luma AI's generation models. This process uses deep learning technology to understand text descriptions and convert them into visual representations. Users can fine-tune the generation process by adjusting various parameters, including resolution, guidance scale, and negative prompts.

Additionally, the node supports using reference images and concept guidance to further influence the generation results, allowing creators to more precisely achieve their creative vision.

## Source Code

\[Node Source Code (Updated on 2025-05-03)]

```python  theme={null}

class LumaImageGenerationNode(ComfyNodeABC):
    """
    Generates images synchronously based on prompt and aspect ratio.
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
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Prompt for the image generation",
                    },
                ),
                "model": ([model.value for model in LumaImageModel],),
                "aspect_ratio": (
                    [ratio.value for ratio in LumaAspectRatio],
                    {
                        "default": LumaAspectRatio.ratio_16_9,
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
                "style_image_weight": (
                    IO.FLOAT,
                    {
                        "default": 1.0,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                        "tooltip": "Weight of style image. Ignored if no style_image provided.",
                    },
                ),
            },
            "optional": {
                "image_luma_ref": (
                    LumaIO.LUMA_REF,
                    {
                        "tooltip": "Luma Reference node connection to influence generation with input images; up to 4 images can be considered."
                    },
                ),
                "style_image": (
                    IO.IMAGE,
                    {"tooltip": "Style reference image; only 1 image will be used."},
                ),
                "character_image": (
                    IO.IMAGE,
                    {
                        "tooltip": "Character reference images; can be a batch of multiple, up to 4 images can be considered."
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
        model: str,
        aspect_ratio: str,
        seed,
        style_image_weight: float,
        image_luma_ref: LumaReferenceChain = None,
        style_image: torch.Tensor = None,
        character_image: torch.Tensor = None,
        auth_token=None,
        **kwargs,
    ):
        # handle image_luma_ref
        api_image_ref = None
        if image_luma_ref is not None:
            api_image_ref = self._convert_luma_refs(
                image_luma_ref, max_refs=4, auth_token=auth_token
            )
        # handle style_luma_ref
        api_style_ref = None
        if style_image is not None:
            api_style_ref = self._convert_style_image(
                style_image, weight=style_image_weight, auth_token=auth_token
            )
        # handle character_ref images
        character_ref = None
        if character_image is not None:
            download_urls = upload_images_to_comfyapi(
                character_image, max_images=4, auth_token=auth_token
            )
            character_ref = LumaCharacterRef(
                identity0=LumaImageIdentity(images=download_urls)
            )

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
                aspect_ratio=aspect_ratio,
                image_ref=api_image_ref,
                style_ref=api_style_ref,
                character_ref=character_ref,
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

    def _convert_luma_refs(
        self, luma_ref: LumaReferenceChain, max_refs: int, auth_token=None
    ):
        luma_urls = []
        ref_count = 0
        for ref in luma_ref.refs:
            download_urls = upload_images_to_comfyapi(
                ref.image, max_images=1, auth_token=auth_token
            )
            luma_urls.append(download_urls[0])
            ref_count += 1
            if ref_count >= max_refs:
                break
        return luma_ref.create_api_model(download_urls=luma_urls, max_refs=max_refs)

    def _convert_style_image(
        self, style_image: torch.Tensor, weight: float, auth_token=None
    ):
        chain = LumaReferenceChain(
            first_ref=LumaReference(image=style_image, weight=weight)
        )
        return self._convert_luma_refs(chain, max_refs=1, auth_token=auth_token)

```
