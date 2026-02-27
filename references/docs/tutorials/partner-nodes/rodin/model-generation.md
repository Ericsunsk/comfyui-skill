> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Rodin API Node Model Generation ComfyUI Official Example

> This article will introduce how to use Rodin node's API in ComfyUI for model generation

Hyper3D Rodin (hyper3d.ai) is a platform focused on rapidly generating high-quality, production-ready 3D models and materials through artificial intelligence.
ComfyUI has now natively integrated the corresponding Rodin model generation API, allowing you to conveniently use the related nodes in ComfyUI for model generation.

Currently, ComfyUI's Partner nodes support the following Rodin model generation capabilities:

* Single-view model generation
* Multi-view model generation
* Model generation with different levels of detail

<Tip>
  To use the API nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [API Nodes Overview](/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the API nodes.
</Tip>

<Tip>
  <Tabs>
    <Tab title="Portable or self deployed users">
      Make sure your ComfyUI is updated.

      * [Download ComfyUI](https://www.comfy.org/download)
      * [Update Guide](/installation/update_comfyui)

      Workflows in this guide can be found in the [Workflow Templates](/interface/features/template).
      If you can't find them in the template, your ComfyUI may be outdated. (Desktop version's update will delay sometime)

      If nodes are missing when loading a workflow, possible reasons:

      1. You are not using the latest ComfyUI version (Nightly version)
      2. Some nodes failed to import at startup
    </Tab>

    <Tab title="Desktop or Cloud users">
      * The Desktop is base on ComfyUI stable release, it will auto-update when there is a new Desktop stable release available.
      * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

      So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.
    </Tab>
  </Tabs>
</Tip>

## Single-view Model Generation Workflow

### 1. Workflow File Download

Download the file below and drag it into ComfyUI to load the corresponding workflow.

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/rodin_image_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Json Format Workflow File</p>
</a>

Download the image below as input image

![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/doll.jpg)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ed79f1fb8546ed41a3d157cece818ee9" alt="ComfyUI Rodin Image to Model Step Guide" data-og-width="3184" width="3184" data-og-height="1966" height="1966" data-path="images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bb2b6e3ac6ed70eacf7eeac89fd00f52 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=19a1db47eea31a4666f42bb6607cb513 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=75cbf45620b8886b60a396330a9bb382 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c33ffd2c8306ea9d2d9ba27191374af7 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bf0689795ccfaa241823dcf6ae4bd2e3 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=03f0404c646e21eaac437e9d2959c174 2500w" />

You can refer to the numbers in the image to complete the basic text-to-image workflow execution:

1. In the `Load Image` node, load the provided input image
2. (Optional) In `Rodin 3D Generate - Regular Generate` adjust the corresponding parameters
   * polygon\_count: You can set different polygon counts, the higher the value, the smoother and more detailed the model
3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/Rodin` directory
4. In the `Preview 3D` node, click to expand the menu
5. Select `Export` to directly export the corresponding model

## Multi-view Model Generation Workflow

The corresponding `Rodin 3D Generate - Regular Generate` allows up to 5 image inputs

### 1. Workflow File Download

You can modify the single-view workflow to a multi-view workflow, or directly download the workflow file below

Download the file below and drag it into ComfyUI to load the corresponding workflow.

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/api_rodin_multiview_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Json Format Workflow File</p>
</a>

Download the images below as input images

![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/front.jpg)
![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/back.jpg)
![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/left.jpg)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6241527775e83bd480811631ef4d88ed" alt="ComfyUI Rodin Image to Model Step Guide" data-og-width="3062" width="3062" data-og-height="1862" height="1862" data-path="images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3bdf978dce46f6db8ab13a0437f8af6 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a867df65f89c9cfd6bb6ce6d84de998f 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4a64175900800ea8ed9c10834b1a659a 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=85a75906989c2303477a70a57bc2a749 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=24ca3f810e13d8e7eab70ceb2ec96dfd 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c82bea8ae4fbf55442bdc61abfd3dc8c 2500w" />

You can refer to the numbers in the image to complete the basic text-to-image workflow execution:

1. In the `Load Image` node, load the provided input images
2. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/Rodin` directory
3. In the `Preview 3D` node, click to expand the menu
4. Select `Export` to directly export the corresponding model

## Other Related Nodes

Currently, Rodin provides different types of model generation nodes in ComfyUI, since the corresponding input conditions are the same as the workflow introduced in this article, you can enable them as needed. In addition, we have provided corresponding nodes in the corresponding templates, you can also modify the corresponding node mode as needed to enable them

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7caf60a6b994156e71476564c856fc15" alt="Rodin Other Related Nodes" data-og-width="975" width="975" data-og-height="1170" height="1170" data-path="images/tutorial/api_nodes/rodin/other_nodes.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=37c61a8000c0d3bfd5db85417a4ef98a 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ed2d06928db9041c249ab44b780c0127 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d4faca003f5b868e16be6f45b03d8a8f 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=52067d9b1de876f176083b6b2c0cc8f5 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=86fffeaf114a2532b28a95a75d5f5df7 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=945fdf363130d1e3bad049c2062dd231 2500w" />
