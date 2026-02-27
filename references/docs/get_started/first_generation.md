> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with AI Image Generation

> This tutorial will guide you through your first image generation with ComfyUI, covering basic interface operations like workflow loading, model installation, and image generation

This guide aims to help you understand ComfyUI's basic operations and complete your first image generation. We'll cover:

1. Loading example workflows
   * Loading from ComfyUI's workflow templates
   * Loading from images with workflow metadata
2. Model installation guidance
   * Automatic model installation
   * Manual model installation
   * Using ComfyUI Manager for model installation
3. Completing your first text-to-image generation

## About Text-to-Image

Text-to-Image is a fundamental AI drawing feature that generates images from text descriptions. It's one of the most commonly used functions in AI art generation. You can think of the process as telling your requirements (positive and negative prompts) to an artist (the drawing model), who will then create what you want. Detailed explanations about text-to-image will be covered in the [Text to Image](/tutorials/basic/text-to-image) chapter.

## ComfyUI Text-to-Image Workflow Tutorial

### 1. Launch ComfyUI

Make sure you've followed the [installation guide](/installation/system_requirements) to start ComfyUI and can successfully enter the ComfyUI interface. Alternatively, you can use [Comfy Cloud](/get_started/cloud) to use ComfyUI without any installation.

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8d74bbaaf16e92f0e41fbf446bce8655" alt="ComfyUI Interface" data-og-width="1068" width="1068" data-og-height="819" height="819" data-path="images/interface/comfyui-boot-screen.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5cb9199e3321fff7ad0f3d05b98b5fb0 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d8079eb6460f02357a19daf916789cca 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8f430035873b1af54fbefe18ccb7f89f 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=901fc46444d049a7c309f3d3dde04168 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=74ef473885ed787270cdba6b753ec96b 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/comfyui-boot-screen.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=eb273ff76ed49bc91d290de3db733468 2500w" />

If you have not installed ComfyUI, please choose a suitable version to install based on your device.

