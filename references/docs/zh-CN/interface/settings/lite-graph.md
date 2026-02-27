> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 画面(LiteGraph)设置

> ComfyUI 图形渲染引擎 LiteGraph 的设置选项详细说明

LiteGraph 是 ComfyUI 的底层图形渲染引擎，这个分类下的设置主要控制画布、节点、链接等图形界面的行为和外观。

## 画布相关设置

### 显示选择工具箱

* **默认值**：启用
* **功能**：选择工具箱是选中节点后在节点上浮动显示的快捷操作工具栏，提供了常用的快捷操作如部分运行、固定、删除、颜色修改等等

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=58f8da6ea3f276272d9be4c4e1e5ebb1" alt="显示选择工具箱" data-og-width="1316" width="1316" data-og-height="756" height="756" data-path="images/interface/setting/lite-graph/selection-toolbox.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0852d125213f53175878df6fa7ca6a0b 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=387feb2717783c88f242df53ba34585c 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=abdd92feb502d99b79e866826806a3c8 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bafd39d46c38f51e73882f7a1edc2b6c 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=650035cfd4c313de8f498ae453099761 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d9083ca10bbeaee4286ad04b2a99d72c 2500w" />

### 低质量渲染缩放阈值

* **默认值**：0.6
* **范围**：0.1 - 1.0
* **功能**： 在渲染界面时，特别是当工作流特别复杂及整个画布特别大时，对应元素的前端渲染会消耗特别多的内存而造成卡顿，通过调低此阈值，可以控制元素在缩放到特定百分比时进入低质量渲染模式，从而降低内存消耗，对应不同渲染模式如下图

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e6481f3430f77f8312d78b853d307774" alt="低质量渲染" data-og-width="1536" width="1536" data-og-height="1008" height="1008" data-path="images/interface/setting/lite-graph/render-mode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9ef378358eb4456f90b98919e1869573 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a1187ef33614dc82ab68badc0e511716 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2342fc9d728bbb28074f821d164491d1 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b9e7dd615fa32ad7f6b2237c9f7d9bcb 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=cf24d96b6acdc6755988b308baddaece 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6d920a9762db0305aac10ff12f950c41 2500w" />

### 最大FPS

* **默认值**：0（使用屏幕刷新率）
* **范围**：0 - 120
* **功能**：限制画布的渲染帧率，0表示使用屏幕刷新率，越高的 FPS 会让画面（Canvas） 渲染越流畅，但同时也会消耗更多性能，但过小时则会有越明显的卡顿感。

### 始终吸附到网格

* **默认值**：禁用
* **功能**：在此选项没有启用时，你可以按住 `Shift` 键来使节点边缘和网格对齐，在启用后则无需按住 `Shift` 键即可自动对齐网格

<video controls>
  <source src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/snap-to-grid.mp4?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=2afb1c5c09f9fca9f4b8333e975d0f44" type="video/mp4" data-path="images/interface/setting/lite-graph/snap-to-grid.mp4" />
</video>

### 吸附网格大小

* **范围**：1 - 500
* **功能**：在启用自动吸附或者按住 `Shift` 键进行节点的移动时，这个参数会决定吸附的网格大小，默认值为 10，你可以根据你的需求进行调整。

### 启用快速缩放快捷键

* **默认值**：启用
* **功能**：启用 `Ctrl + Shift + 鼠标左键拖拽` 的快速缩放功能，提供更快速的缩放操作方式

<video controls>
  <source src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/fast-zoom.mp4?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2d6e53041600bb97d28cb81786af40fd" type="video/mp4" data-path="images/interface/setting/lite-graph/fast-zoom.mp4" />
</video>

### 显示图形画布菜单

* **默认值**：启用
* **功能**：控制是否显示右下角的画布菜单

画布菜单位于整个 ComfyUI 界面的右下角，包含了画布的缩放、临时隐藏所有连线、快速缩放工作流到适应画布等操作，如下图所示

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=23c8c2f94f2befbfc9cd3a484140af5b" alt="显示图形画布菜单" data-og-width="360" width="360" data-og-height="764" height="764" data-path="images/interface/setting/lite-graph/canvas_menu.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=114872d393c2d9e608b74229fc222b56 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4993f24b3b9953267d53e1936538deab 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d2a8481ae2e09ad7f3e72afccb3cefc6 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f60dc6b8de22500f4caa0167871cf4c8 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c703da828402b98155cd2f344f90c13e 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=675a0c9e832d4b93662fdada952eaef7 2500w" />

