> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Image to Video - ComfyUI Native Node Documentation

> A node that converts static images to dynamic videos using MiniMax AI

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=20daea4b1e99477334f1a7be3d3cb4d3" alt="ComfyUI Native MiniMax Image to Video Node" data-og-width="1731" width="1731" data-og-height="1360" height="1360" data-path="images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1bf0e97a0a4ba3d78b5bb31179834feb 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0e8b54168d3722db035c60ccd51eaa31 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=063762bc777a56217d88e984d85c07b9 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=848e10dd87fc30b16072f3ba41c23175 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=fbe894102020f7b8e27b5f15ebc250e2 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/minimax/minimax-image-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=34e4fda31f26d1e28a63c600a84d4145 2500w" />

The MiniMax Image to Video node uses MiniMax's API to generate videos from input images and text prompts.

## Parameters

### Required Parameters

| Parameter    | Type   | Default  | Description                                                  |
| ------------ | ------ | -------- | ------------------------------------------------------------ |
| image        | image  | -        | Input image used as the first frame of video                 |
| prompt\_text | string | ""       | Text prompt to guide video generation                        |
| model        | select | "I2V-01" | Available models: "I2V-01-Director", "I2V-01", "I2V-01-live" |

### Optional Parameters

| Parameter | Type    | Description                      |
| --------- | ------- | -------------------------------- |
| seed      | integer | Random seed for noise generation |

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| VIDEO  | video | Generated video |

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}

class MinimaxImageToVideoNode(MinimaxTextToVideoNode):
    """
    Generates videos synchronously based on an image and prompt, and optional parameters using Minimax's API.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": (
                    IO.IMAGE,
                    {
                        "tooltip": "Image to use as first frame of video generation"
                    },
                ),
                "prompt_text": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "tooltip": "Text prompt to guide the video generation",
                    },
                ),
                "model": (
                    [
                        "I2V-01-Director",
                        "I2V-01",
                        "I2V-01-live",
                    ],
                    {
                        "default": "I2V-01",
                        "tooltip": "Model to use for video generation",
                    },
                ),
            },
            "optional": {
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
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    RETURN_TYPES = ("VIDEO",)
    DESCRIPTION = "Generates videos from an image and prompts using Minimax's API"
    FUNCTION = "generate_video"
    CATEGORY = "api node/video/Minimax"
    API_NODE = True
    OUTPUT_NODE = True
```
