> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Tripo API Node Model Generation ComfyUI Official Example

> This article will introduce how to use Tripo node's API in ComfyUI for model generation

Tripo AI is a company focused on generative AI 3D modeling. It provides user-friendly platforms and API services that can quickly convert text prompts or 2D images (single or multiple) into high-quality 3D models.
ComfyUI has now natively integrated the corresponding Tripo API, allowing you to conveniently use the related nodes in ComfyUI for model generation.

Currently, ComfyUI's Partner nodes support the following Tripo model generation capabilities:

* Text-to-model
* Image-to-model
* Multi-view model generation
* Rig model
* Retarget rigged model

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

### 1. Workflow File Download

Download the file below and drag it into ComfyUI to load the corresponding workflow.

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/api_tripo_text_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Json Format Workflow File</p>
</a>

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b25199fbdd5c00f3fd8a1b587586bbed" alt="ComfyUI Tripo Text to Model Step Guide" data-og-width="2318" width="2318" data-og-height="1564" height="1564" data-path="images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=808ef38a541ba42c3b620b3e55ff56f3 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=ca327bac2f1d7a11cc6d8433607e85ed 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=432f2214d0abbb7709ec85850f76b9c9 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f34d08594b7a1720ae80afa4c91b3142 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=a68421325e3a559a58e8a1a84395cf17 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1c434abf6d478d1f86f1385614cc29a8 2500w" />

You can refer to the numbers in the image to complete the basic text-to-model workflow execution:

1. In the `Tripo: Text to Model` node, input your prompt in the `prompt` field
   * model: You can select different models, currently only v1.4 model supports subsequent optimization with `Tripo: Refine Draft model`
   * style: You can set different styles
   * texture\_quality: You can set different texture qualities
2. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/` directory
3. In the `Preview 3D` node, click to expand the menu
4. Select `Export` to directly export the corresponding model

## Image-to-Model Workflow

### 1. Workflow File Download

Download the file below and drag it into ComfyUI to load the corresponding workflow.

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/image_to_model/api_tripo_image_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Json Format Workflow File</p>
</a>

Download the image below as input image

![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/image_to_model/panda.jpg)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=302a46095bbb73ea478f441fa489b763" alt="ComfyUI Tripo Text to Model Step Guide" data-og-width="2242" width="2242" data-og-height="2610" height="2610" data-path="images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d8e92cb71153fceb6c2f0dbb4c1274f3 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0a94c80971b9c0af74607418869d99e5 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c52fda410d968df9b53b62282bd0af75 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f38d19355d3a8bdb3f1c7d9754f2e186 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e2d4f2d0e7592eddc65143626053ebe4 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=88b1cbf8fce76b0e1810bf6ec9aa2a6c 2500w" />

You can refer to the numbers in the image to complete the basic image-to-model workflow execution:

1. In the `Load Image` node, load the provided input image
2. In the `Tripo: Image to Model` node, modify the corresponding parameter settings
   * model: You can select different models, currently only v1.4 model supports subsequent optimization with `Tripo: Refine Draft model`
   * style: You can set different styles
   * texture\_quality: You can set different texture qualities
3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/` directory
4. For model download, please refer to the instructions in the text-to-model section

## Multi-view Model Generation Workflow

### 1. Workflow File Download

Download the file below and drag it into ComfyUI to load the corresponding workflow.

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/api_tripo_multiview_to_model.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Json Format Workflow File</p>
</a>

Download the images below as input images

![Front View](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/front.jpg)
![Back View](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/back.jpg)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5c4abf93f36e2ea96202c7cdb92d9917" alt="ComfyUI Tripo Text to Model Step Guide" data-og-width="4474" width="4474" data-og-height="2210" height="2210" data-path="images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=280&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=1652f6fdc87287b6740f8ba562ffe58d 280w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=560&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=dc97a91541029fac8049a1b9d8b54d8b 560w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=840&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f2ff33370148a64dcf2aa4866a3f5e19 840w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=1100&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=e377ddfcb814d22fb8f6254725a9d806 1100w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=1650&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=c8ac321431fb9f399eed6cad35629cd9 1650w, https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?w=2500&fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=701f03c24907864e48309ac5fa5eed11 2500w" />

You can refer to the numbers in the image to complete the basic multi-view to model workflow execution:

1. In the `Load Image` nodes, load the provided input images respectively
2. In the `Tripo: Image to Model` node, modify the corresponding parameter settings
   * model: You can select different models, currently only v1.4 model supports subsequent optimization with `Tripo: Refine Draft model`
   * style: You can set different styles
   * texture\_quality: You can set different texture qualities
3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation. After the workflow completes, the corresponding model will be automatically saved to the `ComfyUI/output/` directory
4. For other view inputs, you can refer to the step diagram and set the corresponding node mode to `Always` to enable it
5. For model download, please refer to the instructions in the text-to-model section

## Subsequent Task Processing for the Same Task

Tripo's corresponding nodes provide subsequent processing for the same task, you only need to input the corresponding `model_task_id` in the relevant nodes, and we have also provided the corresponding nodes in the relevant templates, you can also modify the corresponding node mode as needed to enable it

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ad7966d458e1d327c98d2b21eccdd7a4" alt="Tripo Task Processing" data-og-width="904" width="904" data-og-height="696" height="696" data-path="images/tutorial/api_nodes/tripo/other_nodes.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=de8dda0c9a610962374d6d45ef9ef81b 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=aa635a07bf3de940c377e07e9bb9b323 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=853f4de5683d2adaf09fc590ee0afda1 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b673f11e9724c3bb397d3a13b71fcc47 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=58e9b87b84f3d2edcdda3ce067e52aa1 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=57cc00957d0d65bf950a8ffcf014fc6a 2500w" />

<Error>
  The `Tripo: Refine Draft model` node only supports V1.4 model, other models do not support it
</Error>
