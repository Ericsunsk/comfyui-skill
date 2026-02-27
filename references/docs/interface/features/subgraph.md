> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Subgraph - Simplify your workflow

> An introduction to the Subgraph feature in ComfyUI, including how to create, navigate, and manage subgraphs.

<Note>
  The subgraph feature requires ComfyUI frontend version 1.24.3 or later. If you don't see this feature, please refer to: [How to Update ComfyUI](/installation/update_comfyui)

  * Images in this document are made with nightly version frontend, please refer to the actual interface
  * Some features like converting subgraph back to nodes will be supported in the future
</Note>

<Tip>
  For developer documentation on working with subgraphs programmatically, see the [Subgraph Developer Guide](/custom-nodes/js/subgraphs).
</Tip>

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/xgQoGT-VpxE?si=hD5196gcX0RW-0Ko" title="ComfyUI Selection Toolbox New Features" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

A subgraph is a powerful ComfyUI feature that lets you package complex workflows into a single reusable subgraph node, making them easier to manage and share.

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=931b7a8e3c9c167864a963b46602208f" alt="Subgraph" data-og-width="3080" width="3080" data-og-height="814" height="814" data-path="images/interface/features/subgraph/subgraph.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=7484ecff612a8790621622f2291818ca 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ffb9eb854478f05648f36d6551dba497 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=510c48cb75c3de020a318ccec4cd1fe5 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=f3619aed6ae3b013a2265deac64ddd52 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5e36e319fa749583004ee266d53ef793 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=7202b1be7d6f81497bc8b358608d91f5 2500w" />

Think of a subgraph as a "folder" for your workflow – you can group related nodes together and use the entire collection as one unified subgraph node.

**Use subgraphs to:**

* Simplify complex workflows
* Reuse common node combinations
* Build more efficient workflows with modular components

## Creating a Subgraph

