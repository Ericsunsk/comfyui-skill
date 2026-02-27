> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI LiteGraph (Canvas) Settings

> Detailed description of ComfyUI graphics rendering engine LiteGraph setting options

LiteGraph is the underlying graphics rendering engine of ComfyUI. The settings in this category mainly control the behavior and appearance of graphical interfaces such as canvas, nodes, and links.

## Canvas

### Show selection toolbox

* **Default Value**: Enabled
* **Function**: The selection toolbox is a floating quick action toolbar that appears on nodes after they are selected, providing common quick operations such as partial execution, pinning, deletion, color modification, etc.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=58f8da6ea3f276272d9be4c4e1e5ebb1" alt="Show selection toolbox" data-og-width="1316" width="1316" data-og-height="756" height="756" data-path="images/interface/setting/lite-graph/selection-toolbox.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0852d125213f53175878df6fa7ca6a0b 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=387feb2717783c88f242df53ba34585c 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=abdd92feb502d99b79e866826806a3c8 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bafd39d46c38f51e73882f7a1edc2b6c 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=650035cfd4c313de8f498ae453099761 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/selection-toolbox.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d9083ca10bbeaee4286ad04b2a99d72c 2500w" />

### Low quality rendering zoom threshold

* **Default Value**: 0.6
* **Range**: 0.1 - 1.0
* **Function**: When rendering the interface, especially when the workflow is particularly complex and the entire canvas is particularly large, the frontend rendering of corresponding elements will consume a lot of memory and cause lag. By lowering this threshold, you can control elements to enter low quality rendering mode when scaled to a specific percentage, thereby reducing memory consumption. The corresponding different rendering modes are shown below

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e6481f3430f77f8312d78b853d307774" alt="Low quality rendering" data-og-width="1536" width="1536" data-og-height="1008" height="1008" data-path="images/interface/setting/lite-graph/render-mode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9ef378358eb4456f90b98919e1869573 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a1187ef33614dc82ab68badc0e511716 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2342fc9d728bbb28074f821d164491d1 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b9e7dd615fa32ad7f6b2237c9f7d9bcb 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=cf24d96b6acdc6755988b308baddaece 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/render-mode.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6d920a9762db0305aac10ff12f950c41 2500w" />

### Maximum FPS

* **Default Value**: 0 (use screen refresh rate)
* **Range**: 0 - 120
* **Function**: Limits the rendering frame rate of the canvas. 0 means using the screen refresh rate. Higher FPS will make the canvas rendering smoother, but will also consume more performance. Too low values will cause more obvious stuttering.

### Always snap to grid

* **Default Value**: Disabled
* **Function**: When this option is not enabled, you can hold the `Shift` key to align node edges with the grid. When enabled, node edges will automatically align with the grid without holding the `Shift` key.

<video controls>
  <source src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/snap-to-grid.mp4?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=2afb1c5c09f9fca9f4b8333e975d0f44" type="video/mp4" data-path="images/interface/setting/lite-graph/snap-to-grid.mp4" />
</video>

### Snap to grid size

* **Range**: 1 - 500
* **Function**: When auto-snap is enabled or when moving nodes while holding the `Shift` key, this parameter determines the grid size for snapping. The default value is 10, and you can adjust it according to your needs.

### Enable fast-zoom shortcut (Ctrl + Shift + Drag)

* **Default Value**: Enabled
* **Function**: Enables the `Ctrl + Shift + Left Mouse Button Drag` fast zoom function, providing a faster zoom operation method

<video controls>
  <source src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/fast-zoom.mp4?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2d6e53041600bb97d28cb81786af40fd" type="video/mp4" data-path="images/interface/setting/lite-graph/fast-zoom.mp4" />
</video>

### Show graph canvas menu

* **Default Value**: Enabled
* **Function**: Controls whether to display the canvas menu in the bottom right corner

The canvas menu is located in the bottom right corner of the entire ComfyUI interface, containing operations such as canvas zooming, temporarily hiding all connections, quickly scaling the workflow to fit the canvas, etc., as shown in the image below

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=23c8c2f94f2befbfc9cd3a484140af5b" alt="Show graph canvas menu" data-og-width="360" width="360" data-og-height="764" height="764" data-path="images/interface/setting/lite-graph/canvas_menu.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=114872d393c2d9e608b74229fc222b56 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4993f24b3b9953267d53e1936538deab 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d2a8481ae2e09ad7f3e72afccb3cefc6 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f60dc6b8de22500f4caa0167871cf4c8 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c703da828402b98155cd2f344f90c13e 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas_menu.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=675a0c9e832d4b93662fdada952eaef7 2500w" />

