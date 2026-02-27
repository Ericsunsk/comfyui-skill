> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Luma Text to Video API Node ComfyUI Official Guide

> Learn how to use the Luma Text to Video Partner node in ComfyUI

The [Luma Text to Video](/built-in-nodes/partner-node/video/luma/luma-text-to-video) node allows you to create high-quality, smooth videos from text descriptions using Luma AI's innovative video generation technology.

In this guide, we'll show you how to set up a text-to-video workflow using this node.

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

## Luma Text to Video Node Documentation

Check out the following documentation to learn more about the node parameters:

<Card title="Luma Text to Video Node Docs" icon="book" href="/built-in-nodes/partner-node/video/luma/luma-text-to-video">
  Documentation for the Luma Text to Video Partner node
</Card>

<Card title="Luma Concepts Node Docs" icon="book" href="/built-in-nodes/partner-node/video/luma/luma-concepts">
  Documentation for the Luma Concepts Partner node
</Card>

## Text to Video Workflow with Luma API Node

The Luma Text to Video node requires text prompts to describe the video content. In this guide, we've created examples using `prompt` and `luma_concepts` to showcase Luma AI's excellent video generation capabilities.

### 1. Download the Workflow

The workflow information is included in the metadata of the video below. Download and drag it into ComfyUI to load the workflow.

![Luma Text to Video Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2v/luma_t2v.mp4)

### 2. Follow the Steps

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=96c92693534372a8522603f9c13f088c" alt="Luma Text to Video Workflow Steps" data-og-width="2097" width="2097" data-og-height="1691" height="1691" data-path="images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7650813bb283f9aabc784d63f2b51547 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ec60e49f9dd61d17f616779b56f785bc 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=de082bf41aef1a9d5464b2971d4f2e2b 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=566048bcd6c3df8e54bb999af0e94715 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7cfc31fc22b5ebd5c567e9f1fecb51bf 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2v_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c0c093965f3aa083066ed153937f8dab 2500w" />

Follow these basic steps to run the workflow:

1. Write your prompt in the `Luma Text to Video` node to describe the video content you want
2. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to generate the video
3. After the API returns results, you can view the generated video in the `Save Video` node. The video will also be saved to the `ComfyUI/output/` directory

> (Optional) Modify the `Luma Concepts` node to control camera movements and add professional cinematography

### 3. Additional Notes

* **Writing Prompts**: Describe scenes, subjects, actions, and mood in detail for best results
* **Luma Concepts**: Mainly used for camera control to create professional video shots
* **Seed Parameter**: Only determines if the node should rerun, doesn't affect generation results
* **Model Selection**: Different video models have different features, adjustable via the model parameter
* **Resolution and Duration**: Adjust output video resolution and length using these parameters
* **Ray 1.6 Model Note**: Duration and resolution parameters don't work when using the Ray 1.6 model
