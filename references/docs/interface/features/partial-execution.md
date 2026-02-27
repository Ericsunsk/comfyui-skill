> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Partial Execution - Run Only Part of Your workflow in ComfyUI

> How to use and the requirements for the Partial Execution feature in ComfyUI

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=790f2410f7764701d6569a0bcdb8848a" alt="Partial Execution Feature" data-og-width="1254" width="1254" data-og-height="530" height="530" data-path="images/interface/features/partial-execution/partial-execution-icon.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=a15bf6730203c7f1ae919d827d8b532a 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=98753703cd874327dc14a0e042684fe2 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=b6533929a7339b99b8120b2edf3eef3f 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8a89d4d2e27bc35be992cbd0b044a50f 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d16057a8ac6becff9ea767f94160c804 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=2a5749cb3ce13e6128f06c6ccf40eeb4 2500w" />

The Partial Execution feature is located in the ComfyUI node selection toolbox. It allows you to run only a part of your workflow instead of executing all nodes. This feature is only available when the selected node is an output node, and when available, it appears as a green triangle icon.

## What is Partial Execution?

Partial Execution, as the name suggests, lets you run only a part of your workflow instead of executing all nodes in the workflow.

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5e7946c8ee4a7ad0b649a4704c53ff20" alt="Partial Execution" data-og-width="1775" width="1775" data-og-height="834" height="834" data-path="images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d6ba18df7c50e5c8df85e275073679c4 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=1b5c07cf73137e9f603da8badad607f5 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=aec697713a449c9abbe3c772eb871d7d 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=420613fd2964d45baf1a53b3d22996eb 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=02a9c63a0357ac77fe591da731d27a99 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=25b0dee989ff504b5f4e769224c8e8af 2500w" />

The diagram above compares Partial Execution and running the entire workflow:

1. Partial Execution (left): Only runs the branch of the workflow from the starting node to the output node.
2. Run Workflow (right): Runs all nodes in the workflow.

This feature allows you to flexibly execute specific parts of your workflow, rather than running the entire workflow every time.

## How to Use the Partial Execution Feature?

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=fa00fd6867f29fdecfb6da4caa9a9c85" alt="Partial Execution Requirements" data-og-width="1311" width="1311" data-og-height="422" height="422" data-path="images/interface/features/partial-execution/requirement.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c1aaaab45238408187aebc6866235a26 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=62e8baac8cc30674f8d8b4ba71cc3ceb 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=f11d3aaabd7638311b8384c7476c0257 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5bdf23e88670e1328ecae65c15bfa330 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0f28c61141927e77e2d1a7528748993c 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=eccc42d70db6ba778720ec1115b6c7de 2500w" />

To use the Partial Execution feature, the currently selected node must be an output node, such as preview or save nodes. When the corresponding node meets the criteria, after selecting the node, the button in the toolbox will display as a green triangle icon. Click this icon to run the partial workflow.

## Common Issues

Q: Why do all nodes run when I use this feature?
A: Please ensure your ComfyUI frontend version is after v1.23.4, or possibly requires v1.24.x version. The corresponding bug was fixed around version 1.24.x, so please update your ComfyUI to the latest version to ensure the frontend version meets the requirements.
