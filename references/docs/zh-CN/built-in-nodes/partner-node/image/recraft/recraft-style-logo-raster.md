> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Style - Logo Raster - ComfyUI 原生节点文档

> 为Recraft图像生成设置Logo栅格风格的辅助节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=ec7753b1c7e871abc94ce5ea90472301" alt="ComfyUI 原生 Recraft Style - Logo Raster 节点" data-og-width="1506" width="1506" data-og-height="559" height="559" data-path="images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0832354a50cd4765a6a4f992a3d26a36 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=59b35d3a5f4177c426f1d46207bbf081 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=326dfef3cde71e431ea62b58cc23828f 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=74597c93195f41a6960bee3d9a7ef7d2 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7b457d9b4a563b22d5c810e400a122ac 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-style-logo-raster.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=0b41eba69cccc600e8e3bfe45e3c3c0d 2500w" />

此节点创建一个风格配置对象，用于指导Recraft的图像生成过程朝向专业标志设计的视觉效果。通过选择不同的子风格，可以定义生成标志的设计风格、复杂度和适用场景。

## 参数说明

### 基本参数

| 参数       | 类型  | 默认值 | 说明                 |
| -------- | --- | --- | ------------------ |
| substyle | 选择项 | -   | Logo栅格风格的具体子风格(必选) |

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
class RecraftStyleV3LogoRasterNode(RecraftStyleV3RealisticImageNode):
    """
    Select vector_illustration style and optional substyle.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "substyle": (get_v3_substyles(s.RECRAFT_STYLE, include_none=False),),
            }
        }

    RECRAFT_STYLE = RecraftStyleV3.logo_raster
```
