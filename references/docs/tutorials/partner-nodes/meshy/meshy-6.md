> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Meshy 6 API Node Model Generation ComfyUI Official Example

> This article will introduce how to use Meshy 6 node's API in ComfyUI for 3D model generation

Meshy is a leading AI-powered 3D generation platform that enables users to create high-quality 3D models from text prompts, images, or multi-view inputs. ComfyUI has now natively integrated the Meshy API, allowing you to conveniently use the related nodes for 3D model generation.

## About Meshy 6

Meshy 6 is the latest generation of Meshy's 3D model generation technology, featuring significant improvements in geometry quality, texture fidelity, and workflow efficiency.

**Model highlights:**

* **Smarter geometry**: Improved mesh topology with cleaner edges and more coherent structures
* **Higher texture fidelity**: Enhanced texture generation with better detail preservation and color accuracy
* **Faster workflows**: Optimized generation pipeline for quicker turnaround times
* **Multiple input modes**: Supports text-to-3D, image-to-3D, and multi-view to 3D generation
* **PBR support**: Generate physically-based rendering maps including metallic, roughness, and normal maps

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

## Text-to-Model Workflow

Generate 3D models directly from text descriptions using Meshy 6.

<CardGroup cols={2}>
  <Card title="Try on Cloud" icon="cloud" href="https://cloud.comfy.org/?template=api_meshy_text_to_model&utm_source=docs">
    Run the text-to-model workflow instantly on Comfy Cloud.
  </Card>

  <Card title="Download Workflow" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_text_to_model.json">
    Download the workflow JSON file for local use.
  </Card>
</CardGroup>

## Image-to-Model Workflow

Convert 2D images into detailed 3D models with Meshy 6's image-to-3D capabilities.

<CardGroup cols={2}>
  <Card title="Try on Cloud" icon="cloud" href="https://cloud.comfy.org/?template=api_meshy_image_to_model&utm_source=docs">
    Run the image-to-model workflow instantly on Comfy Cloud.
  </Card>

  <Card title="Download Workflow" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_image_to_model.json">
    Download the workflow JSON file for local use.
  </Card>
</CardGroup>

## Multi-view to Model Workflow

Generate 3D models from multiple view images for more accurate geometry and texture reconstruction.

<CardGroup cols={2}>
  <Card title="Try on Cloud" icon="cloud" href="https://cloud.comfy.org/?template=api_meshy_multi_image_to_model&utm_source=docs">
    Run the multi-view workflow instantly on Comfy Cloud.
  </Card>

  <Card title="Download Workflow" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_multi_image_to_model.json">
    Download the workflow JSON file for local use.
  </Card>
</CardGroup>