### Canvas zoom speed

* **Default Value**: 1.1
* **Range**: 1.01 - 2.5
* **Function**: Controls the speed of canvas zooming, adjusts the sensitivity of mouse wheel zooming

### Show canvas info on bottom left corner (fps, etc.)

* **Default Value**: Enabled
* **Function**: Controls whether to display canvas information in the bottom left corner, showing performance metrics like FPS

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=5ed9833f409780098accd32464b864fe" alt="Canvas info" data-og-width="732" width="732" data-og-height="498" height="498" data-path="images/interface/setting/lite-graph/canvas-info.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f853330ca1bbe5ee49583263d7f3ec70 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9e5a8716fab45917d1d49f34160483f5 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=87abec047a50012befe4464c210f8b29 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c9c1cbcffd7e80c87a02daa46972877d 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0301e23c24b1506c37c300f89aa0b5e8 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/canvas-info.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bcf5bb37e1dfc1cac0c54bf5598532d7 2500w" />

## Context Menu

### Scale node combo widget menus (lists) when zoomed in

* **Default Value**: Enabled
* **Function**: Controls whether to scale node combo widget menus (lists) when zoomed in, allowing users to select node combo widgets

## Graph

### Link Render Mode

* **Default Value**: 2 (Spline)
* **Options**: Straight, Linear, Spline, Hidden
* **Function**: Sets the rendering style of connections, controlling the visual style of links between nodes

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b5ab460adf08e167a83fb640d5c5a4bb" alt="Link Render Mode" data-og-width="1324" width="1324" data-og-height="478" height="478" data-path="images/interface/setting/lite-graph/link-render-mode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f5a03cfe4e686e6548a5c8bcd5b1619c 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0a55cf7ab6448ac3dc17ce34b7a924d9 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=86f3068b94667a57be6517bc998326a3 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=87a42a420f29fc92d948360430ad96d2 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=88ec0edbab4d1a5140ed41e3203e0ccd 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-render-mode.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dbc7b9d2957443ab3971b4e4f818d598 2500w" />

## Group

This section of settings is mainly related to node group functionality

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=02765d28e1720e5cc0bc2f6a1f70ab02" alt="Node Group" data-og-width="1487" width="1487" data-og-height="915" height="915" data-path="images/interface/setting/lite-graph/node-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=344ee0c96c34e0186efb34451ce7733c 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dce5fe6f6e7d320667e375307c7ba1de 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ccaaa08b04e1ae8d79f3b53b088019c7 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b32a9107f488d73ed314a8de830092d3 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6c06dff62e5aaac38fee0cb76371fb14 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ad20abab050fa338c1af7ea59f7215c2 2500w" />

### Double click group title to edit

* **Default Value**: Enabled
* **Function**: Controls whether you can double-click the node title to edit it, allowing users to rename nodes, marked as part `1` in the image

### Group selected nodes padding

* **Default Value**: 10
* **Range**: 0 - 100
* **Function**: Sets the inner padding when grouping selected nodes, controlling the spacing between the group frame and nodes, marked as the arrow annotation part `2` in the image

## Link

### Link midpoint markers

* **Default Value**: Circle
* **Options**: None, Circle, Arrow
* **Function**: Sets the marker style at link midpoints, displaying direction indicators at link midpoints

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=119b8c37616b50cda464333cbc87d2d6" alt="Link midpoint markers" data-og-width="1026" width="1026" data-og-height="568" height="568" data-path="images/interface/setting/lite-graph/link-midpoint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4b97534b43210749730acbb2062aefa6 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4b7fbf041cf69479991fd9e027ec1e20 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=80b9f765622c9c3b1b7942406f61849b 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e007a98ff4c61bde6521e18f79bffa40 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c3b50f60ca0929e895f4dc984c6eab87 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-midpoint.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=67ecd934c9b7b7c650e7714be2610134 2500w" />

## Link Release

This menu section currently mainly controls related operations when link connections are released. The current two related operations are:

**A node recommendation list related to the current input/output will appear after release**

<video controls>
  <source src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-release-contenxt-menu.mp4?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=1b8a078d5a122fa327f9ffefebc9e489" type="video/mp4" data-path="images/interface/setting/lite-graph/link-release-contenxt-menu.mp4" />