### 画布缩放速度

* **默认值**：1.1
* **范围**：1.01 - 2.5
* **功能**：控制画布缩放的速度，调整鼠标滚轮缩放的敏感度

### 在左下角显示画布信息（fps等）

* **默认值**：启用
* **功能**：控制是否在左下角显示画布信息，显示性能指标如 FPS 等

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=5ed9833f409780098accd32464b864fe" alt="快速缩放" data-og-width="732" width="732" data-og-height="498" height="498" data-path="images/interface/setting/lite-graph/canvas-info.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f853330ca1bbe5ee49583263d7f3ec70 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9e5a8716fab45917d1d49f34160483f5 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=87abec047a50012befe4464c210f8b29 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c9c1cbcffd7e80c87a02daa46972877d 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0301e23c24b1506c37c300f89aa0b5e8 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bcf5bb37e1dfc1cac0c54bf5598532d7 2500w" />

## 上下文菜单

### 放大时缩放节点组合部件菜单（列表）

* **默认值**：启用
* **功能**：控制是否在放大时显示节点组合部件菜单（列表），允许用户选择节点组合部件

## 画面

### 连线渲染模式

* **默认值**：2（Spline样条线）
* **选项**：直线、线性、样条线、隐藏
* **功能**：设置连线的渲染样式，控制节点间连线的视觉样式

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b5ab460adf08e167a83fb640d5c5a4bb" alt="连线渲染模式" data-og-width="1324" width="1324" data-og-height="478" height="478" data-path="images/interface/setting/lite-graph/link-render-mode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f5a03cfe4e686e6548a5c8bcd5b1619c 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0a55cf7ab6448ac3dc17ce34b7a924d9 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=86f3068b94667a57be6517bc998326a3 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=87a42a420f29fc92d948360430ad96d2 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=88ec0edbab4d1a5140ed41e3203e0ccd 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dbc7b9d2957443ab3971b4e4f818d598 2500w" />

## 组

这部分的设置主要和节点组功能相关

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=02765d28e1720e5cc0bc2f6a1f70ab02" alt="节点组" data-og-width="1487" width="1487" data-og-height="915" height="915" data-path="images/interface/setting/lite-graph/node-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=344ee0c96c34e0186efb34451ce7733c 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dce5fe6f6e7d320667e375307c7ba1de 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ccaaa08b04e1ae8d79f3b53b088019c7 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b32a9107f488d73ed314a8de830092d3 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6c06dff62e5aaac38fee0cb76371fb14 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ad20abab050fa338c1af7ea59f7215c2 2500w" />

### 双击组标题以编辑

* **默认值**：启用
* **功能**：控制是否可以双击节点标题进行编辑，允许用户重命名节点，图中标注为 `1` 的部分

### 分组选中节点填充

* **默认值**：10
* **范围**：0 - 100
* **功能**：设置分组选中节点时的内边距，控制分组框与节点间的间距，图中标注为 `2` 箭头标注部分

## 连线

### 链接中点标记

* **默认值**：Circle（圆形）
* **选项**：无、圆形、箭头
* **功能**：设置链接中点的标记样式，在链接中点显示方向指示

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=119b8c37616b50cda464333cbc87d2d6" alt="连线渲染模式" data-og-width="1026" width="1026" data-og-height="568" height="568" data-path="images/interface/setting/lite-graph/link-midpoint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4b97534b43210749730acbb2062aefa6 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4b7fbf041cf69479991fd9e027ec1e20 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=80b9f765622c9c3b1b7942406f61849b 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e007a98ff4c61bde6521e18f79bffa40 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c3b50f60ca0929e895f4dc984c6eab87 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=67ecd934c9b7b7c650e7714be2610134 2500w" />

## 释放链接

这部分的菜单目前主要控制当链接连线释放时的相关操作，目前两个相关操作为：

**释放后会出现和当前输入 / 输出相关的节点推荐列表**

<video controls>
  <source src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-release-contenxt-menu.mp4?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=1b8a078d5a122fa327f9ffefebc9e489" type="video/mp4" data-path="images/interface/setting/lite-graph/link-release-contenxt-menu.mp4" />
</video>

**释放后会启动搜索框**

