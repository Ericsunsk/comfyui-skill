> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 部分执行 - 允许你只运行 ComfyUI 中的部分节点

> ComfyUI 中部分执行（Partial Execution）功能的使用方法和条件

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=790f2410f7764701d6569a0bcdb8848a" alt="部分执行功能" data-og-width="1254" width="1254" data-og-height="530" height="530" data-path="images/interface/features/partial-execution/partial-execution-icon.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=a15bf6730203c7f1ae919d827d8b532a 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=98753703cd874327dc14a0e042684fe2 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=b6533929a7339b99b8120b2edf3eef3f 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8a89d4d2e27bc35be992cbd0b044a50f 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d16057a8ac6becff9ea767f94160c804 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-icon.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=2a5749cb3ce13e6128f06c6ccf40eeb4 2500w" />

**部分执行** 功能是位于 ComfyUI 节点选择工具箱上的一个功能，它能够让你 **只运行工作流的一部分** ，而不是完整运行工作流中的所有节点，它仅在所选节点是一个 **输出节点** 时才可用，可用时会显示为绿色的三角形图标

## 什么是部分执行？

部分执行（Partial Execution），就像它字面上的意思一样，只运行工作流的一部分，而不是完整运行工作流中的所有节点

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5e7946c8ee4a7ad0b649a4704c53ff20" alt="部分执行" data-og-width="1775" width="1775" data-og-height="834" height="834" data-path="images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d6ba18df7c50e5c8df85e275073679c4 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=1b5c07cf73137e9f603da8badad607f5 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=aec697713a449c9abbe3c772eb871d7d 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=420613fd2964d45baf1a53b3d22996eb 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=02a9c63a0357ac77fe591da731d27a99 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=25b0dee989ff504b5f4e769224c8e8af 2500w" />

在上面的示意图中，是部分执行与运行工作流功能的对比

1. 部分执行（左侧）：只运行从起始节点到输出节点分支的工作流
2. 运行工作流（右侧）：运行工作流中的所有节点

这个功能能够运行你更灵活地运行工作流的特定部分，而不是每次都运行整个工作流。

## 如何使用部分执行功能？

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=fa00fd6867f29fdecfb6da4caa9a9c85" alt="部分执行功能的使用条件" data-og-width="1311" width="1311" data-og-height="422" height="422" data-path="images/interface/features/partial-execution/requirement.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c1aaaab45238408187aebc6866235a26 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=62e8baac8cc30674f8d8b4ba71cc3ceb 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=f11d3aaabd7638311b8384c7476c0257 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5bdf23e88670e1328ecae65c15bfa330 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0f28c61141927e77e2d1a7528748993c 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/partial-execution/requirement.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=eccc42d70db6ba778720ec1115b6c7de 2500w" />

要使用部分执行功能，需要满足，当前选中的节点是一个输出节点，如保存或者预览节点，当对应的节点符合条件时，选中节点后选择工作箱上的按钮会显示为绿色三角形图标，点击该图标即可运行部分工作流

## 常见问题

Q: 为什么在使用这个功能的时候，所有节点都运行了？
A: 前确保你的 ComfyUI 前端版本是在 v1.23.4 版本之后，甚至可能需要 v1.24.x 的版本，对应的缺陷是在 1.24.x 左右版本的才修复，所以请更新你的 ComfyUI 到最新版本，确保前端版本符合要求
