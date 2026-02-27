> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Image to Video - ComfyUI Built-in Node

> A node that converts static images to dynamic videos using Kling's AI technology

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d4c1f57cbb7824acee3d6c584252dbdd" alt="ComfyUI Built-in Kling Image to Video Node" data-og-width="1731" width="1731" data-og-height="1759" height="1759" data-path="images/built-in-nodes/api_nodes/kwai_vgi/kling-image-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-image-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3fea62b8125d97e1bc9120ce31807737 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-image-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7c8fcda5ec3e60b804a72c518e56b485 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-image-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=fcce6e7ca1ed6ee44ade5d680bd8e693 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-image-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=fe8e7a3a27e0a61d99a2f638d00a67bd 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-image-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9647385514ef8a88ac0679146625bc9f 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-image-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=dcd995989590d5bb17f04696b2c26c74 2500w" />

The Kling Image to Video node converts static images into dynamic video content using Kling's image-to-video API.

## Parameters

### Basic Parameters

All parameters below are required:

| Parameter        | Type   | Default      | Description                                     |
| ---------------- | ------ | ------------ | ----------------------------------------------- |
| start\_frame     | Image  | -            | Input source image                              |
| prompt           | String | ""           | Text prompt describing video action and content |
| negative\_prompt | String | ""           | Elements to avoid in the video                  |
| cfg\_scale       | Float  | 7.0          | Controls how closely to follow the prompt       |
| model\_name      | Select | "kling-v1-5" | Model type to use                               |
| aspect\_ratio    | Select | "16:9"       | Output video aspect ratio                       |
| duration         | Select | "5s"         | Generated video duration                        |
| mode             | Select | "pro"        | Video generation mode                           |

### Output

| Output    | Type   | Description             |
| --------- | ------ | ----------------------- |
| VIDEO     | Video  | Generated video         |
| video\_id | String | Unique video identifier |
| duration  | String | Actual video duration   |

## Source Code

\[Node Source Code (Updated 2025-05-03)]

```python  theme={null}

class KlingImage2VideoNode(KlingNodeBase):
    """Kling Image to Video Node"""

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "start_frame": model_field_to_node_input(
                    IO.IMAGE, KlingImage2VideoRequest, "image"
                ),
                "prompt": model_field_to_node_input(
                    IO.STRING, KlingImage2VideoRequest, "prompt", multiline=True
                ),
                "negative_prompt": model_field_to_node_input(
                    IO.STRING,
                    KlingImage2VideoRequest,
                    "negative_prompt",
                    multiline=True,
                ),
                "model_name": model_field_to_node_input(
                    IO.COMBO,
                    KlingImage2VideoRequest,
                    "model_name",
                    enum_type=KlingVideoGenModelName,
                ),
                "cfg_scale": model_field_to_node_input(
                    IO.FLOAT, KlingImage2VideoRequest, "cfg_scale"
                ),
                "mode": model_field_to_node_input(
                    IO.COMBO,
                    KlingImage2VideoRequest,
                    "mode",
                    enum_type=KlingVideoGenMode,
                ),
                "aspect_ratio": model_field_to_node_input(
                    IO.COMBO,
                    KlingImage2VideoRequest,
                    "aspect_ratio",
                    enum_type=KlingVideoGenAspectRatio,
                ),
                "duration": model_field_to_node_input(
                    IO.COMBO,
                    KlingImage2VideoRequest,
                    "duration",
                    enum_type=KlingVideoGenDuration,
                ),
            },
            "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
        }

    RETURN_TYPES = ("VIDEO", "STRING", "STRING")
    RETURN_NAMES = ("VIDEO", "video_id", "duration")
    DESCRIPTION = "Kling Image to Video Node"

    def get_response(self, task_id: str, auth_token: str) -> KlingImage2VideoResponse:
        return poll_until_finished(
            auth_token,
            ApiEndpoint(
                path=f"{PATH_IMAGE_TO_VIDEO}/{task_id}",
                method=HttpMethod.GET,
                request_model=KlingImage2VideoRequest,
                response_model=KlingImage2VideoResponse,
            ),
        )

    def api_call(
        self,
        start_frame: torch.Tensor,
        prompt: str,
        negative_prompt: str,
        model_name: str,
        cfg_scale: float,
        mode: str,
        aspect_ratio: str,
        duration: str,
        camera_control: Optional[KlingCameraControl] = None,
        end_frame: Optional[torch.Tensor] = None,
        auth_token: Optional[str] = None,
    ) -> tuple[VideoFromFile]:
        validate_prompts(prompt, negative_prompt, MAX_PROMPT_LENGTH_I2V)
        initial_operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path=PATH_IMAGE_TO_VIDEO,
                method=HttpMethod.POST,
                request_model=KlingImage2VideoRequest,
                response_model=KlingImage2VideoResponse,
            ),
            request=KlingImage2VideoRequest(
                model_name=KlingVideoGenModelName(model_name),
                image=tensor_to_base64_string(start_frame),
                image_tail=(
                    tensor_to_base64_string(end_frame)
                    if end_frame is not None
                    else None
                ),
                prompt=prompt,
                negative_prompt=negative_prompt if negative_prompt else None,
                cfg_scale=cfg_scale,
                mode=KlingVideoGenMode(mode),
                aspect_ratio=KlingVideoGenAspectRatio(aspect_ratio),
                duration=KlingVideoGenDuration(duration),
                camera_control=camera_control,
            ),
            auth_token=auth_token,
        )

        task_creation_response = initial_operation.execute()
        validate_task_creation_response(task_creation_response)
        task_id = task_creation_response.data.task_id

        final_response = self.get_response(task_id, auth_token)
        validate_video_result_response(final_response)

        video = get_video_from_response(final_response)
        return video_result_to_node_output(video)

```
