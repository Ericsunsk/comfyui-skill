> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Pixverse Template - ComfyUI 原生节点文档

> 为Pixverse视频生成提供预设模板的辅助节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=9995576d223575123de26cc31872a7f1" alt="ComfyUI 原生 Pixverse Template 节点" data-og-width="1731" width="1731" data-og-height="694" height="694" data-path="images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=603937102f495f8a3fb3ff83676cca70 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4628eb175c018d421ce9b721e117d080 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ee169c282b5862fe461e93cf38e0c0c9 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f957824eb713681eb4e792466067b8b5 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=8fde847a6014189746bb77b83948bd06 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/pixverse/pixverse-template.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=022f8f0a2edf3ddc7f6a760c42dfa4c0 2500w" />

Pixverse Template 节点允许你从预定义的视频生成模板中选择，用于控制Pixverse视频生成节点的输出风格和效果。这是一个辅助节点，可以连接到Pixverse的视频生成节点，让用户能够快速应用预设的视频风格，而无需手动调整复杂的参数组合。

## 参数说明

### 必需参数

| 参数       | 类型  | 说明                    |
| -------- | --- | --------------------- |
| template | 选择项 | 从可用的预设视频生成模板列表中选择一个模板 |

### 输出

| 输出                 | 类型                  | 说明            |
| ------------------ | ------------------- | ------------- |
| pixverse\_template | PixverseIO.TEMPLATE | 包含所选模板ID的配置对象 |

## 源码参考

\[节点源码 (更新于2025-05-05)]

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