<AccordionGroup>
  <Accordion title="ComfyUI Desktop">
    ComfyUI Desktop currently supports standalone installation for **Windows and MacOS (ARM)**, currently in Beta

    * Code is open source on [Github](https://github.com/Comfy-Org/desktop)

    <Tip>
      Because Desktop is always built based on the **stable release**, so the latest updates may take some time to experience for Desktop, if you want to always experience the latest version, please use the portable version or manual installation
    </Tip>

    You can choose the appropriate installation for your system and hardware below

    <Tabs>
      <Tab title="Windows">
        <Card title="ComfyUI Desktop (Windows) Installation Guide" icon="link" href="/installation/desktop/windows">
          Suitable for **Windows** version with **Nvidia** GPU
        </Card>
      </Tab>

      <Tab title="MacOS(Apple Silicon)">
        <Card title="ComfyUI Desktop (MacOS) Installation Guide" icon="link" href="/installation/desktop/macos">
          Suitable for MacOS with **Apple Silicon**
        </Card>
      </Tab>

      <Tab title="Linux">
        <Note>ComfyUI Desktop **currently has no Linux prebuilds**, please visit the [Manual Installation](/installation/manual_install) section to install ComfyUI</Note>
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="ComfyUI Portable (Windows)">
    Portable version is a ComfyUI version that integrates an independent embedded Python environment, using the portable version you can experience the latest features, currently only supports **Windows** system

    <Card title="ComfyUI Portable (Windows) Installation Guide" icon="link" href="/installation/comfyui_portable_windows">
      Supports **Windows** ComfyUI version running on **Nvidia GPUs** or **CPU-only**, always use the latest commits and completely portable.
    </Card>
  </Accordion>

  <Accordion title="Manual Installation">
    <Card title="ComfyUI Manual Installation Guide" icon="link" href="/installation/manual_install">
      Supports all system types and GPU types (Nvidia, AMD, Intel, Apple Silicon, Ascend NPU, Cambricon MLU)
    </Card>
  </Accordion>
</AccordionGroup>

### 2. Load Default Text-to-Image Workflow

ComfyUI usually loads the default text-to-image workflow automatically when launched. However, you can try different methods to load workflows to familiarize yourself with ComfyUI's basic operations:

<Tabs>
  <Tab title="Load from Workflow Template">
    <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9d27e08e27b8eb3d201b83f9e310fcf1" alt="ComfyUI Interface" data-og-width="973" width="973" data-og-height="696" height="696" data-path="images/tutorial/gettingstarted/first-image-generation-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b8fcf7b9cf036e830c80d5c7d08277eb 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=024bfa97dcc43a5544614536571f6cfa 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=bbf0c3c26374de9f92be8dcf2c010623 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=135c10c9218d1e205c7d14a0648e20ab 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=04b75e491e8734279e7e595b8ad8557f 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8a40678cb2b4ceb856ddc3d2e867b372 2500w" />
    Follow the numbered steps in the image:

    1. Click the **Fit View** button in the bottom right to ensure any loaded workflow isn't hidden
    2. Click the **folder icon (workflows)** in the sidebar
    3. Click the **Browse example workflows** button at the top of the Workflows panel

    Continue with:
    <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=95604069c95b98aaaecfac6141eadadc" alt="Load Workflow" data-og-width="972" width="972" data-og-height="692" height="692" data-path="images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0eb0a67fc3fe9e9cb951fd92fa871e7e 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d6180ba2452c01eda59a52e8f1af7446 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=493e05c8c000d4d44b963afa6c6b968c 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fe206a76045f658b209d05463f414363 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=99d1dd62a0ef8e5296477f8cbecb47e6 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-2-load-workflow.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6f939111ff708e666db1c331f608c22f 2500w" />

    4. Select the first default workflow **Image Generation** to load it

    Alternatively, you can select **Browse workflow templates** from the workflow menu
    <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=bbc70cd0f990a2674b9db9d6f080e026" alt="ComfyUI Menu - Browse Workflow Templates" data-og-width="612" width="612" data-og-height="536" height="536" data-path="images/tutorial/gettingstarted/first-image-generation-1-menu.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=08dbdd225603ece1d7d92b70c4ca5bd6 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=94951273209435d7e744f8354364f51d 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=cae53710d2bcbb862a75bdd5218cfb44 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=692cf88d6cf8868d898c2d7450e90cf6 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8368d39fd5611a52749df6d66260c766 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-1-menu.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ced69fca7e53b06aa1b36d1067aa75a0 2500w" />
  </Tab>

  <Tab title="Load from Images with Metadata">
    All images generated by ComfyUI contain metadata including workflow information. You can load workflows by:

    * Dragging and dropping a ComfyUI-generated image into the interface
    * Using menu **Workflows** -> **Open** to open an image

    Try loading the workflow using this example image:
    ![ComfyUI-Text to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/text-to-image-workflow.png)
  </Tab>

  <Tab title="Load from workflow.json">
    ComfyUI workflows can be stored in JSON format. You can export workflows using menu **Workflows** -> **Export**.

    Try downloading and loading this example workflow:

    <a className="prose" href="https://github.com/Comfy-Org/docs/blob/main/public/text-to-image.json" download style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
      <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download text-to-image.json</p>
    </a>

    After downloading, use menu **Workflows** -> **Open** to load the JSON file.
  </Tab>
</Tabs>

### 3. Model Installation

Most ComfyUI installations don't include base models by default. After loading the workflow, if you don't have the [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) model installed, you'll see this prompt:

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=631b68f7fd227245f032c1837b6e44e7" alt="Missing Models" data-og-width="972" width="972" data-og-height="696" height="696" data-path="images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=bf07d8fa6107520f408460032a331d0a 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=04d7ecb43ff2b94040742a31b9dc621b 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=103f5bf2c1bfaf50c9b4084d84a8e9a7 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=005a3b038883b9c372080cfa0bb770fc 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=11adbcce9945ab8aac33ad7b8c509417 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-3-missing-models.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c0ec6fab2f0449810fef6a376da685e0 2500w" />

All models are stored in `<your ComfyUI installation>/ComfyUI/models/` with subfolders like `checkpoints`, `embeddings`, `vae`, `lora`, `upscale_model`, etc. ComfyUI detects models in these folders and paths configured in `extra_model_paths.yaml` at startup.

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9715b090919f665331e3500712d5e9e7" alt="ComfyUI Models Folder" data-og-width="1564" width="1564" data-og-height="1228" height="1228" data-path="images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=657fd94230a1a7796906339c48b8c3b0 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7d884de0fc538ab8ef00c14da507b9a8 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=31938fcc781769c8fabc60ddef58363a 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b005cfc130ac988cf28f8ceb7315596b 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=dc0ae8e2a2f2ffaf7c63c57316b6fde1 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-models-folder.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d0ee5cb2437d9ea25cab05dca82d81d0 2500w" />

You can install models through:

<Tabs>
  <Tab title="Automatic Download">
    After you click the **Download** button, ComfyUI will execute the download, and different behaviors will be performed depending on the version you are using.

    <Tabs>
      <Tab title="ComfyUI Desktop">
        The desktop version will automatically complete the model download and save it to the `<your ComfyUI installation location>/ComfyUI/models/checkpoints` directory.
        You can wait for the installation to complete or view the installation progress in the model panel on the sidebar.

                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=850acf678de82f1358fd230347f41a86" alt="Model Download Progress" data-og-width="974" width="974" data-og-height="697" height="697" data-path="images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=54a28a5d0739ccec1b41f6def3f88ddb 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5f210d81700174972dacef081a56659d 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c4b78e4ac1b98ebc33d5f3e6285f10bb 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2b3167deb99fcd5ba3b01dfb25b9ff69 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9718f43183df17023ccccb41a6fb8ffa 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-download-status.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6084de5bb78eb5956a497389383512f0 2500w" />

        If everything goes smoothly, the model should be able to download locally. If the download fails for a long time, please try other installation methods.
      </Tab>

      <Tab title="ComfyUI Portable">
        The browser will execute file downloads. Please save the file to the `<your ComfyUI installation location>/ComfyUI_windows_portable/ComfyUI/models/checkpoints` directory after the download is complete.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="ComfyUI Manager">
    ComfyUI Manager is a tool for managing custom nodes, models, and plugins.

    <Steps>
      <Step title="Open ComfyUI Manager">
                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=63bea93b65f4aa69499343eaa8f8fa3d" alt="ComfyUI Manager Installation" data-og-width="492" width="492" data-og-height="124" height="124" data-path="images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3960c57be9777c85e7704ed7d838f389 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=cf45c060e2e6e2d9c7ac9de6071b3004 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=0fbccad434fdbadf7951372cf2e674db 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=2ca5b357da7a0163b274c3eadddd04d8 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fd74e46709d4bd2e573aa79ea66e0daf 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=4238a1c13094c4e16f7f976a1375d1bb 2500w" />

        Click the `Manager` button to open ComfyUI Manager
      </Step>

      <Step title="Open Model Manager">
                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f263705f288d59e181c4fbd5d2ce8077" alt="ComfyUI Manager Model Management" data-og-width="1200" width="1200" data-og-height="723" height="723" data-path="images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=1ba12adec58d6664a2222b80db97254b 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d6d2feadaf68a0fcca57333e1dc4cfe2 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a3eae65d43bf4d9e1dc1827f3611fafd 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3d54457cd8213afd45d728a38d665d57 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=443471cc0f938f916d96aa1213db34e9 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-model-manager.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6e3e020446ebe6a348aec7239811d4e4 2500w" />

        Click `Model Manager`
      </Step>

      <Step title="Search and Install Model">
                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3af1349a1b3a91b680030d3511a53695" alt="ComfyUI Manager Model Download" data-og-width="1200" width="1200" data-og-height="723" height="723" data-path="images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7963c563d6ac8d95b2c043623dd21660 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fa757c67c6889c30975d0611159a9151 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d5f1855f2d8dd89899b781fe4116d3c0 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=397a777a3c91325e5c9ec95a5d268271 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=18ade34b5f43a854f7296f6a90ed4b65 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-4-comfyui-manager-download-model.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f209b1b10e09c634cd1d5ffe45ce7cfa 2500w" />

        1. Search for `v1-5-pruned-emaonly.ckpt`
        2. Click `install` on the desired model
      </Step>
    </Steps>
  </Tab>

  <Tab title="Manual Installation">
    Visit [v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) and follow this guide:

        <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=15c2560c44e7e4276b6a351809f7bf9f" alt="Hugging Face Model Download" data-og-width="769" width="769" data-og-height="727" height="727" data-path="images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8a0a11ce09344e6137d0318c4b3b9719 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8089b1a5012ff008f26ebec351eab046 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c7d903b4cfd6ac8e1104f577d865f8b1 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e712597b7d24bbb7564c0b50e7a073de 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a96dc866b2123b98a2addbe33920543b 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=31971d485c7495f4f71baf350f1b83cc 2500w" />

    Save the downloaded file to:

    <Tabs>
      <Tab title="ComfyUI Desktop">
        Save to `<your ComfyUI installation>/ComfyUI/models/checkpoints`

                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=275add7233b1f048455cff0f162847b9" alt="ComfyUI Desktop Model Save Location" data-og-width="911" width="911" data-og-height="710" height="710" data-path="images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9bde4750c8ff36b3c64bc610ebb05b57 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e3340ae124d7239717afe84315d6079d 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=27da936e2e5be7f615411a89244732bc 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=cd6a3d90f78767506c30deb0c36e8170 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=390a871fda8ffe2debbe8da45f6d93ab 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fe78a0f9c474924a916a57c8a02348e7 2500w" />
      </Tab>

      <Tab title="ComfyUI Portable">
        Save to `ComfyUI_windows_portable/ComfyUI/models/checkpoints`

                <img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=48976b87bcfdba962b119d901c43b286" alt="ComfyUI Portable Model Save Location" data-og-width="1081" width="1081" data-og-height="709" height="709" data-path="images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e24f9a271a0aea30a444c519a4991c48 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d2a219d501d98acbc88eb4ef0a3da736 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=c49908bc31bf6c82e47138199558e74e 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b66628ad620d7ba1a77d824804d68660 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e41817dee653258bf714a83e29edcede 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=49379cc7f2f8c0c359a6e97a93d091ad 2500w" />
      </Tab>
    </Tabs>

    Refresh or restart ComfyUI after saving.
  </Tab>
</Tabs>

### 4. Load Model and Generate Your First Image

After installing the model:

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e0c8f5d7af48afa25076309392f02129" alt="Image Generation" data-og-width="2640" width="2640" data-og-height="1384" height="1384" data-path="images/tutorial/gettingstarted/first-image-generation-7-queue.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a2c75afbbad046faedacdc0d49847785 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=51baad1b8a08a3d07956f62cf18b11b5 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=b414fc5ca9f56a55bc317bfc9a6bc445 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=16fff107aa1c88d7772c01adae99430f 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=3e6a2c94b9760ea8e4ca615a4d2be760 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-7-queue.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=d8b83b791ae3a2cc979326454d6cc654 2500w" />

1. In the **Load Checkpoint** node, ensure **v1-5-pruned-emaonly-fp16.safetensors** is selected
2. Click `Queue` or press `Ctrl + Enter` to generate

The result will appear in the **Save Image** node. Right-click to save locally.

<img src="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=92b100190dd8f91abb37b01cc2e09a59" alt="ComfyUI First Image Generation Result" data-og-width="2642" width="2642" data-og-height="1390" height="1390" data-path="images/tutorial/gettingstarted/first-image-generation-8-result.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=280&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=f0c2219d45e70c2f21ebd64032fddb50 280w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=560&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=9391713ee886380f8302e396975a94aa 560w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=840&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=ace21872a174725c45788b7ce5ce8a34 840w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=1100&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=a579037cd0b65cd2115280f8eee6e80b 1100w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=1650&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8dba16d2de187f3f6356af67ee1040ef 1650w, https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-8-result.jpg?w=2500&fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=adfc35ce5d546ca79f140b45dee3fe2d 2500w" />

For detailed text-to-image instructions, see our comprehensive guide:

<Card title="ComfyUI Text-to-Image Workflow Guide" icon="link" href="/tutorials/basic/text-to-image">
  Click here for detailed text-to-image workflow instructions
</Card>

## Troubleshooting

### Model Loading Issues

If the `Load Checkpoint` node shows no models or displays "null", verify your model installation location and try refreshing or restarting ComfyUI.
