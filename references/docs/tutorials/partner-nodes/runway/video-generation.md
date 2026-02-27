> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Runway API Node Video Generation ComfyUI Official Example

> This article will introduce how to use Runway nodes in ComfyUI for video generation workflows

Runway is a company focused on generative AI, providing powerful video generation capabilities. Currently, ComfyUI has integrated the Runway API, allowing you to directly use the related nodes in ComfyUI for video generation.

Currently, ComfyUI natively integrates the following Runway video generation models:

* Runway Gen3a turbo
* Runway Gen4 turbo
* Runway First Last Frame to video

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

## Gen3a turbo Image-to-Video Workflow

### 1. Workflow File Download

The video below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow.

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen3a_turbo_image_to_video/runway_image_to_video_gen3a_turbo.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen3a_turbo_image_to_video/runway_image_to_video_gen3a_turbo.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Json Format Workflow File</p>
</a>

Download the image below as input image

![ComfyUI Runway gen3a turbo image to video Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen3a_turbo_image_to_video/steampunk.png)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c173269c427a4c3fcc08f5b0ead4ffab" alt="ComfyUI Runway gen3a turbo image to video Step Guide" data-og-width="2202" width="2202" data-og-height="1188" height="1188" data-path="images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0a59187c4a18d53b4568d662092f12de 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=23df8ac507adbadca3e4e49883e7ce8b 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=5c511ccab9bbfdde11116edfe184999b 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=770b47e6170450ce300b163f8ed77ccc 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=58f31be12e93ece370302cae526092a9 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen3a_turbo_image_to_video_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3ced3310fde20979a1159def906fa388 2500w" />

You can refer to the numbers in the image to complete the basic image-to-video workflow execution:

1. In the `Load Image` node, load the provided input image
2. In the `Runway Gen3a turbo` node, set the `prompt` to describe video content, modify the `duration` parameter to set video length, modify the `ratio` parameter to set video aspect ratio
3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.
4. After waiting for the API to return results, you can view the generated video in the `Save Video` node (right-click to save). The corresponding video will also be saved to the `ComfyUI/output/` directory.

## Gen4 turbo Image-to-Video Workflow

### 1. Workflow File Download

The video below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow.

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/runway_gen4_turo_image_to_video.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/runway_gen4_turo_image_to_video.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Json Format Workflow File</p>
</a>

Download the image below as input image

![ComfyUI Runway gen4 turbo image to video Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/godfather.jpg)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1c2df6f00cd1a0fc221a058621cd1449" alt="ComfyUI Runway gen4 turbo image to video Step Guide" data-og-width="2202" width="2202" data-og-height="1152" height="1152" data-path="images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=676ee2e7986565c3e482f153871858de 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=49184313bdcc3931cfdf6aec01fd7170 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=11dc5ed72c9e578e83484ff3a24ed8f3 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ada028966a71fed3c695a5fafc5ba08b 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9344d3b599961ce42bd43e7f5a9dd23f 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=81a52c64571c1a3c61410e63f9183a72 2500w" />

You can refer to the numbers in the image to complete the basic image-to-video workflow execution:

1. In the `Load Image` node, load the provided input image
2. In the `Runway Gen4 turbo` node, set the `prompt` to describe video content, modify the `duration` parameter to set video length, modify the `ratio` parameter to set video aspect ratio
3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.
4. After waiting for the API to return results, you can view the generated video in the `Save Video` node (right-click to save). The corresponding video will also be saved to the `ComfyUI/output/` directory.

## First-Last Frame Video Generation Workflow

### 1. Workflow File Download

The video below contains workflow information in its `metadata`. Please download and drag it into ComfyUI to load the corresponding workflow.

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/first_last_frame_to_video/runway_first_last_frame.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/first_last_frame_to_video/runway_first_last_frame.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download Json Format Workflow File</p>
</a>

Download the images below as input images

![ComfyUI Runway gen4 turbo image to video Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/first_last_frame_to_video/first.jpg)
![ComfyUI Runway gen4 turbo image to video Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/first_last_frame_to_video/last.jpg)

### 2. Complete the Workflow Execution Step by Step

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4cf592284e4ef7d48a1780e10483f03c" alt="ComfyUI Runway gen4 turbo image to video Step Guide" data-og-width="2082" width="2082" data-og-height="1154" height="1154" data-path="images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d39249726e6ff98915ca48dbd010c81e 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ad3e00b1647cfa32b12682f69ecc004d 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0570bf102ba92d8b823caf6cf604126f 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d969338e625f09c6e54a07eb5c6f1ce1 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bcd44d0a555ee1c9893d5ddb154f1266 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_first_last_frame_step_guide.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cb6a1b59c2f2904f1c7d7e0fdcde23d0 2500w" />

You can refer to the numbers in the image to complete the basic first-last frame to video workflow execution:

1. In the `Load Image` node, load the starting frame
2. In the `Load Image` node, load the ending frame
3. In the `Runway First-Last-Frame to Video` node, set the `prompt` to describe video content, modify the `duration` parameter to set video length, modify the `ratio` parameter to set video aspect ratio
4. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.
5. After waiting for the API to return results, you can view the generated video in the `Save Video` node (right-click to save). The corresponding video will also be saved to the `ComfyUI/output/` directory.