<video controls>
  <source src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-release-search-box.mp4?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=52747dcfcf1d0c31b2163961c62e9efb" type="video/mp4" data-path="images/interface/setting/lite-graph/link-release-search-box.mp4" />
</video>

### 链接释放动作（Shift键）

* **默认值**： 搜索框
* **选项**： 上下文菜单、搜索框、无操作
* **功能**：设置按住Shift键释放链接时的动作，按住Shift释放链接时的特殊行为

### 链接释放动作（无修饰键）

* **默认值**： 上下文菜单
* **选项**： 上下文菜单、搜索框、无操作
* **功能**：设置释放链接时的默认动作，控制拖拽链接后释放时的行为

## 节点

### 始终收缩新节点

* **默认值**：启用
* **功能**：控制是否在创建新节点时自动收缩，从而让节点能够始终显示最小的尺寸，但可能会导致添加时有些文本显示会被截断，需要手动调整节点大小

### 启用DOM元素裁剪（启用可能会降低性能）

* **默认值**：启用
* **功能**：启用DOM元素裁剪（可能影响性能），优化渲染但可能降低性能

### 中键单击创建新的转接点

* **默认值**：启用
* **功能**：中键点击时创建新的重路由节点，快速创建用于整理连线的重路由节点

### 删除节点时保留连线

* **默认值**：启用
* **功能**：删除中间节点时自动绕过连接，删除节点时尝试重新连接其输入输出链接

### 吸附高亮节点

* **默认值**：启用
* **功能**：拖拽链接到节点时高亮显示节点，提供视觉反馈，显示可连接的节点,启用后效果如下图，对应链接的一侧会显示高亮的样式

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=242f3b88d95229d99744f720cf86c935" alt="吸附高亮节点" data-og-width="1600" width="1600" data-og-height="1117" height="1117" data-path="images/interface/setting/lite-graph/highlights-node.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=7f09e4ab23066f929261f914435ca863 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ee512a2dc0f93c929bc63bc4044c68a9 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=97489e53e0bb76fdfca88ae9ea06c25a 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b0f1a2bb9487a2c4f04c22d89c31290b 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=24cd0f898c96f82d8c83a8a7b9dcbc3d 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4645004d83ccd6319f10d340b4e359b2 2500w" />

### 连线自动吸附到节点接口

* **默认值**：启用
* **功能**：拖拽链接到节点上时自动吸附到可用插槽，简化连接操作，自动找到合适的输入插槽

<video controls>
  <source src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/snap-link-to-node-slot.mp4?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=1f517cf34f3f994c4c03a267d8fbbd91" type="video/mp4" data-path="images/interface/setting/lite-graph/snap-link-to-node-slot.mp4" />
</video>

### 启用工具提示

* **默认值**：启用
* **功能**：在部分节点信息中会包含一些工具提示，包含了一些参数说明等，当启用后会在鼠标悬停时显示这些工具提示，如下图

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=df329458465d6f20efea955e638c9656" alt="工具提示" data-og-width="970" width="970" data-og-height="812" height="812" data-path="images/interface/setting/lite-graph/tooltips.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=0b1dcdb41ced6b2a6e8e5149979b94e2 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=9ae884ced3a5ba1e8f2e8ae57f029c48 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a02a16c504d702daaae15e6a1ae8db66 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdc7306c00ae81da9436b75f16eff554 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=d4f0ff45b6e5d07c05ded7e175bb5f6d 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=033d80a751cdb677cfeee70d20696a40 2500w" />

### 工具提示延迟

* **默认值**：500
* **功能**：控制工具提示的延迟时间，单位为毫秒，设置为0表示立即显示工具提示

### 节点制作周期标签

* **默认值**：ShowAll（显示全部）
* **功能**：控制节点生命周期标记的显示，显示节点的状态信息

### 节点ID标签

* **默认值**：None（不显示）
* **功能**：控制节点ID标记的显示，显示节点的唯一标识符

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ca8e1edfff6c7673f1432ba0ac2edde5" alt="节点ID标签" data-og-width="1934" width="1934" data-og-height="882" height="882" data-path="images/interface/setting/lite-graph/node-id-badge.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b4a7cb9bb4f3f93c8d809fe95edd1016 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2b0e969d8ba95913da96a89dbf053594 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b2bd300153771746ace189c8ab222f4d 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6b4ea2ddf5aaaf71c9cc67f080c941f0 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=70260117330068ae383785ad5c2eb487 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=3c979e6c55b7d0e905d803340b6c7d8c 2500w" />

