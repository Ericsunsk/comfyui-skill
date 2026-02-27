> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan 3D API Node Model Generation ComfyUI Official Example

> This article will introduce how to use Hunyuan 3D node's API in ComfyUI for 3D model generation

Hunyuan 3D 3.0 is Tencent's state-of-the-art 3D generation model that enables minutes-level 3D content creation. It can generate production-ready 3D assets from text prompts, images, or sketches with far lower barriers to entry than traditional 3D modeling pipelines.

ComfyUI has now natively integrated the corresponding Hunyuan 3D API, allowing you to conveniently use the related nodes in ComfyUI for model generation.

Currently, ComfyUI's Partner nodes support the following Hunyuan 3D model generation capabilities:

* Text-to-3D generation
* Image-to-3D generation
* Multi-view-to-3D generation

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

## Use cases

* **Game development ideation**: Fast generation of characters, props, and environments with optimized topology for rigging and real-time rendering
* **Product & e-commerce**: Turn product photos into interactive 3D models for online display
* **Industrial design**: Sketch-to-3D prototyping and 3D-print-ready part decomposition
* **VFX & animation**: High-resolution assets with professional UVs and PBR materials

## Getting started

### 1. Access workflow templates

1. Open the Template Library in the sidebar
2. Navigate to **3D** → **Hunyuan 3D**
3. Select a workflow template for Hunyuan 3D

### 2. Run the workflow

1. Input your text prompt, images, or sketches depending on the workflow type
2. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation
3. After the workflow completes, preview and export your 3D model

## Text-to-3D workflow

Enter a text description to generate a 3D model in one click. The model accurately follows style, shape, and material details for consistent results.

**Example prompt**: "Mechanical dolphin with gears, steampunk"

<Card title="Hunyuan 3D Text-to-3D Workflow" icon="cloud" href="https://cloud.comfy.org/?template=api_hunyuan3d_text_to_model&utm_source=docs&utm_medium=inhouse_social&utm_campaign=inhouse_feature_launches&utm_content=post&utm_niche=workflow_engineering&utm_creator=purz">
  Run on Comfy Cloud
</Card>

## Image-to-3D workflow

Upload one or more images to generate high-quality 3D models. Support for 2–4 multi-view images improves geometry and material fidelity.

<Card title="Hunyuan 3D Image-to-3D Workflow" icon="cloud" href="https://cloud.comfy.org/?template=api_hunyuan3d_image_to_model&utm_source=docs&utm_medium=inhouse_social&utm_campaign=inhouse_feature_launches&utm_content=post&utm_niche=workflow_engineering&utm_creator=purz">
  Run on Comfy Cloud
</Card>

## Multi-view-to-3D workflow

Provide multiple view images (front, back, side) to generate 3D models with improved accuracy and detail. This uses the same workflow as Image-to-3D—simply upload 2–4 images from different angles.

<Card title="Hunyuan 3D Image-to-3D Workflow" icon="cloud" href="https://cloud.comfy.org/?template=api_hunyuan3d_image_to_model&utm_source=docs&utm_medium=inhouse_social&utm_campaign=inhouse_feature_launches&utm_content=post&utm_niche=workflow_engineering&utm_creator=purz">
  Run on Comfy Cloud
</Card>
