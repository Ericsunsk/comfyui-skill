> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Style - Realistic Image - ComfyUI Native Node Documentation

> A helper node for setting realistic photo style in Recraft image generation

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d841ce2d09abd4dd25d467f459f3734f" alt="ComfyUI Native Recraft Style - Realistic Image Node" data-og-width="1506" width="1506" data-og-height="596" height="596" data-path="images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a64f8338a4dc2d541f82729051be06eb 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ebb48df01dcd01b3510f54a48117e837 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0d724b58b204c8f17055b4db1dbf9dbc 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f95e20e4b19070f5eae88e2d13d62982 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=bb647eba9abbbb0d79cb234affde4696 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4384ca703b9cc5f99c4e2aed5d437d4e 2500w" />

The Recraft Style - Realistic Image node helps set up realistic photo styles for Recraft image generation, with various substyle options to control the visual characteristics of generated images.

## Node Function

This node creates a style configuration object that guides Recraft's image generation process towards realistic photo effects.

## Parameters

### Basic Parameters

| Parameter | Type   | Default | Description                                     |
| --------- | ------ | ------- | ----------------------------------------------- |
| substyle  | select | None    | Specific substyle of realistic photo (Required) |

### Output

| Output         | Type          | Description                                                |
| -------------- | ------------- | ---------------------------------------------------------- |
| recraft\_style | Recraft Style | Style config object to connect to Recraft generation nodes |

## Usage Example

<Card title="Recraft Text to Image Workflow Example" icon="book" href="/tutorials/partner-nodes/recraft/recraft-text-to-image">
  Recraft Text to Image Workflow Example
</Card>

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}

class RecraftStyleV3RealisticImageNode:
    """
    Select realistic_image style and optional substyle.
    """

    RETURN_TYPES = (RecraftIO.STYLEV3,)
    RETURN_NAMES = ("recraft_style",)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "create_style"
    CATEGORY = "api node/image/Recraft"

    RECRAFT_STYLE = RecraftStyleV3.realistic_image

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "substyle": (get_v3_substyles(s.RECRAFT_STYLE),),
            }
        }

    def create_style(self, substyle: str):
        if substyle == "None":
            substyle = None
        return (RecraftStyle(self.RECRAFT_STYLE, substyle),)

```
