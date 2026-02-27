> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# PixVerse Transition Video - ComfyUI 原生节点文档

> 使用 PixVerse 的AI技术创建从起始帧到结束帧平滑过渡的视频

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=13d19c52ceb204b914331211525aca82" alt="ComfyUI 原生 PixVerse Transition Video 节点" data-og-width="1731" width="1731" data-og-height="1659" height="1659" data-path="images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=76907b3f70d9154dec1e893a684a786b 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d6ce25f5e717234c0e05e58ce16ad4fd 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e43117de110af376e5f6ee9226f77933 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=cd15acee6531d79c546762e9d824088d 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f73c102b783260a78ef68551789a3a29 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-transition-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=57c484331df6355691cd0201e4206dcc 2500w" />

PixVerse Transition Video 节点连接到 PixVerse 的过渡视频生成 API，允许你提供开始和结束图像，生成在两者之间平滑过渡的视频序列。节点会自动创建所有中间帧，产生流畅的变换效果，特别适合创建变形、场景转换和对象演变等视觉效果。

## 参数说明

### 必需参数

| 参数                | 类型  | 默认值                         | 说明                       |
| ----------------- | --- | --------------------------- | ------------------------ |
| first\_frame      | 图像  | -                           | 视频的起始帧图像                 |
| last\_frame       | 图像  | -                           | 视频的结束帧图像                 |
| prompt            | 字符串 | ""                          | 描述视频内容和过渡效果的文本提示词        |
| quality           | 选择项 | "PixverseQuality.res\_540p" | 生成视频的质量级别                |
| duration\_seconds | 选择项 | -                           | 生成视频的持续时间                |
| motion\_mode      | 选择项 | -                           | 视频的动作模式                  |
| seed              | 整数  | 0                           | 生成过程的随机种子，范围0-2147483647 |

### 可选参数

| 参数                 | 类型                 | 默认值  | 说明                     |
| ------------------ | ------------------ | ---- | ---------------------- |
| negative\_prompt   | 字符串                | ""   | 指定不希望在视频中出现的元素         |
| pixverse\_template | PIXVERSE\_TEMPLATE | None | 可选的PixVerse模板配置，影响生成风格 |

### 参数限制说明

* 当quality设置为1080p时，动作模式(motion\_mode)会强制设为normal，持续时间(duration\_seconds)会强制设为5秒
* 当持续时间(duration\_seconds)不等于5秒时，动作模式(motion\_mode)会强制设为normal

### 输出

| 输出    | 类型 | 说明      |
| ----- | -- | ------- |
| VIDEO | 视频 | 生成的视频结果 |

## 源码参考

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
