> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Creative Upscale - ComfyUI 原生节点文档

> 使用AI技术创意增强图像细节和分辨率的 Recraft 合作伙伴节点

<img src="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-creative-upscale-image.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=7478834eaacd7370aad308c51518c743" alt="ComfyUI 原生Recraft Creative Upscale节点" data-og-width="1506" width="1506" data-og-height="547" height="547" data-path="images/built-in-nodes/api_nodes/recraft/recraft-creative-upscale-image.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-creative-upscale-image.jpg?w=280&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d7a2bfb2973f947441a41fc72fdd9c4d 280w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-creative-upscale-image.jpg?w=560&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=527b4e2932b567ae3e1dad257bc54def 560w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-creative-upscale-image.jpg?w=840&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=d906b58bfbe8eb97f96e14b78affd1ea 840w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-creative-upscale-image.jpg?w=1100&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=56f4cc3114f3c59ac52aa34215c8e5f4 1100w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-creative-upscale-image.jpg?w=1650&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=acc6507de6af817f90a37ccd58e72c98 1650w, https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/recraft-creative-upscale-image.jpg?w=2500&fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=e4b03f62886a34f4fa862e4b74a86cd6 2500w" />

Recraft Creative Upscale 节点使用 Recraft 的 API 增加图像分辨率，还创造性地增强和丰富图像细节。

## 参数说明

### 基本参数

| 参数    | 类型 | 默认值 | 说明          |
| ----- | -- | --- | ----------- |
| image | 图像 | -   | 需要创意放大的输入图像 |

### 输出

| 输出    | 类型 | 说明           |
| ----- | -- | ------------ |
| IMAGE | 图像 | 创意放大后的高分辨率图像 |

## 源码参考

\[节点源码 (更新于2025-05-03)]

```python  theme={null}
class RecraftCreativeUpscaleNode(RecraftCrispUpscaleNode):
    """
    Upscale image synchronously.
    Enhances a given raster image using ‘creative upscale’ tool, boosting resolution with a focus on refining small details and faces.
    """

    RETURN_TYPES = (IO.IMAGE,)
    DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
    FUNCTION = "api_call"
    API_NODE = True
    CATEGORY = "api node/image/Recraft"

    RECRAFT_PATH = "/proxy/recraft/images/creativeUpscale"
```
