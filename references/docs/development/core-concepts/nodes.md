> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Nodes

> Understand the concept of a node in ComfyUI.

In ComfyUI, nodes are the fundamental building blocks for executing tasks. Each node is an independently built module, whether it's a **Comfy Core** node or a **Custom Node**, with its own unique functionality. Nodes connect to each other through links, allowing us to build complex functionality like assembling LEGO blocks.
The combinations of different nodes create the unlimited possibilities of ComfyUI.

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=aed5e1f863c37948107cfcb3458955b7" alt="Comfy Core K-Sampler Node" data-og-width="854" width="854" data-og-height="767" height="767" data-path="images/comfy_core/sampling/k_sampler.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f891fb24b7fcbb6616bad811d797cd10 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=d3597cfd9ef1b324ceb8b8e529246540 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=e714d81c3a3214ef9fe1da89cdc2efd3 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=5001918af1c739866639c03df51a3c19 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ff62cab54c0c1fa1432d98c69877706d 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/sampling/k_sampler.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=350b8494ce4c1e004ddd94f7977563d7 2500w" />

For example, in the K-Sampler node, you can see it has multiple inputs and outputs, and also includes multiple parameter settings. These parameters determine the logic of node execution. Behind each node is well-written Python logic, allowing you to achieve corresponding functionality without having to write code yourself.

<Note>
  ComfyUI is under active development, so some details here may be outdated. If you spot something that's changed, feel free to [help us update the docs](https://github.com/Comfy-Org/docs).
</Note>

## Nodes perform operations

In computer science, a ***node*** is a container for information, usually including programmed instructions to perform some task. Nodes almost never exist in isolation, they're almost always connected to other nodes in a networked graph. In ComfyUI, nodes take the visual form of boxes that are connected to each other.

ComfyUI nodes are usually ***function operators***. This means that they operate on some data to perform a function. A function is a process that accepts input data, performs some operation on it, and produces output data. In other words, nodes do some work, contributing to the completion of a task such as generating an image. So ComfyUI nodes almost always have at least one input or output, and usually have multiple inputs and outputs.

## Different Node States

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=150ab91575a7c9300b7ed20d8026e499" alt="Node States" data-og-width="3167" width="3167" data-og-height="900" height="900" data-path="images/concepts/node/status.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=72ff0c9fc86e4de4abc041f54e9a76a4 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ec6264e55b41fe6f284bb32ccf7e09cb 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0964829012a38d6540d89773a163e5eb 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0b013434ced278f2029243136f80198d 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f4077f9da03b83ae9ee4a4d28cce19e7 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=68a03e96245d13250e0864a8951c2b7f 2500w" />

In ComfyUI, nodes have multiple states. Here are some common node states:

1. **Normal State**: The default state
2. **Running State**: The running state, typically displayed when a node is executing after you start running the workflow
3. **Error State**: Node error, typically displayed after running the workflow if there's a problem with the node's input, indicated by red marking of the erroneous input node. You need to fix the problematic input to ensure the workflow runs correctly
4. **Missing State**: This state usually appears after importing workflows, with two possibilities:
   * Comfy Core native node missing: This usually happens because ComfyUI has been updated, but you're using an older version of ComfyUI. You need to update ComfyUI to resolve this issue
   * Custom node missing: The workflow uses custom nodes developed by third-party authors, but your local ComfyUI version doesn't have these custom nodes installed. You can use [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) to find and install the missing custom nodes

## Connections Between Nodes

In ComfyUI, nodes are connected through [links](/development/core-concepts/links), allowing data of the same type to flow between different processing units to achieve the final result.

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=40a62b27aa2f44cb97eae917c8c1f8da" alt="ComfyUI Node Links" data-og-width="2000" width="2000" data-og-height="1108" height="1108" data-path="images/concepts/node/inpaint.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c90df520b2046575f0d0005253cf359e 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7850db8dad1f1096fe1e7870b47f772b 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=613be61533b2737be42795c6162d77b9 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4db8d8d46ec77ded6285a4939d8cb1cc 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=76228d5a4063d7923d02fb718938bd71 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=49f3f3318cf1e678bec7499f116c8065 2500w" />

