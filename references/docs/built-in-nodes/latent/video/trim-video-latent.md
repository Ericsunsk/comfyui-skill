> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# TrimVideoLatent Node

> Trim video frames in latent space

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=87bf02eabffeba90db7e9409ddf48dd1" alt="ComfyUI TrimVideoLatent Node" data-og-width="1608" width="1608" data-og-height="762" height="762" data-path="images/built-in-nodes/latent/video/trim-video-latent.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8cabf59929e83251d9c4faced9f4559f 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=51e4b50bfc4f860f1118006743c72add 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=50cbec822d7d2788a5130da31b75e5c2 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c654433a8b05804a967cf79eaf9d30b4 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e2aacbe2d5b4822bb66da6e5e0a47fd7 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/latent/video/trim-video-latent.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=90e007a0181c33d3d285eaefccd5fba3 2500w" />

The TrimVideoLatent node is used to trim video frames in latent space (LATENT). It is commonly used when processing video latent sequences to remove unwanted frames from the beginning, achieving "forward trimming" of the video.

Basic usage: Input the video latent data to be trimmed into samples, and set trim\_amount to the number of frames to trim. The node will trim the specified number of frames from the beginning of the video and output the remaining latent sequence.
Typical scenarios: Used in video generation, video editing and other scenarios to remove unwanted leading frames, or to work with other nodes to achieve video segment splicing and processing.

## Parameters

### Input Parameters

| Parameter    | Type   | Required | Default | Description                           |
| ------------ | ------ | -------- | ------- | ------------------------------------- |
| samples      | LATENT | Yes      | None    | Input latent video data               |
| trim\_amount | INT    | Yes      | 0       | Number of frames to trim (from start) |

### Output Parameters

| Parameter | Type   | Description               |
| --------- | ------ | ------------------------- |
| samples   | LATENT | Trimmed video latent data |

## Usage Example

<Card title="Wan2.1 VACE Video Generation Workflow Example" icon="book" href="/tutorials/video/wan/vace">
  Wan2.1 VACE Video Generation Workflow Example
</Card>

### Source Code

```python  theme={null}
class TrimVideoLatent:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "samples": ("LATENT",),
                              "trim_amount": ("INT", {"default": 0, "min": 0, "max": 99999}),
                             }}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "op"

    CATEGORY = "latent/video"

    EXPERIMENTAL = True

    def op(self, samples, trim_amount):
        samples_out = samples.copy()

        s1 = samples["samples"]
        samples_out["samples"] = s1[:, :, trim_amount:]
        return (samples_out,)

```
