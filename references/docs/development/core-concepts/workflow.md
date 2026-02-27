> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflow

## A graph of nodes

ComfyUI is an environment for building and running generative content ***workflows***. In this context, a workflow is defined as a collection of program objects called ***nodes*** that are connected to each other, forming a network. This network is also known as a ***graph***.

A ComfyUI workflow can generate any type of media: image, video, audio, AI model, AI agent, and so on.

## Sample workflows

To get started, use the built-in [Workflow Templates](/interface/features/template). Open them via `Workflow` → `Browse Workflow Templates` in the menu. These templates use only the Core nodes included in the ComfyUI installation and will automatically prompt you to download any required models. A thriving community of developers has created a rich [ecosystem](https://registry.comfy.org) of custom nodes to extend the functionality of ComfyUI.

### Simple Example

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=60028deaf5c13f399515ca2027f680e6" alt="simple workflow" data-og-width="1400" width="1400" data-og-height="637" height="637" data-path="images/simple_workflow.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=44b4c2822d777030f13340f9076c9e41 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=17c74acde982dffc3890f4d4d0781bf8 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6c44653c323146e9578e277dca28d6bd 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=867c4d06c3510d67daeddff1251a47ea 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3fad15ddc2e7c040f2b444fe2b62849a 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/simple_workflow.jpeg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a23372305e8c14c8797350f56ef29078 2500w" />

## Visual programming

A node-based computer program like ComfyUI provides a level of power and flexibility that can’t be achieved with traditional menu- and button-driven applications. The ComfyUI node graph is not limited by the tools provided in a traditional computer application. It’s a high-level ***visual programming environment*** allowing users to design complex systems without needing to write program code or understand advanced mathematics.

Many other computer applications use this same node graph paradigm. Examples include the compositing application called Nuke, the 3D programs Maya and Blender, the Unreal real-time graphics engine, and the interactive media authoring program called Max.

### More Complex Example

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=72268aab0bf1c70be6388930d50aa983" alt="complex workflow" data-og-width="1000" width="1000" data-og-height="511" height="511" data-path="images/complex_workflow.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9efef3c1cfc3f6987ee96b766e13e5f3 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c0b199f01cfd67377ee9b38c361764a3 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6a8866c954c07678fc29dbe1748f61cf 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a7c7ec3f73860b7d36c41889b65911cb 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b800e44f63e64f1346cb72b60b51864b 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/complex_workflow.jpeg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c5559937ae61c95c9e025977585b8a68 2500w" />

## Procedural framework

Another term used to describe a node-based application is ***procedural framework***. Procedural means generative: some procedure or algorithm is employed to generate content such as a 3D model or a musical composition.

ComfyUI is all of these things: a node graph, a visual programming environment, and a procedural framework. What makes ComfyUI different (and amazing!) is that its radically open structure allows us to generate any type of media asset such as picture, movie, sound, 3D model, AI model, etc.

In the context of ComfyUI, the term ***workflow*** is a synonym for the node network or graph. It corresponds to the ***scene graph*** in a 3D or multimedia program: the network of all of the nodes within a particular disk file. 3D programs call this a ***scene file***. Video editing, compositing, and multimedia programs usually call it a ***project file***.

## Saving workflows

The ComfyUI workflow is automatically saved in the metadata of any generated image, allowing users to open and use the graph that generated the image. A workflow can also be stored in a human-readable text file that follows the JSON data format. This is necessary for media formats that don’t support metadata. ComfyUI workflows stored as JSON files are very small, allowing convenient versioning, archiving, and sharing of graphs, independently of any generated media.
