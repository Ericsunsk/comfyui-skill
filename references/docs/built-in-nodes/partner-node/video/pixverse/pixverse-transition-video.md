> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# PixVerse Transition Video - ComfyUI Native Node Documentation

> Create smooth transition videos between start and end frames using PixVerse AI

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=13d19c52ceb204b914331211525aca82" alt="ComfyUI Native PixVerse Transition Video Node" data-og-width="1731" width="1731" data-og-height="1659" height="1659" data-path="images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=76907b3f70d9154dec1e893a684a786b 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d6ce25f5e717234c0e05e58ce16ad4fd 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e43117de110af376e5f6ee9226f77933 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=cd15acee6531d79c546762e9d824088d 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f73c102b783260a78ef68551789a3a29 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=57c484331df6355691cd0201e4206dcc 2500w" />

The Pixverse Transition Video node connects to PixVerse's API to generate smooth video transitions between two images. It automatically creates all intermediate frames to produce fluid transformations, perfect for morphing effects, scene transitions, and object evolution.

## Parameters

### Required Parameters

| Parameter         | Type    | Default                     | Description                                 |
| ----------------- | ------- | --------------------------- | ------------------------------------------- |
| first\_frame      | Image   | -                           | Starting frame image                        |
| last\_frame       | Image   | -                           | Ending frame image                          |
| prompt            | String  | ""                          | Text prompt describing video and transition |
| quality           | Select  | "PixverseQuality.res\_540p" | Output video quality                        |
| duration\_seconds | Select  | -                           | Length of generated video                   |
| motion\_mode      | Select  | -                           | Video motion style                          |
| seed              | Integer | 0                           | Random seed (range: 0-2147483647)           |

### Optional Parameters

| Parameter          | Type               | Default | Description                |
| ------------------ | ------------------ | ------- | -------------------------- |
| negative\_prompt   | String             | ""      | Elements to avoid in video |
| pixverse\_template | PIXVERSE\_TEMPLATE | None    | Optional style preset      |

### Parameter Constraints

* When quality is set to 1080p, motion\_mode is forced to normal and duration\_seconds to 5 seconds
* When duration\_seconds is not 5 seconds, motion\_mode is forced to normal

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| VIDEO  | Video | Generated video |

## Source Code

```python  theme={null}

class PixverseTransitionVideoNode(ComfyNodeABC):
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
                "first_frame": (
                    IO.IMAGE,
                ),
                "last_frame": (
                    IO.IMAGE,
                ),
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Prompt for the video generation",
                    },
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
        first_frame: torch.Tensor,
        last_frame: torch.Tensor,
        prompt: str,
        quality: str,
        duration_seconds: int,
        motion_mode: str,
        seed,
        negative_prompt: str=None,
        pixverse_template: int=None,
        auth_token=None,
        **kwargs,
    ):
        first_frame_id = upload_image_to_pixverse(first_frame, auth_token=auth_token)
        last_frame_id = upload_image_to_pixverse(last_frame, auth_token=auth_token)

        # 1080p is limited to 5 seconds duration
        # only normal motion_mode supported for 1080p or for non-5 second duration
        if quality == PixverseQuality.res_1080p:
            motion_mode = PixverseMotionMode.normal
            duration_seconds = PixverseDuration.dur_5
        elif duration_seconds != PixverseDuration.dur_5:
            motion_mode = PixverseMotionMode.normal

        operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path="/proxy/pixverse/video/transition/generate",
                method=HttpMethod.POST,
                request_model=PixverseTransitionVideoRequest,
                response_model=PixverseVideoResponse,
            ),
            request=PixverseTransitionVideoRequest(
                first_frame_img=first_frame_id,
                last_frame_img=last_frame_id,
                prompt=prompt,
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
