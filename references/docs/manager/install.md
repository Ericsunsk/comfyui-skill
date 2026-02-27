> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI-Manager Installation

> How to install ComfyUI-Manager for different setups

## Desktop users

If you're using [ComfyUI Desktop](/installation/desktop/windows), ComfyUI-Manager is already included and enabled by default. No additional installation is required.

## Portable users

For users running the [Windows Portable](/installation/comfyui_portable_windows) version, the new ComfyUI-Manager is built into ComfyUI core but needs to be enabled.

1. Install the manager dependencies:
   ```bash  theme={null}
   .\python_embeded\python.exe -m pip install -r ComfyUI\manager_requirements.txt
   ```

2. Launch ComfyUI with the manager enabled:
   ```bash  theme={null}
   .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --enable-manager
   pause
   ```

## Manual install users

For users with a [manual installation](/installation/manual_install), the new ComfyUI-Manager is built into ComfyUI core but needs to be enabled.

1. Activate your virtual environment:
   ```bash  theme={null}
   # Windows
   venv\Scripts\activate

   # Linux/macOS
   source venv/bin/activate
   ```

2. Install the manager dependencies:
   ```bash  theme={null}
   pip install -r manager_requirements.txt
   ```

3. Enable the manager with the `--enable-manager` flag when running ComfyUI:
   ```bash  theme={null}
   python main.py --enable-manager
   ```

### Command line options

| Flag                         | Description                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------- |
| `--enable-manager`           | Enable ComfyUI-Manager                                                                               |
| `--enable-manager-legacy-ui` | Use the legacy manager UI instead of the new UI (requires `--enable-manager`)                        |
| `--disable-manager-ui`       | Disable the manager UI and endpoints while keeping background features (requires `--enable-manager`) |

### Switch between new and legacy UI

The following version updates only support pip installations. Versions installed via custom nodes do not support switching to the new UI.

<Tabs>
  <Tab title="Non-Desktop users">
    To use the new UI:

    ```bash  theme={null}
    python main.py --enable-manager
    ```

    To use the legacy UI:

    ```bash  theme={null}
    python main.py --enable-manager --enable-manager-legacy-ui
    ```
  </Tab>

  <Tab title="Desktop users">
    Desktop users can switch to the legacy UI in **Server Settings → UI Settings → Use legacy manager interface**
    <img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=5a47648f9d602868c022a17b01c4d2df" alt="Switch to legacy UI" data-og-width="4266" width="4266" data-og-height="3150" height="3150" data-path="images/manager/manager_use_legacy_manager_ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=baa4edc5f4d9895075a700f2604e4267 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=bdf783e2f12f73ce035b29dedc420909 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=ad704d0f1f3ad7e6144626cbe2c8abb5 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=4cee0d03a591218db7cd761f78793182 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=358a657146fbd814fd2f3de617a927c0 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=479d1e46ca27d0476aa99578852979dd 2500w" />
  </Tab>
</Tabs>

## Legacy installation methods

<Accordion title="Method 1: Git clone (general installation)">
  To install ComfyUI-Manager in addition to an existing installation of ComfyUI:

  1. Navigate to `ComfyUI/custom_nodes` directory in terminal
  2. Clone the repository:
     ```bash  theme={null}
     git clone https://github.com/ltdrdata/ComfyUI-Manager comfyui-manager
     ```
  3. Install the manager dependencies:
     ```bash  theme={null}
     cd comfyui-manager
     pip install -r requirements.txt
     ```
  4. Restart ComfyUI
</Accordion>

<Accordion title="Method 2: Portable version (Windows)">
  1. Install [Git for Windows](https://git-scm.com/download/win) (standalone version, select "use windows default console window")
  2. Download [install-manager-for-portable-version.bat](https://github.com/ltdrdata/ComfyUI-Manager/raw/main/scripts/install-manager-for-portable-version.bat) into your `ComfyUI_windows_portable` directory
  3. Double-click the batch file to install
</Accordion>

<Accordion title="Method 3: comfy-cli (recommended for new installations)">
  comfy-cli provides various features to manage ComfyUI from the CLI.

  **Prerequisites**: Python 3, Git

  **Windows:**

  ```bash  theme={null}
  python -m venv venv
  venv\Scripts\activate
  pip install comfy-cli
  comfy install
  ```

  **Linux/macOS:**

  ```bash  theme={null}
  python -m venv venv
  . venv/bin/activate
  pip install comfy-cli
  comfy install
  ```

  See also: [comfy-cli documentation](/comfy-cli/getting-started)
</Accordion>

<Accordion title="Method 4: Linux + venv">
  **Prerequisites**: python-is-python3, python3-venv, git

  1. Download [install-comfyui-venv-linux.sh](https://github.com/comfy-org/ComfyUI-Manager/raw/main/scripts/install-comfyui-venv-linux.sh) into an empty install directory
  2. Run:
     ```bash  theme={null}
     chmod +x install-comfyui-venv-linux.sh
     ./install-comfyui-venv-linux.sh
     ```
  3. Execute ComfyUI with `./run_gpu.sh` or `./run_cpu.sh`
</Accordion>

<Warning>
  **Installation precautions:**

  * ComfyUI-Manager files must be accurately located in the path `ComfyUI/custom_nodes/comfyui-manager`
  * Do not decompress directly into `ComfyUI/custom_nodes` (files like `__init__.py` should not be in that directory)
  * Do not install in paths like `ComfyUI/custom_nodes/ComfyUI-Manager/ComfyUI-Manager` or `ComfyUI/custom_nodes/ComfyUI-Manager-main`
</Warning>
