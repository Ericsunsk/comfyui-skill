> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Veo2 Video - ComfyUI 原生节点文档

> 使用Google的Veo2技术通过文本描述生成视频的节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/google/veo2-video-generation.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7188b0bfb821b1fc12f9e4670a84223f" alt="ComfyUI 原生 Google Veo2 Video 节点" data-og-width="1731" width="1731" data-og-height="1645" height="1645" data-path="images/built-in-nodes/api_nodes/google/veo2-video-generation.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/google/veo2-video-generation.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=5bb8cc72e70485b6640936c97014e43a 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/google/veo2-video-generation.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d66ec182bc9d402ed4b15893ca416b6f 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/google/veo2-video-generation.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9d37ce58de83d05a0adb0730cc6291cb 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/google/veo2-video-generation.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=444db725e0ab7f50be4c5a663cb0cedb 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/google/veo2-video-generation.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ea6a5765b5f28c4793472e979146b3b5 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/google/veo2-video-generation.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=fc61f4a8faa831690268083087d2d938 2500w" />

Google Veo2 Video 节点通过文本描述生成高质量视频，利用Google的Veo2 API技术将文本提示转换为动态视频内容。

## 参数说明

### 基本参数

| 参数                 | 类型  | 默认值     | 说明                         |
| ------------------ | --- | ------- | -------------------------- |
| prompt             | 字符串 | ""      | 详细描述要生成视频内容的文本             |
| aspect\_ratio      | 选择项 | "16:9"  | 输出视频的宽高比，可选"16:9"或"9:16"   |
| negative\_prompt   | 字符串 | ""      | 指导系统避免在视频中出现的内容            |
| duration\_seconds  | 整数  | 5       | 输出视频的持续时间，5-8秒             |
| enhance\_prompt    | 布尔值 | True    | 是否使用AI辅助增强提示词              |
| person\_generation | 选择项 | "ALLOW" | 是否允许生成人物，可选"ALLOW"或"BLOCK" |
| seed               | 整数  | 0       | 随机种子，0表示随机生成               |

### 可选参数

| 参数    | 类型 | 默认值  | 说明               |
| ----- | -- | ---- | ---------------- |
| image | 图像 | None | 可选的参考图像，用于引导视频生成 |

### 输出

| 输出    | 类型 | 说明      |
| ----- | -- | ------- |
| VIDEO | 视频 | 生成的视频结果 |

## 源码参考

\[节点源码 (更新于2025-05-03)]