<Steps>
  <Step title="Select nodes">
    Select the nodes you want to group in ComfyUI
  </Step>

  <Step title="Click the subgraph icon">
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_icon.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=03070a0d4e9ea4289c32d63d0c99ae8d" alt="Subgraph icon" data-og-width="1517" width="1517" data-og-height="700" height="700" data-path="images/interface/features/subgraph/subgraph_icon.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_icon.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0dd55888b474edadae51bee82901d398 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_icon.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0cd57cd019aa94a24145809c89fcd8bb 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_icon.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=529ff40b5d7a0b888e367ff49b0b7bfe 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_icon.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d09520a5f62043b0aadd2af169e3cd64 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_icon.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0bcbb82ff01f07841bf18ce3c77b2fb2 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_icon.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=e5db376d8c58dd8224557070b36dcd31 2500w" />
    Find the subgraph icon in the toolbar
  </Step>

  <Step title="Subgraph created">
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/workflow_using_subgraph.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=66f5a81ffad4b33458c9f3c273601caa" alt="Workflow using subgraph" data-og-width="1820" width="1820" data-og-height="884" height="884" data-path="images/interface/features/subgraph/workflow_using_subgraph.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/workflow_using_subgraph.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c05457df039bdf78c996cc0b62d21afa 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/workflow_using_subgraph.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4c31a704ed275c11cb87d4a0278872da 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/workflow_using_subgraph.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=2bfbacd9216b472a907a49fa0831df00 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/workflow_using_subgraph.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=cb5b011244fb07b78a2711c2331fcb6b 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/workflow_using_subgraph.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=901d398b4feb0293090047763852d066 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/workflow_using_subgraph.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=037d19249e1f20481c2ea133d315b510 2500w" />
    ComfyUI automatically creates a subgraph based on your selected nodes' inputs and outputs
  </Step>

  <Step title="Customize your subgraph">
    Refer to [Editing Subgraphs](#editing-subgraphs), you can edit and organize the subgraph to create a fully functional node
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_after_edited.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=091d4223d6fb2cd2d44009cfee191bab" alt="Workflow using subgraph" data-og-width="1820" width="1820" data-og-height="884" height="884" data-path="images/interface/features/subgraph/subgraph_after_edited.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_after_edited.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=139a8e65714a299ad5dc49bac126e031 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_after_edited.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=626c34ba0e4de784d8cfcae4566970a0 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_after_edited.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=cf7a4be96f187e7d8939834a33af3744 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_after_edited.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ce5f3c3b7bee31df3dadbfd87d00645f 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_after_edited.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=e206f63587afa90fee39dd611f0de73e 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_after_edited.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=43cb284ca2fd2eca53ee9581563dbc44 2500w" />
  </Step>
</Steps>

## Working with Subgraphs

### Basic Operations

Subgraphs work just like regular nodes. You can:

* Change colors and names
* Use bypass to disable
* Apply all standard node operations

### Editing Subgraphs

**To enter edit mode:**

* Double-click the empty area inside the subgraph (not on widgets), or
* Click the subgraph edit button

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4802435f0ede07e1172b9f7fbd459399" alt="Subgraph editing mode" data-og-width="1820" width="1820" data-og-height="1203" height="1203" data-path="images/interface/features/subgraph/editing_subgraph.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c5004638bdaae3d2edcd8aa9e87e1a22 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5784b8ab234eade79fd01dc289ccc16f 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=fdde61548dc9421b794ee6ad221e09c7 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=b4e60fafda5a9d0ae693c34d64bc6fc5 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d68f2a0aefa79203affffdfdb6ae4750 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c09e3b4e183792d54740d945eac2f5fb 2500w" />

**In edit mode you'll see:**

1. **Navigation bar**: Exit the current subgraph and return to the parent level
2. **Input slots**: Internal node inputs exposed to the outside
   * Connect outputs to slots like normal nodes
   * **Right-click** connection points to rename/delete exposed slots
3. **Output slots**: Outputs exposed to the outside (same functionality as input slots)

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_slot.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5f4cdd87ea46007d9bf35921576f12cb" alt="Subgraph slots" data-og-width="1736" width="1736" data-og-height="921" height="921" data-path="images/interface/features/subgraph/subgraph_slot.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_slot.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=a9a3a3a362787bd4ec8baf0b81d7f3be 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_slot.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=cad68d957f2a21f92df351efaf61a722 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_slot.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0f807ae47f75ca5fb378eba4db01a836 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_slot.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0c36bf5ddf538699ee69823b93ce1d5f 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_slot.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4df72f73a01f53cd944bb50a067c8266 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_slot.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=27ad35bf488e79c92e25efd4132c4e0a 2500w" />

**Working with slots:**

1. **Default slot** (labeled 1): Use this to add new input/output connections
2. **Right-click** existing slots to rename, delete, or disconnect from original nodes

> Note: Slot connections follow standard data type validation rules

### Parameters Panel

With ComfyUI v0.3.66 or later, you can edit the subgraph parameters directly from the parameters panel without entering the subgraph.

You can select any subgraph and use the "Edit Subgraph Widgets" button to open the parameters panel.
<img src="https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_open.jpg?fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=efe2c0c6b281f2fe19b2e814454c2f82" alt="Open Parameters Panel" data-og-width="1330" width="1330" data-og-height="1176" height="1176" data-path="images/interface/features/subgraph/parameters_panel_open.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_open.jpg?w=280&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=e1bc5a95dc4ebdfcfdfcf52f8ddc4413 280w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_open.jpg?w=560&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=7f6bb92fa13d3bf2391ad78655cd911c 560w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_open.jpg?w=840&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=b49651ee712172a415be39bc2a02a4a3 840w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_open.jpg?w=1100&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=badede49baa2a56d4443713d8ae34818 1100w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_open.jpg?w=1650&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=4a524b24649b4f98dbaa1ad7f14c9ee6 1650w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_open.jpg?w=2500&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=71f5cfae2c659d52a59a9279b293a935 2500w" />

After it is opened, you can edit the order and visibility of the subgraph widgets directly in the parameters panel.

<img src="https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_edit.jpg?fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=4c77e4e50454e6ccd15c2d02a64feb0e" alt="Open Parameters Panel" data-og-width="1456" width="1456" data-og-height="1492" height="1492" data-path="images/interface/features/subgraph/parameters_panel_edit.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_edit.jpg?w=280&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=b693731c43937fbaa374fe94be350fae 280w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_edit.jpg?w=560&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=72695443ec942f5eeda51af85acbda41 560w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_edit.jpg?w=840&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=6a73b1061c2ea3d40ac6ef49b3016bcb 840w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_edit.jpg?w=1100&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=1eab5b592ecbab71f5a2b22c96926431 1100w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_edit.jpg?w=1650&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=b99457333b5d92aaa197bf376ead1717 1650w, https://mintcdn.com/dripart/l9YPgCbipT00aLbn/images/interface/features/subgraph/parameters_panel_edit.jpg?w=2500&fit=max&auto=format&n=l9YPgCbipT00aLbn&q=85&s=94460ffb4449c56e91eea6aacbde7fe8 2500w" />

1. Reordering: you use right-click and hold the widget to drag it to the desired position
2. Visibility: you can check the visibility of the widget by clicking the eye icon

### Nested Subgraphs

Create even more complex workflows by nesting subgraphs within subgraphs.

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_nested.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=7e92ac585c91b067ab2527da1b5c521c" alt="Nested subgraph" data-og-width="1820" width="1820" data-og-height="1203" height="1203" data-path="images/interface/features/subgraph/subgraph_nested.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_nested.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=a98bb3ff8b829e604fa4bb30ec9e13c2 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_nested.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=7def59b7271a33c9d9580d9124672f60 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_nested.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=54bb00b8554c5467fc22d6e2ec4cb4ed 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_nested.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=a604574cadfd063eff7194cef285b62c 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_nested.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=a4d75bab687f549c3479e2cf6a391e96 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_nested.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=1a8838a69eadae908cb1ef65185d73fb 2500w" />

The navigation bar shows your current level and lets you easily move between nested subgraphs.

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_navigation.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=81b0b1bdb46f54e856600de892cf7089" alt="Nested subgraph navigation" data-og-width="1820" width="1820" data-og-height="1203" height="1203" data-path="images/interface/features/subgraph/subgraph_navigation.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_navigation.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=b286efcf22cd5369ecb2574ee6b7c936 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_navigation.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=6be4422e80fed2df3695b27d0793fe85 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_navigation.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=11cf00c50eb0b4e40ea66f9c703b7212 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_navigation.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8505431b1f4457f9279ae49cde0e7700 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_navigation.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=f6f0268fb51976095cf28f8428ab56df 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_navigation.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0f55b6380a1981b1770194ec4b849619 2500w" />

### Exit subgraph

To exit a subgraph and return to the parent level:

* Use the **Navigation bar** (labeled 1 in the image) at the top of the canvas, or
* Press the **Esc** key

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4802435f0ede07e1172b9f7fbd459399" alt="Subgraph editing mode" data-og-width="1820" width="1820" data-og-height="1203" height="1203" data-path="images/interface/features/subgraph/editing_subgraph.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c5004638bdaae3d2edcd8aa9e87e1a22 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5784b8ab234eade79fd01dc289ccc16f 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=fdde61548dc9421b794ee6ad221e09c7 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=b4e60fafda5a9d0ae693c34d64bc6fc5 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d68f2a0aefa79203affffdfdb6ae4750 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/editing_subgraph.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c09e3b4e183792d54740d945eac2f5fb 2500w" />

Click on the navigation bar or press Esc to exit the current subgraph and return to the parent workflow.

## Unpack Subgraphs to Nodes

When you're done creating a subgraph, you can convert it back to nodes if you need to.

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_to_nodes.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=3f6dfede84ad760f7775846259e0b3e6" alt="Subgraph to node" data-og-width="912" width="912" data-og-height="548" height="548" data-path="images/interface/features/subgraph/subgraph_to_nodes.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_to_nodes.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=addf861fcb10c6ffb94dc3467730618c 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_to_nodes.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4afb9253344041b4196f0d405943e506 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_to_nodes.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=9b11700c233cda409b0deb8b673dda55 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_to_nodes.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=f6194c67fe2ecfc9e41c1e6f14ae495f 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_to_nodes.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=251cde5945070473fb15fa76b11668c5 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_to_nodes.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=e335ec3ffc26e4ef6f03c283adba1bb6 2500w" />

1. You can select the subgraph node then use right-click menu "Unpack subgraph" to convert it back to nodes.
2. Click the "Unpack subgraph" button in the select toolbox to convert it back to nodes.

## Subgraph Blueprint

With ComfyUI frontend version 1.27.7 or later, you can publish your subgraph to the node library.

This feature allows you to convert a subgraph to a `Subgraph Blueprints` node, which means it's a reusable subgraph node.

### Publish Subgraph to Node Library

<img src="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_publishing.jpg?fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=5079af05b2211b0547a3cc3b999c3c1a" alt="Publish Subgraph" data-og-width="1286" width="1286" data-og-height="1214" height="1214" data-path="images/interface/features/subgraph/subgraph_publishing.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_publishing.jpg?w=280&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=29e2581b133c92737c301b43e0a20df1 280w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_publishing.jpg?w=560&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=3bcc71ef0d24637239023e3cdbab56df 560w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_publishing.jpg?w=840&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=301c24eb26a93299e2cc4b4fae8eba5c 840w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_publishing.jpg?w=1100&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=a339604f87d7d63c891543ee3607c1ad 1100w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_publishing.jpg?w=1650&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=e27886b5e462b7ae4fd837b376daab4a 1650w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_publishing.jpg?w=2500&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=9970571e2c50bbe63b52cfde34468f48 2500w" />

Currently, you have two ways to publish subgraph to node library, both are in the selection toolbox:

1. Click the `book(publish)` icon on the selection toolbox
2. Open the selection toolbox menu, use the `Add Subgraph to Library` menu to publish subgraph

After you click on the `book(publish)` icon or `Add Subgraph to Library` menu, you will see the following dialog:

<img src="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_naming.jpg?fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=0b20fc138a6e4e8ac826176067b5848e" alt="Subgraph naming" data-og-width="1286" width="1286" data-og-height="840" height="840" data-path="images/interface/features/subgraph/subgraph_naming.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_naming.jpg?w=280&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=5083e28f19b2931c6aae05d7f5c5b1d3 280w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_naming.jpg?w=560&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=63d78999de119d283d542805eafcfa58 560w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_naming.jpg?w=840&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=719ddf790a00869d79e82a6a4a0f4514 840w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_naming.jpg?w=1100&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=ab19c52163f56fcf90b232a443275632 1100w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_naming.jpg?w=1650&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=2ee570463b0291e86e2afd7c269bc143 1650w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_naming.jpg?w=2500&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=3068efa382497f73ba39a8ccfda0003a 2500w" />

By default, the subgraph will use the name of the subgraph node as the name of the subgraph blueprint.

After publishing, you will see the subgraph blueprint node in the node library.

<img src="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_blueprints.jpg?fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=90242f76da15ce0de949692114757aeb" alt="Subgraph blueprint node" data-og-width="2003" width="2003" data-og-height="1242" height="1242" data-path="images/interface/features/subgraph/subgraph_blueprints.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_blueprints.jpg?w=280&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=82212b77bae2a2e794e5a9fbb01573ab 280w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_blueprints.jpg?w=560&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=d61c4a3c34f82da681455976f6867b64 560w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_blueprints.jpg?w=840&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=1560181fb4b2ab798eea193703df68ef 840w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_blueprints.jpg?w=1100&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=e8f7ed0bf63d0d432434981fb70e26af 1100w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_blueprints.jpg?w=1650&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=e6e0d590a98c979171a0a1e0b1ac37d6 1650w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_blueprints.jpg?w=2500&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=887b43b903c9e3f76db59702ff2801a4 2500w" />

Now, you can drag or search the subgraph just like a normal node. The new subgraph node that has been added from Subgraph Blueprints is still isolated, which means after adding it to the workflow, it can be edited independently, they will not affect each other.

### Edit Subgraph Blueprint

If you want to edit the subgraph blueprint, you can click the edit button just like the image below, you can delete it as well.

<img src="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/edit_subgraph_blueprints.jpg?fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=d5d63e62403ea8cf4b95274c968ab835" alt="Edit Subgraph Blueprint" data-og-width="2000" width="2000" data-og-height="1245" height="1245" data-path="images/interface/features/subgraph/edit_subgraph_blueprints.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/edit_subgraph_blueprints.jpg?w=280&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=a7ed619282d9cbe8eb5162d4f02dd4ad 280w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/edit_subgraph_blueprints.jpg?w=560&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=a0730a03c3ff65d1b8e90e5cc6f684b3 560w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/edit_subgraph_blueprints.jpg?w=840&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=99c07e5d038060c1b480ec3572a83dc9 840w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/edit_subgraph_blueprints.jpg?w=1100&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=e75f6845171ab376132850d2e9545a89 1100w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/edit_subgraph_blueprints.jpg?w=1650&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=34e43eb8c09e1fe9db2db904d9c401a2 1650w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/edit_subgraph_blueprints.jpg?w=2500&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=d1289aa590a56b59d3f25cfc7ae8058b 2500w" />

This will enable the subgraph editing mode

<img src="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_editing_mode.jpg?fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=de6bfcfe9561003dc7fe738eff6acdc2" alt="Subgraph editing mode" data-og-width="2000" width="2000" data-og-height="1359" height="1359" data-path="images/interface/features/subgraph/subgraph_editing_mode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_editing_mode.jpg?w=280&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=93f1eae882fe5fc32f81e0489b67481c 280w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_editing_mode.jpg?w=560&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=30fb6521e389de81c556100261194549 560w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_editing_mode.jpg?w=840&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=9457940713df4050a7966ed11fbf6fe7 840w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_editing_mode.jpg?w=1100&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=a13f8aba451eebcd18e40663f05f5568 1100w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_editing_mode.jpg?w=1650&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=6c5182b163ff7860acfe8caf4d452e52 1650w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/subgraph_editing_mode.jpg?w=2500&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=20f0905025a4ea70273de710b5efeb16 2500w" />

After editing the subgraph blueprint, you can go to the parent level to preview the subgraph.

<img src="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/save_updated_subgraph.jpg?fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=976ddb2fc548798253b795d6f19aa044" alt="Update Subgraph Blueprint" data-og-width="2000" width="2000" data-og-height="1359" height="1359" data-path="images/interface/features/subgraph/save_updated_subgraph.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/save_updated_subgraph.jpg?w=280&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=e2054a8c9ff84f911d7d2a634f7c3cfe 280w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/save_updated_subgraph.jpg?w=560&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=612d8ceffaf348a65f9e86baf271f8a8 560w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/save_updated_subgraph.jpg?w=840&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=374109865fd37381fcbcaa2519d132c8 840w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/save_updated_subgraph.jpg?w=1100&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=b8368191351b9489bf6061970b2fbe0e 1100w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/save_updated_subgraph.jpg?w=1650&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=eea83242299e62247324d63926a6f2f9 1650w, https://mintcdn.com/dripart/fLKXN8EDUY0BDXQk/images/interface/features/subgraph/save_updated_subgraph.jpg?w=2500&fit=max&auto=format&n=fLKXN8EDUY0BDXQk&q=85&s=68f2d9dc08241dc8bf608dcfa354ae02 2500w" />

If you want to save the updated subgraph blueprint, you can click the save button or use the shortcut key Ctrl + S.
