> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Style - Logo Raster - ComfyUI Built-in Node Documentation

> Helper node for setting logo raster style in Recraft image generation

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ec7753b1c7e871abc94ce5ea90472301" alt="ComfyUI Built-in Recraft Style - Logo Raster Node" data-og-width="1506" width="1506" data-og-height="559" height="559" data-path="images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0832354a50cd4765a6a4f992a3d26a36 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=59b35d3a5f4177c426f1d46207bbf081 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=326dfef3cde71e431ea62b58cc23828f 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=74597c93195f41a6960bee3d9a7ef7d2 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7b457d9b4a563b22d5c810e400a122ac 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0b41eba69cccc600e8e3bfe45e3c3c0d 2500w" />

This node creates a style configuration object that guides Recraft's image generation process toward professional logo design effects. By selecting different substyles, you can define the design style, complexity and use cases of the generated logo.

## Parameters

### Basic Parameters

| Parameter | Type      | Default | Description                                  |
| --------- | --------- | ------- | -------------------------------------------- |
| substyle  | Selection | -       | Specific substyle for logo raster (Required) |

### Output

| Output         | Type          | Description                                                     |
| -------------- | ------------- | --------------------------------------------------------------- |
| recraft\_style | Recraft Style | Style configuration object, connects to Recraft generation node |

## Usage Example

<Card title="Recraft Text to Image Workflow Example" icon="book" href="/tutorials/partner-nodes/recraft/recraft-text-to-image">
  Recraft Text to Image Workflow Example
</Card>

## Source Code

\[Node Source Code (Updated 2025-05-03)]

```python  theme={null}
class RecraftStyleV3LogoRasterNode(RecraftStyleV3RealisticImageNode):
    """
    Select vector_illustration style and optional substyle.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "substyle": (get_v3_substyles(s.RECRAFT_STYLE, include_none=False),),
            }
        }

    RECRAFT_STYLE = RecraftStyleV3.logo_raster
```
