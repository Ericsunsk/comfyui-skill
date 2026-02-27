> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Controls - ComfyUI Native Node Documentation

> Node providing advanced control parameters for Recraft image generation

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-contorols.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6c5b9b0c3f9e255975e9bca7d12a9d2b" alt="ComfyUI Native Recraft Controls Node" data-og-width="1506" width="1506" data-og-height="556" height="556" data-path="images/built-in-nodes/api_nodes/recraft/recraft-contorols.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-contorols.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f9af5a68245f18802627cb8fac6236eb 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-contorols.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0a248fae86e42157a33fa0f494faf417 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-contorols.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=eaa5a11dde8d914734484925b30a8e60 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-contorols.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=8f2eb8275c9267cd02ae62360c613460 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-contorols.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=8156e45f55c046a11b139e79f0376ad6 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-contorols.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=eff587249e8652cd80b6f4f1088d671a 2500w" />

The Recraft Controls node lets you define control parameters (like colors and background colors) to guide Recraft's image generation process. This node combines multiple control inputs into a unified control object.

## Parameters

### Optional Parameters

| Parameter         | Type          | Description                         |
| ----------------- | ------------- | ----------------------------------- |
| colors            | Recraft Color | Color controls for image generation |
| background\_color | Recraft Color | Background color control            |

### Output

| Output            | Type             | Description                                        |
| ----------------- | ---------------- | -------------------------------------------------- |
| recraft\_controls | Recraft Controls | Control config object for Recraft generation nodes |

## Usage Example

<Card title="Recraft Text to Image Workflow Example" icon="book" href="/tutorials/partner-nodes/recraft/recraft-text-to-image">
  Recraft Text to Image Workflow Example
</Card>

## How It Works

Node process:

1. Collects input control parameters (colors and background\_color)
2. Combines these parameters into a structured control object
3. Outputs this control object for connecting to Recraft generation nodes

When connected to Recraft generation nodes, these control parameters influence the AI generation process. The AI considers multiple factors beyond just the text prompt's semantic content. If color inputs are configured, the AI will try to use these colors appropriately in the generated image.

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}
class RecraftControlsNode:
    """
    Create Recraft Controls for customizing Recraft generation.
    """

    RETURN_TYPES = (RecraftIO.CONTROLS,)
    RETURN_NAMES = ("recraft_controls",)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "create_controls"
    CATEGORY = "api node/image/Recraft"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
            "optional": {
                "colors": (RecraftIO.COLOR,),
                "background_color": (RecraftIO.COLOR,),
            }
        }

    def create_controls(self, colors: RecraftColorChain=None, background_color: RecraftColorChain=None):
        return (RecraftControls(colors=colors, background_color=background_color), )

```
