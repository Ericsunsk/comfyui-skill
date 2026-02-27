> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ClipTextEncodeHunyuanDit - ComfyUI Built-in Node Documentation

> The ClipTextEncodeHunyuanDit node is used to encode text prompts into HunyuanDiT-compatible conditioning embeddings.

The `CLIPTextEncodeHunyuanDiT` node's main function is to convert input text into a form that the model can understand. It is an advanced conditioning node specifically designed for the dual text encoder architecture of the HunyuanDiT model.
Its primary role is like a translator, converting our text descriptions into "machine language" that the AI model can understand. The `bert` and `mt5xl` inputs prefer different types of prompt inputs.

## Inputs

| Parameter | Data Type | Description                                                                                                                                  |
| --------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `clip`    | CLIP      | A CLIP model instance used for text tokenization and encoding, which is core to generating conditions.                                       |
| `bert`    | STRING    | Text input for encoding, prefers phrases and keywords, supports multiline and dynamic prompts.                                               |
| `mt5xl`   | STRING    | Another text input for encoding, supports multiline and dynamic prompts (multilingual), can use complete sentences and complex descriptions. |

## Outputs

| Parameter      | Data Type    | Description                                                                     |
| -------------- | ------------ | ------------------------------------------------------------------------------- |
| `CONDITIONING` | CONDITIONING | The encoded conditional output used for further processing in generation tasks. |
