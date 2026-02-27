> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Custom nodes allow you to implement new features and share them with the wider community.

A custom node is like any Comfy node: it takes input, does something to it, and produces an output.
While some custom nodes perform highly complex tasks, many just do one thing. Here's an example of a
simple node that takes an image and inverts it.

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=8088073e29e8af1bc700937ecb3b77e9" alt="Unique Images Node" data-og-width="564" width="564" data-og-height="279" height="279" data-path="images/invert_image_node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6fa9f912f38ec608ee43f4e456cedf42 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=aeae6dd8bc6393935ebabe3de4b8ed85 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3dbe92afa58705aca5f218df9f5c5a52 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=dfda0a7b67616219ac9b7ec9742cb0d4 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a3b84be0acf1b9248b9ac0086a49bd53 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/invert_image_node.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=2113625a7743f680050980330f4f928d 2500w" />

Custom node examples：

* [cookiecutter-comfy-extension](https://github.com/Comfy-Org/cookiecutter-comfy-extension)
* [ComfyUI-React-Extension-Template](https://github.com/Comfy-Org/ComfyUI-React-Extension-Template)
* [ComfyUI\_frontend\_vue\_basic](https://github.com/jtydhr88/ComfyUI_frontend_vue_basic)

## Client-Server Model

Comfy runs in a client-server model. The server, written in Python, handles all the real work: data-processing, models, image diffusion etc. The client, written in Javascript, handles the user interface.

Comfy can also be used in API mode, in which a workflow is sent to the server by a non-Comfy client (such as another UI, or a command line script).

Custom nodes can be placed into one of four categories:

### Server side only

The majority of Custom Nodes run purely on the server side, by defining a Python class that specifies the input and output types, and provides a function that can be called to process inputs and produce an output.

### Client side only

A few Custom Nodes provide a modification to the client UI, but do not add core functionality. Despite the name, they may not even add new nodes to the system.

### Independent Client and Server

Custom nodes may provide additional server features, and additional (related) UI features (such as a new widget to deal with a new data type). In most cases, communication between the client and server can be handled by the Comfy data flow control.

### Connected Client and Server

In a small number of cases, the UI features and the server need to interact with each other directly.

<Warning>Any node that requires Client-Server communication will not be compatible with use through the API.</Warning>
