> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Moonvalley API Node Official ComfyUI Example

> This article introduces how to use Moonvalley Partner nodes for text-to-video, image-to-video, and video-to-video capabilities in ComfyUI.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/8Z8X9fFKapQ?si=lK_KFSzDcT0Mepk9" title="ComfyUI Selection Toolbox New Features" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Moonvalley Marey Realism v1.5 is an AI video generation model designed for cinematic-level creation. The model is **trained entirely with commercially licensed content**, ensuring **copyright compliance and commercial safety**.

## Product Highlights

* Exceptional prompt comprehension: Accurately interprets complex prompt instructions.
* Native 1080p HD quality: The training dataset is based on **1080P** videos, resulting in fine and detailed output.
* Realistic physics and dynamic performance: Precisely simulates physical motion models and natural dynamics, delivering professional-grade realism.
* Complex scene layering and advanced lighting effects: Supports foreground, midground, and background layering in complex scenes, with intelligent spatial relationship understanding.
* Production-level control features such as motion and pose transfer: Automatically generates realistic lighting for composite scenes.

Currently, Moonvalley-related Partner nodes are natively supported in ComfyUI. You can use the corresponding text-to-video, image-to-video, and video-to-video capabilities directly in ComfyUI.

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

## Moonvalley Text-to-Video Workflow

### 1. Download the Workflow File

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_text_to_video.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_text_to_video.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download the workflow file in JSON format</p>
</a>

### 2. Follow the Steps to Run the Workflow

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=75dc005efbab705ab95cea22b36f7a24" alt="Text-to-Video Workflow" data-og-width="3160" width="3160" data-og-height="2434" height="2434" data-path="images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=28c9273328f87a89dbd8471160792362 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3b69032638a7e8c21f48648587263ba 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=44a6909ce38a300f0fb289592229a7c1 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b1ace57a8eff4446f831b6348c37abd5 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=27e34daf102a1d0866aa937a2c6dd780 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=415c88b1d9a8b5bfbbefefa19e50bc2a 2500w" />

1. Enter the positive prompt (content you want to appear in the video)
2. Enter the negative prompt (content you do not want to appear in the video)
3. Modify the video output resolution
4. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to start video generation
5. After the API returns the result, you can view the generated video in the `Save Video` node. The video will also be saved in the `ComfyUI/output/` directory

## Moonvalley Image-to-Video Workflow

### 1. Download the Workflow File

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download the workflow file in JSON format</p>
</a>

Download the image below as the input image

![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video_input.webp)

### 2. Follow the Steps to Run the Workflow

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9467e0f19d709f9b77cc4778a97f04a8" alt="Image-to-Video Workflow" data-og-width="3966" width="3966" data-og-height="1350" height="1350" data-path="images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=15f722730ad8914c66953fd80343c68b 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=09c1e830f9a49d385496d720fa9cc2f8 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=75d4f6b4f7f6774e696c8c66b5b5fdaf 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f2835d3b2719b0738ef0fb005be0d919 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=467702de371d0a5f4f2069313bef68b2 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3e79e56ce7f9516a5ab105dfb47aa4c9 2500w" />

1. Load the input image in the `Load Image` node
2. Enter the positive prompt (content you want to appear in the video)
3. Enter the negative prompt (content you do not want to appear in the video)
4. Modify the video output resolution
5. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to start video generation
6. After the API returns the result, you can view the generated video in the `Save Video` node. The video will also be saved in the `ComfyUI/output/` directory

## Moonvalley Video-to-Video Workflow

The `Moonvalley Marey Video to Video` node allows you to input a reference video for video re-drawing. You can use the reference video's motion or character poses for video generation.

### 1. Download the Workflow File

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_video_to_video.mp4" />

<a className="prose" target="_blank" href="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_video_to_video.json" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download the workflow file in JSON format</p>
</a>

Download the video below as the input video:

<video controls className="w-full aspect-video" src="https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_video_to_video_input.mp4" />

### 2. Follow the Steps to Run the Workflow

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ee9e202bdc9a3b39c8dc6ba5b10577b5" alt="Video-to-Video Workflow" data-og-width="3966" width="3966" data-og-height="1350" height="1350" data-path="images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=cf6664f2196ff60462c2d1d28003eea5 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=77a0cd776ba0564f497915231d13f1cb 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0d6f58d692e5dcfc16703a678c3621dd 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=91f3ea51b33634ed0c54c1b1501bf7f0 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=99f1bfd447b88531d16c38c55b9aadeb 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=82f6b3a3c04808d4f5d5997b3dc53bc6 2500w" />

1. Load the reference video (or your own material) in the `Load Video` node
   * If the final video duration is 5s, the input video must be longer than 5s
   * If the final video duration is 10s, the input video must be longer than 10s
2. Enter the positive prompt (content you want to appear in the video)
3. Enter the negative prompt (content you do not want to appear in the video)
4. Set the `control_type` parameter to choose the reference type for video re-drawing
   * `Motion Transfer`: Generate based on the motion in the reference video
   * `Pose Transfer`: Generate based on the character poses in the reference video
5. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to start video generation
6. After the API returns the result, you can view the generated video in the `Save Video` node. The video will also be saved in the `ComfyUI/output/` directory
