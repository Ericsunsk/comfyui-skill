> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Load CLIP Vision - ComfyUI Built-in Node Documentation

> The Load CLIP Vision node is used to load CLIP Vision models from the `ComfyUI/models/clip_vision` folder.

This node automatically detects models located in the `ComfyUI/models/clip_vision` folder, as well as any additional model paths configured in the `extra_model_paths.yaml` file. If you add models after starting ComfyUI, please **refresh the ComfyUI interface** to ensure the latest model files are listed.

## Inputs

| Field       | Data Type      | Description                                                                 |
| ----------- | -------------- | --------------------------------------------------------------------------- |
| `clip_name` | COMBO\[STRING] | Lists all supported model files in the `ComfyUI/models/clip_vision` folder. |

## Outputs

| Field         | Data Type    | Description                                                                        |
| ------------- | ------------ | ---------------------------------------------------------------------------------- |
| `clip_vision` | CLIP\_VISION | Loaded CLIP Vision model, ready for encoding images or other vision-related tasks. |