</video>

**A search box will be launched after release**

<video controls>
  <source src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/link-release-search-box.mp4?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=52747dcfcf1d0c31b2163961c62e9efb" type="video/mp4" data-path="images/interface/setting/lite-graph/link-release-search-box.mp4" />
</video>

### Action on link release (Shift)

* **Default Value**: search box
* **Options**: context menu, search box, no action
* **Function**: Sets the action when releasing links while holding the Shift key, special behavior when releasing links while holding Shift

### Action on link release (No modifier)

* **Default Value**: context menu
* **Options**: context menu, search box, no action
* **Function**: Sets the default action when releasing links, controls the behavior after dragging and releasing links

## Node

### Always shrink new nodes

* **Default Value**: Enabled
* **Function**: Controls whether to automatically shrink when creating new nodes, so nodes can always display the minimum size, but may cause some text display to be truncated when adding, requiring manual adjustment of node size

### Enable DOM element clipping (enabling may reduce performance)

* **Default Value**: Enabled
* **Function**: Enables DOM element clipping (may affect performance), optimizes rendering but may reduce performance

### Middle-click creates a new Reroute node

* **Default Value**: Enabled
* **Function**: Creates a new reroute node when middle-clicking, quickly creates reroute nodes for organizing connections

### Keep all links when deleting nodes

* **Default Value**: Enabled
* **Function**: Automatically bypasses connections when deleting intermediate nodes, attempts to reconnect input and output links when deleting nodes

### Snap highlights node

* **Default Value**: Enabled
* **Function**: Highlights nodes when dragging links to them, provides visual feedback, shows connectable nodes. When enabled, the effect is as shown in the image below, the corresponding side of the link will display highlighted style

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=242f3b88d95229d99744f720cf86c935" alt="Snap highlights node" data-og-width="1600" width="1600" data-og-height="1117" height="1117" data-path="images/interface/setting/lite-graph/highlights-node.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=7f09e4ab23066f929261f914435ca863 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ee512a2dc0f93c929bc63bc4044c68a9 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=97489e53e0bb76fdfca88ae9ea06c25a 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b0f1a2bb9487a2c4f04c22d89c31290b 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=24cd0f898c96f82d8c83a8a7b9dcbc3d 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4645004d83ccd6319f10d340b4e359b2 2500w" />

### Auto snap link to node slot

* **Default Value**: Enabled
* **Function**: Automatically snaps to available slots when dragging links to nodes, simplifies connection operations, automatically finds suitable input slots

<video controls>
  <source src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/snap-link-to-node-slot.mp4?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=1f517cf34f3f994c4c03a267d8fbbd91" type="video/mp4" data-path="images/interface/setting/lite-graph/snap-link-to-node-slot.mp4" />
</video>

### Enable Tooltips

* **Default Value**: Enabled
* **Function**: Some node information will contain tooltips, including parameter descriptions, etc. When enabled, these tooltips will be displayed when hovering the mouse, as shown in the image below

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=df329458465d6f20efea955e638c9656" alt="Enable Tooltips" data-og-width="970" width="970" data-og-height="812" height="812" data-path="images/interface/setting/lite-graph/tooltips.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=0b1dcdb41ced6b2a6e8e5149979b94e2 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=9ae884ced3a5ba1e8f2e8ae57f029c48 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a02a16c504d702daaae15e6a1ae8db66 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdc7306c00ae81da9436b75f16eff554 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=d4f0ff45b6e5d07c05ded7e175bb5f6d 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=033d80a751cdb677cfeee70d20696a40 2500w" />

### Tooltip Delay

* **Default Value**: 500
* **Function**: Controls the delay time for tooltips, in milliseconds. Setting to 0 means displaying tooltips immediately

### Node life cycle badge mode

* **Default Value**: Show all
* **Function**: Controls the display of node lifecycle markers, showing node status information

### Node ID badge mode

* **Default Value**: Show all
* **Function**: Controls the display of node ID markers, showing node unique identifiers

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ca8e1edfff6c7673f1432ba0ac2edde5" alt="Node ID badge mode" data-og-width="1934" width="1934" data-og-height="882" height="882" data-path="images/interface/setting/lite-graph/node-id-badge.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b4a7cb9bb4f3f93c8d809fe95edd1016 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2b0e969d8ba95913da96a89dbf053594 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b2bd300153771746ace189c8ab222f4d 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=6b4ea2ddf5aaaf71c9cc67f080c941f0 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=70260117330068ae383785ad5c2eb487 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=3c979e6c55b7d0e905d803340b6c7d8c 2500w" />

