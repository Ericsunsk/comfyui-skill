> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Install Custom Nodes in ComfyUI

> This guide will show you different methods to install custom nodes in ComfyUI

## What are Custom Nodes ?

Custom nodes are extensions for ComfyUI that add new functionality like advanced image processing, machine learning fine-tuning, color adjustments, and more. These community-developed nodes can significantly expand ComfyUI's core capabilities.

<Warning>
  Before installing custom nodes, it's important to review them carefully. Since ComfyUI is an open-source project, malicious plugins could potentially exploit custom nodes:

  1. Only install custom nodes from trusted authors and those commonly used by the community
  2. Understand the plugin's functionality before installing and avoid unknown sources to ensure system security
  3. Avoid installing obscure or suspicious plugins - unverified plugins may pose security risks that could lead to system compromise
</Warning>

All custom node installations require completing these two steps:

1. Clone the node code to the `ComfyUI/custom_nodes` directory
2. Install the required Python dependencies

This guide covers three installation methods. Here's a comparison of their pros and cons. While [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager) isn't yet part of the core dependencies, it will be in the future. We still provide other installation guides to meet different needs.

| Method                            | Advantages                                                                  | Disadvantages                                                                           |
| --------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **ComfyUI Manager** (Recommended) | 1. Automated installation<br />2. Dependency handling<br />3. GUI interface | Cannot directly search for nodes not registered in the registry                         |
| **Git Clone**                     | Can install nodes not registered in the registry                            | 1. Requires Git knowledge<br />2. Manual dependency handling<br />3. Installation risks |
| **Repository ZIP Download**       | 1. No Git required<br />2. Manual control                                   | 1. Manual dependency handling<br />2. No version control<br />3. Installation risks     |

Tip: Before installing custom nodes, check the plugin's README file to understand installation methods, usage, and requirements like specific models, dependency versions, and common issue solutions.

## Method 1: ComfyUI Manager (Recommended)

