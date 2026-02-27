> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ClipVisionEncode - ComfyUI Built-in Node Documentation

> The ClipVisionEncode node is used to encode input images into visual feature vectors through the CLIP Vision model.

The `CLIP Vision Encode` node is an image encoding node in ComfyUI, used to convert input images into visual feature vectors through the CLIP Vision model. This node is an important bridge connecting image and text understanding, and is widely used in various AI image generation and processing workflows.

**Node Functionality**

* **Image feature extraction**: Converts input images into high-dimensional feature vectors
* **Multimodal bridging**: Provides a foundation for joint processing of images and text
* **Conditional generation**: Provides visual conditions for image-based conditional generation

## Inputs

| Parameter Name | Data Type    | Description                                                          |
| -------------- | ------------ | -------------------------------------------------------------------- |
| `clip_vision`  | CLIP\_VISION | CLIP vision model, usually loaded via the CLIPVisionLoader node      |
| `image`        | IMAGE        | The input image to be encoded                                        |
| `crop`         | Dropdown     | Image cropping method, options: center (center crop), none (no crop) |

## Outputs

| Output Name          | Data Type            | Description             |
| -------------------- | -------------------- | ----------------------- |
| CLIP\_VISION\_OUTPUT | CLIP\_VISION\_OUTPUT | Encoded visual features |

This output object contains:

* `last_hidden_state`: The last hidden state
* `image_embeds`: Image embedding vector
* `penultimate_hidden_states`: The penultimate hidden state
* `mm_projected`: Multimodal projection result (if available)
