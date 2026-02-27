> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling Camera Controls - ComfyUI 原生节点文档

> 为Kling视频生成提供摄像机控制参数的节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-controls.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=916ab6bab186b773cfda29470f7a45b6" alt="ComfyUI 原生 Kling Camera Controls 节点" data-og-width="1731" width="1731" data-og-height="1230" height="1230" data-path="images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-controls.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-controls.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=73ee6a25e834211e7b59b3ac934a944d 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-controls.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=482ea3be2c12fd99d54cef71f13df76f 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-controls.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=95918400a1034806f08a9cb42dd4c7b6 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-controls.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c8092b9da0d15b1e84c02f5607130863 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-controls.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=36be5336daba8a6d44fa6d7305f744b0 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/kwai_vgi/kling-camera-controls.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c4f2beeb6cd023272b577d4194c7571c 2500w" />

Kling Camera Controls 节点用于定义虚拟摄像机的行为参数，控制Kling视频生成过程中的镜头运动和视角变化。

## 参数说明

| 参数                    | 类型  | 默认值      | 说明                                                                                                                                             |
| --------------------- | --- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| camera\_control\_type | 选择项 | "simple" | 预定义的摄像机运动类型。simple: 可自定义的摄像机运动；down\_back: 摄像机下降并向后移动；forward\_up: 摄像机向前移动并向上倾斜；right\_turn\_forward: 向右旋转并向前移动；left\_turn\_forward: 向左旋转并向前移动 |
| horizontal\_movement  | 浮点数 | 0        | 控制摄像机沿水平轴（x轴）的移动。负值表示向左，正值表示向右                                                                                                                 |
| vertical\_movement    | 浮点数 | 0        | 控制摄像机沿垂直轴（y轴）的移动。负值表示向下，正值表示向上                                                                                                                 |
| pan                   | 浮点数 | 0.5      | 控制摄像机在垂直平面上的旋转（x轴）。负值表示向下旋转，正值表示向上旋转                                                                                                           |
| tilt                  | 浮点数 | 0        | 控制摄像机在水平平面上的旋转（y轴）。负值表示向左旋转，正值表示向右旋转                                                                                                           |
| roll                  | 浮点数 | 0        | 控制摄像机的滚动量（z轴）。负值表示逆时针，正值表示顺时针                                                                                                                  |
| zoom                  | 浮点数 | 0        | 控制摄像机焦距的变化。负值表示视场变窄，正值表示视场变宽                                                                                                                   |

**注意**：至少需要一个非零值的摄像机控制参数才有效。

### 输出

| 输出              | 类型              | 说明           |
| --------------- | --------------- | ------------ |
| camera\_control | CAMERA\_CONTROL | 包含摄像机设置的配置对象 |

**注意**：并非所有模型和模式组合都支持摄像机控制。请参考Kling API文档了解更多信息。

## 源码参考

\[节点源码 (更新于2025-05-03)]

```python  theme={null}

class KlingCameraControls(KlingNodeBase):
    """Kling Camera Controls Node"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "camera_control_type": (
                    IO.COMBO,
                    {
                        "options": [
                            camera_control_type.value
                            for camera_control_type in CameraType
                        ],
                        "default": "simple",
                        "tooltip": "Predefined camera movements type. simple: Customizable camera movement. down_back: Camera descends and moves backward. forward_up: Camera moves forward and tilts up. right_turn_forward: Rotate right and move forward. left_turn_forward: Rotate left and move forward.",
                    },
                ),
                "horizontal_movement": get_camera_control_input_config(
                    "Controls camera's movement along horizontal axis (x-axis). Negative indicates left, positive indicates right"
                ),
                "vertical_movement": get_camera_control_input_config(
                    "Controls camera's movement along vertical axis (y-axis). Negative indicates downward, positive indicates upward."
                ),
                "pan": get_camera_control_input_config(
                    "Controls camera's rotation in vertical plane (x-axis). Negative indicates downward rotation, positive indicates upward rotation.",
                    default=0.5,
                ),
                "tilt": get_camera_control_input_config(
                    "Controls camera's rotation in horizontal plane (y-axis). Negative indicates left rotation, positive indicates right rotation.",
                ),
                "roll": get_camera_control_input_config(
                    "Controls camera's rolling amount (z-axis). Negative indicates counterclockwise, positive indicates clockwise.",
                ),
                "zoom": get_camera_control_input_config(
                    "Controls change in camera's focal length. Negative indicates narrower field of view, positive indicates wider field of view.",
                ),
            }
        }

    DESCRIPTION = "Kling Camera Controls Node. Not all model and mode combinations support camera control. Please refer to the Kling API documentation for more information."
    RETURN_TYPES = ("CAMERA_CONTROL",)
    RETURN_NAMES = ("camera_control",)
    FUNCTION = "main"

    @classmethod
    def VALIDATE_INPUTS(
        cls,
        horizontal_movement: float,
        vertical_movement: float,
        pan: float,
        tilt: float,
        roll: float,
        zoom: float,
    ) -> bool | str:
        if not is_valid_camera_control_configs(
            [
                horizontal_movement,
                vertical_movement,
                pan,
                tilt,
                roll,
                zoom,
            ]
        ):
            return "Invalid camera control configs: at least one of the values must be non-zero"
        return True

    def main(
        self,
        camera_control_type: str,
        horizontal_movement: float,
        vertical_movement: float,
        pan: float,
        tilt: float,
        roll: float,
        zoom: float,
    ) -> tuple[CameraControl]:
        return (
            CameraControl(
                type=CameraType(camera_control_type),
                config=CameraConfig(
                    horizontal=horizontal_movement,
                    vertical=vertical_movement,
                    pan=pan,
                    roll=roll,
                    tilt=tilt,
                    zoom=zoom,
                ),
            ),
        )
```
