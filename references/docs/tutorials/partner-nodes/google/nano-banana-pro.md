> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Nano Banana Pro and ComfyUI Official Example

> This article will introduce how to use Google's Nano Banana Pro (Gemini 3 Pro Image) in ComfyUI for high-fidelity image generation and editing

Nano Banana Pro is Google DeepMind's new flagship model for high-fidelity image generation and editing. It pushes beyond casual creation into production-ready visuals with advanced capabilities including 4K generation, text rendering, and character consistency.

In this guide, we will walk you through using Nano Banana Pro in ComfyUI.

## Highlights of Nano Banana Pro

* **World knowledge:** Generates accurate, real-world images by tapping into Search's knowledge base.
* **Text & translation:** Renders clean text and supports detection/translation across **10 languages**.
* **High resolutions and studio controls:** Blend up to **14 images**, adjust angles and focus, apply color grading, and create in native **4K**.
* **Consistency:** Turns sketches into dresses or blueprints into 3D visuals with high-fidelity consistency.

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

## Get started

### For new users

The easiest way to use Nano Banana Pro is to go to Comfy Cloud through the link below. No extra setup needed.

<a className="prose" target="_blank" href="https://cloud.comfy.org/?template=api_nano_banana_pro&utm_source=blog" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Try Nano Banana Pro on Comfy Cloud</p>
</a>

### For local users

Please update ComfyUI and go to Template → Nano Banana Pro to access the workflow.
