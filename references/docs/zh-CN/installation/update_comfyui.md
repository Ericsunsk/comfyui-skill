> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 如何更新 ComfyUI

> 本部分将指导你详细了解 ComfyUI 的更新过程

尽管我们可能已经在不同版本的各部分章节，对于 ComfyUI 的更新过程都有所说明，但是为了方便用户能够更清楚的了解 ComfyUI 的更新过程，我们会在这部分对于 ComfyUI 的更新进行详细的说明。

## 如何更新 ComfyUI?

<Tabs>
  <Tab title="便携版">
    ComfyUI 便携版提供了便捷的批处理脚本来完成更新操作。

    ### 更新脚本位置

    在便携版安装目录下的 `update` 文件夹中，可以找到以下更新脚本：

    ```
    ComfyUI_windows_portable
    └─ 📂update
       ├── update.py
       ├── update_comfyui.bat                           // 更新到最新开发版本
       ├── update_comfyui_stable.bat                    // 更新到最新稳定版本
       └── update_comfyui_and_python_dependencies.bat   // ⚠️ 危险：重装依赖 - 可能导致冲突
    ```

    <Warning>更新过程中请保持网络连接稳定，如果在中国大陆地区可能需要配置网络代理来保证能够顺利访问 GitHub 仓库</Warning>

    <Warning>
      **⚠️ 危险：请谨慎使用 `update_comfyui_and_python_dependencies.bat`！**

      这个脚本比普通更新更彻底，它会：

      * ✅ 更新 ComfyUI 代码本身
      * ✅ 更新 PyTorch（针对 NVIDIA GPU CUDA 12.9）
      * ✅ 重新安装所有 Python 依赖包

      **风险提示：**

      * 可能与现有配置产生依赖冲突
      * 可能破坏依赖特定包版本的自定义节点
      * 可能覆盖手动配置的包版本

      **⚠️ 仅在以下情况使用此脚本：**

      * 需要修复依赖问题时
      * 进行大版本更新时
      * 日常更新建议使用 `update_comfyui.bat`

      **运行此脚本前必须：**

      1. **备份整个 ComfyUI 安装目录**
      2. 记录已安装的自定义包版本
      3. 做好重新安装自定义节点的准备
    </Warning>
  </Tab>

  <Tab title="桌面版">
    ComfyUI 桌面版采用自动更新机制，确保你始终使用最新版本，不过由于 Desktop 版本是基于稳定版本构建的，所以它的功能更新相对滞后，你也可以访问 [下载页面](https://www.comfy.org/download) 来获取最新版本。

    ### 自动更新设置

    请确保在设置中已经启用自动更新功能：
    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5006c9c0e4ad3e4f6ca0cef51132fbf3" alt="ComfyUI 桌面版设置" data-og-width="1065" width="1065" data-og-height="815" height="815" data-path="images/desktop/comfyui-desktop-update-setting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=25f0e90e8df014d0640205bb73e4253c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0137407c528ac79439d4320701e4c0b1 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=73f85bd7cbbeeeaeabad54154b60af7e 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4f880973b712a83849b16a78ce5868f5 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=174dc6b670118f452834cece0df52dbd 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1b72afe13029997c797c16772daeff98 2500w" />

    ### 手动检查更新

    你也可以手动检查是否有可用的更新：

    1. 点击菜单栏中的 `菜单`
    2. 选择 `帮助`
    3. 点击 `检查更新`
       <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0f2bf5d6ad204e762ed858f29df4282c" alt="ComfyUI 桌面版检查更新" data-og-width="415" width="415" data-og-height="477" height="477" data-path="images/desktop/desktop_check_for_updates.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c8f28a7f5ef143b0ca31e839187a5a65 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ffef0bd3b488b1545c0390d65ffbd445 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e46efe596b9b5b7f38da68489c245e4c 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9dd9460b2daafd8b398145e1961d668c 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=218f1e5e502286b7a90e21d5f60100fc 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f7e03d947a487ad2a5624f8d14c68e40 2500w" />

    <Note>桌面版会自动处理所有更新过程，包括 ComfyUI 核心代码和相关依赖的更新</Note>
  </Tab>

  <Tab title="手动安装">
    手动安装的 ComfyUI 需要通过 Git 命令来完成更新操作。

    ### 更新前准备

    确保你的系统已安装 [Git](https://git-scm.com/downloads) 并且 ComfyUI 是通过 Git 克隆安装的。

    ### 更新步骤

    <Steps>
      <Step title="激活虚拟环境">
        首先激活 ComfyUI 的 Python 虚拟环境（如果使用了虚拟环境）：

        ```bash  theme={null}
        # 对于 conda 环境
        conda activate comfyui

        # 对于 venv 环境
        # Windows
        venv\Scripts\activate
        # macOS/Linux  
        source venv/bin/activate
        ```
      </Step>

      <Step title="拉取最新代码">
        进入 ComfyUI 安装目录并拉取最新代码：

        ```bash  theme={null}
        cd <ComfyUI安装路径>
        git pull
        ```
      </Step>

      <Step title="更新依赖">
        安装或更新 ComfyUI 的依赖包：

        ```bash  theme={null}
        pip install -r requirements.txt
        ```

        <Warning>
          请确保当前处于 ComfyUI 的虚拟环境中，避免污染系统级 Python 环境
        </Warning>
      </Step>

      <Step title="重启 ComfyUI">
        更新完成后重新启动 ComfyUI：

        ```bash  theme={null}
        python main.py
        ```
      </Step>
    </Steps>

    ### 切换版本（可选）

    如果需要切换到特定版本，可以使用以下命令：

    ```bash  theme={null}
    # 查看提交历史
    git log --oneline

    # 切换到特定提交
    git checkout <commit-hash>

    # 返回最新版本
    git checkout master
    ```

    <Tip>建议定期更新以获得最新功能和安全修复，同时推荐使用稳定版本以确保系统稳定性</Tip>
  </Tab>
</Tabs>

## ComfyUI 的不同版本说明

首先取决于你安装方式的不同，目前 ComfyUI 有以下的几种安装版本，下面的相关链接中已经包含了针对不同版本的更新说明。

<AccordionGroup>
  <Accordion title="ComfyUI 桌面版">
    ComfyUI 桌面版目前支持 **Windows 及 MacOS(Apple Silicon)** 的独立安装，目前仍在 Beta 版本

    * 代码开源在 [Github](https://github.com/Comfy-Org/desktop)

    <Tip>
      由于 Desktop 总是基于稳定版本发布构建，所以我们最新的一些更新，对于 Desktop 来说可能需要等待一段时间才能体验到，如果你想要总是体验最新版本，请使用便携版或者手动安装
    </Tip>

    你可以从下面选择适合你的系统和硬件开始安装 ComfyUI

    <Tabs>
      <Tab title="Windows">
        <Card title="ComfyUI桌面版(Windows)安装指南" icon="link" href="/zh-CN/installation/desktop/windows">
          适合带有 **Nvdia** 显卡 **Windows** 版本的 ComfyUI 桌面版
        </Card>
      </Tab>

      <Tab title="MacOS(Apple Silicon)">
        <Card title="ComfyUI桌面版(MacOS)安装指南" icon="link" href="/zh-CN/installation/desktop/macos">
          适合带有 **Apple Silicon** 的 MacOS ComfyUI 桌面版
        </Card>
      </Tab>

      <Tab title="Linux">
        <Note>ComfyUI桌面版，**暂时没有 Linux 的预构建**，请访问[手动安装](/zh-CN/installation/manual_install)部分进行 ComfyUI 的安装</Note>
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="ComfyUI 便携版(Windows)">
    便携版是一个集成了独立的嵌入式 Python 环境的 ComfyUI 版本，使用便携版你可以体验到最新的功能，目前仅支持 **Windows** 系统

    <Card title="ComfyUI桌面版(Windows)安装指南" icon="link" href="/zh-CN/installation/comfyui_portable_windows">
      支持 **Navida 显卡** 和在 **CPU** 运行的 **Windows** ComfyUI 版本，始终使用最新 commit 的代码
    </Card>
  </Accordion>

  <Accordion title="手动安装 ComfyUI">
    <Card title="ComfyUI 手动安装教程" icon="link" href="/zh-CN/installation/manual_install">
      支持所有的系统类型和 GPU 类型（Nvidia、AMD、Intel、Apple Silicon、Ascend NPU、寒武纪 MLU）的用户都可以尝试使用手动安装 ComfyUI
    </Card>
  </Accordion>
</AccordionGroup>

## 在更新 ComfyUI 时都需要更新什么内容？

目前 ComfyUI 的更新主要需要确保两部分内容：

1. 更新 ComfyUI 的核心代码
2. 更新 ComfyUI 的核心依赖，包括必要的 Python 依赖和 ComfyUI 的功能依赖包。

**核心代码**： 新的节点，新的模型支持，新的功能等。
**核心依赖**： 主要包括 ComfyUI 的前端功能，工作流模板，节点帮助文档等。

```
comfyui-frontend-package   # ComfyUI 前端功能
comfyui-workflow-templates # ComfyUI 工作流模板  
comfyui-embedded-docs      # ComfyUI 节点的帮助文档
comfy-kitchen              # ComfyUI 核心工具库
comfy-aimdo                # ComfyUI 核心工具库
```

目前这些核心依赖项目分别在不同的仓库中维护：

* [ComfyUI\_frontend](https://github.com/Comfy-Org/ComfyUI_frontend/) - 前端界面和交互功能
* [workflow\_templates](https://github.com/Comfy-Org/workflow_templates) - 预置工作流模板
* [comfyui-embedded-docs](https://github.com/Comfy-Org/embedded-docs) - 节点帮助文档
* [comfy-kitchen](https://github.com/Comfy-Org/comfy-kitchen) - 支持多种计算后端的 Diffusion 推理快速内核库
* [comfy-aimdo](https://github.com/Comfy-Org/comfy-aimdo) - AI 模型按需卸载分配器

另外很有必要说明的一点是，开发版本(nightly) 和 稳定版本(release) 的区别：

* **开发版本(nightly)**：最新 commit 的代码，你可以体验到我们最新提供的一些功能，但是也有可能存在一些潜在的问题
* **稳定版本(release)**：是基于稳定版本构建，通常会滞后于开发版本，但是稳定性更高，我们会在相关功能发布稳定后对稳定版本进行支持

目前较多用户总是在更新过程中处于 release 版本或者桌面版，但是发现需要的功能是开发版本中提供的对应版本并不存在，对于此情况请检查本地 `ComfyUI/requirements.txt` 和[nightly 版本的依赖](https://github.com/comfyanonymous/ComfyUI/blob/master/requirements.txt)是否一致，来确定当前是否所有依赖都是我们最新版本的功能支持。

## 常见更新问题

### 更新后前端、工作流模板、节点帮助文档等缺失或滞后

<Tabs>
  <Tab title="未正确更新依赖">
    经常有用户只是使用 `git pull` 命令来更新 ComfyUI 的代码，但**忽略了核心依赖更新**，导致出现以下问题：

    * 前端功能缺失或显示异常
    * 找不到新增的工作流模板
    * 节点帮助文档过时或缺失
    * 新功能没有对应的前端支持

    请在使用了 `git pull` 命令后，在对应的 ComfyUI 环境使用 `pip install -r requirements.txt` 命令来更新依赖。
  </Tab>

  <Tab title="依赖更新失败">
    如果依赖更新失败常见可能是网络或者计算机权限问题，目前在更新过程中如果出现了核心依赖失败的情况会回退到旧版本，通常你可以在启动日志中看到类似下面的日志：

    ```
    Falling back to the default frontend.
    ComfyUI frontend version: xxx
    ```

    请按以下步骤排查：

    1. 在对应的环境中使用 `pip list` 命令来查看当前安装的依赖包，如果发现有版本不一致的情况，请在对应的 ComfyUI 环境使用 `pip install -r requirements.txt` 命令来尝试再次更新依赖。
    2. 如果更新后仍然存在问题，请检查网络连接是否正常，如果在中国大陆地区可能需要配置网络代理来保证能够顺利访问 GitHub 仓库。
    3. 如果仍然存在问题，请检查计算机权限是否正常，如果需要管理员权限，请使用管理员权限运行命令行。
  </Tab>
</Tabs>

### 如何正确更新核心依赖

<Tabs>
  <Tab title="便携版">
    **推荐方法**：使用 `ComfyUI_windows_portable\update\update_comfyui.bat` 这个批处理脚本，这个脚本会同时更新 ComfyUI 代码和所有 Python 依赖包。

    **手动更新依赖**：
    如果你需要手动更新依赖，可以使用以下命令：

    ```bash  theme={null}
    # 在便携版目录下打开命令行
    .\python_embeded\python.exe -m pip install -r ComfyUI\requirements.txt
    ```
  </Tab>

  <Tab title="手动安装">
    **标准更新流程**：

    <Steps>
      <Step title="激活虚拟环境">
        如你使用 Conda 管理虚拟环境，请先激活虚拟环境：

        ```bash  theme={null}
        conda activate comfyui  # 或其他环境名
        ```
      </Step>

      <Step title="更新代码">
        这一步我们需要进入 ComfyUI 的根目录，并使用 Git 更新对应的代码。

        ```
        cd <ComfyUI根目录>
        git pull
        ```
      </Step>

      <Step title="更新依赖">
        这一步我们需要更新 ComfyUI 的依赖，这个步骤非常重要，特别是前端 `comfyui-frontend-package` 的更新

        ```
        pip install -r requirements.txt
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="桌面版">
    桌面版通常会自动处理依赖更新。如果遇到问题：

    1. **检查自动更新设置**是否启用
    2. **手动触发更新**：菜单 → 帮助 → 检查更新
    3. **重新安装桌面版**（极端情况下）
  </Tab>
</Tabs>

### 依赖更新故障排除

如果依赖更新失败，请按以下步骤排查：

<Steps>
  <Step title="检查网络连接">
    如果位于中国大陆地区，请确保能够访问 PyPI 或配置中国境内镜像：

    ```bash  theme={null}
    # 使用清华大学镜像
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```
  </Step>

  <Step title="逐个安装核心包">
    如果批量安装失败，可尝试逐个安装。**首先查看 `ComfyUI/requirements.txt` 中的版本要求**：

    **然后按照指定版本安装（使用 requirements.txt 中的版本号）：**

    ```bash  theme={null}
    pip install comfyui-frontend-package==<version> 
    pip install comfyui-workflow-templates==<version>
    pip install comfyui-embedded-docs==<version>
    pip install comfy-kitchen==<version>
    pip install comfy-aimdo==<version>
    ```

    <Warning>
      建议使用 `ComfyUI/requirements.txt` 中指定的确切版本号，不要自行升级到最新版本，这可能导致兼容性问题。
    </Warning>
  </Step>
</Steps>

### 为什么我更新后找不到新功能？

这是最常见的问题之一：

* 如果你使用的是**桌面版**，因为桌面版是基于稳定版本构建的，它的功能更新相对滞后
* 请确定你使用的是**开发版本(nightly)**，而不是**稳定版本(release)**

另外还需要确保在更新过程中对应的依赖已经成功更新，如果更新后仍然存在问题，请参考[依赖更新故障排除](#依赖更新故障排除)章节来排查问题。

### 如何切换到开发（nightly）版本或者稳定（release）版本？

不同版本的区别

<Tabs>
  <Tab title="开发版本 (nightly)">
    * **特点**：包含最新的 commit 代码
    * **优势**：可以第一时间体验到最新功能和改进
    * **风险**：可能存在未发现的 bug 或不稳定因素
    * **适合人群**：开发者、测试用户、想要体验最新功能的用户
  </Tab>

  <Tab title="稳定版本 (release)">
    * **特点**：经过测试和验证的稳定代码
    * **优势**：稳定性高，适合生产环境使用
    * **劣势**：功能更新会有延迟，可能落后开发版本数周或数月
    * **适合人群**：需要稳定性的用户、生产环境用户
  </Tab>
</Tabs>

<Tabs>
  <Tab title="便携版">
    使用 `update_comfyui.bat` 而不是 `update_comfyui_stable.bat`：

    ```
    # 开发版本（最新功能）
    double-click: update_comfyui.bat

    # 稳定版本
    double-click: update_comfyui_stable.bat
    ```
  </Tab>

  <Tab title="手动安装">
    ```bash  theme={null}
    # 切换到开发版本
    git checkout master
    git pull

    # 切换到最新稳定版本
    git fetch --tags
    git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
    ```
  </Tab>

  <Tab title="桌面版">
    桌面版通常基于稳定版本构建,目前暂时不支持切换版本，如果你需要最新功能，建议：

    1. 等待桌面版更新
    2. 或者使用便携版/手动安装来体验最新功能
  </Tab>
</Tabs>

### 更新后出现错误怎么办？

1. **检查依赖**：运行 `pip install -r requirements.txt` 确保所有依赖都已更新
2. **检查自定义节点**：某些自定义节点可能与新版本不兼容
3. **回退版本**：如果问题严重，可以回退到之前的稳定版本

如果出现问题，可以参考我们的问题排查页面来解决。

<Card title="故障排查" icon="bug" href="/zh-CN/troubleshooting/overview">
  查看如何进行 ComfyUI 的故障排查
</Card>

### 如何了解最新功能？

* **GitHub Releases**：查看 [ComfyUI Releases](https://github.com/comfyanonymous/ComfyUI/releases) 了解稳定版本更新
* **GitHub Commits**：查看 [最新提交](https://github.com/comfyanonymous/ComfyUI/commits/master) 了解开发进度
* **社区讨论**：关注我们的[博客](https://blog.comfy.org)和[推特](https://x.com/comfyui)来了解最新动态
