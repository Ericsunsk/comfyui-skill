> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Canny - ComfyUI Built-in Node Documentation

> The Canny node used to extract edge lines from photos.

Extract all edge lines from photos, like using a pen to outline a photo, drawing out the contours and detail boundaries of objects.

## Working Principle

Imagine you are an artist who needs to use a pen to outline a photo. The Canny node acts like an intelligent assistant, helping you decide where to draw lines (edges) and where not to.

This process is like a screening job:

* **High threshold** is the "must draw line standard": only very obvious and clear contour lines will be drawn, such as facial contours of people and building frames
* **Low threshold** is the "definitely don't draw line standard": edges that are too weak will be ignored to avoid drawing noise and meaningless lines
* **Middle area**: edges between the two standards will be drawn together if they connect to "must draw lines", but won't be drawn if they are isolated

The final output is a black and white image, where white parts are detected edge lines and black parts are areas without edges.

## Inputs

| Parameter Name   | Data Type | Input Type | Default | Range     | Function Description                                                                                            |
| ---------------- | --------- | ---------- | ------- | --------- | --------------------------------------------------------------------------------------------------------------- |
| `image`          | IMAGE     | Input      | -       | -         | Original photo that needs edge extraction                                                                       |
| `low_threshold`  | FLOAT     | Widget     | 0.4     | 0.01-0.99 | Low threshold, determines how weak edges to ignore. Lower values preserve more details but may produce noise    |
| `high_threshold` | FLOAT     | Widget     | 0.8     | 0.01-0.99 | High threshold, determines how strong edges to preserve. Higher values only keep the most obvious contour lines |

## Outputs

| Output Name | Data Type | Description                                                                                     |
| ----------- | --------- | ----------------------------------------------------------------------------------------------- |
| `image`     | IMAGE     | Black and white edge image, white lines are detected edges, black areas are parts without edges |

## Parameter Comparison

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e19fdaa3bd2abafb185fb663b1e3d2ed" alt="Original Image" data-og-width="716" width="716" data-og-height="716" height="716" data-path="images/built-in-nodes/canny/input.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=824b6c04bf12f0178b9e6df714395391 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6042657960eb1ec2bb202ed95eb67459 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ca28e7b476c36587135b2ea4e1be2561 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5be0ade4e451d2ba917c170d63d8f867 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=55ca7259b256dc41949fd5b35bb340eb 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c4b1dcf33487963a29e728f91bb66082 2500w" />

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9992b55c628d860dbf1f676687e638ce" alt="Parameter Comparison" data-og-width="1039" width="1039" data-og-height="1331" height="1331" data-path="images/built-in-nodes/canny/compare.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=40ce24f56d9bb8f4a0a9487f3472cf96 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=224588df1839ae86519deed88b555dc6 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=dd4e3a6d33e18024452f1273acd2de1d 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=46fe8ded5d1d7095fdb1b01a24843df8 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=313a9b558bdbfebc2b20abfb4122450f 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4329cbfbdc01e671a82dfb6e7c69d6f6 2500w" />

**Common Issues:**

* Broken edges: Try lowering high threshold
* Too much noise: Raise low threshold
* Missing important details: Lower low threshold
* Edges too rough: Check input image quality and resolution
