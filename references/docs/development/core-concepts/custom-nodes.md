> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Nodes

> Learn about installing, enabling dependencies, updating, disabling, and uninstalling custom nodes in ComfyUI

## About Custom Nodes

After installing ComfyUI, you'll discover that it includes many built-in nodes. These native nodes are called **Comfy Core** nodes, which are officially maintained by ComfyUI.

Additionally, there are numerous [**custom nodes**](https://registry.comfy.org) created by various authors from the ComfyUI community. These custom nodes bring extensive functionality to ComfyUI, greatly expanding its capabilities and feature boundaries.

In this guide, we'll cover various operations related to custom nodes, including installation, updates, disabling, uninstalling, and dependency installation.

Anyone can develop their own custom extensions for ComfyUI and share them with others. You can find many community custom nodes [here](https://registry.comfy.org). If you want to develop your own custom nodes, visit the section below to get started:

<Card title="Start Developing Custom Nodes" icon="link" href="/custom-nodes/overview">
  Learn how to start developing a custom node
</Card>

## Custom Node Management

In this section we will cover:

* Installing custom nodes
* Installing node dependencies
* Custom node version control
* Uninstalling custom nodes
* Temporarily disabling custom nodes
* Handling custom node dependency conflicts

### 1. Installing Custom Nodes

Currently, ComfyUI supports installing custom nodes through multiple methods, including:

* [Install via ComfyUI Manager (Recommended)](#install-via-comfyui-manager)
* Install via Git
* Manual installation

We recommend installing custom nodes through **ComfyUI Manager**, which is a highly significant tool in the ComfyUI custom node ecosystem. It makes custom node management (such as searching, installing, updating, disabling, and uninstalling) simple - you just need to search for the node you want to install in ComfyUI Manager and click install.

However, since all custom nodes are currently stored on GitHub, for regions that cannot access GitHub normally, we have written detailed instructions for different custom node installation methods in this guide.

Additionally, since we recommend using **ComfyUI Manager** for plugin management, we recommend using this tool for plugin management. You can find its source code [here](https://github.com/Comfy-Org/ComfyUI-Manager).
Therefore, in this documentation, we will use installing ComfyUI Manager as a custom node installation example, and supplement how to use it for node management in the relevant introduction sections.

<Tabs>
  <Tab title="Install via ComfyUI Manager">
    Since ComfyUI Manager has very rich functionality, we will use a separate document to introduce the ComfyUI Manager installation chapter. Please visit the link below to learn how to use ComfyUI Manager to install custom nodes.

    <Card title="Install Custom Nodes with ComfyUI Manager" icon="link" href="/installation/install_custom_node#method-1%3A-comfyui-manager-recommended">
      Learn how to use ComfyUI Manager to install custom nodes
    </Card>
  </Tab>

  <Tab title="Install via Git">
    <Steps>
      <Step title="Ensure Git is Installed">
        First, you need to ensure that Git is installed on your system. You can check if Git is installed by entering the following command in your system terminal:

        ```bash  theme={null}
        git --version
        ```

        If Git is installed, you will see output similar to the following:

                <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c0e90164d3a1c8f9ed0f54164b16443b" alt="Windows Terminal" data-og-width="1114" width="1114" data-og-height="228" height="228" data-path="images/concepts/custom_nodes/win_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a357e53c048002cce88022038c5bf828 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9cb6790f16ae6e6f63235f1e959600d5 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=271a0c821c923b7b2fdc3d5746dfeaa8 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bc288cf2488e869ae3d2f6a8a56063ed 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2af5489655f4e5cb48890bf017a7b647 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=808b660d6e7116094aadda28a1dfb2d6 2500w" />

        If not yet installed, please visit [git-scm.com](https://git-scm.com/) to download the corresponding installation package. Linux users please refer to [git-scm.com/downloads/linux](https://git-scm.com/downloads/linux) for installation instructions.

        <Tip>
          For ComfyUI Desktop version, you can use the Desktop terminal as shown below to complete the installation.
          <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=946b0d382dc99eba1b7c33072ed1bce2" alt="ComfyUI Desktop Terminal" data-og-width="1800" width="1800" data-og-height="1403" height="1403" data-path="images/concepts/custom_nodes/desktop_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4ce6791b7ace89fa5a1e7fd8438b8dc0 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6e9fcf09190d3cfa4ee6ef730d6b9fe6 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=fc1b03b1b9b43062a5c4bd31dbea62d9 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=216afbc5d75842f85ebc8f1b76b2d5be 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cce1b33c7a01b016a61baa10339c97df 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1216d21a3cc886305cc67a8c22edfb91 2500w" />
        </Tip>
      </Step>

      <Step title="Clone Custom Node Code to Directory">
        After completing the Git installation, we need the repository address of the custom node. Here we use the ComfyUI-Manager repository address as an example:

        ```bash  theme={null}
        https://github.com/Comfy-Org/ComfyUI-Manager
        ```

        <Tip>For regions that cannot access GitHub smoothly, you can try using other code hosting service websites to fork the corresponding repository, then use that repository address to complete the node installation, such as gitee, etc.</Tip>

        First, we need to navigate to the ComfyUI custom nodes directory. Using ComfyUI portable version as an example, if the folder location is `D:\ComfyUI_windows_portable`, then you should be able to find the custom nodes folder at `D:\ComfyUI_windows_portable\ComfyUI\custom_nodes`. First, we need to use the `cd` command to enter the corresponding directory:

        ```bash  theme={null}
        cd D:\ComfyUI_windows_portable\ComfyUI\custom_nodes
        ```

        Then we use the `git clone` command to complete the node installation:

        ```bash  theme={null}
        git clone https://github.com/Comfy-Org/ComfyUI-Manager
        ```

        If everything goes smoothly, you will see output similar to the following:

                <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=80409dceca35c9d58c42dde48c4c53a5" alt="Install Custom Nodes via Git" data-og-width="1116" width="1116" data-og-height="317" height="317" data-path="images/concepts/custom_nodes/install_custom_nodes_by_git.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=11856e33ebf16d403fc1bfd7dea88fa7 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=3fe94004114027d4c921c43f3d42a9d9 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ac2c83634737859345407522169a2777 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b1a5d9aecc3d51fcf9cd8a254797f565 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=dd666e0e9c82d0929c1c4e0430003571 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=205985da6950ff470816f40f5fc51500 2500w" />

        This means you have successfully cloned the custom node code. Next, we need to install the corresponding dependencies.
      </Step>

      <Step title="Install Dependencies">
        Please refer to the instructions in the [Installing Node Dependencies](#installing-node-dependencies) section for dependency installation.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Manual Installation">
    Manual installation is not the recommended installation method, but it serves as a backup option when you cannot install smoothly using git.

    <Warning>
      Plugins installed this way will lose the corresponding git version history information and will not be convenient for subsequent version management.
    </Warning>

    <Steps>
      <Step title="Download Custom Node Code ZIP Package">
        For manual installation, we need to first download the corresponding node code and then extract it to the appropriate directory.

                <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=34fa06cf4580152428c5d2b55b192911" alt="Download Node Code" data-og-width="1011" width="1011" data-og-height="618" height="618" data-path="images/concepts/custom_nodes/download_zip.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=abe163da0d4486c9ac953740efa53132 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=938e6e59ac49b2f6f4d5a6ab8e3fc34b 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4d2b335af8cf590678abf746ad2faad0 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=40a958844a5808923eb70f12ecdca784 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ea0a46e7137e32594e7d3525b679865c 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b8980eb0deed06232f1081ceb18ed528 2500w" />

        Visit the corresponding custom node repository page:

        1. Click the `Code` button
        2. Then click the `Download ZIP` button to download the ZIP package
        3. Extract the ZIP package
      </Step>

      <Step title="Copy Files to ComfyUI Custom Nodes Directory">
        Copy the extracted code from the above steps to the ComfyUI custom nodes directory. Using ComfyUI portable version as an example, if the folder location is `D:\ComfyUI_windows_portable`, then you should be able to find the custom nodes folder at `D:\ComfyUI_windows_portable\ComfyUI\custom_nodes`. Copy the extracted code from the above steps to the corresponding directory.
      </Step>

      <Step title="Install Dependencies">
        Please refer to the instructions in the [Installing Node Dependencies](#installing-node-dependencies) section for dependency installation.
      </Step>
    </Steps>
  </Tab>
</Tabs>

### 2. Installing Node Dependencies

Custom nodes all require the installation of related dependencies. For example, for ComfyUI-Manager, you can visit the [requirements.txt](https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/requirements.txt) file to view the dependency package requirements.

In the previous steps, we only cloned the custom node code locally and did not install the corresponding dependencies, so next we need to install the corresponding dependencies.

<Note>
  Actually, if you use ComfyUI-Manager to install plugins, ComfyUI Manager will automatically help you complete the dependency installation. You just need to restart ComfyUI after installing the plugin. This is why we strongly recommend using ComfyUI Manager to install custom nodes.

  But perhaps you may not be able to use ComfyUI Manager to install custom nodes smoothly in some situations, so we provide this more detailed dependency installation guide.
</Note>

In the [Dependencies](/development/core-concepts/dependencies) chapter, we introduced the relevant content about dependencies in ComfyUI. ComfyUI is a **Python**-based project, and we built an independent **Python** runtime environment for running ComfyUI. All related dependencies need to be installed in this independent **Python** runtime environment.

If you run `pip install -r requirements.txt` directly in the system-level terminal, the corresponding dependencies may be installed in the system-level **Python** environment, which will cause the dependencies to still be missing in ComfyUI's environment, preventing the corresponding custom nodes from running normally.

So next we need to use ComfyUI's independent Python runtime environment to complete the dependency installation.

Depending on different ComfyUI versions, we will use different methods to install the corresponding dependencies:

<Tabs>
  <Tab title="ComfyUI Portable">
    For ComfyUI Portable version, it uses an embedded Python located in the `\ComfyUI_windows_portable\python_embeded` directory. We need to use this Python to complete the dependency installation.

    First, start the terminal in the portable version directory, or use the `cd` command to navigate to the `\ComfyUI_windows_portable\` directory after starting the terminal.

        <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ee4569d27b4ef901c5f67d8f795b448c" alt="Start Terminal" data-og-width="1822" width="1822" data-og-height="1187" height="1187" data-path="images/concepts/custom_nodes/open_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6e1589dff5dd380e4484e6ae44172df4 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=107a3e8c8020ddc46b1473004a2e8394 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9eb529d60d9cfb939bed1014c0895939 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f17cb8cb8a0f24461baaa909482591e0 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=649ce090ec9804a49662f81b20e192c9 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=26d70d0642ffe52424f940463d770a2b 2500w" />

    Ensure that the terminal directory is `\ComfyUI_windows_portable\`, as shown below for `D:\ComfyUI_windows_portable\`

        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f6da2e8c4eef1016e6fde84ee5527ce0" alt="Terminal" data-og-width="2400" width="2400" data-og-height="1147" height="1147" data-path="images/concepts/custom_nodes/terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d4c3e07411aed9823f7b52287e8c4d95 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5dd7ecf31d1183f950d31c9b9b4b97c9 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0bc86f9512c81d0045ec3cc8e3067846 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e54eab41295a7fb58c69bca2b1310f73 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=eef8a3bad5e20eb6bf0b14c756cdef1b 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b91b3d6f97318bcae7aa99c6613e42ee 2500w" />

    Then use `python_embeded\python.exe` to complete the dependency installation:

    ```bash  theme={null}
    python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-Manager\requirements.txt
    ```

    Of course, you can replace ComfyUI-Manager with the name of the custom node you actually installed, but make sure that a `requirements.txt` file exists in the corresponding node directory.
  </Tab>

  <Tab title="ComfyUI Desktop">
    <Tip>
      Since ComfyUI Desktop already has ComfyUI-Manager and its dependencies installed during the installation process, and this guide uses ComfyUI Manager as an example for custom node installation, you don't actually need to perform ComfyUI Manager dependency installation in the desktop version.
      If there are no unexpected issues, we recommend using ComfyUI Manager to install custom nodes, so you don't need to manually install dependencies.
    </Tip>

        <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=946b0d382dc99eba1b7c33072ed1bce2" alt="ComfyUI Desktop Terminal" data-og-width="1800" width="1800" data-og-height="1403" height="1403" data-path="images/concepts/custom_nodes/desktop_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4ce6791b7ace89fa5a1e7fd8438b8dc0 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=6e9fcf09190d3cfa4ee6ef730d6b9fe6 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=fc1b03b1b9b43062a5c4bd31dbea62d9 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=216afbc5d75842f85ebc8f1b76b2d5be 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cce1b33c7a01b016a61baa10339c97df 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/desktop_terminal.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=1216d21a3cc886305cc67a8c22edfb91 2500w" />

    Then use the following command to install the dependencies for the corresponding plugin:

    ```bash  theme={null}
    pip install -r .\custom_nodes\<corresponding_custom_node_name>\requirements.txt
    ```

    As shown below, this is the dependency installation for ComfyUI-Hunyuan3Dwrapper:

        <img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=23366292f947d238ea260f07d8529502" alt="ComfyUI Desktop Dependency Installation" data-og-width="2038" width="2038" data-og-height="1472" height="1472" data-path="images/concepts/custom_nodes/install_dependencies.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8849616b5cbe36efa5096e396ab83795 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=32c343240d23faf1f40d94ba43f9c747 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=859ffceb951a83654e3c363a489c3c7a 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=376dd9c1750dbff7a9a796285ce1704e 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=26af3d5f53099c4b5ebb4c51c13053d8 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_dependencies.jpg?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=34db9db7e172a2cd0af03eb08ee1265a 2500w" />
  </Tab>

  <Tab title="Custom Python Environment Users">
    For users with custom Python environments, we recommend using `pip install -r requirements.txt` to complete the dependency installation.
  </Tab>
</Tabs>

### Custom Node Version Control

Custom node version control is actually based on Git version control. You can manage node versions through Git, but ComfyUI Manager has already integrated this version management functionality very well. Many thanks to [@Dr.Lt.Data](https://github.com/ltdrdata) for bringing us such a convenient tool.

In this section, we will still explain these two different plugin version management methods for you, but if you use ZIP packages for manual installation, the corresponding git version history information will be lost, making it impossible to perform version management.

<Tabs>
  <Tab title="Version Management with ComfyUI Manager">
    <Tip>Since we are iterating on ComfyUI Manager, the actual latest interface and steps may change significantly</Tip>

    <Steps>
      <Step title="Enter Node Management Interface">
        Perform the corresponding operations as shown to enter the ComfyUI Manager interface
      </Step>

      <Step title="Find the Corresponding Custom Node Package">
        You can use the corresponding filters to filter out installed node packages and then perform the corresponding node management
      </Step>

      <Step title="Perform Version Switching">
        Switch to the corresponding version. Manager will help you complete the corresponding dependency updates and installation. Usually, you need to restart ComfyUI after switching versions for the changes to take effect.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Version Management with Git">
    <Steps>
      <Step title="Navigate to Directory Using Command Line">
        Find the directory folder where your corresponding node is located, such as `ComfyUI/custom_nodes/ComfyUI-Manager`
        Use the `cd` command to enter the corresponding folder:

        ```bash  theme={null}
        cd <your_installation_directory>/ComfyUI/custom_nodes/ComfyUI-Manager
        ```
      </Step>

      <Step title="View Versions Using Git Commands">
        You can use the following command to view all available tags and releases:

        ```bash  theme={null}
        git tag
        ```

        This will list all version tags, and you can choose the version you want to switch to.
      </Step>

      <Step title="Switch to Specified Version">
        Use the following command to switch to a specified tag or release:

        ```bash  theme={null}
        git checkout <tag_name>
        ```

        Replace `<tag_name>` with the specific version tag you want to switch to.
      </Step>

      <Step title="Switch to Specific Commit Version">
        If you want to switch to a specific commit version, you can use the following command:

        ```bash  theme={null}
        git checkout <commit_hash>
        ```

        Replace `<commit_hash>` with the specific commit hash you want to switch to.
      </Step>

      <Step title="Install Dependencies">
        Since the dependencies of the corresponding custom node package may change after version switching, you need to reinstall the dependencies for the corresponding node. Please refer to the instructions in the [Installing Node Dependencies](#2-installing-node-dependencies) section to enter the corresponding environment for installation.
      </Step>
    </Steps>
  </Tab>
</Tabs>

### Uninstalling Custom Nodes

To be updated

### Temporarily Disabling Custom Nodes

To be updated

### Custom Node Dependency Conflicts

To be updated

## ComfyUI Manager

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cea0de500828224b23b64cef84a31936" alt="ComfyUI Manager Interface" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/concepts/core-concepts_nodes_manager.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b66fffe074ba15068c2868e5e127cc41 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=951aa7941493ea56018c7aa77d1bc143 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=93e156a11636d64258510480fe1c28c2 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=352d680f30f32e457031be3c6de987d9 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a034b1663b608f4d64c6a690ea652b88 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4ca79e9090f1ed2513db42fa9838af40 2500w" />

This tool is currently included by default in the [Desktop version](/installation/desktop/windows), while in the [Portable version](/installation/comfyui_portable_windows), you need to refer to the installation instructions in the [Install Manager](#installing-custom-nodes) section of this document.

<Note>
  As ComfyUI continues to develop, ComfyUI Manager plays an increasingly important role in ComfyUI. Currently, ComfyUI-Manager has officially joined the Comfy Org organization, officially becoming part of ComfyUI's core dependencies, and continues to be maintained by the original author [Dr.Lt.Data](https://github.com/ltdrdata). You can read [this blog post](https://blog.comfy.org/p/comfyui-manager-joins-comfy-org) for more information.
  In future iterations, we will greatly optimize the use of ComfyUI Manager, so the interface shown in this documentation may differ from the latest version of ComfyUI Manager.
</Note>

### Installing the Manager

If you are running the ComfyUI server application, you need to install the manager. If ComfyUI is running, please close it before continuing.

The first step is to install Git, which is a command-line application for software version control. Git will download the ComfyUI manager from [github.com](https://github.com). Download and install Git from [git-scm.com](https://git-scm.com/).

After installing Git, navigate to the ComfyUI server program directory and enter the folder labeled **custom\_nodes**. Open a command window or terminal. Make sure the command line shows the current directory path as **custom\_nodes**. Enter the following command. This will download the manager. Technically, this is called *cloning a Git repository*.

### Detecting Missing Nodes

After installing the manager, you can detect missing nodes in the manager.

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cea0de500828224b23b64cef84a31936" alt="ComfyUI Manager Interface" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/concepts/core-concepts_nodes_manager.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=b66fffe074ba15068c2868e5e127cc41 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=951aa7941493ea56018c7aa77d1bc143 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=93e156a11636d64258510480fe1c28c2 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=352d680f30f32e457031be3c6de987d9 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a034b1663b608f4d64c6a690ea652b88 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4ca79e9090f1ed2513db42fa9838af40 2500w" />

## Developing a Custom Node

If you have some development capabilities, please start with the documentation below to learn how to begin developing a custom node.

<Card title="Start Developing Custom Nodes" icon="link" href="/custom-nodes/overview">
  Learn how to start developing a custom node
</Card>
