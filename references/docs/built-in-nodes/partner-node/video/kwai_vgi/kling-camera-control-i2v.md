> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Image to Video (Camera Control) - ComfyUI Built-in Node

> Image to video conversion node with camera control features

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-i2v.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0a03149e96eb31344041b9fe455bba1d" alt="ComfyUI Built-in Kling Image to Video (Camera Control) Node" data-og-width="1731" width="1731" data-og-height="1339" height="1339" data-path="images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-i2v.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-i2v.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=65d73e44206f5161db5572dace860692 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-i2v.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=734b98820da37dd2f96de34e8abe43a1 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-i2v.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f687675a86cfb9507165ba3716836df1 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-i2v.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7f8eb6b8586146eae677cfd0959d6058 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-i2v.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=8191888415f17dab1c9fadf88989cf5a 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-control-i2v.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3a66bef78061a4fdd6d2b876e22bac0c 2500w" />

The Kling Image to Video (Camera Control) node converts static images into videos with professional camera movements. It supports camera controls like zoom, rotation, pan, tilt and first-person view while maintaining focus on the original image content.

## Parameters

### Basic Parameters

| Parameter        | Type   | Default | Description                                     |
| ---------------- | ------ | ------- | ----------------------------------------------- |
| start\_frame     | Image  | -       | Input image to convert to video                 |
| prompt           | String | ""      | Text prompt describing video action and content |
| negative\_prompt | String | ""      | Elements to avoid in the video                  |
| cfg\_scale       | Float  | 7.0     | Controls how closely to follow the prompt       |
| aspect\_ratio    | Select | 16:9    | Output video aspect ratio                       |

### Camera Control Parameters

| Parameter       | Type          | Description                                           |
| --------------- | ------------- | ----------------------------------------------------- |
| camera\_control | CameraControl | Camera control config from Kling Camera Controls node |

### Output

| Output | Type  | Description     |
| ------ | ----- | --------------- |
| VIDEO  | Video | Generated video |

## Source Code

\[Node Source Code (Updated 2025-05-03)]

```python  theme={null}

class KlingCameraControlI2VNode(KlingImage2VideoNode):
    """
    Kling Image to Video Camera Control Node. This node is a image to video node, but it supports controlling the camera.
    Duration, mode, and model_name request fields are hard-coded because camera control is only supported in pro mode with the kling-v1-5 model at 5s duration as of 2025-05-02.
    """

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
                "cfg_scale": model_field_to_node_input(
                    IO.FLOAT, KlingImage2VideoRequest, "cfg_scale"
                ),
                "aspect_ratio": model_field_to_node_input(
                    IO.COMBO,
                    KlingImage2VideoRequest,
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

    DESCRIPTION = "Transform still images into cinematic videos with professional camera movements that simulate real-world cinematography. Control virtual camera actions including zoom, rotation, pan, tilt, and first-person view, while maintaining focus on your original image."

    def api_call(
        self,
        start_frame: torch.Tensor,
        prompt: str,
        negative_prompt: str,
        cfg_scale: float,
        aspect_ratio: str,
        camera_control: CameraControl,
        auth_token: Optional[str] = None,
    ):
        return super().api_call(
            model_name="kling-v1-5",
            start_frame=start_frame,
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
