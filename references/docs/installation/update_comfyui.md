> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Update ComfyUI

> This section provides a comprehensive guide to updating ComfyUI

While we've covered ComfyUI updates across different installation methods in various sections, this comprehensive guide consolidates all update procedures to help users clearly understand how to update ComfyUI.

## How to Update ComfyUI?

<Tabs>
  <Tab title="Portable">
    ComfyUI Portable provides convenient batch scripts for easy updates.

    ### Update Script Location

    In the `update` folder within your portable installation directory, you'll find the following update scripts:

    ```
    ComfyUI_windows_portable
    └─ 📂update
       ├── update.py
       ├── update_comfyui.bat                           // Update to latest development version
       ├── update_comfyui_stable.bat                    // Update to latest stable version
       └── update_comfyui_and_python_dependencies.bat   // ⚠️ DANGER: Reinstalls dependencies - may cause conflicts
    ```

    <Warning>Ensure a stable internet connection during updates.</Warning>

    <Warning>
      **⚠️ DANGER: Use `update_comfyui_and_python_dependencies.bat` with extreme caution!**

      This script is more thorough than regular updates and will:

      * ✅ Update ComfyUI code itself
      * ✅ Update PyTorch (for NVIDIA GPU CUDA 12.9)
      * ✅ Reinstall ALL Python dependencies

      **Risks:**

      * May cause dependency conflicts with your existing setup
      * Can break custom nodes that rely on specific package versions
      * May overwrite manually configured packages

      **⚠️ Only use this script when:**

      * You need to fix dependency issues
      * Performing major version updates
      * For daily updates, use `update_comfyui.bat` instead

      **Before running this script:**

      1. **Back up your entire ComfyUI installation**
      2. Document any custom package versions you've installed
      3. Be prepared to reinstall custom nodes if needed
    </Warning>
  </Tab>

  <Tab title="Desktop">
    ComfyUI Desktop features automatic updates to ensure you're always running the latest version. However, since the Desktop version is built on stable releases, feature updates may lag behind. You can also visit the [download page](https://www.comfy.org/download) to get the latest version.

    ### Auto-Update Settings

    Ensure automatic updates are enabled in your settings:
    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5006c9c0e4ad3e4f6ca0cef51132fbf3" alt="ComfyUI Desktop Settings" data-og-width="1065" width="1065" data-og-height="815" height="815" data-path="images/desktop/comfyui-desktop-update-setting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=25f0e90e8df014d0640205bb73e4253c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0137407c528ac79439d4320701e4c0b1 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=73f85bd7cbbeeeaeabad54154b60af7e 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4f880973b712a83849b16a78ce5868f5 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=174dc6b670118f452834cece0df52dbd 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1b72afe13029997c797c16772daeff98 2500w" />

    ### Manual Update Check

    You can also manually check for available updates:

    1. Click `Menu` in the menu bar
    2. Select `Help`
    3. Click `Check for Updates`
       <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0f2bf5d6ad204e762ed858f29df4282c" alt="ComfyUI Desktop Check Updates" data-og-width="415" width="415" data-og-height="477" height="477" data-path="images/desktop/desktop_check_for_updates.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c8f28a7f5ef143b0ca31e839187a5a65 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ffef0bd3b488b1545c0390d65ffbd445 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e46efe596b9b5b7f38da68489c245e4c 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9dd9460b2daafd8b398145e1961d668c 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=218f1e5e502286b7a90e21d5f60100fc 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f7e03d947a487ad2a5624f8d14c68e40 2500w" />

    <Note>Desktop version automatically handles all update processes, including ComfyUI core code and dependency updates</Note>
  </Tab>

  <Tab title="Manual Installation">
    Manually installed ComfyUI requires Git commands to complete updates.

    ### Pre-Update Requirements

    Ensure your system has [Git](https://git-scm.com/downloads) installed and ComfyUI was installed via Git clone.

    ### Update Steps

    <Steps>
      <Step title="Activate Virtual Environment">
        First, activate ComfyUI's Python virtual environment (if using one):

        ```bash  theme={null}
        # For conda environment
        conda activate comfyui

        # For venv environment
        # Windows
        venv\Scripts\activate
        # macOS/Linux  
        source venv/bin/activate
        ```
      </Step>

      <Step title="Pull Latest Code">
        Navigate to your ComfyUI installation directory and pull the latest code:

        ```bash  theme={null}
        cd <ComfyUI-installation-path>
        git pull
        ```
      </Step>

      <Step title="Update Dependencies">
        Install or update ComfyUI's dependency packages:

        ```bash  theme={null}
        pip install -r requirements.txt
        ```

        <Warning>
          Ensure you're in ComfyUI's virtual environment to avoid contaminating the system-level Python environment
        </Warning>
      </Step>

      <Step title="Restart ComfyUI">
        After updating, restart ComfyUI:

        ```bash  theme={null}
        python main.py
        ```
      </Step>
    </Steps>

    ### Version Switching (Optional)

    To switch to a specific version, use these commands:

    ```bash  theme={null}
    # View commit history
    git log --oneline

    # Switch to specific commit
    git checkout <commit-hash>

    # Return to latest version
    git checkout master
    ```

    <Tip>Regular updates are recommended for the latest features and security fixes, while stable versions are recommended for system stability</Tip>
  </Tab>
</Tabs>

## ComfyUI Version Types

Depending on your installation method, ComfyUI offers several installation versions. The links below contain update instructions for each version.

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

## What Needs to Be Updated When Updating ComfyUI?

ComfyUI updates primarily consist of two components:

1. Update ComfyUI's core code
2. Update ComfyUI's core dependencies, including necessary Python dependencies and ComfyUI functional dependency packages

**Core Code**: New nodes, new model support, new features, etc.
**Core Dependencies**: Mainly includes ComfyUI's frontend functionality, workflow templates, node help documentation, etc.

```
comfyui-frontend-package   # ComfyUI frontend functionality
comfyui-workflow-templates # ComfyUI workflow templates  
comfyui-embedded-docs      # ComfyUI node help documentation
comfy-kitchen              # ComfyUI core utilities
comfy-aimdo                # ComfyUI core utilities
```

These core dependencies are maintained in separate repositories:

* [ComfyUI\_frontend](https://github.com/Comfy-Org/ComfyUI_frontend/) - Frontend interface and interactive features
* [workflow\_templates](https://github.com/Comfy-Org/workflow_templates) - Pre-built workflow templates
* [comfyui-embedded-docs](https://github.com/Comfy-Org/embedded-docs) - Node help documentation
* [comfy-kitchen](https://github.com/Comfy-Org/comfy-kitchen) - Fast kernel library for Diffusion inference with multiple compute backends
* [comfy-aimdo](https://github.com/Comfy-Org/comfy-aimdo) - AI Model Demand Offloading Allocator

It's important to understand the difference between development (nightly) and stable (release) versions:

* **Development version (nightly)**: Latest commit code, giving you access to the newest features, but may contain potential issues
* **Stable version (release)**: Built on stable releases, usually lags behind development versions but offers higher stability. We support stable versions after features are tested and stabilized

Many users often find themselves on release versions or desktop versions during updates, but discover that needed features are only available in development versions. In such cases, check if your local `ComfyUI/requirements.txt` matches the [nightly version dependencies](https://github.com/comfyanonymous/ComfyUI/blob/master/requirements.txt) to determine if all dependencies support the latest features.

## Common Update Issues

### Missing or Outdated Frontend, Workflow Templates, Node  After Updates

<Tabs>
  <Tab title="Dependencies Not Properly Updated">
    Users often only use the `git pull` command to update ComfyUI code but **neglect core dependency updates**, leading to the following issues:

    * Missing or abnormal frontend functionality
    * Cannot find newly added workflow templates
    * Outdated or missing node help documentation
    * New features lack corresponding frontend support

    After using the `git pull` command, use the corresponding ComfyUI environment to use `pip install -r requirements.txt` to update dependencies.
  </Tab>

  <Tab title="Dependency Update Failures">
    If dependency updates fail, it's commonly due to network or computer permission issues. When core dependency failures occur during updates, the system falls back to older versions. You'll typically see logs like this during startup:

    ```
    Falling back to the default frontend.
    ComfyUI frontend version: xxx
    ```

    Follow these troubleshooting steps:

    1. Use `pip list` in the appropriate environment to view currently installed dependency packages. If you find version inconsistencies, use `pip install -r requirements.txt` in the ComfyUI environment to attempt dependency updates again.
    2. If issues persist after updating, check your network connection. Users in mainland China may need to configure a proxy to reliably access GitHub repositories.
    3. If problems continue, check computer permissions. If administrator privileges are required, run the command line with administrator rights.
  </Tab>
</Tabs>

### How to Properly Update Core Dependencies

<Tabs>
  <Tab title="Portable">
    **Recommended Method**: Use the `ComfyUI_windows_portable\update\update_comfyui.bat` batch script, which will update both ComfyUI code and all Python dependencies.

    **Manual Dependency Update**:
    If you need to manually update dependencies, use the following command:

    ```bash  theme={null}
    # Open command line in portable version directory
    .\python_embeded\python.exe -m pip install -r ComfyUI\requirements.txt
    ```
  </Tab>

  <Tab title="Manual Installation">
    <Steps>
      <Step title="Activate Python Environment">
        If you use Conda to manage Python environments, activate your environment first:

        ```bash  theme={null}
        conda activate comfyui  # or other environment name
        ```
      </Step>

      <Step title="Update Code">
        Navigate to the ComfyUI root directory and update the code using Git:

        ```
        cd <ComfyUI_ROOT_PATH>
        git pull
        ```
      </Step>

      <Step title="Update Dependencies">
        Update ComfyUI dependencies - this step is crucial, especially for the `comfyui-frontend-package`:

        ```
        pip install -r requirements.txt
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Desktop">
    Desktop version usually handles dependency updates automatically. If you encounter issues:

    1. **Check if auto-update** is enabled
    2. **Manually trigger update**: Menu → Help → Check for Updates
    3. **Reinstall desktop version** (in extreme cases)
  </Tab>
</Tabs>

### Core Dependency Update Troubleshooting

If core dependency updates fail, follow these troubleshooting steps:

<Steps>
  <Step title="Check Network Connection">
    If located in mainland China, ensure you can access PyPI or configure a domestic mirror:

    ```bash  theme={null}
    # Using Tsinghua University mirror
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```
  </Step>

  <Step title="Install Core Packages Individually">
    If batch installation fails, try installing packages individually. **First check version requirements in `ComfyUI/requirements.txt`**:

    **Then install according to specified versions (use version numbers from your requirements.txt):**

    ```bash  theme={null}
    pip install comfyui-frontend-package==<version> 
    pip install comfyui-workflow-templates==<version>
    pip install comfyui-embedded-docs==<version>
    pip install comfy-kitchen==<version>
    pip install comfy-aimdo==<version>
    ```

    <Warning>
      It's recommended to use the exact version numbers specified in `ComfyUI/requirements.txt`. Don't upgrade to the latest versions independently, as this may cause compatibility issues.
    </Warning>
  </Step>
</Steps>

### Why Can't I Find New Features After Updating?

This is one of the most common issues:

* If you're using the **Desktop version**, features may lag behind because the desktop version is built on stable releases
* Ensure you're using the **development version (nightly)**, not the **stable version (release)**

Additionally, ensure that corresponding dependencies have been successfully updated during the update process. If issues persist after updating, refer to the [Dependency Update Troubleshooting](#dependency-update-troubleshooting) section to diagnose problems.

### How to Switch Between Development (Nightly) and Stable (Release) Versions?

Differences between versions:

<Tabs>
  <Tab title="Development Version (Nightly)">
    * **Characteristics**: Contains the latest commit code
    * **Advantages**: Experience the latest features and improvements first
    * **Risks**: May contain undiscovered bugs or unstable factors
    * **Suitable for**: Developers, testers, users wanting to experience the latest features
  </Tab>

  <Tab title="Stable Version (Release)">
    * **Characteristics**: Tested and verified stable code
    * **Advantages**: High stability, suitable for production environments
    * **Disadvantages**: Feature updates have delays, may lag behind development versions by weeks or months
    * **Suitable for**: Users requiring stability, production environment users
  </Tab>
</Tabs>

<Tabs>
  <Tab title="Portable">
    Use `update_comfyui.bat` instead of `update_comfyui_stable.bat`:

    ```
    # Development version (latest features)
    double-click: update_comfyui.bat

    # Stable version
    double-click: update_comfyui_stable.bat
    ```
  </Tab>

  <Tab title="Manual Installation">
    ```bash  theme={null}
    # Switch to development version
    git checkout master
    git pull

    # Switch to latest stable version
    git fetch --tags
    git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
    ```
  </Tab>

  <Tab title="Desktop">
    Desktop version is typically built on stable releases and doesn't currently support version switching. If you need the latest features, we recommend:

    1. Wait for desktop version updates
    2. Or use portable/manual installation to experience the latest features
  </Tab>
</Tabs>

### What to Do When Errors Occur After Updates?

1. **Check Dependencies**: Run `pip install -r requirements.txt` to ensure all dependencies are updated
2. **Check Custom Nodes**: Some custom nodes may be incompatible with new versions
3. **Roll Back Version**: If issues are severe, you can roll back to a previous stable version

If problems occur, refer to our troubleshooting page for solutions.

<Card title="Troubleshooting" icon="bug" href="/troubleshooting/overview">
  Learn how to troubleshoot ComfyUI issues
</Card>

### How to Stay Updated on New Features?

* **GitHub Releases**: Check [ComfyUI Releases](https://github.com/comfyanonymous/ComfyUI/releases) for stable version updates
* **GitHub Commits**: View [latest commits](https://github.com/comfyanonymous/ComfyUI/commits/master) to understand development progress
* **Community Discussion**: Follow our [blog](https://blog.comfy.org) and [Twitter](https://x.com/comfyui) for the latest updates
