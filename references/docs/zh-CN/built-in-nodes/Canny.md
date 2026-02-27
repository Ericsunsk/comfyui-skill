> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Canny - ComfyUI 原生节点文档

> Canny 节点是 ComfyUI 中用于提取图像边缘的节点。

从照片中提取所有边缘线条，就像用钢笔为照片描边一样，把物体的轮廓和细节边界都画出来。

## 工作原理

想象您是一位画家，要用钢笔为一张照片描边。Canny节点就像一个智能助手，帮您决定哪些地方需要画线（边缘），哪些地方不需要。

这个过程就像筛选工作：

* **高阈值**是"必须画线的标准"：只有非常明显、清晰的轮廓线才会被画出来，比如人物脸部轮廓、建筑物边框
* **低阈值**是"完全不画线的标准"：太微弱的边缘会被忽略，避免画出噪点和无意义的线条
* **中间区域**：介于两个标准之间的边缘，如果连着"必须画的线"就一起画出来，如果是孤立的就不画

最终输出一张黑白图像，白色部分是检测到的边缘线条，黑色部分是没有边缘的区域。

## 输入

| 参数名称 | 数据类型  | 输入方式 | 默认值 | 取值范围      | 功能说明                              |
| ---- | ----- | ---- | --- | --------- | --------------------------------- |
| 图像   | IMAGE | 连接   | -   | -         | 需要提取边缘的原始照片                       |
| 低阈值  | FLOAT | 手动输入 | 0.4 | 0.01-0.99 | 低阈值，决定忽略多弱的边缘。数值越小保留的细节越多，但可能产生噪点 |
| 高阈值  | FLOAT | 手动输入 | 0.8 | 0.01-0.99 | 高阈值，决定保留多强的边缘。数值越大只保留最明显的轮廓线      |

## 输出

| 输出名称 | 数据类型  | 说明                            |
| ---- | ----- | ----------------------------- |
| 图像   | IMAGE | 黑白边缘图像，白色线条为检测到的边缘，黑色区域为无边缘部分 |

## 参数对比

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e19fdaa3bd2abafb185fb663b1e3d2ed" alt="原图" data-og-width="716" width="716" data-og-height="716" height="716" data-path="images/built-in-nodes/canny/input.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=824b6c04bf12f0178b9e6df714395391 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6042657960eb1ec2bb202ed95eb67459 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ca28e7b476c36587135b2ea4e1be2561 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5be0ade4e451d2ba917c170d63d8f867 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=55ca7259b256dc41949fd5b35bb340eb 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/input.webp?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c4b1dcf33487963a29e728f91bb66082 2500w" />

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9992b55c628d860dbf1f676687e638ce" alt="参数对比" data-og-width="1039" width="1039" data-og-height="1331" height="1331" data-path="images/built-in-nodes/canny/compare.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=40ce24f56d9bb8f4a0a9487f3472cf96 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=224588df1839ae86519deed88b555dc6 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=dd4e3a6d33e18024452f1273acd2de1d 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=46fe8ded5d1d7095fdb1b01a24843df8 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=313a9b558bdbfebc2b20abfb4122450f 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/built-in-nodes/canny/compare.webp?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4329cbfbdc01e671a82dfb6e7c69d6f6 2500w" />

**常见问题：**

* 边缘断断续续：尝试降低高阈值
* 出现很多噪点：提高低阈值
* 丢失重要细节：降低低阈值
* 边缘太粗糙：检查输入图像质量和分辨率
