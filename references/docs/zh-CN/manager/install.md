> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI-Manager 安装

> 如何为不同环境安装 ComfyUI-Manager

## 桌面版用户

如果您使用的是 [ComfyUI 桌面版](/zh-CN/installation/desktop/windows)，ComfyUI-Manager 已默认包含并启用。无需额外安装。

## 便携版用户

对于使用 [Windows 便携版](/zh-CN/installation/comfyui_portable_windows) 的用户，新版 ComfyUI-Manager 已内置于 ComfyUI 核心中，但需要启用。

1. 安装管理器依赖：
   ```bash  theme={null}
   .\python_embeded\python.exe -m pip install -r ComfyUI\manager_requirements.txt
   ```

2. 启用管理器启动 ComfyUI：
   ```bash  theme={null}
   .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --enable-manager
   pause
   ```

## 手动安装用户

对于[手动安装](/zh-CN/installation/manual_install)的用户，新版 ComfyUI-Manager 已内置于 ComfyUI 核心中，但需要启用。

1. 激活虚拟环境：
   ```bash  theme={null}
   # Windows
   venv\Scripts\activate

   # Linux/macOS
   source venv/bin/activate
   ```

2. 安装管理器依赖：
   ```bash  theme={null}
   pip install -r manager_requirements.txt
   ```

3. 运行 ComfyUI 时使用 `--enable-manager` 标志启用管理器：
   ```bash  theme={null}
   python main.py --enable-manager
   ```

### 命令行选项

| 标志                           | 描述                                           |
| ---------------------------- | -------------------------------------------- |
| `--enable-manager`           | 启用 ComfyUI-Manager                           |
| `--enable-manager-legacy-ui` | 使用旧版管理器 UI 而非新版 UI（需要 `--enable-manager`）    |
| `--disable-manager-ui`       | 禁用管理器 UI 和端点，同时保留后台功能（需要 `--enable-manager`） |

### 切换新旧版UI

以下版本更新仅支持 pip 版本， 通过自定义节点方式安装的版本不支持切换到新版 UI

<Tabs>
  <Tab title="非桌面版用户">
    使用新版本 UI

    ```bash  theme={null}
    python main.py --enable-manager
    ```

    使用旧版UI

    ```bash  theme={null}
    python main.py --enable-manager --enable-manager-legacy-ui
    ```
  </Tab>

  <Tab title="桌面版用户">
    桌面版请在 服务器设置 -> UI 设置 -> 使用旧版管理器界面 切换到旧版 UI
    <img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=5a47648f9d602868c022a17b01c4d2df" alt="切换旧版 UI " data-og-width="4266" width="4266" data-og-height="3150" height="3150" data-path="images/manager/manager_use_legacy_manager_ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=baa4edc5f4d9895075a700f2604e4267 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=bdf783e2f12f73ce035b29dedc420909 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=ad704d0f1f3ad7e6144626cbe2c8abb5 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=4cee0d03a591218db7cd761f78793182 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=358a657146fbd814fd2f3de617a927c0 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=479d1e46ca27d0476aa99578852979dd 2500w" />
  </Tab>
</Tabs>

## 自定义节点版本安装方法

<Accordion title="方法 1：Git clone（通用安装）">
  在现有 ComfyUI 安装基础上安装 ComfyUI-Manager：

  1. 在终端中导航到 `ComfyUI/custom_nodes` 目录
  2. 克隆仓库：
     ```bash  theme={null}
     git clone https://github.com/ltdrdata/ComfyUI-Manager comfyui-manager
     ```
  3. 安装管理器依赖：
     ```bash  theme={null}
     cd comfyui-manager
     pip install -r requirements.txt
     ```
  4. 重启 ComfyUI
</Accordion>

<Accordion title="方法 2：便携版（Windows）">
  1. 安装 [Git for Windows](https://git-scm.com/download/win)（独立版本，选择"使用 Windows 默认控制台窗口"）
  2. 将 [install-manager-for-portable-version.bat](https://github.com/ltdrdata/ComfyUI-Manager/raw/main/scripts/install-manager-for-portable-version.bat) 下载到您的 `ComfyUI_windows_portable` 目录
  3. 双击批处理文件进行安装
</Accordion>

<Accordion title="方法 3：comfy-cli（推荐用于新安装）">
  comfy-cli 提供各种功能，可从命令行管理 ComfyUI。

  **前提条件**：Python 3、Git

  **Windows：**

  ```bash  theme={null}
  python -m venv venv
  venv\Scripts\activate
  pip install comfy-cli
  comfy install
  ```

  **Linux/macOS：**

  ```bash  theme={null}
  python -m venv venv
  . venv/bin/activate
  pip install comfy-cli
  comfy install
  ```

  另请参阅：[comfy-cli 文档](/zh-CN/comfy-cli/getting-started)
</Accordion>

<Accordion title="方法 4：Linux + venv">
  **前提条件**：python-is-python3、python3-venv、git

  1. 将 [install-comfyui-venv-linux.sh](https://github.com/comfy-org/ComfyUI-Manager/raw/main/scripts/install-comfyui-venv-linux.sh) 下载到空的安装目录
  2. 运行：
     ```bash  theme={null}
     chmod +x install-comfyui-venv-linux.sh
     ./install-comfyui-venv-linux.sh
     ```
  3. 使用 `./run_gpu.sh` 或 `./run_cpu.sh` 执行 ComfyUI
</Accordion>

<Warning>
  **安装注意事项：**

  * ComfyUI-Manager 文件必须准确位于路径 `ComfyUI/custom_nodes/comfyui-manager`
  * 不要直接解压到 `ComfyUI/custom_nodes`（`__init__.py` 等文件不应在该目录中）
  * 不要安装在 `ComfyUI/custom_nodes/ComfyUI-Manager/ComfyUI-Manager` 或 `ComfyUI/custom_nodes/ComfyUI-Manager-main` 等路径
</Warning>
