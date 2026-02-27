> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Vectorize Image - ComfyUI Built-in Node Documentation

> A Recraft Partner node that converts raster images to vector SVG format

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-vectorize-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=5d51a1b8e3e0147a608b40a2b63fd03b" alt="ComfyUI Built-in Recraft Vectorize Image Node" data-og-width="1506" width="1506" data-og-height="532" height="532" data-path="images/built-in-nodes/api_nodes/recraft/recraft-vectorize-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-vectorize-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=23fbfb9abc4484081911d9429b7189c8 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-vectorize-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=be602747c0232c39af30f0f3eaf6e4dc 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-vectorize-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=c54d33accece97bb0eb1ceb2684c59a2 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-vectorize-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=63a99715430be89ccc99c8d180e70ae9 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-vectorize-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ef44ee8a4f8a61c60adf74f27921888e 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-vectorize-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d10dd46c68bd11dddcb3042ba5a8da38 2500w" />

The Recraft Vectorize Image node uses Recraft's API to convert raster images (like photos, PNGs or JPEGs) into vector SVG format.

## Parameters

### Basic Parameters

| Parameter | Type  | Default | Description                           |
| --------- | ----- | ------- | ------------------------------------- |
| image     | Image | -       | Input image to be converted to vector |

### Output

| Output | Type   | Description                                                                 |
| ------ | ------ | --------------------------------------------------------------------------- |
| SVG    | Vector | Converted SVG vector graphic, needs to be connected to SaveSVG node to save |

## Usage Example

<Card title="Recraft Text to Image Workflow Example" icon="book" href="/tutorials/partner-nodes/recraft/recraft-text-to-image">
  Recraft Text to Image Workflow Example
</Card>

## Source Code

\[Node Source Code (Updated 2025-05-03)]

```python  theme={null}

class RecraftVectorizeImageNode:
    """
    Generates SVG synchronously from an input image.
    """

    RETURN_TYPES = (RecraftIO.SVG,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/image/Recraft"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": (IO.IMAGE, ),
            },
            "optional": {
            },
            "hidden": {
                "auth_token": "AUTH_TOKEN_COMFY_ORG",
            },
        }

    def api_call(
        self,
        image: torch.Tensor,
        auth_token=None,
        **kwargs,
    ):
        svgs = []
        total = image.shape[0]
        pbar = ProgressBar(total)
        for i in range(total):
            sub_bytes = handle_recraft_file_request(
                image=image[i],
                path="/proxy/recraft/images/vectorize",
                auth_token=auth_token,
            )
            svgs.append(SVG(sub_bytes))
            pbar.update(1)

        return (SVG.combine_all(svgs), )

```
