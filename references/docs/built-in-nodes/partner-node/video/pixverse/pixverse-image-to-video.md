> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# PixVerse Image to Video - ComfyUI Native Node Documentation

> A node that converts static images to dynamic videos using PixVerse AI

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=5dad32a76df9845caf721b255b39df09" alt="ComfyUI Native PixVerse Image to Video Node" data-og-width="1731" width="1731" data-og-height="1659" height="1659" data-path="images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3155afe1969bafa8920123e9917e54e0 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6a8e5c91f4d608ef3dde687fc9c43541 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=03241f98cc99bc9b3bd6a41e361a1a73 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a2ebe2cb1fb508cf2b1d2c3c1d5b2c1b 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1035165aa7732d5e36faa262d6ede118 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-image-to-video.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=951bf8ba9400bbb5c25471ef63ff0fa4 2500w" />

The PixVerse Image to Video node uses PixVerse's API to transform static images into dynamic videos. It preserves the visual features of the original image while adding natural motion based on text prompts.

## Parameters

### Required Parameters

| Parameter        | Type    | Default      | Description                                 |
| ---------------- | ------- | ------------ | ------------------------------------------- |
| image            | Image   | -            | Input image to convert to video             |
| prompt           | String  | ""           | Text prompt describing video motion/content |
| negative\_prompt | String  | ""           | Elements to avoid in the video              |
| seed             | Integer | -1           | Random seed (-1 for random)                 |
| quality          | Select  | "high"       | Output video quality level                  |
| aspect\_ratio    | Select  | "r16\_9"     | Output video aspect ratio                   |
| duration         | Select  | "seconds\_4" | Length of generated video                   |
| motion\_mode     | Select  | "standard"   | Video motion style                          |

### Optional Parameters

| Parameter          | Type               | Default | Description                |
| ------------------ | ------------------ | ------- | -------------------------- |
| pixverse\_template | PIXVERSE\_TEMPLATE | None    | Optional PixVerse template |

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| VIDEO  | Video | Generated video |

## Source Code

\[Node Source Code (Updated 2025-05-05)]

```python  theme={null}
class PixverseImageToVideoNode(ComfyNodeABC):
    """
    Pixverse Image to Video

    Generates videos from an image and prompts.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "prompt": ("STRING", {"multiline": True, "default": ""}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "seed": ("INT", {"default": -1, "min": -1, "max": 0xffffffffffffffff}),
                "quality": (list(PixverseQuality.__members__.keys()), {"default": "high"}),
                "aspect_ratio": (list(PixverseAspectRatio.__members__.keys()), {"default": "r16_9"}),
                "duration": (list(PixverseDuration.__members__.keys()), {"default": "seconds_4"}),
                "motion_mode": (list(PixverseMotionMode.__members__.keys()), {"default": "standard"}),
            },
            "optional": {
                "pixverse_template": ("PIXVERSE_TEMPLATE",),
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    RETURN_TYPES = ("VIDEO",)
    DESCRIPTION = "Generates videos from an image and prompts using Pixverse's API"
    FUNCTION = "generate_video"
    CATEGORY = "api node/video/Pixverse"
    API_NODE = True
    OUTPUT_NODE = True
```
