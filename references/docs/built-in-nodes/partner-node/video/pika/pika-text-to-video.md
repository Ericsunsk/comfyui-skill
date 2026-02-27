> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Pika 2.2 Text to Video - ComfyUI Native Node Documentation

> A node that converts text descriptions into videos using Pika AI

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3eea0be5229f14d73d79d17a1b9872ea" alt="ComfyUI Native Pika 2.2 Text to Video Node" data-og-width="1731" width="1731" data-og-height="1712" height="1712" data-path="images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d12e35717b758b3fe6edee67ea6bf3f1 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=01e926f28ab200aa7ecd60eeed6bb791 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ceaced8c4a6712925c5506eac3fc00af 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b62485e36320061e636d7b34ee9747a4 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9c1bd0cd3ab168fd6f92de1d3dc0a9ab 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pika/pika-2-2-text-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=03cd041ab170254cc97f90fed682169b 2500w" />

The Pika 2.2 Text to Video node uses Pika's 2.2 API to create videos from text descriptions. It connects to Pika's text-to-video API, allowing users to generate videos using text prompts with various control parameters.

## Parameters

### Required Parameters

| Parameter        | Type    | Default            | Description                                   |
| ---------------- | ------- | ------------------ | --------------------------------------------- |
| prompt\_text     | String  | ""                 | Text prompt describing the video content      |
| negative\_prompt | String  | ""                 | Elements to exclude from the video            |
| seed             | Integer | 0                  | Random seed for generation                    |
| resolution       | Select  | "1080p"            | Output video resolution                       |
| duration         | Select  | "5s"               | Length of generated video                     |
| aspect\_ratio    | Float   | 1.7777777777777777 | Video aspect ratio, range 0.4-2.5, step 0.001 |

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| VIDEO  | Video | Generated video |

## Source Code

\[Node Source Code (Updated 2025-05-05)]

```python  theme={null}

class PikaTextToVideoNodeV2_2(PikaNodeBase):
    """Pika 2.2 Text to Video Node."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_base_inputs_types(PikaBodyGenerate22T2vGenerate22T2vPost),
                "aspect_ratio": model_field_to_node_input(
                    IO.FLOAT,
                    PikaBodyGenerate22T2vGenerate22T2vPost,
                    "aspectRatio",
                    step=0.001,
                    min=0.4,
                    max=2.5,
                    default=1.7777777777777777,
                ),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    RETURN_TYPES = ("VIDEO",)
    DESCRIPTION = "Sends a text prompt to the Pika API v2.2 to generate a video."

    def api_call(
        self,
        prompt_text: str,
        negative_prompt: str,
        seed: int,
        resolution: str,
        duration: int,
        aspect_ratio: float,
        auth_token: Optional[str] = None,
    ) -> tuple[VideoFromFile]:
        """API call for Pika 2.2 Text to Video."""
        initial_operation = SynchronousOperation(
            endpoint=ApiEndpoint(
                path=PATH_TEXT_TO_VIDEO,
                method=HttpMethod.POST,
                request_model=PikaBodyGenerate22T2vGenerate22T2vPost,
                response_model=PikaGenerateResponse,
            ),
            request=PikaBodyGenerate22T2vGenerate22T2vPost(
                promptText=prompt_text,
                negativePrompt=negative_prompt,
                seed=seed,
                resolution=resolution,
                duration=duration,
                aspectRatio=aspect_ratio,
            ),
            auth_token=auth_token,
            content_type="application/x-www-form-urlencoded",
        )

        return self.execute_task(initial_operation, auth_token)


```