<Steps>
  <Step title="Click the `Manager` button in ComfyUI interface">
        <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-1.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c9ea2c5459becf2073564c99d5918ebd" alt="Click ComfyUI Manager" data-og-width="2000" width="2000" data-og-height="1250" height="1250" data-path="images/installation/custom_nodes/install-custom-nodes-by-manager-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-1.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=7973b4e0e017ffb16d264d4231536aee 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-1.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=86d4657014cdf4b1cfbce57188ce5575 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-1.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=7788731e9e63f200a9f95aee0019ffb8 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-1.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5f747b98ad3ca8a8c1a2d04cde58bd33 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-1.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=6ad5eacec17533604fa9150ada34d639 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-1.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=caacb306d394a006d78fd81cf2c0d231 2500w" />
  </Step>

  <Step title="Select `Install Custom Nodes`">
        <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-2.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=51a2fb20415d6fc9a2efae30b5801e4f" alt="Select Install Custom Nodes" data-og-width="2000" width="2000" data-og-height="1250" height="1250" data-path="images/installation/custom_nodes/install-custom-nodes-by-manager-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-2.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=cc2be0d13ff5c434f3a52d5387f9e276 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-2.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=6b1d53ffaed9f5ff3f97060c03de113f 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-2.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ff47226ca76ea50b41cc8b171875355b 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-2.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=74a3ce868907f913b2b4fec034d59752 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-2.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d596a8b3a9913edd910657e82208fecb 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-2.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c46471859d7b8f02c1c154e1411cdf6b 2500w" />
  </Step>

  <Step title="Browse the custom nodes list">
    <Warning>
      Custom nodes listed in ComfyUI Manager aren't necessarily safe. Understand their functionality before installing and ensure you only install trusted plugins and those from popular authors to avoid potential device risks.
    </Warning>

    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-3.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=3bf04620a7efb24a3559116c8b3e2c1c" alt="Enter node name in search box" data-og-width="2000" width="2000" data-og-height="1250" height="1250" data-path="images/installation/custom_nodes/install-custom-nodes-by-manager-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-3.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=2c306cff6c8576ea6f2485633aa55b14 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-3.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ca91d3a1610076758cafac993e735a8b 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-3.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=eda0750485ba62521d0999b2b769d9bb 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-3.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4aabed0ad5c07b93d2dfbf50c8be53a4 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-3.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=2c5d76bb1df8f33797517854389087bf 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-3.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=797bf30cc03e28f867266a9072336818 2500w" />
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-4.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=61bc2c04fad5a918678885c156c7aadc" alt="Enter node name in search box" data-og-width="2000" width="2000" data-og-height="1250" height="1250" data-path="images/installation/custom_nodes/install-custom-nodes-by-manager-4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-4.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4ac1a60bb52edb26c0fe3784aedfd38d 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-4.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=646ac9473cb0be4e3c4579ba0ec07cb2 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-4.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=815f9b634b2843044bf32b9414b5024e 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-4.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8e6e3308fd597a943890fa6f36b6dcd6 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-4.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=dea18ed9554ac7a83d72016f028ad502 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-4.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ff321f2dcf95634ded67bda9f20dd01b 2500w" />

    1. Nodes marked with `⚠️` may have dependency conflicts with other plugins
    2. Author names marked with `✅` indicate their activity level on Github
    3. Potential plugin risks are highlighted in red - ensure plugin safety before installing
  </Step>

  <Step title="Click the `Install` button for the desired node">
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-5.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=2ab49bbc1cbc8afa55b3fc422827944e" alt="Click Install button for the node" data-og-width="2000" width="2000" data-og-height="1250" height="1250" data-path="images/installation/custom_nodes/install-custom-nodes-by-manager-5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-5.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=8f09eb71acbc2e828d90380272ecdbfa 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-5.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=daeee4413d5d46d6c7b6039bee0c3d40 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-5.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=757702fffa5d8d24b407ddb49f7dada8 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-5.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=3410efa332227612ce41abb59b51eb08 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-5.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=38f5cd193a5c609bf316ba8e99747ce6 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-5.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=6a13aabe76c4e9a3b2a92750b7f5e1eb 2500w" />
    Find the node you want to install and click the `Install` button.
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-6.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=79795d6c93adadebc01ee7c96f51b1ec" alt="Click Install button for the node" data-og-width="2000" width="2000" data-og-height="1250" height="1250" data-path="images/installation/custom_nodes/install-custom-nodes-by-manager-6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-6.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=356cb779b432f7f223b4ae5b87a09b74 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-6.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=e49670f42e4a9d28fb86b1618d6f5a22 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-6.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0127ddc9a66b8cc898e8b88ea59106e5 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-6.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4333ddc04205376867748812a67ec894 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-6.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=6302c261b567801b4aa0e83afca878bf 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-6.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=855555e64d068cb33da523c1798fd8e2 2500w" />

    * At this step, if you select the `nightly` version, it will directly download the latest source code of the plugin from Github. However, if your Manager's `security_level` is set to `normal`, you will not be allowed to download the source code directly from Github because the code has not been scanned.
    * If you select other versions such as `latest` or a stable version with a number, the code will be downloaded from [https://registry.comfy.org/](https://registry.comfy.org/), which means the code has been reviewed and will not trigger a security check.

    <Tip>
      The `nightly` version is usually the latest version, but since it is downloaded directly from Github and has not been reviewed, there is a certain code risk. If you really need to install the `nightly` version, please set the Manager's `security_level` to `weak`.
      The configuration file path is `ComfyUI/user/default/ComfyUI-Manager/config.ini`. Please note that this is not our recommended configuration and should only be used temporarily.
    </Tip>
  </Step>

  <Step title="Wait for dependencies to install and restart ComfyUI">
    Manager will automatically install dependencies and prompt you to restart ComfyUI when complete
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0d0a41967984241d0cd9f91718142abc" alt="Restart ComfyUI and refresh browser after installation" data-og-width="2000" width="2000" data-og-height="1254" height="1254" data-path="images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5ae436ee875468dc5f1d4727b66f70bd 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5a198fbad24a062929a2cc1a7b924596 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=b6c1a6fc5dd012db17980a281ca58c0f 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=a2bc2a9c52f1ac9ddb409bd387d66e34 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ee878686926d5099aef5727fa34e95ab 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=951407671177ea4bf96d7824a455a562 2500w" />
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4fabdae56e5d3dc110b9bc69a0dc78f8" alt="Restart ComfyUI and refresh browser after installation" data-og-width="2000" width="2000" data-og-height="1250" height="1250" data-path="images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d0f0c66addb3f7de935c87d8aeb1628f 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=9b2e3cc35941dcc21dd553c24214a86d 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=6b8efb4032e1f39facc208b46938eeca 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=28d897239a624c71b9e54fb4198f8642 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5e244ed42d1f9085ae8e78949f88560f 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=9050141993949c95bf9b2c9ee69db2a9 2500w" />
  </Step>

  <Step title="Verify successful installation">
    Check ComfyUI Manager after restart to confirm the plugin installed successfully and there are no `import failed` errors
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c1d9fa38bbfe862ae661177e2948599c" alt="Restart ComfyUI and refresh browser after installation" data-og-width="2000" width="2000" data-og-height="1250" height="1250" data-path="images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c6b7124e5fd11e68b1c95b37c1100de9 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=cb41de584815df2118164653fd0504b9 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ca524bc5f88a01c26d4c6829304c7001 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=96e49901b2fb537edd6dd882e3a97d8c 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=dae8ce344a3ffea691fa672188b0515b 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ae8c5e0c1e02413a587b1bb042815c4f 2500w" />
  </Step>
</Steps>

## Method 2: Manual Installation Using Git

Suitable for new nodes not found in Manager or when specific versions are needed. Requires [Git](https://git-scm.com/) installed on your system.

<Steps>
  <Step title="Get the repository URL">
    Click the "Code" button on GitHub and copy the HTTPS link
  </Step>

  <Step title="Navigate to custom_nodes directory">
    ```bash  theme={null}
    cd /path/to/ComfyUI/custom_nodes
    ```
  </Step>

  <Step title="Clone the repository">
    ```bash  theme={null}
    git clone [repository URL]
    ```
  </Step>

  <Step title="Install dependencies">
    Dependencies must be installed in your ComfyUI environment - be careful not to mix with your system environment to avoid contamination

    <Tabs>
      <Tab title="Windows Portable">
        For Windows portable version, install dependencies in the embedded Python environment

        ```bash  theme={null}
        python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\[node directory]\requirements.txt
        ```
      </Tab>

      <Tab title="Manual Install">
        Install dependencies in your ComfyUI environment

        ```bash  theme={null}
        cd [node directory]
        pip install -r requirements.txt
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Restart ComfyUI and refresh browser">
    Restart ComfyUI and refresh your browser. Check startup logs for any `import failed` errors
  </Step>
</Steps>

## Method 3: ZIP Download Installation

Suitable for users who cannot use Git or Manager

<Warning>
  We don't recommend this installation method as it loses version control capabilities
</Warning>

<Steps>
  <Step title="Click `Code` → `Download ZIP` on GitHub">
    Click `Code` → `Download ZIP` on the GitHub page
    <img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-zip.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=442d68eaf9a445b1d3d62f046e9f7b69" alt="Click Code → Download ZIP on GitHub" data-og-width="2000" width="2000" data-og-height="1115" height="1115" data-path="images/installation/custom_nodes/install-custom-nodes-by-zip.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-zip.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=a234780546a81960e49c21322f8d9278 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-zip.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=facd00051fefee30ab4bd93ce51c9070 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-zip.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=becba0c76aecd5376ca1b09884bf19ee 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-zip.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c8fea29fdcbcd9e0c942ecc83bedb78f 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-zip.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=9afb8609ce2965097cb3fb34472319f8 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-zip.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=52b81f5d9d26c13d8cbc2e8d02cf6e50 2500w" />
  </Step>

  <Step title="Extract the ZIP file">
    Extract the downloaded ZIP file
  </Step>

  <Step title="Copy extracted folder to `ComfyUI/custom_nodes/` directory">
    Copy the extracted folder to `ComfyUI/custom_nodes/` directory
  </Step>

  <Step title="Install dependencies manually (same as Git method step 4)">
    Restart ComfyUI and refresh browser
  </Step>

  <Step title="Verify successful installation">
    Check ComfyUI Manager after restart to confirm the plugin installed successfully and there are no `import failed` errors
  </Step>
</Steps>

## Custom Node Resources

In ComfyUI, besides the basic node extension functionality, custom nodes can also include the following additional resources:

* [Node Documentation](/custom-nodes/help_page): This feature supports all custom and basic nodes. You can use it to view node documentation, understand the purpose and usage of nodes, and contribute documentation via PRs to the author.
* [Custom Node Workflow Templates](/custom-nodes/workflow_templates): Workflow templates provided by node authors as example workflows, which can be browsed and loaded from the ComfyUI templates.
* [Multi-language Support](/custom-nodes/i18n)

If you are a custom node developer, you can add these resources to make your custom node more user-friendly.
