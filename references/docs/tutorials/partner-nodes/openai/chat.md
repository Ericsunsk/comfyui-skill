> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Chat API Node ComfyUI Official Example

> This article will introduce how to use OpenAI Chat Partner nodes in ComfyUI to complete conversational functions

OpenAI is a company focused on generative AI, providing powerful conversational capabilities. Currently, ComfyUI has integrated the OpenAI API, allowing you to directly use the related nodes in ComfyUI to complete conversational functions.

In this guide, we will walk you through completing the corresponding conversational functionality.

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

## OpenAI Chat Workflow

### 1. Workflow File Download

Please download the Json file below and drag it into ComfyUI to load the corresponding workflow.

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/openai/api_openai_chat.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Json Format Workflow File</p>
</a>

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a101638c18cc6656457c72f47bf0307c" alt="OpenAI Chat Step Guide" data-og-width="3834" width="3834" data-og-height="2148" height="2148" data-path="images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=fa3d9c490702f1376543a6d1717c117d 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f0072e6b06444e5be5b5d1a146458ef6 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c7febc5dd35adb937dd39a3771da0559 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cfdd9933ef732e40cdf1ac7bbd91a39f 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8343e98d4e6ad3f5edc919136c681cd1 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=62799060fa2a14fdbc8980dca0fe45a7 2500w" />

<Note>
  In the corresponding template, we have built a role setting for analyzing prompt generation.
</Note>

You can refer to the numbers in the image to complete the basic text-to-image workflow execution:

1. In the `Load Image` node, load the image you need AI to interpret
2. (Optional) If needed, you can modify the settings in `OpenAI Chat Advanced Options` to have AI execute specific tasks
3. In the `OpenAI Chat` node, you can modify `Prompt` to set the conversation prompt, or modify `model` to select different models
4. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute the conversation.
5. After waiting for the API to return results, you can view the corresponding AI returned content in the `Preview Any` node.

### 3. Additional Notes

* Currently, the file input node `OpenAI Chat Input Files` requires files to be uploaded to the `ComfyUI/input/` directory first. This node is being improved, and we will modify the template after updates
* The workflow provides an example using `Batch Images` for input. If you have multiple images that need AI interpretation, you can refer to the step diagram and use right-click to set the corresponding node mode to `Always` to enable it
