> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Text to Video (Camera Control) - ComfyUI Built-in Node

> A text to video generation node with camera control features

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-t2v.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6ed35f4f4394e141a9405d2f1cefb22c" alt="ComfyUI Built-in Kling Text to Video (Camera Control) Node" data-og-width="1731" width="1731" data-og-height="1301" height="1301" data-path="images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-t2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-t2v.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=8f7f64f82e66f744775afe183479c034 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-t2v.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0f78117d6f187bc8ba40050fb374589f 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-t2v.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=5642ec9a908be1e89ca088e43375b0f5 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-t2v.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7cc6e6de384c093de245e20299cb542b 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-t2v.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c2b0f57422764c251257be6bcd72f98b 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-t2v.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1f9a2a9215323df503ec8ac582c5b346 2500w" />

The Kling Text to Video (Camera Control) node converts text into videos with professional camera movements. It extends the standard Kling Text to Video node by adding camera control capabilities.

## Parameters

### Basic Parameters

| Parameter        | Type            | Default | Description                                     |
| ---------------- | --------------- | ------- | ----------------------------------------------- |
| prompt           | String          | ""      | Text prompt describing video content            |
| negative\_prompt | String          | ""      | Elements to avoid in the video                  |
| cfg\_scale       | Float           | 7.0     | Controls how closely to follow the prompt       |
| aspect\_ratio    | Select          | "16:9"  | Output video aspect ratio                       |
| camera\_control  | CAMERA\_CONTROL | -       | Camera settings from Kling Camera Controls node |

### Fixed Parameters

Note: The following parameters are fixed and cannot be changed:

* Model: kling-v1-5
* Mode: pro
* Duration: 5 seconds

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| VIDEO  | Video | Generated video |

## Source Code

\[Node Source Code (Updated 2025-05-03)]

```python  theme={null}

class KlingCameraControlT2VNode(KlingTextToVideoNode):
    """
    Kling Text to Video Camera Control Node. This node is a text to video node, but it supports controlling the camera.
    Duration, mode, and model_name request fields are hard-coded because camera control is only supported in pro mode with the kling-v1-5 model at 5s duration as of 2025-05-02.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": model_field_to_node_input(
                    IO.STRING, KlingText2VideoRequest, "prompt", multiline=True
                ),
                "negative_prompt": model_field_to_node_input(
                    IO.STRING,
                    KlingText2VideoRequest,
                    "negative_prompt",
                    multiline=True,
                ),
                "cfg_scale": model_field_to_node_input(
                    IO.FLOAT, KlingText2VideoRequest, "cfg_scale"
                ),
                "aspect_ratio": model_field_to_node_input(
                    IO.COMBO,
                    KlingText2VideoRequest,
                    "aspect_ratio",
                    enum_type=AspectRatio,
                ),
                "camera_control": (
                    "CAMERA_CONTROL",
                    {
                        "tooltip": "Can be created using the Kling Camera Controls node. Controls the camera movement and motion during the video generation.",
                    },
                ),
            },
            "hidden": {"auth_token": "AUTH_TOKEN_COMFY_ORG"},
        }

    DESCRIPTION = "Transform text into cinematic videos with professional camera movements that simulate real-world cinematography. Control virtual camera actions including zoom, rotation, pan, tilt, and first-person view, while maintaining focus on your original text."

    def api_call(
        self,
        prompt: str,
        negative_prompt: str,
        cfg_scale: float,
        aspect_ratio: str,
        camera_control: Optional[CameraControl] = None,
        auth_token: Optional[str] = None,
    ):
        return super().api_call(
            model_name="kling-v1-5",
            cfg_scale=cfg_scale,
            mode="pro",
            aspect_ratio=aspect_ratio,
            duration="5",
            prompt=prompt,
            negative_prompt=negative_prompt,
            camera_control=camera_control,
            auth_token=auth_token,
        )



```
