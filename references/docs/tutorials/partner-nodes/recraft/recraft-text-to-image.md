> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Recraft Text to Image API Node ComfyUI Official Example

> Learn how to use the Recraft Text to Image Partner node in ComfyUI

The [Recraft Text to Image](/built-in-nodes/partner-node/image/recraft/recraft-text-to-image) node allows you to create high-quality images in various styles using Recraft AI's image generation technology based on text descriptions.

In this guide, we'll show you how to set up a text-to-image workflow using this node.

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

## Recraft Text to Image API Node Workflow

### 1. Download the Workflow File

The workflow information is included in the metadata of the image below. Download and drag it into ComfyUI to load the workflow.

![Recraft Text to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/recraft/t2i/recraft_t2i.png)

### 2. Follow the Steps to Run the Workflow

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=26e3744a4e7c44a1d72840e8ffef5c3c" alt="Recraft Text to Image Workflow Steps" data-og-width="2822" width="2822" data-og-height="1505" height="1505" data-path="images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=dc89e07d6e583587d024f85b99626261 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=10cce0cedd135dbfef4efe38ea61eeab 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=46b3c2bbad43ffa402380f256c2e899d 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4617e18965b44fb37f0c6652a1b8961c 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=02b68dffb02846a5793b0487a2a34173 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b341b7afdec336aabccf223c6312f31f 2500w" />

Follow these numbered steps to run the basic workflow:

1. (Optional) Change the `Recraft Color RGB` in the `Color` node to your desired color
2. (Optional) Modify the `Recraft Style` node to control the visual style, such as digital art, realistic photo, or logo design. This group includes other style nodes you can enable as needed
3. (Optional) Edit the `prompt` parameter in the `Recraft Text to Image` node. You can also change the `size` parameter
4. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to generate the image
5. After the API returns the result, you can view the generated image in the `Save Image` node. The image will also be saved to the `ComfyUI/output/` directory

> (Optional) We've included a **Convert to SVG** group in the workflow. Since the `Recraft Vectorize Image` node in this group consumes additional credits, enable it only when you need to convert the generated image to SVG format

### 3. Additional Notes

* **Recraft Style**: Offers various preset styles like realistic photos, digital art, and logo designs
* **Seed Parameter**: Only used to determine if the node should run again, the actual generation result is not affected by the seed value

## Related Node Documentation

Check the following documentation for detailed parameter settings of the nodes

<Card title="Recraft Text to Image Node Documentation" icon="book" href="/built-in-nodes/partner-node/image/recraft/recraft-text-to-image">
  Documentation for the Recraft Text to Image Partner node
</Card>

<Card title="Recraft Style Node Documentation" icon="book" href="/built-in-nodes/partner-node/image/recraft/recraft-style-realistic-image">
  Documentation for the Recraft Style - Realistic Image Partner node
</Card>

<Card title="Recraft Controls Node Documentation" icon="book" href="/built-in-nodes/partner-node/image/recraft/recraft-controls">
  Documentation for the Recraft Controls Partner node
</Card>