Each node receives some input, processes it through its module, and converts it to corresponding output. Connections between different nodes must conform to the data type requirements. In ComfyUI, we use different colors to distinguish node data types. Below are some basic data types:

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5" alt="ComfyUI Node Data Types" data-og-width="685" width="685" data-og-height="356" height="356" data-path="images/concepts/node/data_type.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3a128b7a0a1e6e93733f2fe649efd330 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=56df7925857870daf0995d69dcca1c24 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=69feb5a2bdde5813c9444c500710e1cb 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=087178033c73065ed5a521cb04f3f5cb 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=389aadb6b698921a58ffb6e3c65ce796 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9ee271b46d36d4ab90b1688dbcf80c5d 2500w" />

| Data type                 | Color        |
| ------------------------- | ------------ |
| diffusion model           | lavender     |
| CLIP model                | yellow       |
| VAE model                 | rose         |
| conditioning              | orange       |
| latent image              | pink         |
| pixel image               | blue         |
| mask                      | green        |
| number (integer or float) | light green  |
| mesh                      | bright green |

As ComfyUI evolves, we may expand to more data types to meet the needs of more scenarios.

### Connecting and Disconnecting Nodes

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/link_nodes.gif?s=06359a20664f48e43763696313a063f9" alt="ComfyUI Node Connecting" data-og-width="820" width="820" data-og-height="724" height="724" data-path="images/concepts/node/link_nodes.gif" data-optimize="true" data-opv="3" />

**Connecting**: Drag from the output point of one node to the input of the same color on another node to connect them
**Disconnecting**: Click on the input endpoint and drag the mouse left button to disconnect, or cancel the connection through the midpoint menu of the link

## Node Appearance

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=e7ed881cf2c91cc9c48892dd491cae7b" alt="Node Appearance" data-og-width="950" width="950" data-og-height="560" height="560" data-path="images/index/node.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0c7f3950359535f427c0b23ed36b99f7 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0b937677a863b6fefd2d7a68e60c012f 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=a9c398582e0b5bf75033405e469dda22 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5f05d24d5e77ccb4d050706792186d25 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=828de922e8e1f8816d3d8a674304abe5 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=33297be56d4722e5b5e8b5462129ec7e 2500w" />

We provide various style settings for you to customize the appearance of nodes:

* Modify styles
* Double-click the node title to modify the node name
* Resize the node by dragging any corner

<video controls className="w-full aspect-video" src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_appearance.mp4?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2fb1ff4aac3396cb3e4ecbebd8db7b14" data-path="images/concepts/node/node_appearance.mp4" />

### Node Badges

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1e22b62c50745c547e2b99c5f13df990" alt="Node Badges" data-og-width="1207" width="1207" data-og-height="606" height="606" data-path="images/concepts/node/badge.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5725996ab758f6ca7476c8bc3c68b58a 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=dec77789c181bb56a23c8d8ede919ced 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=fc1a4671387cc7ffceb4ae130f543dac 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=cb938d3aebd43c9d9db64ec629d07781 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4dfa69ff4270496cacc3a9843d4fc841 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=17a8ec9f470311a50cbcd2c0bfa36ac1 2500w" />

We provide multiple node badge display features, such as:

* Node ID
* Node source

Currently, **Comfy Core nodes** use a fox icon for display, while custom nodes use their names. This way you can quickly understand which node package a node comes from.

You can set the corresponding display in the menu:

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f63c9698836a1debc6a1bed84d77fdf2" alt="Badge Settings" data-og-width="1500" width="1500" data-og-height="561" height="561" data-path="images/concepts/node/badge_setting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2ff04102c6062521c93d30324c921e61 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bb5156ae606e2844b6aa118c09b962aa 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=343b00bd89bff5e04ecef00e0f999b36 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=090801a432d756d73ece2379d0339f19 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=6a7f9adec98fca0dff194b2cc8db9314 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c9f0fc340c48d63b80f7a66d6956a4f1 2500w" />

