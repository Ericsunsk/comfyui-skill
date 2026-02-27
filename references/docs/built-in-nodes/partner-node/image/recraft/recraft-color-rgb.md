> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Color RGB - ComfyUI Native Node Documentation

> Helper node for defining color controls in Recraft image generation

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=406b336f43d8d8872ab620d8d5777f5f" alt="ComfyUI Native Recraft Color RGB Node" data-og-width="1506" width="1506" data-og-height="819" height="819" data-path="images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=be322b9b302d150a36e81ed0c10ef67c 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a8c1bf7219288c4996059121900edf4e 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=87a17664ad9c3e57123d97e503103f12 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=28e64e100a1eac1f4b0b2fc5dfec0095 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b4d421d5f9ec44105ffa1430af7e89e8 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-color-rgb.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a87dc6d0a03ef2446a85c62ca728adc7 2500w" />
The Recraft Color RGB node lets you define precise RGB color values to control colors in Recraft image generation.

## Node Function

This node creates a color configuration object that connects to the Recraft Controls node to specify colors used in generated images.

## Parameters

### Basic Parameters

| Parameter | Type    | Default | Description           |
| --------- | ------- | ------- | --------------------- |
| r         | integer | 0       | Red channel (0-255)   |
| g         | integer | 0       | Green channel (0-255) |
| b         | integer | 0       | Blue channel (0-255)  |

### Output

| Output         | Type          | Description                                        |
| -------------- | ------------- | -------------------------------------------------- |
| recraft\_color | Recraft Color | Color config object to connect to Recraft Controls |

## Usage Example

<Card title="Recraft Text to Image Workflow Example" icon="book" href="/tutorials/partner-nodes/recraft/recraft-text-to-image">
  Recraft Text to Image Workflow Example
</Card>

## Source Code

\[Node source code (Updated on 2025-05-03)]

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
