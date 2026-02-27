> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Style - Realistic Image - ComfyUI 原生节点文档

> 为Recraft图像生成设置真实照片风格的辅助节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d841ce2d09abd4dd25d467f459f3734f" alt="ComfyUI 原生 Recraft Style - Realistic Image 节点" data-og-width="1506" width="1506" data-og-height="596" height="596" data-path="images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=a64f8338a4dc2d541f82729051be06eb 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ebb48df01dcd01b3510f54a48117e837 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0d724b58b204c8f17055b4db1dbf9dbc 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f95e20e4b19070f5eae88e2d13d62982 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=bb647eba9abbbb0d79cb234affde4696 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-realistic-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=4384ca703b9cc5f99c4e2aed5d437d4e 2500w" />

Recraft Style - Realistic Image 节点用于设置Recraft图像生成的真实照片风格，提供多种子风格选项，以控制生成图像的视觉特性。

## 节点功能

此节点创建一个风格配置对象，用于指导Recraft的图像生成过程朝向真实照片的视觉效果。

## 参数说明

### 基本参数

| 参数       | 类型  | 默认值  | 说明               |
| -------- | --- | ---- | ---------------- |
| substyle | 选择项 | None | 真实照片风格的具体子风格（必选） |

### 输出

| 输出             | 类型            | 说明                    |
| -------------- | ------------- | --------------------- |
| recraft\_style | Recraft Style | 风格配置对象，连接到Recraft生成节点 |

## 使用示例

<Card title="Recraft Text to Image 工作流示例" icon="book" href="/zh-CN/tutorials/partner-nodes/recraft/recraft-text-to-image">
  Recraft Text to Image 工作流示例
</Card>

## 源码参考

\[节点源码 (更新于2025-05-03)]

```python  theme={null}

class RecraftStyleV3RealisticImageNode:
    """
    Select realistic_image style and optional substyle.
    """

    RETURN_TYPES = (RecraftIO.STYLEV3,)
    RETURN_NAMES = ("recraft_style",)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "create_style"
    CATEGORY = "api node/image/Recraft"

    RECRAFT_STYLE = RecraftStyleV3.realistic_image

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "substyle": (get_v3_substyles(s.RECRAFT_STYLE),),
            }
        }

    def create_style(self, substyle: str):
        if substyle == "None":
            substyle = None
        return (RecraftStyle(self.RECRAFT_STYLE, substyle),)

```
