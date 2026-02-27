> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Bria FIBO Edit API Node ComfyUI Official Example

> Learn how to use the Bria FIBO Edit Partner node for precision image editing in ComfyUI

FIBO Edit is Bria AI's JSON-native image editing model, now available in ComfyUI through Partner Nodes. It lets you combine images with structured JSON prompts to make precise, targeted edits—no prompt guessing, no unwanted changes to the rest of your image.

## About FIBO Edit

**Key features:**

* **Surgical edits**: Change specific attributes (lighting, color, texture, materials) without breaking the rest of the scene
* **Background swaps and object modifications**: Precise control over targeted areas
* **Reproducible, auditable edits**: Structured JSON inputs for consistent results
* **100% licensed data**: Full governance and legal clarity for commercial use
* **Strong prompt adherence**: Validated on PRISM-style evaluations

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

## FIBO Edit Workflows

<CardGroup cols={2}>
  <Card title="Image Edit Workflow" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_image_edit.json">
    Download the Bria FIBO Image Edit workflow.
  </Card>

  <Card title="Image Outpainting Workflow" icon="download" href="https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_image_outpainting.json">
    Download the Bria FIBO Image Outpainting workflow.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Run Image Edit on Cloud" icon="cloud" href="https://cloud.comfy.org/?template=api_bria_image_edit&utm_source=docs">
    Try the Image Edit workflow instantly on Comfy Cloud.
  </Card>

  <Card title="Run Outpainting on Cloud" icon="cloud" href="https://cloud.comfy.org/?template=api_bria_image_outpainting&utm_source=docs">
    Try the Image Outpainting workflow instantly on Comfy Cloud.
  </Card>
</CardGroup>

## Example outputs

FIBO Edit excels at various editing tasks:

* **Time of day changes**: Relight your scene or change the time of day
* **Material and texture swaps**: Try different colors, materials, fabrics, and clothing
* **Object material replacement**: Swap out the material on specific objects
* **Masked area editing**: Mask out a specific area to edit with precision
* **Text adjustment**: Adjust the text in an image
* **Art style transformation**: Re-imagine your image in a different art style
