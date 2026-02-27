> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 连线

> 了解 ComfyUI 中的连接链接

<Note>
  由于 ComfyUI 仍旧在快速迭代和开发中，我们每天都在持续迭代，所以本文中相关操作的部分，可能会有一定变动或者遗漏，请以实际为准，如果你遇到实际的操作有变动，可能是因为我们进行了迭代更新，你也可以 fork [这个 repo](https://github.com/Comfy-Org/docs) 的和我们一起完善这个文档。
</Note>

## 连线连接节点

在 ComfyUI 的术语中，节点之间的线条或曲线称为 ***连线***。这些连线可以以多种方式显示，例如曲线、直角线、直线或直接完全隐藏。

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/link_styles.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=f8d0e4e3831f8d6ff87f35f0c99ba9cf" alt="连线样式" data-og-width="1589" width="1589" data-og-height="917" height="917" data-path="images/interface/link/link_styles.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/link_styles.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=03c3b63b23f9f66234a8c970b1ac87a4 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/link_styles.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=2ca5e7791ae5cebe760201527d1e721d 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/link_styles.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5d3a6cdf39918c5ca833750c27d7585c 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/link_styles.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=dd607c8f625230d3e3666eaf52ea9b7d 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/link_styles.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0e14b4122210e7b2bb8733bb366eb5e0 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/link_styles.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8db036858fb704e08de8177246e6394b 2500w" />

你可以在 **设置菜单** --> **画面（Lite Graph）** --> **画面（Grap）** --> **连线渲染模式(Link Render Mode)** 进行连线样式的修改。

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/link/render_mode.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=96d63b1af226ef4b9ffbb71eecc62d79" alt="Canvas Menu" data-og-width="1066" width="1066" data-og-height="764" height="764" data-path="images/zh/interface/link/render_mode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/link/render_mode.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2f073fd1f95f9995f63d95faf58f2638 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/link/render_mode.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=dc3a500958de1cc2f425c7d16e6a0435 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/link/render_mode.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a7b747b2837a031b69b0e9d19285da93 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/link/render_mode.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a137eed3e7bb0e2b865b43bb24b71c03 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/link/render_mode.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e27cf488005746314cc40b45718cacee 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/link/render_mode.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e0643a5811ea8121afa4c7f37baf0a19 2500w" />

也可以在 **Canvas Menu** 中临时隐藏连线。

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/canvas_menu.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=85e33ad64f139785144b0e379c793045" alt="Canvas Menu" data-og-width="272" width="272" data-og-height="620" height="620" data-path="images/interface/link/canvas_menu.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/canvas_menu.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8930a2fa7914e4a3994b14eb2162d90b 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/canvas_menu.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ee78f1b13a81190bb932f6e9d4e86294 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/canvas_menu.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=dc4a3191147bdaa4c09c97350bfc7b3c 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/canvas_menu.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=9e1c99e6ebd74831df213de4b6c858c4 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/canvas_menu.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=eaf9a88a01b09a62c2c9d87cfa3fbd59 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/canvas_menu.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ac011e8679bd3f117bcc3b7dbc4e3089 2500w" />

根据情况，可能需要查看所有链接。特别是在学习、分享或仅仅理解工作流时，连线之间的可见性可以让其它用户理解不同节点之间的相互作用。但对于那些不打算被更改的打包工作流，你也可以隐藏连线从而获得一个干净简洁的布局。

### 重新路由节点

通常，当我们节点过多时，对应的连接线难免被遮挡或者出现交叉，这时理解工作流作用就变得十分困难，如果你想要对应连线保持清晰，则可以采用一个 **重新路由（reroute）** 节点来手动调整连线。

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/reroute.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=473539e846d7bb6b4c3d61c5d78a2c91" alt="ComfyUI 重新路由节点" data-og-width="900" width="900" data-og-height="365" height="365" data-path="images/interface/link/reroute.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/reroute.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c89a5d5ba3992b366bd140e40b9e7ec4 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/reroute.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5b0e9691e87bfdad69570b1a52dd893a 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/reroute.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=96ab5d1fd8c9086f7c0b36ccac7fccf5 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/reroute.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=6bdb8be3153d06a3e5354f2d488922e6 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/reroute.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=9f874a9ab894f51dbe51306bd0c730ea 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/reroute.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=312fda60408cc84e0ac59dd98c5ed807 2500w" />

同时我们也在努力迭代，我们也已经完善 litegraph 原生的重路由功能，我们更建议在未来使用这个功能进行连线的重新组织。

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/native_reroute.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=9f33c8c4d344a3cb2758e7f33ef65a0b" alt="ComfyUI 重新路由节点" data-og-width="463" width="463" data-og-height="315" height="315" data-path="images/interface/link/native_reroute.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/native_reroute.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ed36c01b39b1a51e5d3fd7472431fc83 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/native_reroute.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=7993952e65b9b4d48273a581b44e5560 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/native_reroute.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=e9de8c15d06c7ed73012046d6b98610b 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/native_reroute.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=50c6e6421a8c2310c6815c7ab745553a 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/native_reroute.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=25ab2a58bc0e00f2f4c181cf5c242037 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/link/native_reroute.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=6afda371c5a718f1656e83d5ead5a302 2500w" />

## 颜色编码

节点属性的数据类型通过输入/输出端口和链接连接线的颜色编码来表示。我们总是可以通过颜色判断哪些输入和输出可以相互连接。端口只能连接到相同颜色的其他端口来保证对应数据类型的匹配。

目前常见数据类型：

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5" alt="ComfyUI 节点数据类型" data-og-width="685" width="685" data-og-height="356" height="356" data-path="images/concepts/node/data_type.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3a128b7a0a1e6e93733f2fe649efd330 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=56df7925857870daf0995d69dcca1c24 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=69feb5a2bdde5813c9444c500710e1cb 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=087178033c73065ed5a521cb04f3f5cb 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=389aadb6b698921a58ffb6e3c65ce796 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9ee271b46d36d4ab90b1688dbcf80c5d 2500w" />

| 数据类型       | 颜色   |
| ---------- | ---- |
| 扩散模型       | 薰衣草色 |
| CLIP 模型    | 黄色   |
| VAE 模型     | 玫瑰色  |
| 条件化        | 橙色   |
| 潜在图像       | 粉色   |
| 像素图像       | 蓝色   |
| 蒙版         | 绿色   |
| 数字（整数或浮点数） | 浅绿色  |
| 网格（Mesh）   | 亮绿色  |