## Node Context Menus

Node context menus are mainly divided into two types:

* Context menu for the node itself
* Context menu for inputs/outputs

### Node Context Menu

By right-clicking on a node, you can expand the corresponding node context menu:
<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d7d99664537a4f2b09aaf0acc228da4f" alt="Node Context Menu" data-og-width="2100" width="2100" data-og-height="1832" height="1832" data-path="images/concepts/node/context_menus_1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f6d35bba454f50422ed60bd36f7d0ffc 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=961e5d91a9363fe91db3c28196f58052 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bd3ca784987ef4c4931229c920c0239d 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a544cec80957d1cb035197c4edebf57e 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4a8684c82442b8ed435fbbd715c3963e 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d2ffc3276a6e340a5e92a7d32e697ff2 2500w" />

In the node's right-click context menu, you can:

* Adjust the node's color style
* Modify the title
* Clone, copy, or delete the node
* Set the node's mode

In this menu, besides appearance-related settings, the following menu operations are important:

* **Mode**: Set the node's mode: Always, Never, Bypass

#### Mode

For modes, you may notice that we currently provide: Always, Never, On Event, On Trigger - four modes, but actually only **Always** and **Never** are effective. **On Event** and **On Trigger** are currently ineffective as we haven't fully implemented this feature. Additionally, you can understand **Bypass** as a mode. Below is an explanation of the available modes:

* **Always**: The default node mode. The node will execute whenever it runs for the first time or when any of its inputs change since the last execution
* **Never**: The node will never execute under any circumstances, as if it's been deleted. Subsequent nodes cannot read or receive any data from it
* **Bypass**: The node will never execute under any circumstances, but subsequent nodes can still try to obtain data that hasn't been processed by this node

Below is a comparison of the `Never` and `Bypass` modes:

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7024037e0a22285a21484d102dae0f0c" alt="Never vs Bypass Mode" data-og-width="3000" width="3000" data-og-height="1092" height="1092" data-path="images/concepts/node/never_vs_bypass.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=6344fa2d9cd016f427b02c74e1cf1740 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ea96796a2e23fef29363b065df5a16a9 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=aba3e1a0b57114dd729dc8c96e0adb05 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=fb4dd9dd8030ce2f4e789056955beaac 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=011c5d6f09f51e031c53488b0580db07 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/never_vs_bypass.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5a6a4976bfd7ee42816e6d8b852c9274 2500w" />

In this comparison example, you can see that both workflows apply two LoRA models simultaneously, with the difference being that one `Load LoRA` node is set to `Never` mode while the other is set to `Bypass` mode.

* The node set to `Never` mode causes subsequent nodes to show errors because they don't receive any input data
* The node set to `Bypass` mode still allows subsequent nodes to receive unprocessed data, so they load the output data from the first `Load LoRA` node, allowing the subsequent workflow to continue running normally

### Input/Output Context Menu

This context menu is mainly related to the data type of the corresponding input/output:

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2daf16654cdd151a6b9ace6ef9d9e530" alt="Node Input/Output Context Menu" data-og-width="1774" width="1774" data-og-height="910" height="910" data-path="images/concepts/node/context_menus_2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=21205850f45887caf0f440de0aef9e19 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a7037a646b1abadb3a8a03cf99b57f53 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0cfefc04ce317796d93a1d9c52f00d27 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0c92cbeef4b1beabd4105cd0872a3ae0 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=34f6d22e3d1dcb60697ccd4b811e3687 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ece7fca06a344e909a62444d253abfa2 2500w" />

