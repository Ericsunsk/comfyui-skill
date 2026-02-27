> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Remove Background - ComfyUI Native Node Documentation

> A Recraft Partner node that automatically removes image backgrounds and creates transparent alpha channels

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-remove-background.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1248f93a0a34044b97c8d43a384fcf42" alt="ComfyUI Native Recraft Remove Background Node" data-og-width="1506" width="1506" data-og-height="576" height="576" data-path="images/built-in-nodes/api_nodes/recraft/recraft-remove-background.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-remove-background.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=022060f5697acf3ab310425a4df21961 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-remove-background.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=6ce54c49ab75a6de6cad82eab3b39452 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-remove-background.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0591c2f04665f3c9081ec6567a8c9cc5 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-remove-background.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=cfa052abab198fb5ad0a627b28918c78 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-remove-background.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=86a0c5382a198f5d3d9ed6cea471093d 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-remove-background.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=3967b3ea3c785716274d6d2c1a0acd04 2500w" />

The Recraft Remove Background node uses Recraft's API to intelligently detect and remove image backgrounds, creating images with transparent backgrounds and corresponding alpha masks.

## Parameters

### Basic Parameters

| Parameter | Type  | Default | Description                           |
| --------- | ----- | ------- | ------------------------------------- |
| image     | image | -       | Input image to remove background from |

### Output

| Output | Type  | Description                                          |
| ------ | ----- | ---------------------------------------------------- |
| IMAGE  | image | Image with background removed (with alpha channel)   |
| MASK   | mask  | Mask of the main subject (white areas are preserved) |

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}
class RecraftRemoveBackgroundNode:
    """
    Remove background from image, and return processed image and mask.
    """

    RETURN_TYPES = (IO.IMAGE, IO.MASK)
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
        images = []
        total = image.shape[0]
        pbar = ProgressBar(total)
        for i in range(total):
            sub_bytes = handle_recraft_file_request(
                image=image[i],
                path="/proxy/recraft/images/removeBackground",
                auth_token=auth_token,
            )
            images.append(torch.cat([bytesio_to_image_tensor(x) for x in sub_bytes], dim=0))
            pbar.update(1)

        images_tensor = torch.cat(images, dim=0)
        # use alpha channel as masks, in B,H,W format
        masks_tensor = images_tensor[:,:,:,-1:].squeeze(-1)
        return (images_tensor, masks_tensor)

```
