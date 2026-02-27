> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Color RGB - ComfyUI 原生节点文档

> 为Recraft图像生成定义颜色控制的辅助节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=406b336f43d8d8872ab620d8d5777f5f" alt="ComfyUI 原生 Recraft Color RGB 节点" data-og-width="1506" width="1506" data-og-height="819" height="819" data-path="images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=be322b9b302d150a36e81ed0c10ef67c 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a8c1bf7219288c4996059121900edf4e 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=87a17664ad9c3e57123d97e503103f12 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=28e64e100a1eac1f4b0b2fc5dfec0095 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b4d421d5f9ec44105ffa1430af7e89e8 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a87dc6d0a03ef2446a85c62ca728adc7 2500w" />
Recraft Color RGB 节点允许你定义精确的RGB颜色值，用于控制Recraft图像生成过程中的颜色使用。

## 节点功能

此节点创建一个颜色配置对象，可以连接到Recraft Controls节点，用于指定生成图像中应使用的颜色。

## 参数说明

### 基本参数

| 参数 | 类型 | 默认值 | 说明           |
| -- | -- | --- | ------------ |
| r  | 整数 | 0   | 红色通道值(0-255) |
| g  | 整数 | 0   | 绿色通道值(0-255) |
| b  | 整数 | 0   | 蓝色通道值(0-255) |

### 输出

| 输出             | 类型            | 说明                           |
| -------------- | ------------- | ---------------------------- |
| recraft\_color | Recraft Color | 颜色配置对象，连接到Recraft Controls节点 |

## 使用示例

<Card title="Recraft Text to Image 工作流示例" icon="book" href="/zh-CN/tutorials/partner-nodes/recraft/recraft-text-to-image">
  Recraft Text to Image 工作流示例
</Card>

## 源码参考

\[节点源码 (更新于2025-05-03)]

```python  theme={null}
class RecraftColorRGBNode:
    """
    Create Recraft Color by choosing specific RGB values.
    """

    RETURN_TYPES = (RecraftIO.COLOR,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    RETURN_NAMES = ("recraft_color",)
    FUNCTION = "create_color"
    CATEGORY = "api node/image/Recraft"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "r": (IO.INT, {
                    "default": 0,
                    "min": 0,
                    "max": 255,
                    "tooltip": "Red value of color."
                }),
                "g": (IO.INT, {
                    "default": 0,
                    "min": 0,
                    "max": 255,
                    "tooltip": "Green value of color."
                }),
                "b": (IO.INT, {
                    "default": 0,
                    "min": 0,
                    "max": 255,
                    "tooltip": "Blue value of color."
                }),
            },
            "optional": {
                "recraft_color": (RecraftIO.COLOR,),
            }
        }

    def create_color(self, r: int, g: int, b: int, recraft_color: RecraftColorChain=None):
        recraft_color = recraft_color.clone() if recraft_color else RecraftColorChain()
        recraft_color.add(RecraftColor(r, g, b))
        return (recraft_color, )

```
