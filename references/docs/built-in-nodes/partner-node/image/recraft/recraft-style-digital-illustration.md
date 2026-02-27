> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Style - Digital Illustration - ComfyUI Native Node Documentation

> A helper node for setting digital illustration style in Recraft image generation

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-digital-illustraion.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=dce25f2de84056b2fe15b3264ffcf80e" alt="ComfyUI Native Recraft Style Digital Illustration Node" data-og-width="1506" width="1506" data-og-height="559" height="559" data-path="images/built-in-nodes/api_nodes/recraft/recraft-style-digital-illustraion.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-digital-illustraion.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=1b7aff4378f2ff6fbc49b9c6ac03b611 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-digital-illustraion.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=04ea86ec8c3929ef84a3a9ad377e858a 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-digital-illustraion.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=716dbb9bc5b09f88fee46700a1e03474 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-digital-illustraion.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d1c579f74e4ff39e9cd00f0fdd46b46f 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-digital-illustraion.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=32878d0e6f167d30cb50e2d405cb73ec 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-digital-illustraion.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e512147ed8a424cf24887bb4b0125db5 2500w" />

This node creates a style configuration object that guides Recraft's image generation process towards a digital illustration look.

## Parameters

### Basic Parameters

| Parameter | Type   | Default | Description                               |
| --------- | ------ | ------- | ----------------------------------------- |
| substyle  | select | None    | Specific substyle of digital illustration |

### Output

| Output         | Type          | Description                                                |
| -------------- | ------------- | ---------------------------------------------------------- |
| recraft\_style | Recraft Style | Style config object to connect to Recraft generation nodes |

## Usage Example

<Card title="Recraft Text to Image Workflow Example" icon="book" href="/tutorials/partner-nodes/recraft/recraft-text-to-image">
  Recraft Text to Image Workflow Example
</Card>

## Source Code

\[Node source code (Updated on 2025-05-03)]

```python  theme={null}
class RecraftStyleV3DigitalIllustrationNode(RecraftStyleV3RealisticImageNode):
    """
    Select digital_illustration style and optional substyle.
    """

    RECRAFT_STYLE = RecraftStyleV3.digital_illustration

```