### Node source badge mode

* **Options**:
  * None
  * Hide built-in
  * Show all
* **Function**: Controls the display mode of node source markers, showing node source information. The corresponding display effect is shown in the image below. If show all is selected, it will display labels for both custom nodes and built-in nodes, making it convenient for you to determine the corresponding node source. The corresponding fox logo represents ComfyUI built-in nodes

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=383afc337b63f52be2f8d3cb9e7c4ed7" alt="Node source badge mode" data-og-width="1934" width="1934" data-og-height="1444" height="1444" data-path="images/interface/setting/lite-graph/node-source-badge.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2adbbf69732c7b73dcab2a8e01d0b402 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4baf2f78dfcb8b23db6804197dd009ec 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=885a023913bd9b48ce59dbfbeaf403e1 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=74d8da68c50aee918213f41748cb774e 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a5df61943a4fdb6a0f87980733371f5e 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=033de7b26a0cb9d615c626b996350f0d 2500w" />

### Double click node title to edit

* **Default Value**: Enabled
* **Function**: Controls whether you can double-click the node title to edit it, allowing users to rename nodes

## Node Widget

### Float widget rounding decimal places \[0 = auto]

* **Default Value**: 0 (auto)
* **Range**: 0 - 6
* **Function**: Sets the decimal places for float widget rounding, 0 means auto, requires page reload

### Disable default float widget rounding

* **Default Value**: Disabled
* **Function**: Controls whether to disable default float widget rounding, requires page reload, cannot be disabled when the node backend has set rounding

### Disable node widget sliders

* **Default Value**: Disabled
* **Function**: Controls whether to disable slider controls in node widgets, forcing text input instead of sliders

### Preview image format

* **Default Value**: Empty string (use original format)
* **Function**: Sets the format for preview images in image widgets, converts to lightweight formats like webp, jpeg, etc.

### Show width × height below the image preview

* **Default Value**: Enabled
* **Function**: Displays width × height information below image previews, showing image dimension information

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e7fdfd5227158a413b5b0051a6e171bf" alt="Show width × height below the image preview" data-og-width="1344" width="1344" data-og-height="904" height="904" data-path="images/interface/setting/lite-graph/show-size.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=11ef68d7975fd3e639e78bc2a184607c 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=039c262051b8d4340e7cb0282ad933ab 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2c534553d00ee7944410ff839c3de645 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=74e330c841673a679ea01107154bdaf4 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d42ab780f2ba87dcde3005ac34e765cb 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e6641012043335c3254d14e223abc264 2500w" />

## Pointer

### Enable trackpad gestures

* **Default Value**: Enabled
* **Function**: This setting enables trackpad mode for the canvas, allowing two-finger pinch zoom and drag.

### Double click interval (maximum)

* **Default Value**: 300
* **Function**: Maximum time (milliseconds) between two clicks of a double-click. Increasing this value helps solve issues where double-clicks are sometimes not recognized.

### Pointer click drift delay

* **Default Value**: 150
* **Function**: Maximum time (milliseconds) to ignore pointer movement after pressing the pointer button. Helps prevent accidental mouse movement when clicking.

### Pointer click drift (maximum distance)

* **Default Value**: 6
* **Function**: If the pointer moves more than this distance while holding the button, it is considered a drag (rather than a click). Helps prevent accidental mouse movement when clicking.

## Reroute

### Reroute spline offset

* **Default Value**: 20
* **Function**: Used to determine the smoothness of curves on both sides of reroute nodes. Larger values make curves smoother, smaller values make curves sharper.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a76bc935bc5e37fe1b3c99129c7b5fe3" alt="Reroute spline offset" data-og-width="1568" width="1568" data-og-height="752" height="752" data-path="images/interface/setting/lite-graph/reroute-spline-offset.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2554871390417e2446d7a54f068457ab 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=8fc90b4d5a202590e89d415db9476d64 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b62484d0c4a42903c87d0c2017c48c6c 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=85b04e2c73fbe5b5c142a4194bdd4f09 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=5a9b9ae976c0df2ab1aa52b57cc377db 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b10e3d24d3da03186411aa0d543c5e14 2500w" />
