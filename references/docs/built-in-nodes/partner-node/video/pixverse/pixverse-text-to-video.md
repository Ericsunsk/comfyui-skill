> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# PixVerse Text to Video - ComfyUI Built-in Node Documentation

> A node that converts text descriptions into videos using PixVerse AI technology

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-text-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b565631bd9ca69e804d839e8d79a799c" alt="ComfyUI Built-in PixVerse Text to Video Node" data-og-width="1731" width="1731" data-og-height="1689" height="1689" data-path="images/built-in-nodes/api_nodes/pixverse/pixverse-text-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-text-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=8e6098d1ef620e31633c0b4a47e0c82b 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-text-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d9432ec30c5d2af16fb70aceaf5202ae 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-text-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=66543725029b6c747ad4ef61953cef49 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-text-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6864d606bcf6ebc5245445d75cecef75 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-text-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9f510cffe2825d9855cbbf8588f80d92 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-text-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a439e4b778c50a5af9d3a0b72b070fca 2500w" />

The PixVerse Text to Video node connects to PixVerse's text-to-video API, allowing users to generate high-quality videos from text descriptions. Users can customize their creations by adjusting various parameters like video quality, duration, and motion mode.

## Parameters

### Required Parameters

| Parameter         | Type    | Default                   | Description                                   |
| ----------------- | ------- | ------------------------- | --------------------------------------------- |
| prompt            | string  | ""                        | Text prompt describing the video content      |
| aspect\_ratio     | select  | -                         | Output video aspect ratio                     |
| quality           | select  | PixverseQuality.res\_540p | Video quality level                           |
| duration\_seconds | select  | -                         | Video duration                                |
| motion\_mode      | select  | -                         | Video motion mode                             |
| seed              | integer | 0                         | Random seed for consistent generation results |

### Optional Parameters

| Parameter          | Type               | Default | Description                          |
| ------------------ | ------------------ | ------- | ------------------------------------ |
| negative\_prompt   | string             | ""      | Elements to exclude from the video   |
| pixverse\_template | PIXVERSE\_TEMPLATE | None    | Optional template for style settings |

### Limitations

* 1080p quality only supports normal motion mode with 5-second duration
* Non 5-second durations only support normal motion mode

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| VIDEO  | video | Generated video |

## Source Code

\[Node Source Code (Updated 2025-05-05)]

```python  theme={null}

class PixverseTextToVideoNode(ComfyNodeABC):
    """
    Generates videos synchronously based on prompt and output_size.
    """

    RETURN_TYPES = (IO.VIDEO,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/video/Pixverse"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Prompt for the video generation",
                    },
                ),
                "aspect_ratio": (
                    [ratio.value for ratio in PixverseAspectRatio],
                ),
                "quality": (
                    [resolution.value for resolution in PixverseQuality],
                    {
                        "default": PixverseQuality.res_540p,
                    },
                ),
                "duration_seconds": ([dur.value for dur in PixverseDuration],),
                "motion_mode": ([mode.value for mode in PixverseMotionMode],),
                "seed": (
                    IO.INT,
                    {
                        "default": 0,
                        "min": 0,
                        "max": 2147483647,
                        "control_after_generate": True,
                        "tooltip": "Seed for video generation.",
                    },
                ),
            },
            "optional": {
                "negative_prompt": (
                    IO.STRING,
                    {
                        "default": "",
                        "forceInput": True,
                        "tooltip": "An optional text description of undesired elements on an image.",
                    },
                ),
                "pixverse_template": (
                    PixverseIO.TEMPLATE,
                    {
                        "tooltip": "An optional template to influence style of generation, created by the Pixverse Template node."
                    }
                )
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    def api_call(
        self,
        prompt: str,
        aspect_ratio: str,
        quality: str,
        duration_seconds: int,
        motion_mode: str,
        seed,
        negative_prompt: str=None,
        pixverse_template: int=None,
        auth_token=None,
        **kwargs,
    ):
        # 1080p is limited to 5 seconds duration
        # only normal motion_mode supported for 1080p or for non-5 second duration
        if quality == PixverseQuality.res_1080p:
            motion_mode = PixverseMotionMode.normal
            duration_seconds = PixverseDuration.dur_5
        elif duration_seconds != PixverseDuration.dur_5:
            motion_mode = PixverseMotionMode.normal

        operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path="/proxy/pixverse/video/text/generate",
                method=HttpMethod.POST,
                request_model=PixverseTextVideoRequest,
                response_model=PixverseVideoResponse,
            ),
            request=PixverseTextVideoRequest(
                prompt=prompt,
                aspect_ratio=aspect_ratio,
                quality=quality,
                duration=duration_seconds,
                motion_mode=motion_mode,
                negative_prompt=negative_prompt if negative_prompt else None,
                template_id=pixverse_template,
                seed=seed,
            ),
            auth_token=auth_token,
        )
        response_api = operation.execute()

        if response_api.Resp is None:
            raise Exception(f"Pixverse request failed: '{response_api.ErrMsg}'")

        operation = PollingOperation(
            poll_endpoint=ApiEndpoint(
                path=f"/proxy/pixverse/video/result/{response_api.Resp.video_id}",
                method=HttpMethod.GET,
                request_model=EmptyRequest,
                response_model=PixverseGenerationStatusResponse,
            ),
            completed_statuses=[PixverseStatus.successful],
            failed_statuses=[PixverseStatus.contents_moderation, PixverseStatus.failed, PixverseStatus.deleted],
            status_extractor=lambda x: x.Resp.status,
            auth_token=auth_token,
        )
        response_poll = operation.execute()

        vid_response = requests.get(response_poll.Resp.url)
        return (VideoFromFile(BytesIO(vid_response.content)),)

```
