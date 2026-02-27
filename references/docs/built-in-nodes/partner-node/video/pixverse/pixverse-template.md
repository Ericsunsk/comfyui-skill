> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# PixVerse Template - ComfyUI Native Node Documentation

> A helper node that provides preset templates for PixVerse video generation

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9995576d223575123de26cc31872a7f1" alt="ComfyUI Native PixVerse Template Node" data-og-width="1731" width="1731" data-og-height="694" height="694" data-path="images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=603937102f495f8a3fb3ff83676cca70 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4628eb175c018d421ce9b721e117d080 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ee169c282b5862fe461e93cf38e0c0c9 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f957824eb713681eb4e792466067b8b5 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=8fde847a6014189746bb77b83948bd06 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=022f8f0a2edf3ddc7f6a760c42dfa4c0 2500w" />

The PixVerse Template node lets you choose from predefined video generation templates to control the style and effects of PixVerse video generation nodes.
This helper node connects to PixVerse video generation nodes, allowing users to quickly apply preset video styles without manually adjusting complex parameter combinations.

## Parameters

### Required Parameters

| Parameter | Type   | Description                                    |
| --------- | ------ | ---------------------------------------------- |
| template  | Select | Choose a template from available video presets |

### Output

| Output             | Type                | Description                                              |
| ------------------ | ------------------- | -------------------------------------------------------- |
| pixverse\_template | PixverseIO.TEMPLATE | Configuration object containing the selected template ID |

## Source Code

\[Node Source Code (Updated 2025-05-05)]

```python  theme={null}

class PixverseTemplateNode:
    """
    Select template for Pixverse Video generation.
    """

    RETURN_TYPES = (PixverseIO.TEMPLATE,)
    RETURN_NAMES = ("pixverse_template",)
    FUNCTION = "create_template"
    CATEGORY = "api node/video/Pixverse"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "template": (list(pixverse_templates.keys()), ),
            }
        }

    def create_template(self, template: str):
        template_id = pixverse_templates.get(template, None)
        if template_id is None:
            raise Exception(f"Template '{template}' is not recognized.")
        # just return the integer
        return (template_id,)

```