### 节点源标签

* **选项**：
  * None（不显示）
  * HideBuiltIn（隐藏内置）
  * ShowAll（显示全部）
* **功能**：控制节点源标记的显示模式，显示节点来源信息,对应的显示效果如下图，如果显示全部则会显示自定义节点和内置节点的标签，方便你判断对应的节点来源，对应小狐狸标志为 ComfyUI 内置节点

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=383afc337b63f52be2f8d3cb9e7c4ed7" alt="节点源标签" data-og-width="1934" width="1934" data-og-height="1444" height="1444" data-path="images/interface/setting/lite-graph/node-source-badge.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2adbbf69732c7b73dcab2a8e01d0b402 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4baf2f78dfcb8b23db6804197dd009ec 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=885a023913bd9b48ce59dbfbeaf403e1 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=74d8da68c50aee918213f41748cb774e 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a5df61943a4fdb6a0f87980733371f5e 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=033de7b26a0cb9d615c626b996350f0d 2500w" />

### 双击节点标题以编辑

* **默认值**：启用
* **功能**：控制是否可以双击节点标题进行编辑，允许用户重命名节点

## 节点组件

### 浮点组件四舍五入的小数位数 \[0 = 自动]

* **默认值**：0（自动）
* **范围**：0 - 6
* **功能**：设置浮点小部件四舍五入的小数位数，0表示自动，需要页面重新加载

### 禁用默认浮点组件四舍五入

* **默认值**：禁用
* **功能**：控制是否禁用默认的浮点小部件四舍五入，需要页面重新加载，当节点后端设置了四舍五入时无法禁用

### 禁用节点组件滑块

* **默认值**：禁用
* **功能**：控制是否禁用节点小部件中的滑块控件，强制使用文本输入而非滑块

### 预览图像格式

* **默认值**：空字符串（使用原格式）
* **功能**：设置图像小部件中预览图像的格式，转换为轻量级格式如 webp、jpeg 等

### 在图像预览下方显示宽度×高度

* **默认值**：启用
* **功能**：在图像预览下方显示宽度×高度信息，显示图像的尺寸信息

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e7fdfd5227158a413b5b0051a6e171bf" alt="在图像预览下方显示宽度×高度" data-og-width="1344" width="1344" data-og-height="904" height="904" data-path="images/interface/setting/lite-graph/show-size.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=11ef68d7975fd3e639e78bc2a184607c 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=039c262051b8d4340e7cb0282ad933ab 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2c534553d00ee7944410ff839c3de645 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=74e330c841673a679ea01107154bdaf4 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d42ab780f2ba87dcde3005ac34e765cb 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e6641012043335c3254d14e223abc264 2500w" />

## 指针

### 启用触控板手势

* **默认值**：启用
* **功能**：此设置为画布启用触控板模式，允许使用双指捏合缩放和拖动。

### 双击间隔（最大）

* **默认值**：300
* **功能**：双击的两次点击之间的最大时间(毫秒)。增加此值有助于解决双击有时未被识别的问题。

### 指针点击漂移延迟

* **默认值**：150
* **功能**：按下指针按钮后，忽略指针移动的最大时间(毫秒)。有助于防止在点击时意外移动鼠标。

### 指针点击漂移（距离）

* **默认值**：6
* **功能**：如果指针在按住按钮时移动超过此距离，则视为拖动(而不是点击)。有助于防止在点击时意外移动鼠标

## 重新路由

### 重新路由样条偏移

* **默认值**：20
* **功能**：用于确定重路由节点两侧的曲线的平滑程度，值越大，曲线越平滑，值越小，曲线越尖锐

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a76bc935bc5e37fe1b3c99129c7b5fe3" alt="重新路由样条偏移" data-og-width="1568" width="1568" data-og-height="752" height="752" data-path="images/interface/setting/lite-graph/reroute-spline-offset.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2554871390417e2446d7a54f068457ab 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=8fc90b4d5a202590e89d415db9476d64 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b62484d0c4a42903c87d0c2017c48c6c 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=85b04e2c73fbe5b5c142a4194bdd4f09 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=5a9b9ae976c0df2ab1aa52b57cc377db 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b10e3d24d3da03186411aa0d543c5e14 2500w" />
