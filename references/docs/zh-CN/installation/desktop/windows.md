> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows桌面版

> 本文将介绍 ComfyUI Desktop Windows 版本的下载以及安装使用

export const log_path_0 = "C:\\Users\\<你的用户名>\\AppData\\Roaming\\ComfyUI\\logs"

export const config_path_0 = "C:\\Users\\<你的用户名>\\AppData\\Roaming\\ComfyUI"

**ComfyUI 桌面版（Desktop）** 是一个独立的安装版本，可以像常规软件一样进行安装，支持快捷安装自动配置 **Python环境及依赖** ，支持导入已有的 ComfyUI 设置、模型、工作流和文件，可以快速从已有的[ComfyUI 便携版](/zh-CN/installation/comfyui_portable_windows)迁移到桌面版

ComfyUI 桌面版是一个开源项目，完整代码请访问 [这里](https://github.com/Comfy-Org/desktop)

ComfyUI 桌面版(Windows)硬件要求：

* NVIDIA 显卡

本篇教程将引导你完成对应的软件安装，并说明相关安装配置说明。

<Warning>由于 **ComfyUI 桌面版** 仍旧处于 **Beta** 状态，实际的安装过程可能会发生变化</Warning>

## ComfyUI 桌面版（Windows）下载

请点击下面的按钮下载对应的针对 Windows 系统的 **ComfyUI 桌面版** 安装包

<a className="prose" href="https://download.comfy.org/windows/nsis/x64" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download for Windows (NVIDIA)</p>
</a>

## ComfyUI 桌面版安装步骤

双击下载到的安装包文件，首先将会执行一次自动安装，并在桌面生成一个 **ComfyUI 桌面版** 的快捷方式

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=91d39867b16a2c5eb803fe2f26cee5bf" alt="ComfyUI logo" data-og-width="731" width="731" data-og-height="486" height="486" data-path="images/desktop/win-comfyui-desktop-shortcut.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9875d7185aebb25f478f1cb94571577c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=01c8b6ba2b24ae54115a3b92667b479a 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=04f19ebfbab1e9726de3bad4e31897ec 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=619e79aab66bd8480a6afe25f37f9350 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=031f8da7cb83b0feca9318fd457f4fd7 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8083e0b55c8c313c4b26b311f868ae6d 2500w" />

双击对应的快捷，进入 ComfyUI 的初始化设置

### ComfyUI 桌面版初始化流程

<Steps>
  <Step title="开始界面">
    <Tabs>
      <Tab title="正常启动">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=778c2d6e0d08a961278a5d0f917221d4" alt="ComfyUI 安装步骤 - 起始" data-og-width="1514" width="1514" data-og-height="1139" height="1139" data-path="images/desktop/win-comfyui-desktop-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5ce5b27d7ef8c915cf92fa225b1744f4 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0c30ea772deb01623140ad0471567b2b 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ba471670151c04fb3fbbbcd087946a6b 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=59102ff039ce2a93492b4de598de3025 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0fe3497ddf26ef941457be73f7de7c6c 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=532407419f6d37ce88536749c29321af 2500w" />
        点击 **Get Started** 开始初始化步骤
      </Tab>

      <Tab title="维护页">
        安装 ComfyUI 可能会出现许多问题。也许在安装 pytorch（15 GB）时网络连接失败，或者你没有安装 git，当检测到问题时，维护页面会自动打开，并提供解决问题的方法。

        你可以使用它来解决大多数问题：

        * 创建一个 Python 虚拟环境
        * 重新安装所有缺失的核心依赖项到由桌面管理的 Python 虦虚拟环境
        * 安装 git，VC redis
        * 选择一个新的安装位置

        默认维护页面会显示当前报错的内容

                <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2a01daff7808d4d342aeb423a072308f" alt="ComfyUI 维护页面" data-og-width="971" width="971" data-og-height="715" height="715" data-path="images/desktop/maintenance-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=6e97afdce4ad87e3a8d0c9149cb346f6 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=83696424cc1d361d118feab76c7daeea 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=140c31b7000ab635c147d40899a1477b 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b6298c53bd547097ea9813245138f6e5 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8c822e6822e839ca25df3d15646e4f02 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bd4e3689bf4b0bcf01a7870457f151b2 2500w" />

        点击 `All` 可以切换查看可以操作的所有内容

                <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b987fe536f542650e7bd16bbb81a9b1a" alt="ComfyUI 维护页面" data-og-width="1213" width="1213" data-og-height="1028" height="1028" data-path="images/desktop/maintenance-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e7ab140496bcd19ccc0b42d881ddfeb2 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d713f7abe3e3f0e803014e23f8007c81 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c7889c0277f2c02c46849515686a09d0 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e5c2fcaddfe6e1f58e22f19342bd3cc8 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e9b8aee2ac65b14724dcfddb210d6cc7 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=429efbb180c2ce8101751b0a27327bcd 2500w" />
      </Tab>
    </Tabs>
  </Step>

  <Step title="Select GPU(GPU选择)">
    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a815bed3616548ac875a6ad832b0d69b" alt="ComfyUI 安装步骤 - GPU 选择" data-og-width="1514" width="1514" data-og-height="1139" height="1139" data-path="images/desktop/win-comfyui-desktop-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7d72433d5f0ea8f617d2c14ec70e0291 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a4607a964fcc3fb923d13f8c65080b11 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=64796c4b32b560385161a5bda8764165 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=36e0b916207c332d7585673506ab132b 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7fd7b5977c69486c65da5d58d577f14a 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=00ee3e6fbf9d7768cdd0531f438438ee 2500w" />
    对应三个选项为：

    1. **Nvidia 显卡（推荐）:** 直接支持使用 pytorch 和 CUDA
    2. **Manual Configuration 手动配置:** 你需要手动安装和配置 python 运行环境，除非你知道应该如何配置，否则请不要选择
    3. **Enable CPU Mode 启用 CPU 模式:** 仅适用于开发人员和特殊情况，除非你确定你需要使用这个模式，否则请不要选择

    如无特殊情况，请按截图所示选择**NVIDIA**，并点击 **Next** 进入下一步
  </Step>

  <Step title="Install location（安装位置）">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=040fa19f9a519d4b96d23b494f2ff8c3" alt="ComfyUI 安装步骤 - 安装位置设置" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2afa0a87a9afa73f172963aa9c09aa51 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=cf2bf3c3412a5f8dd66125d25ce818a7 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=565f8fbd682c8985af3665e0dcc01504 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9e54a85c095c9f5ebebddb8d52b2872a 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8f41c3c89edb4b428c349e51084e7131 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=53ffc127a3f90cdab84bcfd657b6e81e 2500w" />

    在这一步将选择 ComfyUI 以下内容的安装位置：

    * **Python 虚拟环境**
    * **Models 模型文件**
    * **Custom Nodes 自定义节点**

    建议：

    * 请选择**固态硬盘**作为安装位置，这将提高 ComfyUI 访问模型的速度。
    * 请新建一个单独的空白文件夹作为 ComfyUI 的安装目录
    * 请保证对应磁盘至少有 **15G** 左右的磁盘空间，以保证 ComfyUI Desktop 的安装

    <Note>ComfyUI 并非所有文件都安装在此目录下，部分文件依然会安装在 C 盘，后期如需卸载，你可以参考本篇指南的卸载部分完成完整的 ComfyUI 桌面版的卸载</Note>

    完成后点击 **Next** 进入下一步
  </Step>

  <Step title="Migrate from Existing Installation（从已有安装迁移 - 可选）">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d86e70017f3266e2d8ab290f50814967" alt="ComfyUI 安装步骤 - 文件迁移" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9ee204a05ed48a0bdd2b91c34e0549c5 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bca0e1f733cc9f1f3645264974699ce0 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9db8c811a3610b50d221c9dc827dd260 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c5d8407e6eca0f2557dceddc8ef6f388 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=16880b50c70fd120210951b1cc3fc2b1 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e488e02c4b2c099589d1782393af0d10 2500w" />

    在这一步你可以将你已有的 ComfyUI 安装内容迁移到 ComfyUI 桌面版中，如图所示，选择了原本的 **D:\ComfyUI\_windows\_portable\ComfyUI** 安装目录，安装程序会自动识别对应目录下的：

    * **User Files 用户文件**
    * **Models 模型文件:** 不会进行复制，只是与桌面版进行关联
    * **Custom Nodes 自定义节点:** 自定义节点将会重新进行安装

    不要担心，这个步骤并不会复制模型文件，你可以按你的需要勾选或者取消勾选对应的选项，点击 **Next** 进入下一步
  </Step>

  <Step title="Desktop Setting(桌面版设置)">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=daa7e4b3ea6d11d6a157538d3827f34f" alt="ComfyUI 安装步骤 - 桌面版设置" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=fe9d3907ee9e8b498913391b293f87c8 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8f7ea827443427b622e692730ecc2b74 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=de05dc4878a81d7a1697cef7b7b34cb1 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ce780d5f2776d759518b5bd7e78b6929 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bcf6d7f123edf6e6b2c81707171c7579 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=135d0a9b4a86d366ec0bc8343ce2aa3d 2500w" />

    这一步是偏好设置

    1. **Automatic Updates 自动更新:** 是否设置在 ComfyUI 更新可用时自动更新
    2. **Usage Metrics 使用情况分析:** 如果启用，我们将收集**匿名的使用数据** 用于帮助我们改进 ComfyUI
    3. **Mirror Settings 镜像设置:** 由于程序需要联网下载 Python 完成相关环境安装，如果你在安装时候也如图所示出现了红色的❌，提示这可能会导致后续安装过程的失败，则请参考下面步骤进行处理

    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a32fdb0f21efef4aeca85590d019ee38" alt="ComfyUI 安装步骤 - 镜像设置" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7e3f90c9fe0b52d33df0e3f1529f0b8c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=54975797e051816991290d2e8c232177 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=00d77be238cd352fbbeefe9181ded69d 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=731c509d1e8cc4873f53a5321b005434 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5ebdd372eef75c4a9dbc805d69cde27f 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=158391fa1775c73e2fcfa8c6d7bbf3e4 2500w" />
    展开对应的镜像设置，找到具体失败的镜像，在当前截图中错误为 **Python Install Mirror** 镜像失败。

    对于不同的镜像错误，你可以参考下面的内容尝试手动查找不同的镜像，并进行替换

    以下情况主要针对中国境内用户

    #### Python 安装镜像

    如果默认镜像无法使用，请尝试使用下面的镜像

    ```
    https://python-standalone.org/mirror/astral-sh/python-build-standalone
    ```

    如果你需要查找其它备选 GitHub 的镜像地址，请查找并构建指向 `python-build-standalone` 仓库releases的镜像地址

    ```
    https://github.com/astral-sh/python-build-standalone/releases/download
    ```

    构建类似下面格式的链接

    ```
    https://xxx/astral-sh/python-build-standalone/releases/download
    ```

    <info>由于大多 Github 镜像服务都由第三方提供，所以请注意使用过程中的安全性。</info>

    #### PyPI 镜像

    * 阿里云：[https://mirrors.aliyun.com/pypi/simple/](https://mirrors.aliyun.com/pypi/simple/)
    * 腾讯云：[https://mirrors.cloud.tencent.com/pypi/simple/](https://mirrors.cloud.tencent.com/pypi/simple/)
    * 中国科技大学：[https://pypi.mirrors.ustc.edu.cn/simple/](https://pypi.mirrors.ustc.edu.cn/simple/)
    * 上海交通大学：[https://pypi.sjtu.edu.cn/simple/](https://pypi.sjtu.edu.cn/simple/)

    #### Torch 镜像

    * 阿里云: [https://mirrors.aliyun.com/pytorch-wheels/cu121/](https://mirrors.aliyun.com/pytorch-wheels/cu121/)
  </Step>

  <Step title="完成安装">
    如果一切无误，安装程序将完成安装并自动进入 ComfyUI 桌面版界面, 则说明已经安装成功
    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8a86c18801fbede950872e2a26dd4381" alt="ComfyUI 桌面版界面" data-og-width="1678" width="1678" data-og-height="980" height="980" data-path="images/desktop/comfyui-interface.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=efd4befd3f4105de49196f4e568f9dc5 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8d3655f1c724ddfd458d0bc325134399 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4c4bd4537cb38b3de785da3fc375b9da 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ed366119da482d7b4c855cea65f0b0d8 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=751c5c07a0a4c01dc96cfce7356b5673 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4e86835b96ef55a16595ffdcd6b5cf3e 2500w" />
  </Step>
</Steps>

## 重要提示：请勿修改 resource/ComfyUI 文件夹

<Warning>
  请勿在 `/resource/ComfyUI` 文件夹中添加或修改任何内容。此文件夹中的所有内容将在 ComfyUI 桌面版更新时被重置。

  与其他 ComfyUI 版本不同，桌面版会自动管理此文件夹。在安装过程中，你已选择了模型、自定义节点和其他用户文件的自定义存储位置，请使用该位置存放你的文件。
</Warning>

## 进行第一次图片生成

安装成功后，你可以参考访问下面的章节，开始你的 ComfyUI 之路。

<Card title="进行第一次图片生成" icon="link" href="/zh-CN/get_started/first_generation">
  本教程将引导你完成第一次的模型安装以及对应的文本到图片的生成
</Card>

## 如何更新 ComfyUI 桌面版

目前 ComfyUI 桌面版更新采用自动检测更新，请确保在设置中已经启用自动更新

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5006c9c0e4ad3e4f6ca0cef51132fbf3" alt="ComfyUI 桌面版设置" data-og-width="1065" width="1065" data-og-height="815" height="815" data-path="images/desktop/comfyui-desktop-update-setting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=25f0e90e8df014d0640205bb73e4253c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0137407c528ac79439d4320701e4c0b1 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=73f85bd7cbbeeeaeabad54154b60af7e 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4f880973b712a83849b16a78ce5868f5 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=174dc6b670118f452834cece0df52dbd 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1b72afe13029997c797c16772daeff98 2500w" />

你也可以在 `菜单` --> `帮助` --> `检查更新` 中选择手动检查是否有可用的更新

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0f2bf5d6ad204e762ed858f29df4282c" alt="ComfyUI 桌面版检查更新" data-og-width="415" width="415" data-og-height="477" height="477" data-path="images/desktop/desktop_check_for_updates.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c8f28a7f5ef143b0ca31e839187a5a65 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ffef0bd3b488b1545c0390d65ffbd445 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e46efe596b9b5b7f38da68489c245e4c 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9dd9460b2daafd8b398145e1961d668c 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=218f1e5e502286b7a90e21d5f60100fc 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f7e03d947a487ad2a5624f8d14c68e40 2500w" />

## 添加外部模型路径

如果你想要在 `ComfyUI/models` 之外管理你的模型文件，可能出于以下原因:

* 你有多个 ComfyUI 实例，你想要让这些实例共享模型文件，从而减少磁盘占用
* 你有多个不同的类型的 GUI 程序，如：WebUI, 你想要他们共用模型文件
* 模型文件无法被识别或读取到

我们提供了通过 `extra_model_paths.yaml` 配置文件来添加额外模型搜索路径的方法。

### 不同 ComfyUI 版本配置文件位置

<Tabs>
  <Tab title="Portable 及自部署">
    对于[便携版](/zh-CN/installation/comfyui_portable_windows)和[手动安装](/zh-CN/installation/manual_install)的 ComfyUI版本，你可以在 ComfyUI 的根目录下找到 `extra_model_paths.yaml.example` 的示例文件

    ```
    ComfyUI/extra_model_paths.yaml.example
    ```

    复制并重命名为 `extra_model_paths.yaml` 来使用, 并保持在 ComfyUI 的根目录下, 路径应该是 `ComfyUI/extra_model_paths.yaml`

    你也可以在 [这里](https://github.com/comfyanonymous/ComfyUI/blob/master/extra_model_paths.yaml.example) 找到配置示例文件
  </Tab>

  <Tab title="ComfyUI Desktop">
    如果你使用的是 ComfyUI 桌面应用程序，你可以参考下图打开额外模型的配置文件：

        <img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ec4e05559876366ea1e85dba00e98a4b" alt="Open Config File" data-og-width="1072" width="1072" data-og-height="1166" height="1166" data-path="images/zh/desktop/extra_model_paths.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=672b0f4991bd3c0f5e0c50226523f334 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5a1910a0040b6d56f89b56fc1c8c9c57 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=140c5f4a117bc5b8ddbf8c5de4c04b4f 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4980ad35aa2d388a5b4cbdd65cf846f5 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0d6280f2267d23062b6d04bbfba63f39 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/desktop/extra_model_paths.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a4c79b52db5bf34c616e39f8db0dce4c 2500w" />

    或者通过下面的位置打开：

    <Tabs>
      <Tab title="Windows">
        ```
        C:\Users\YourUsername\AppData\Roaming\ComfyUI\extra_models_config.yaml
        ```
      </Tab>

      <Tab title="macOS">
        ```
        ~/Library/Application Support/ComfyUI/extra_models_config.yaml
        ```
      </Tab>
    </Tabs>

    对应的配置文件不应该被改变
  </Tab>
</Tabs>

### 配置示例

比如，你需要额外让 ComfyUI 识别的模型文件位于下面的文件夹:

```
📁 YOUR_PATH/
  ├── 📁models/
  |   ├── 📁 loras/
  |   │   └── xxxxx.safetensors
  |   ├── 📁 checkpoints/
  |   │   └── xxxxx.safetensors
  |   ├── 📁 vae/
  |   │   └── xxxxx.safetensors
  |   └── 📁 controlnet/
  |       └── xxxxx.safetensors
```

那么你可以进行如下的配置来让 ComfyUI 识别到你设备上的模型路径

```
my_custom_config:
    base_path: YOUR_PATH
    loras: models/loras/
    checkpoints: models/checkpoints/
    vae: models/vae/
    controlnet: models/controlnet/
```

或者使用

```
my_custom_config:
    base_path: YOUR_PATH/models/
    loras: loras
    checkpoints: checkpoints
    vae: vae
    controlnet: controlnet
```

<Warning>
  对于桌面版，请在原有配置路径下新增配置，而不覆盖掉安装过程中自动生成的路径配置，请在修改前备份对应的文件，这样在你配置错误时可以及时恢复
</Warning>

或者你也可以参考默认的 [extra\_model\_paths.yaml.example](https://github.com/comfyanonymous/ComfyUI/blob/master/extra_model_paths.yaml.example) 来配置，保存之后， 需要 **重启 ComfyUI** 才能生效。

下面是完整的原始的配置配置示例:

```yaml  theme={null}
#Rename this to extra_model_paths.yaml and ComfyUI will load it


#config for a1111 ui
#all you have to do is change the base_path to where yours is installed
a111:
    base_path: path/to/stable-diffusion-webui/

    checkpoints: models/Stable-diffusion
    configs: models/Stable-diffusion
    vae: models/VAE
    loras: |
         models/Lora
         models/LyCORIS
    upscale_models: |
                  models/ESRGAN
                  models/RealESRGAN
                  models/SwinIR
    embeddings: embeddings
    hypernetworks: models/hypernetworks
    controlnet: models/ControlNet

#config for comfyui
#your base path should be either an existing comfy install or a central folder where you store all of your models, loras, etc.

#comfyui:
#     base_path: path/to/comfyui/
#     # You can use is_default to mark that these folders should be listed first, and used as the default dirs for eg downloads
#     #is_default: true
#     checkpoints: models/checkpoints/
#     clip: models/clip/
#     clip_vision: models/clip_vision/
#     configs: models/configs/
#     controlnet: models/controlnet/
#     diffusion_models: |
#                  models/diffusion_models
#                  models/unet
#     embeddings: models/embeddings/
#     loras: models/loras/
#     upscale_models: models/upscale_models/
#     vae: models/vae/

#other_ui:
#    base_path: path/to/ui
#    checkpoints: models/checkpoints
#    gligen: models/gligen
#    custom_nodes: path/custom_nodes

```

### 添加额外自定义节点路径

除了添加外部模型之外，你同样可以添加不在 ComfyUI 默认路径下的自定义节点路径

<Tip>
  请注意，这并不会改变自定义节点的默认安装路径，只是在启动 ComfyUI 时会增加额外的路径搜索，你仍旧需要在对应的环境中完成自定义节点的依赖的安装，来保证其运行环境的完整性。
</Tip>

下面是一个简单的配置示例（Mac 系统），请根据你的实际情况进行修改，并新增到对应的配置文件中，保存后需要 **重启 ComfyUI** 才能生效:

```yaml  theme={null}
my_custom_nodes:
  custom_nodes: /Users/your_username/Documents/extra_custom_nodes
```

## 桌面端 Python 环境相关

桌面端的安装将在你选择的安装目录下创建一个python 的虚拟环境，通常这是一个隐藏的 `.venv` 文件夹。

如果你需要为 ComfyUI 插件处理相关的依赖则需要在这个环境中进行处理，直接系统系统的命令行会有将对应依赖安装到系统环境的风险，请参考下面的指示完成对应环境的激活。

### 如何使用 桌面端 的 python 环境？

<Tabs>
  <Tab title="Desktop(推荐)">
    你可以使用桌面端自带的终端来使用 python 环境。
    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e82c9f778818d0d33ef7518c536917b6" alt="ComfyUI 桌面版终端" data-og-width="2782" width="2782" data-og-height="1676" height="1676" data-path="images/desktop/desktop_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=dd8c4c7645b64b2ac22c7f8af2e62c82 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=eac1e917bb83fc7f0e62d6c207d303ba 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0ff3ee1451664c14e847068b9441a3cd 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2a5c7e52869e83da9fa03d5744a01965 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ee349a694537302ed8ca2baef5918b8e 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c92df81e233c9a35e996e6384d172c89 2500w" />

    1. 点击菜单栏的 icon 打开底部面板
    2. 点击 `Terminal` 打开终端
    3. 如果你想要看对应环境的 python 安装位置，可以使用下面的命令

    <Tabs>
      <Tab title="Windows">
        ```
          python -c "import sys; print(sys.executable)"
        ```
      </Tab>

      <Tab title="macOS">
        ```
        which python
        ```
      </Tab>
    </Tabs>

    <Warning>
      除非你了解你当前的操作含义，否则你的操作可能会导致对应环境依赖的问题，请谨慎使用此方式进行操作
    </Warning>
  </Tab>

  <Tab title="Terminal">
    你也可以使用你喜欢的终端来使用 python 环境，但在使用之前需要先激活对应的虚拟环境。

    <Warning>
      在使用其它终端进行操作时，如果你不熟悉相关操作，可能会将对应依赖安装到系统环境，请谨慎使用此方式进行操作
    </Warning>

        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=97cbadfa7c28f672be4eba46297a6022" alt="使用系统来激活环境" data-og-width="2620" width="2620" data-og-height="812" height="812" data-path="images/desktop/terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=adaa18b30de61dcf3890bc357e040c56 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7fc0e0be45991b3d40c0d80aa117ebbf 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=38ebbe268f7aec62d1897f473be52b94 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f92065af206e8e4bc75e87873c31e5ab 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=65ff8e5ce0748cf1af9a2ccdcf8e9b37 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c6f7db7fc2ba3497637e39450107b595 2500w" />

    <Warning>
      在截图中，是一个 macOS 终端的示例。如果你使用的是 Windows，请参考以下步骤在系统上激活虚拟环境。
    </Warning>

    <Steps>
      <Step title="打开终端">
        打开你喜欢的终端，使用 `cd` 命令进入你安装的 ComfyUI 的目录如

        ```
        cd <你的 ComfyUI 安装目录>/ComfyUI
        ```
      </Step>

      <Step title="激活虚拟环境">
        在终端中输入下面的命令激活虚拟环境

        <Tabs>
          <Tab title="Windows">
            ```
            .venv/Scripts/activate
            ```
          </Tab>

          <Tab title="macOS">
            ```
            source .venv/bin/activate
            ```
          </Tab>
        </Tabs>

        激活后，你可以在终端中看到类似 `(ComfyUI)` 的提示，表示你已经激活了虚拟环境
      </Step>

      <Step title="确认当前 python 环境">
        使用 `which python` 查看当前 python 所在环境，确认不是系统环境
      </Step>

      完成以上步骤后你就激活了对应的 Python 环境，你可以继续在这个环境里进行依赖安装相关的操作了。
    </Steps>
  </Tab>
</Tabs>

## 如何卸载 ComfyUI 桌面版

对于 **ComfyUI 桌面版** 你可以在 Windows 的系统设置中使用系统的卸载功能来完成对应软件的卸载操作

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a73f165286a128bb0caac36396a68732" alt="ComfyUI 桌面版卸载" data-og-width="1389" width="1389" data-og-height="1008" height="1008" data-path="images/desktop/win-uninstall-comfyui.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5aaa0b596eb6f6a89046d79013258c8c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5a30e2117bea46c000d98d02f4da3bfe 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d9154a7e4cfadc2b04ef83146b163c2f 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4c662269a76cbb5a14fa4edc25bc9f12 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=627a8eccb0bc0c71b4e1a1fd633a9a6d 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3496b1cf52896dcd082de390880435ba 2500w" />

如果你想要完全删除 **ComfyUI 桌面版** 的所有文件，你可以手动删除以下文件夹：

* C:\Users\<你的用户名>\AppData\Local\@comfyorgcomfyui-electron-updater
* C:\Users\<你的用户名>\AppData\Local\Programs\@comfyorgcomfyui-electron
* C:\Users\<你的用户名>\AppData\Roaming\ComfyUI

以上的操作并不会删除以下你的以下文件夹，如果你需要删除对应文件的话，请手动删除：

* models 模型文件
* custom nodes 自定义节点
* input/output directories. 图片输入/输出目录

## 故障排除

### 显示不支持的设备

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b698b91cdff0cca7232fa501f02d0cec" alt="ComfyUI 安装步骤 - 不支持的设备" data-og-width="1646" width="1646" data-og-height="1070" height="1070" data-path="images/desktop/win-comfyui-desktop-0.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1ca5cf563dc51b4c4e394bebfdfe008a 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1e2d44b417e0b06763b23b42629efd9c 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=677fcc1cf15e7ff2035fe02f021a9a76 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=084e4529992f5e5cddb6373176a32594 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=63c01acbc8db2cb8191c2a0f5d9131df 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1344ae04a083b4f841bdf62debe5862b 2500w" />

由于 ComfyUI 桌面版（Windows）仅支持可以使用 **CUDA 的 Nvdia 显卡** 所以如果你的设备不支持，可能会出现此界面

* 请更换使用支持的设备
* 或者考虑使用 [ComfyUI便携版](/zh-CN/installation/comfyui_portable_windows) 或者通过[手动安装](/zh-CN/installation/manual_install)来使用 ComfyUI

### 如何定位安装错误

如果安装失败，你应该可以看到下面的界面显示

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1b5506d072a12fec06e4e8109c07a81f" alt="ComfyUI 安装失败" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4a3b8bc500b1469c23b4e30fcfbd36af 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7c5bae6de3fea5d44ebb66d0ad281cb4 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=49ae6c1de01b136e0da09938f24e4f4a 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0d7c698905502cfd34d159947c177959 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2a1e733756e94307541eee35a9f1eb48 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b4c1159b58a121228ac08e07eb0d2ca0 2500w" />

此时建议你采取以下几种方式查找错误原因

1. 点击 `Show Teriminal` 查看错误问题输出
2. 点击 `Open Logs` 查看安装过程日志
3. 访问官方论坛查找错误反馈
4. 点击`Reinstall`尝试重新安装

建议在提交反馈之前，你可以将对应的**错误输出**以及 **log 文件**信息提供给类似 **GPT**一类的工具

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8775711eafb69c06fd88c068d457d621" alt="ComfyUI 安装失败-错误日志" data-og-width="1514" width="1514" data-og-height="1142" height="1142" data-path="images/desktop/win-comfyui-desktop-8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b3853195bb8599f8e620dba4b7114adb 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a8d720eea46760fadc849f19b6c2512c 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=81c7f420f2882f76da456df6ba22aaa5 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b2a08cedae959954fa063649352ef00e 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b64d43de6e3f62ea1f26da5e16e8b596 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d27bd134c83d62629986a9cbde62b707 2500w" />
<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=cac5f2c54db6f17fde50029a8fcfb315" alt="ComfyUI 安装失败-GPT 反馈" data-og-width="1514" width="1514" data-og-height="1649" height="1649" data-path="images/desktop/win-comfyui-desktop-9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=16ecdec9dee3d9d55167ae26c7e8683b 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=67525d548b448d8b01d7cffe0ccf1a82 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2a722ef5654dcd3b9dc2f5da36077121 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c6c9aa98d5c10df15723b87e52826dc1 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=51ea56d56fc0e764a443515739d59c8d 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5c0d9cd9cf21c16c5d0caa84bdefebd6 2500w" />

如上图，询问对应错误的原因，或者完全删除 ComfyUI 后进行安装重试

### 反馈错误

如果在安装过程中，你发生了任何错误，请通过以下任意方式查看是否有类似错误反馈，或者向我们提交错误

* Github Issues: [https://github.com/Comfy-Org/desktop/issues](https://github.com/Comfy-Org/desktop/issues)
* Comfy 官方论坛: [https://forum.comfy.org/](https://forum.comfy.org/)

请在提交错误时确保提交了以下日志以及配置文件，方便我们进行问题的定位和查找

1. 日志文件

| 文件名         | 描述                                          | 位置           |
| ----------- | ------------------------------------------- | ------------ |
| main.log    | 包含与桌面应用和服务器启动相关的日志，来自桌面的 Electron 进程。       | {log_path_0} |
| comfyui.log | 包含与 ComfyUI 正常运行相关的日志，例如核心 ComfyUI 进程的终端输出。 | {log_path_0} |

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b3d3056cd0203c90712562126a5c204d" alt="ComfyUI 日志文件输出位置" data-og-width="1527" width="1527" data-og-height="987" height="987" data-path="images/desktop/win-comfyui-desktop-10-logs.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=aa2a640d0250582bbf4f5c34fe8ad8c0 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=26647edc8867c1690b6b0d3f3c0c03ce 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=891c9b6f0ec0bc7ee9147da24710ce1c 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2e74c76124371b826f0c8187cdbb2643 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bd30a2c10ead50f539c4c31f7316e306 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=45c116fa61178ae841afe93dd94a9c72 2500w" />

2. 配置文件

| 文件名                      | 描述                           | 位置              |
| ------------------------ | ---------------------------- | --------------- |
| extra\_model\_paths.yaml | 包含 ComfyUI 将搜索模型和自定义节点的额外路径。 | {config_path_0} |
| config.json              | 包含应用配置。此文件通常不应直接编辑。          | {config_path_0} |

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=82fac333832e9222b4534b35131f856d" alt="ComfyUI 配置文件位置" data-og-width="1527" width="1527" data-og-height="987" height="987" data-path="images/desktop/win-comfyui-desktop-11-config.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4391bf98168ae8cc7ba4e11b6d5f6b86 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=35a70d7105699657f74ef7797b520947 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0a21a2c57d59b28159d0f43982badc77 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e23b1a2612b2eb552eb6e1941ce446b2 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3bc2df5c167269238b188f5fd186740d 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=643f71bd078606d366b131255ac6b9a4 2500w" />