When dragging the input/output of a node, if a connection appears but you haven't connected to another node's input or output, releasing the mouse will pop up a context menu for the input/output, used to quickly add related types of nodes.
You can adjust the number of node suggestions in the settings:

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7a063583df5825a8cc24dc13a1723761" alt="Node Suggestion Count" data-og-width="1000" width="1000" data-og-height="314" height="314" data-path="images/concepts/node/node_suggestions.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d407262970bad97799d5105e1bc5cea5 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7bd3a3e2e2e988603d228393390781b0 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9bbb3101a2655835a2b26d19295f0e81 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f40f2b2e28af6a96ead52901a9392ed9 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7baf1d9a57d19a254b9c0675f6644c3e 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=07d79a1ffdbcf13836aa9c11eafe1942 2500w" />

## Node Selection Toolbox

<video controls className="w-full aspect-video" src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/selection_toolbox.mp4?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f2a55de5682187a2e9e012120b968c95" data-path="images/concepts/node/selection_toolbox.mp4" />

The **Node Selection Toolbox** is a floating tool that provides quick operations for nodes. When you select a node, it hovers above the selected node. Through this toolbox, you can:

* Change the node's color
* Quickly set the node to Bypass mode (not execute during runtime)
* Lock the node
* Delete the node

Of course, these functions can also be found in the right-click menu of the corresponding node. The node selection toolbox just provides a shortcut operation. If you want to disable this feature, you can turn it off in the settings.

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=60747b0e83640a2f7a4f1bc66e63a89c" alt="Disable Node Selection Toolbox" data-og-width="1067" width="1067" data-og-height="324" height="324" data-path="images/concepts/node/setting_selection_toolbox.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ded2a8d85c75a7b282e344be55a9a975 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e862be9b2185ba613587c8f8e3c34104 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=beed142e0d37962809b27c53f98602bf 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=6efc4f19b0b54b2daddc9c735d0ec36d 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d2733538bfb0d2749c5f0ea5c7ebdba2 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2b1db6a68c326e2aa3d069f34b1e0da2 2500w" />

## Node Groups

In ComfyUI, you can select multiple parts of a workflow simultaneously, then use the right-click menu to merge them into a node group, making that part a reusable module that can be repeatedly called in your ComfyUI.

## Custom Nodes

ComfyUI includes many powerful nodes in the base installation package. These are known as **Comfy Core** nodes. Additionally, the ComfyUI community has created an amazing array of [***custom nodes***](https://registry.comfy.org) to perform a wide variety of functions.

## ComfyUI Manager

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cea0de500828224b23b64cef84a31936" alt="ComfyUI Manager interface" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/concepts/core-concepts_nodes_manager.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b66fffe074ba15068c2868e5e127cc41 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=951aa7941493ea56018c7aa77d1bc143 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=93e156a11636d64258510480fe1c28c2 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=352d680f30f32e457031be3c6de987d9 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a034b1663b608f4d64c6a690ea652b88 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4ca79e9090f1ed2513db42fa9838af40 2500w" />

The **ComfyUI Manager** window makes it easy to perform custom node management tasks such as search, install, update, disable, and uninstall. The Manager is included in the ComfyUI desktop application, but not in the ComfyUI server application.

### Installing the ComfyUI Manager

If you're running the ComfyUI server application, you need to install the Manager. If ComfyUI is running, shut it down before proceeding.

The first step is to install Git, a command-line application for software version control. Git will download the ComfyUI Manager from [github.com](https://github.com). Download Git from [git-scm.com](https://git-scm.com/) and install it.

Once Git is installed, navigate to the ComfyUI server program directory, to the folder labeled **custom\_nodes**. Open up a command window or terminal. Make sure that the command line displays the current directory path as **custom\_nodes**. Enter the following command. This will download the Manager. Technically, this is known as *cloning a Git repository*.

```bash  theme={null}
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
```

For details or special cases, see [ComfyUI Manager Install](https://github.com/ltdrdata/ComfyUI-Manager?tab=readme-ov-file#installation).
