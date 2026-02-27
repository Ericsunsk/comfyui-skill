> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Concepts - ComfyUI Native Node Documentation

> A helper node that provides concept guidance for Luma image generation

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-concepts.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4b90a3fe60374751cdb7750a3afd1feb" alt="ComfyUI Native Luma Concepts Node" data-og-width="1731" width="1731" data-og-height="880" height="880" data-path="images/built-in-nodes/api_nodes/luma/luma-concepts.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-concepts.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=79424adbc8f8ccaa50d65af596aec5f9 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-concepts.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c51ef6cf53760ff4f96eebf00968352d 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-concepts.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=78fb97a11e9ae8a1ab96a896e5ad29c6 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-concepts.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=415802a6edcbb1d6747b02a378867d4f 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-concepts.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0b9148b064336c2063c29ccfdf6530a6 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/luma/luma-concepts.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6da52abf5b7f252c0bcc263803abdc69 2500w" />

The Luma Concepts node allows you to apply predefined camera concepts to the Luma generation process, providing precise control over camera angles and perspectives without complex prompt descriptions.

## Node Function

This node serves as a helper tool for Luma generation nodes, enabling users to select and apply predefined camera concepts. These concepts include different shooting angles (like overhead or low angle), camera distances (like close-up or long shot), and movement styles (like push-in or follow). It simplifies the creative workflow by providing an intuitive way to control camera effects in the generated output.

## Parameters

### Basic Parameters

| Parameter | Type   | Description                                                       |
| --------- | ------ | ----------------------------------------------------------------- |
| concept1  | select | First camera concept choice, includes various presets and "none"  |
| concept2  | select | Second camera concept choice, includes various presets and "none" |
| concept3  | select | Third camera concept choice, includes various presets and "none"  |
| concept4  | select | Fourth camera concept choice, includes various presets and "none" |

### Optional Parameters

| Parameter      | Type           | Description                                              |
| -------------- | -------------- | -------------------------------------------------------- |
| luma\_concepts | LUMA\_CONCEPTS | Optional Camera Concepts to merge with selected concepts |

### Output

| Output         | Type          | Description                                      |
| -------------- | ------------- | ------------------------------------------------ |
| luma\_concepts | LUMA\_CONCEPT | Combined object containing all selected concepts |

## Usage Examples

<Card title="Luma Text to Video Workflow Example" icon="book" href="/tutorials/partner-nodes/luma/luma-text-to-video">
  Luma Text to Video Workflow Example
</Card>

<Card title="Luma Image to Video Workflow Example" icon="book" href="/tutorials/partner-nodes/luma/luma-image-to-video">
  Luma Image to Video Workflow Example
</Card>

## How It Works

The Luma Concepts node offers a variety of predefined camera concepts including:

* Camera distances (close-up, medium shot, long shot)
* View angles (eye level, overhead, low angle)
* Movement types (push-in, follow, orbit)
* Special effects (handheld, stabilized, floating)

Users can select up to 4 concepts to use together. The node creates an object containing the selected camera concepts, which is then passed to Luma generation nodes. During generation, Luma AI uses these camera concepts to influence the viewpoint and composition of the output, ensuring the results reflect the chosen photographic effects.

By combining multiple camera concepts, users can create complex camera guidance without writing detailed prompt descriptions. This is particularly useful when specific camera angles or compositions are needed.

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}

class LumaConceptsNode(ComfyNodeABC):
    """
    Holds one or more Camera Concepts for use with Luma Text to Video and Luma Image to Video nodes.
    """

    RETURN_TYPES = (LumaIO.LUMA_CONCEPTS,)
    RETURN_NAMES = ("luma_concepts",)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "create_concepts"
    CATEGORY = "api node/image/Luma"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "concept1": (get_luma_concepts(include_none=True),),
                "concept2": (get_luma_concepts(include_none=True),),
                "concept3": (get_luma_concepts(include_none=True),),
                "concept4": (get_luma_concepts(include_none=True),),
            },
            "optional": {
                "luma_concepts": (
                    LumaIO.LUMA_CONCEPTS,
                    {
                        "tooltip": "Optional Camera Concepts to add to the ones chosen here."
                    },
                ),
            },
        }

    def create_concepts(
        self,
        concept1: str,
        concept2: str,
        concept3: str,
        concept4: str,
        luma_concepts: LumaConceptChain = None,
    ):
        chain = LumaConceptChain(str_list=[concept1, concept2, concept3, concept4])
        if luma_concepts is not None:
            chain = luma_concepts.clone_and_merge(chain)
        return (chain,)


```
