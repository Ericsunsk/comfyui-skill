> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Cosmos Predict2 Text-to-Image ComfyUI Official Example

> This guide demonstrates how to complete Cosmos-Predict2 text-to-image workflow in ComfyUI

Cosmos-Predict2 is NVIDIA's next-generation physical world foundation model, specifically designed for high-quality visual generation and prediction tasks in physical AI scenarios.
The model features exceptional physical accuracy, environmental interactivity, and detail reproduction capabilities, enabling realistic simulation of complex physical phenomena and dynamic scenes.

Cosmos-Predict2 supports various generation methods including Text-to-Image (Text2Image) and Video-to-World (Video2World), and is widely used in industrial simulation, autonomous driving, urban planning, scientific research, and other fields.

GitHub:[Cosmos-predict2](https://github.com/nvidia-cosmos/cosmos-predict2)
huggingface: [Cosmos-Predict2](https://huggingface.co/collections/nvidia/cosmos-predict2-68028efc052239369a0f2959)

This guide will walk you through completing **text-to-image** workflow in ComfyUI.

For the video generation section, please refer to the following part:

<Card title="Cosmos Predict2 Video Generation" icon="book" href="/tutorials/video/cosmos/cosmos-predict2-video2world">
  Using Cosmos-Predict2  for video generation
</Card>

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
