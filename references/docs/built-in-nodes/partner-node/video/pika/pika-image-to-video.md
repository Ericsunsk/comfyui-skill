> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Pika 2.2 Image to Video - ComfyUI Native Node Documentation

> A node that converts static images to dynamic videos using Pika AI

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4d84ed0f286826f853aeb820bf01c473" alt="ComfyUI Native Pika 2.2 Image to Video Node" data-og-width="1731" width="1731" data-og-height="1610" height="1610" data-path="images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6231adab3c17f6b259419ea1ca56851b 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f68712438d1dc3b57282825a276e55b1 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=414c952553bf355df8f624badafa6651 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1e9d7bf229f464467877a9e3545f6fdb 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=24a0c522a83a0f2034931f7b4fb86dd7 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-image-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3c88a91bbb2117ae69e7724b3a70ad24 2500w" />

The Pika 2.2 Image to Video node connects to Pika's latest 2.2 API to transform static images into dynamic videos. It preserves the visual features of the original image while adding natural motion based on text prompts.

## Parameters

### Required Parameters

| Parameter        | Type    | Default | Description                                     |
| ---------------- | ------- | ------- | ----------------------------------------------- |
| image            | Image   | -       | Input image to convert to video                 |
| prompt\_text     | String  | ""      | Text prompt describing video motion and content |
| negative\_prompt | String  | ""      | Elements to avoid in the video                  |
| seed             | Integer | 0       | Random seed for generation                      |
| resolution       | Select  | "1080p" | Output video resolution                         |
| duration         | Select  | "5s"    | Length of generated video                       |

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| VIDEO  | Video | Generated video |

## How It Works

The node sends the input image and parameters (prompts, resolution, duration, etc.) to Pika's API server as multipart form data. The API processes this and returns the generated video. Users can control the output by adjusting the prompts, negative prompts, random seed and other parameters.

## Source Code

\[Node Source Code (Updated 2025-05-05)]

```python  theme={null}

class PikaImageToVideoV2_2(PikaNodeBase):
    """Pika 2.2 Image to Video Node."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": (
                    IO.IMAGE,
                    {"tooltip": "The image to convert to video"},
                ),
                **cls.get_base_inputs_types(PikaBodyGenerate22I2vGenerate22I2vPost),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    DESCRIPTION = "Sends an image and prompt to the Pika API v2.2 to generate a video."
    RETURN_TYPES = ("VIDEO",)

    def api_call(
        self,
        image: torch.Tensor,
        prompt_text: str,
        negative_prompt: str,
        seed: int,
        resolution: str,
        duration: int,
        auth_token: Optional[str] = None,
    ) -> tuple[VideoFromFile]:
        """API call for Pika 2.2 Image to Video."""
        # Convert image to BytesIO
        image_bytes_io = tensor_to_bytesio(image)
        image_bytes_io.seek(0)  # Reset stream position

        # Prepare file data for multipart upload
        pika_files = {"image": ("image.png", image_bytes_io, "image/png")}

        # Prepare non-file data using the Pydantic model
        pika_request_data = PikaBodyGenerate22I2vGenerate22I2vPost(
            promptText=prompt_text,
            negativePrompt=negative_prompt,
            seed=seed,
            resolution=resolution,
            duration=duration,
        )

        initial_operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path=PATH_IMAGE_TO_VIDEO,
                method=HttpMethod.POST,
                request_model=PikaBodyGenerate22I2vGenerate22I2vPost,
                response_model=PikaGenerateResponse,
            ),
            request=pika_request_data,
            files=pika_files,
            content_type="multipart/form-data",
            auth_token=auth_token,
        )

        return self.execute_task(initial_operation, auth_token)

```