```python  theme={null}

class VeoVideoGenerationNode(ComfyNodeABC):
    """
    Generates videos from text prompts using Google's Veo API.

    This node can create videos from text descriptions and optional image inputs,
    with control over parameters like aspect ratio, duration, and more.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Text description of the video",
                    },
                ),
                "aspect_ratio": (
                    IO.COMBO,
                    {
                        "options": ["16:9", "9:16"],
                        "default": "16:9",
                        "tooltip": "Aspect ratio of the output video",
                    },
                ),
            },
            "optional": {
                "negative_prompt": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Negative text prompt to guide what to avoid in the video",
                    },
                ),
                "duration_seconds": (
                    IO.INT,
                    {
                        "default": 5,
                        "min": 5,
                        "max": 8,
                        "step": 1,
                        "display": "number",
                        "tooltip": "Duration of the output video in seconds",
                    },
                ),
                "enhance_prompt": (
                    IO.BOOLEAN,
                    {
                        "default": True,
                        "tooltip": "Whether to enhance the prompt with AI assistance",
                    }
                ),
                "person_generation": (
                    IO.COMBO,
                    {
                        "options": ["ALLOW", "BLOCK"],
                        "default": "ALLOW",
                        "tooltip": "Whether to allow generating people in the video",
                    },
                ),
                "seed": (
                    IO.INT,
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFF,
                        "step": 1,
                        "display": "number",
                        "control_after_generate": True,
                        "tooltip": "Seed for video generation (0 for random)",
                    },
                ),
                "image": (IO.IMAGE, {
                    "default": None,
                    "tooltip": "Optional reference image to guide video generation",
                }),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    RETURN_TYPES = (IO.VIDEO,)
    FUNCTION = "generate_video"
    CATEGORY = "api node/video/Veo"
    DESCRIPTION = "Generates videos from text prompts using Google's Veo API"
    API_NODE = True

    def generate_video(
        self,
        prompt,
        aspect_ratio="16:9",
        negative_prompt="",
        duration_seconds=5,
        enhance_prompt=True,
        person_generation="ALLOW",
        seed=0,
        image=None,
        auth_token=None,
    ):
        # Prepare the instances for the request
        instances = []

        instance = {
            "prompt": prompt
        }

        # Add image if provided
        if image is not None:
            image_base64 = convert_image_to_base64(image)
            if image_base64:
                instance["image"] = {
                    "bytesBase64Encoded": image_base64,
                    "mimeType": "image/png"
                }

        instances.append(instance)

        # Create parameters dictionary
        parameters = {
            "aspectRatio": aspect_ratio,
            "personGeneration": person_generation,
            "durationSeconds": duration_seconds,
            "enhancePrompt": enhance_prompt,
        }

        # Add optional parameters if provided
        if negative_prompt:
            parameters["negativePrompt"] = negative_prompt
        if seed > 0:
            parameters["seed"] = seed

        # Initial request to start video generation
        initial_operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path="/proxy/veo/generate",
                method=HttpMethod.POST,
                request_model=Veo2GenVidRequest,
                response_model=Veo2GenVidResponse
            ),
            request=Veo2GenVidRequest(
                instances=instances,
                parameters=parameters
            ),
            auth_token=auth_token
        )

        initial_response = initial_operation.execute()
        operation_name = initial_response.name

        logging.info(f"Veo generation started with operation name: {operation_name}")

        # Define status extractor function
        def status_extractor(response):
            # Only return "completed" if the operation is done, regardless of success or failure
            # We'll check for errors after polling completes
            return "completed" if response.done else "pending"

        # Define progress extractor function
        def progress_extractor(response):
            # Could be enhanced if the API provides progress information
            return None

        # Define the polling operation
        poll_operation = PollingOperation(
            poll_endpoint=ApiEndpoint(
                path="/proxy/veo/poll",
                method=HttpMethod.POST,
                request_model=Veo2GenVidPollRequest,
                response_model=Veo2GenVidPollResponse
            ),
            completed_statuses=["completed"],
            failed_statuses=[],  # No failed statuses, we'll handle errors after polling
            status_extractor=status_extractor,
            progress_extractor=progress_extractor,
            request=Veo2GenVidPollRequest(
                operationName=operation_name
            ),
            auth_token=auth_token,
            poll_interval=5.0
        )

        # Execute the polling operation
        poll_response = poll_operation.execute()

        # Now check for errors in the final response
        # Check for error in poll response
        if hasattr(poll_response, 'error') and poll_response.error:
            error_message = f"Veo API error: {poll_response.error.message} (code: {poll_response.error.code})"
            logging.error(error_message)
            raise Exception(error_message)

        # Check for RAI filtered content
        if (hasattr(poll_response.response, 'raiMediaFilteredCount') and
            poll_response.response.raiMediaFilteredCount > 0):

            # Extract reason message if available
            if (hasattr(poll_response.response, 'raiMediaFilteredReasons') and
                poll_response.response.raiMediaFilteredReasons):
                reason = poll_response.response.raiMediaFilteredReasons[0]
                error_message = f"Content filtered by Google's Responsible AI practices: {reason} ({poll_response.response.raiMediaFilteredCount} videos filtered.)"
            else:
                error_message = f"Content filtered by Google's Responsible AI practices ({poll_response.response.raiMediaFilteredCount} videos filtered.)"

            logging.error(error_message)
            raise Exception(error_message)

        # Extract video data
        video_data = None
        if poll_response.response and hasattr(poll_response.response, 'videos') and poll_response.response.videos and len(poll_response.response.videos) > 0:
            video = poll_response.response.videos[0]

            # Check if video is provided as base64 or URL
            if hasattr(video, 'bytesBase64Encoded') and video.bytesBase64Encoded:
                # Decode base64 string to bytes
                video_data = base64.b64decode(video.bytesBase64Encoded)
            elif hasattr(video, 'gcsUri') and video.gcsUri:
                # Download from URL
                video_url = video.gcsUri
                video_response = requests.get(video_url)
                video_data = video_response.content
            else:
                raise Exception("Video returned but no data or URL was provided")
        else:
            raise Exception("Video generation completed but no video was returned")

        if not video_data:
            raise Exception("No video data was returned")

        logging.info("Video generation completed successfully")

        # Convert video data to BytesIO object
        video_io = io.BytesIO(video_data)

        # Return VideoFromFile object
        return (VideoFromFile(video_io),)

```
