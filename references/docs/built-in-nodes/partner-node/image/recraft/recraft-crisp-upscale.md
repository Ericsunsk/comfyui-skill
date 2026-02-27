> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Crisp Upscale - ComfyUI Native Node Documentation

> A Recraft Partner node that enhances image clarity and resolution using AI

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-crisp-upscale-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=69f9f1c716832688e95c562c1f9be1c2" alt="ComfyUI Native Recraft Crisp Upscale Node" data-og-width="1506" width="1506" data-og-height="557" height="557" data-path="images/built-in-nodes/api_nodes/recraft/recraft-crisp-upscale-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-crisp-upscale-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0c0393fa898e99926335b0025566d595 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-crisp-upscale-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=b4c7f9d1a267e2d5597dfa3c48091f24 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-crisp-upscale-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0b3dc9225c597b0600eab950406aa14f 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-crisp-upscale-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0deb877d4dbdb129dfae58e912984525 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-crisp-upscale-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=fd780c684c97061454bf0ab8349b824f 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-crisp-upscale-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=52407efe5e34d3a18134a16885bdd483 2500w" />

The Recraft Crisp Upscale node uses Recraft's API to improve image resolution and clarity.

## Parameters

### Basic Parameters

| Parameter | Type  | Default | Description                |
| --------- | ----- | ------- | -------------------------- |
| image     | image | -       | Input image to be upscaled |

### Output

| Output | Type  | Description                        |
| ------ | ----- | ---------------------------------- |
| IMAGE  | image | Upscaled and enhanced output image |

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}
class RecraftCrispUpscaleNode:
    """
    Upscale image synchronously.
    Enhances a given raster image using ‘crisp upscale’ tool, increasing image resolution, making the image sharper and cleaner.
    """

    RETURN_TYPES = (IO.IMAGE,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/image/Recraft"

    RECRAFT_PATH = "/proxy/recraft/images/crispUpscale"

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
                path=self.RECRAFT_PATH,
                auth_token=auth_token,
            )
            images.append(torch.cat([bytesio_to_image_tensor(x) for x in sub_bytes], dim=0))
            pbar.update(1)

        images_tensor = torch.cat(images, dim=0)
        return (images_tensor,)
```
