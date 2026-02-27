> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows Desktop Version

> This article introduces how to download, install and use ComfyUI Desktop for Windows

export const log_path_0 = "C:\\Users\\<YOUR_USERNAME>\\AppData\\Roaming\\ComfyUI\\logs"

export const config_path_0 = "C:\\Users\\<YOUR_USERNAME>\\AppData\\Roaming\\ComfyUI"

**ComfyUI Desktop** is a standalone installation version that can be installed like regular software. It supports quick installation and automatic configuration of the **Python environment and dependencies**, and supports one-click import of existing ComfyUI settings, models, workflows, and files. You can quickly migrate from an existing [ComfyUI Portable version](/installation/comfyui_portable_windows) to the Desktop version.

ComfyUI Desktop is an open source project, please visit the full code [here](https://github.com/Comfy-Org/desktop)

ComfyUI Desktop hardware requirements:

* NVIDIA GPU

This tutorial will guide you through the software installation process and explain related configuration details.

<Warning>As **ComfyUI Desktop** is still in **Beta** status, the actual installation process may change</Warning>

## ComfyUI Desktop (Windows) Download

Please click the button below to download the installation package for Windows **ComfyUI Desktop**

<a className="prose" href="https://download.comfy.org/windows/nsis/x64" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download for Windows (NVIDIA)</p>
</a>

## ComfyUI Desktop Installation Steps

Double-click the downloaded installation package file, which will first perform an automatic installation and create a **ComfyUI Desktop** shortcut on the desktop

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=91d39867b16a2c5eb803fe2f26cee5bf" alt="ComfyUI logo" data-og-width="731" width="731" data-og-height="486" height="486" data-path="images/desktop/win-comfyui-desktop-shortcut.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9875d7185aebb25f478f1cb94571577c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=01c8b6ba2b24ae54115a3b92667b479a 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=04f19ebfbab1e9726de3bad4e31897ec 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=619e79aab66bd8480a6afe25f37f9350 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=031f8da7cb83b0feca9318fd457f4fd7 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-shortcut.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8083e0b55c8c313c4b26b311f868ae6d 2500w" />

Double-click the corresponding shortcut to enter ComfyUI initialization settings

### ComfyUI Desktop Initialization Process

<Steps>
  <Step title="Start Screen">
    <Tabs>
      <Tab title="Normal Start">
                <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=778c2d6e0d08a961278a5d0f917221d4" alt="ComfyUI Installation Steps - Start" data-og-width="1514" width="1514" data-og-height="1139" height="1139" data-path="images/desktop/win-comfyui-desktop-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5ce5b27d7ef8c915cf92fa225b1744f4 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0c30ea772deb01623140ad0471567b2b 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ba471670151c04fb3fbbbcd087946a6b 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=59102ff039ce2a93492b4de598de3025 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0fe3497ddf26ef941457be73f7de7c6c 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-1.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=532407419f6d37ce88536749c29321af 2500w" />

        Click **Get Started** to begin initialization
      </Tab>

      <Tab title="Maintenance Page">
        There are many reasons you might have issues installing ComfyUI. Maybe a network connection failed when installing pytorch (15 GB). Or you don’t have git installed. The maintenance page automatically opens when it detects an issue and provides a way to resolve the issue.

        You can use it to resolve most issues:

        * Create a python virtual environment
        * Reinstall all missing core dependencies to your Python virtual environment that’s managed by Desktop
        * Install git, VC redis
        * Choose a new install location

        The default maintenance page displays the current error content

                <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2a01daff7808d4d342aeb423a072308f" alt="ComfyUI Maintenance Page" data-og-width="971" width="971" data-og-height="715" height="715" data-path="images/desktop/maintenance-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=6e97afdce4ad87e3a8d0c9149cb346f6 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=83696424cc1d361d118feab76c7daeea 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=140c31b7000ab635c147d40899a1477b 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b6298c53bd547097ea9813245138f6e5 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8c822e6822e839ca25df3d15646e4f02 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-1.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bd4e3689bf4b0bcf01a7870457f151b2 2500w" />

        Clicking `All` allows you to view all the content that can be operated on currently

                <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b987fe536f542650e7bd16bbb81a9b1a" alt="ComfyUI Maintenance Page" data-og-width="1213" width="1213" data-og-height="1028" height="1028" data-path="images/desktop/maintenance-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e7ab140496bcd19ccc0b42d881ddfeb2 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d713f7abe3e3f0e803014e23f8007c81 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c7889c0277f2c02c46849515686a09d0 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e5c2fcaddfe6e1f58e22f19342bd3cc8 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e9b8aee2ac65b14724dcfddb210d6cc7 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/maintenance-2.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=429efbb180c2ce8101751b0a27327bcd 2500w" />
      </Tab>
    </Tabs>
  </Step>

  <Step title="Select GPU">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a815bed3616548ac875a6ad832b0d69b" alt="ComfyUI Installation Steps - GPU Selection" data-og-width="1514" width="1514" data-og-height="1139" height="1139" data-path="images/desktop/win-comfyui-desktop-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7d72433d5f0ea8f617d2c14ec70e0291 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a4607a964fcc3fb923d13f8c65080b11 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=64796c4b32b560385161a5bda8764165 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=36e0b916207c332d7585673506ab132b 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7fd7b5977c69486c65da5d58d577f14a 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-2.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=00ee3e6fbf9d7768cdd0531f438438ee 2500w" />

    The three options are:

    1. **Nvidia GPU (Recommended):** Direct support for pytorch and CUDA
    2. **Manual Configuration:** You need to manually install and configure the python runtime environment. Don't select this unless you know how to configure
    3. **Enable CPU Mode:** For developers and special cases only. Don't select this unless you're sure you need it

    Unless there are special circumstances, please select **NVIDIA** as shown and click **Next** to proceed
  </Step>

  <Step title="Install location">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=040fa19f9a519d4b96d23b494f2ff8c3" alt="ComfyUI Installation Steps - Installation Location" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2afa0a87a9afa73f172963aa9c09aa51 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=cf2bf3c3412a5f8dd66125d25ce818a7 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=565f8fbd682c8985af3665e0dcc01504 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9e54a85c095c9f5ebebddb8d52b2872a 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8f41c3c89edb4b428c349e51084e7131 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-3.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=53ffc127a3f90cdab84bcfd657b6e81e 2500w" />

    In this step, you will select the installation location for the following ComfyUI content:

    * **Python Environment**
    * **Models Model Files**
    * **Custom Nodes Custom Nodes**

    Recommendations:

    * Please select a **solid-state drive** as the installation location, which will increase ComfyUI's performance when accessing models.
    * Please create a separate empty folder as the ComfyUI installation directory
    * Please ensure that the corresponding disk has at least around **15G** of disk space to ensure the installation of ComfyUI Desktop

    <Note>Not all files are installed in this directory, some files will still be installed on the C drive, and if you need to uninstall in the future, you can refer to the uninstallation section of this guide to complete the full uninstallation of ComfyUI Desktop</Note>

    After completing this step, click **Next** to proceed to the next step
  </Step>

  <Step title="Migrate from Existing Installation (Optional)">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d86e70017f3266e2d8ab290f50814967" alt="ComfyUI Installation Steps - File Migration" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9ee204a05ed48a0bdd2b91c34e0549c5 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bca0e1f733cc9f1f3645264974699ce0 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9db8c811a3610b50d221c9dc827dd260 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c5d8407e6eca0f2557dceddc8ef6f388 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=16880b50c70fd120210951b1cc3fc2b1 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-4.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e488e02c4b2c099589d1782393af0d10 2500w" />

    In this step you can migrate your existing ComfyUI installation content to ComfyUI Desktop. As shown, I selected my original **D:\ComfyUI\_windows\_portable\ComfyUI** installation directory. The installer will automatically recognize:

    * **User Files**
    * **Models:** Will not be copied, only linked with desktop version
    * **Custom Nodes:** Nodes will be reinstalled

    Don't worry, this step won't copy model files. You can check or uncheck options as needed. Click **Next** to continue
  </Step>

  <Step title="Desktop Settings">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=daa7e4b3ea6d11d6a157538d3827f34f" alt="ComfyUI Installation Steps - Desktop Settings" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=fe9d3907ee9e8b498913391b293f87c8 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8f7ea827443427b622e692730ecc2b74 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=de05dc4878a81d7a1697cef7b7b34cb1 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ce780d5f2776d759518b5bd7e78b6929 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bcf6d7f123edf6e6b2c81707171c7579 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-5.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=135d0a9b4a86d366ec0bc8343ce2aa3d 2500w" />

    These are preference settings:

    1. **Automatic Updates:** Whether to set automatic updates when ComfyUI updates are available
    2. **Usage Metrics:** If enabled, we will collect **anonymous usage data** to help improve ComfyUI
    3. **Mirror Settings:** Since the program needs internet access to download Python and complete environment installation, if you see a red ❌ during installation indicating this may cause installation failure, please follow the steps below

    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a32fdb0f21efef4aeca85590d019ee38" alt="ComfyUI Installation Steps - Mirror Settings" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7e3f90c9fe0b52d33df0e3f1529f0b8c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=54975797e051816991290d2e8c232177 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=00d77be238cd352fbbeefe9181ded69d 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=731c509d1e8cc4873f53a5321b005434 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5ebdd372eef75c4a9dbc805d69cde27f 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-6.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=158391fa1775c73e2fcfa8c6d7bbf3e4 2500w" />
    Expand the mirror settings to find the specific failing mirror. In this screenshot the error is **Python Install Mirror** failure.

    For different mirror errors, you can refer to the following content to try to manually find different mirrors and replace them

    The following cases mainly apply to users in China.

    #### Python Installation Mirror

    If the default mirror is unavailable, please try using the mirror below.

    ```
    https://python-standalone.org/mirror/astral-sh/python-build-standalone
    ```

    If you need to find other alternative GitHub mirror addresses, please look for and construct a mirror address pointing to the releases of the `python-build-standalone` repository.

    ```
    https://github.com/astral-sh/python-build-standalone/releases/download
    ```

    Build a link in the following pattern

    ```
    https://xxx/astral-sh/python-build-standalone/releases/download
    ```

    <info>Since most of the Github mirror services are provided by third parties, please pay attention to the security during use.</info>

    #### PyPI Mirror

    * Alibaba Cloud: [https://mirrors.aliyun.com/pypi/simple/](https://mirrors.aliyun.com/pypi/simple/)
    * Tencent Cloud: [https://mirrors.cloud.tencent.com/pypi/simple/](https://mirrors.cloud.tencent.com/pypi/simple/)
    * University of Science and Technology of China: [https://pypi.mirrors.ustc.edu.cn/simple/](https://pypi.mirrors.ustc.edu.cn/simple/)
    * Shanghai Jiao Tong University: [https://pypi.sjtu.edu.cn/simple/](https://pypi.sjtu.edu.cn/simple/)

    #### Torch Mirror

    * Aliyun: [https://mirrors.aliyun.com/pytorch-wheels/cu121/](https://mirrors.aliyun.com/pytorch-wheels/cu121/)
  </Step>

  <Step title="Complete the installation">
    If everything is correct, the installer will complete and automatically enter the ComfyUI Desktop interface, then the installation is successful
    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8a86c18801fbede950872e2a26dd4381" alt="ComfyUI Desktop Interface" data-og-width="1678" width="1678" data-og-height="980" height="980" data-path="images/desktop/comfyui-interface.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=efd4befd3f4105de49196f4e568f9dc5 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8d3655f1c724ddfd458d0bc325134399 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4c4bd4537cb38b3de785da3fc375b9da 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ed366119da482d7b4c855cea65f0b0d8 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=751c5c07a0a4c01dc96cfce7356b5673 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-interface.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4e86835b96ef55a16595ffdcd6b5cf3e 2500w" />
  </Step>
</Steps>

## Important: Do not modify the resource/ComfyUI folder

<Warning>
  Do not add or modify any content in the `/resource/ComfyUI` folder. All content in this folder will be reset when ComfyUI Desktop updates.

  Unlike other ComfyUI versions, the Desktop version manages this folder automatically. During installation, you chose a custom location for your models, custom nodes, and other user files - please use that location instead.
</Warning>

## First Image Generation

After successful installation, you can refer to the section below to start your ComfyUI journey\~

<Card title="First Image Generation" icon="link" href="/get_started/first_generation">
  This tutorial will guide you through your first model installation and text-to-image generation
</Card>

## How to Update ComfyUI Desktop

Currently, ComfyUI Desktop updates use automatic detection updates, please ensure that automatic updates are enabled in the settings

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5006c9c0e4ad3e4f6ca0cef51132fbf3" alt="ComfyUI Desktop Settings" data-og-width="1065" width="1065" data-og-height="815" height="815" data-path="images/desktop/comfyui-desktop-update-setting.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=25f0e90e8df014d0640205bb73e4253c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0137407c528ac79439d4320701e4c0b1 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=73f85bd7cbbeeeaeabad54154b60af7e 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4f880973b712a83849b16a78ce5868f5 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=174dc6b670118f452834cece0df52dbd 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/comfyui-desktop-update-setting.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1b72afe13029997c797c16772daeff98 2500w" />

You can also choose to manually check for available updates in the `Menu` --> `Help` --> `Check for Updates`

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0f2bf5d6ad204e762ed858f29df4282c" alt="ComfyUI Desktop Check for Updates" data-og-width="415" width="415" data-og-height="477" height="477" data-path="images/desktop/desktop_check_for_updates.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c8f28a7f5ef143b0ca31e839187a5a65 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ffef0bd3b488b1545c0390d65ffbd445 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e46efe596b9b5b7f38da68489c245e4c 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9dd9460b2daafd8b398145e1961d668c 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=218f1e5e502286b7a90e21d5f60100fc 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_check_for_updates.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f7e03d947a487ad2a5624f8d14c68e40 2500w" />

## Adding Extra Model Paths

If you want to manage your model files outside of `ComfyUI/models`, you may have the following reasons:

* You have multiple ComfyUI instances and want them to share model files to save disk space
* You have different types of GUI programs (such as WebUI) and want them to use the same model files
* Model files cannot be recognized or found

We provide a way to add extra model search paths via the `extra_model_paths.yaml` configuration file

### Open Config File

<Tabs>
  <Tab title="Portable/Manual Install">
    For the ComfyUI version such as [portable](/installation/comfyui_portable_windows) and [manual](/installation/manual_install), you can find an example file named `extra_model_paths.yaml.example` in the root directory of ComfyUI:

    ```
    ComfyUI/extra_model_paths.yaml.example
    ```

    Copy and rename it to `extra_model_paths.yaml` for use. Keep it in ComfyUI's root directory at `ComfyUI/extra_model_paths.yaml`.
    You can also find the config example file [here](https://github.com/comfyanonymous/ComfyUI/blob/master/extra_model_paths.yaml.example)
  </Tab>

  <Tab title="ComfyUI Desktop">
    If you are using the [ComfyUI Desktop](/installation/desktop/windows) application, you can follow the image below to open the extra model config file:

        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/extra_model_paths.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b2a08255f65a32e3da0c018a3cebb6a2" alt="Open Config File" data-og-width="1056" width="1056" data-og-height="1166" height="1166" data-path="images/desktop/extra_model_paths.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/extra_model_paths.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4f4044b7cef96f0f4a70e7d8a0eb007a 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/extra_model_paths.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=aa576e31096b7306e810c10c97416ad5 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/extra_model_paths.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ff8461eb13a9cec15293e7c5663bc65c 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/extra_model_paths.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2bf5a5335edfa58f37652bfed7a7dc9 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/extra_model_paths.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a1a4c2d6fd021f4a348ea95c4abb5871 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/extra_model_paths.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f508c6130dd86ec9adbef19aaf0d2530 2500w" />

    Or open it directly at:

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

    You should keep the file in the same directory, should not move these files to other places.
  </Tab>
</Tabs>

If the file does not exist, you can create it yourself with any text editor.

### Example Structure

Suppose you want to add the following model paths to ComfyUI:

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

Then you can configure the `extra_model_paths.yaml` file like below to let ComfyUI recognize the model paths on your device:

```
my_custom_config:
    base_path: YOUR_PATH
    loras: models/loras/
    checkpoints: models/checkpoints/
    vae: models/vae/
    controlnet: models/controlnet/
```

or

```
my_custom_config:
    base_path: YOUR_PATH/models/
    loras: loras
    checkpoints: checkpoints
    vae: vae
    controlnet: controlnet
```

<Warning>
  For the desktop version, please add the configuration to the existing configuration path without overwriting the path configuration generated during installation. Please back up the corresponding file before modification, so that you can restore it when you make a mistake.
</Warning>

Or you can refer to the default [extra\_model\_paths.yaml.example](https://github.com/comfyanonymous/ComfyUI/blob/master/extra_model_paths.yaml.example) for more configuration options. After saving, you need to **restart ComfyUI** for the changes to take effect.

Below is the original config example:

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

For example, if your WebUI is located at `D:\stable-diffusion-webui\`, you can modify the corresponding configuration to

```yaml  theme={null}
a111:
    base_path: D:\stable-diffusion-webui\
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
```

### Add Extra Custom Nodes Path

Besides adding external models, you can also add custom nodes paths that are not in the default path of ComfyUI

<Tip>
  Please note that this will not change the default installation path of custom nodes, but will add an extra path search when starting ComfyUI. You still need to complete the installation of custom node dependencies in the corresponding environment to ensure the integrity of the running environment.
</Tip>

Below is a simple configuration example (MacOS), please modify it according to your actual situation and add it to the corresponding configuration file, save it and restart ComfyUI for the changes to take effect:

```yaml  theme={null}
my_custom_nodes:
  custom_nodes: /Users/your_username/Documents/extra_custom_nodes
```

## Desktop Python Environment

The desktop installation will create a Python virtual environment in your chosen installation directory, typically a hidden `.venv` folder.

If you need to handle dependencies for ComfyUI plugins, you'll need to do so within this environment. Using the system command line directly risks installing dependencies to the system environment, so please follow the instructions below to activate the appropriate environment.

### How to use the Desktop Python environment?

<Tabs>
  <Tab title="Desktop (Recommended)">
    You can use the built-in terminal in the desktop app to access the Python environment.
    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e82c9f778818d0d33ef7518c536917b6" alt="ComfyUI Desktop Terminal" data-og-width="2782" width="2782" data-og-height="1676" height="1676" data-path="images/desktop/desktop_terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=dd8c4c7645b64b2ac22c7f8af2e62c82 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=eac1e917bb83fc7f0e62d6c207d303ba 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0ff3ee1451664c14e847068b9441a3cd 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2a5c7e52869e83da9fa03d5744a01965 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ee349a694537302ed8ca2baef5918b8e 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/desktop_terminal.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c92df81e233c9a35e996e6384d172c89 2500w" />

    1. Click the icon in the menu bar to open the bottom panel
    2. Click `Terminal` to open the terminal
    3. If you want to check the Python installation location for the corresponding environment, you can use the following command

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
      Unless you understand the meaning of your current operations, your actions may cause dependency issues in the corresponding environment. Please use this method with caution.
    </Warning>
  </Tab>

  <Tab title="Terminal">
    You can also use your preferred terminal to access the Python environment, but you'll need to activate the virtual environment first.

    <Warning>
      When using other terminals, if you're not familiar with the operations, you may accidentally install dependencies to the system environment. Please use this method with caution.
    </Warning>

        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=97cbadfa7c28f672be4eba46297a6022" alt="Using system to activate environment" data-og-width="2620" width="2620" data-og-height="812" height="812" data-path="images/desktop/terminal.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=adaa18b30de61dcf3890bc357e040c56 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7fc0e0be45991b3d40c0d80aa117ebbf 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=38ebbe268f7aec62d1897f473be52b94 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f92065af206e8e4bc75e87873c31e5ab 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=65ff8e5ce0748cf1af9a2ccdcf8e9b37 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/terminal.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c6f7db7fc2ba3497637e39450107b595 2500w" />

    <Warning>
      In the screenshot, it shows a macOS terminal. If you are using Windows, please refer to the following steps to activate the virtual environment on your system.
    </Warning>

    <Steps>
      <Step title="Open Terminal">
        Open your preferred terminal and use the `cd` command to navigate to your ComfyUI installation directory, for example:

        ```
        cd <your comfyui install directory>/ComfyUI
        ```
      </Step>

      <Step title="Activate Virtual Environment">
        Type the following command in the terminal to activate the virtual environment

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

        After activation, you should see a prompt like `(ComfyUI)` in the terminal, indicating that you've activated the virtual environment.
      </Step>

      <Step title="Confirm Current Python Environment">
        Use `which python` to check the current Python installation location and confirm it's not the system environment.
      </Step>

      After completing these steps, you've activated the corresponding Python environment, and you can continue to perform dependency installation operations in this environment.
    </Steps>
  </Tab>
</Tabs>

## How to Uninstall ComfyUI Desktop

For **ComfyUI Desktop** you can use the system uninstall function in Windows Settings to complete software uninstallation

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a73f165286a128bb0caac36396a68732" alt="ComfyUI Desktop Uninstallation" data-og-width="1389" width="1389" data-og-height="1008" height="1008" data-path="images/desktop/win-uninstall-comfyui.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5aaa0b596eb6f6a89046d79013258c8c 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5a30e2117bea46c000d98d02f4da3bfe 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d9154a7e4cfadc2b04ef83146b163c2f 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4c662269a76cbb5a14fa4edc25bc9f12 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=627a8eccb0bc0c71b4e1a1fd633a9a6d 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-uninstall-comfyui.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3496b1cf52896dcd082de390880435ba 2500w" />

If you want to completely remove all **ComfyUI Desktop** files, you can manually delete these folders:

* C:\Users\<YOUR\_USERNAME>\AppData\Local\@comfyorgcomfyui-electron-updater
* C:\Users\<YOUR\_USERNAME>\AppData\Local\Programs\@comfyorgcomfyui-electron
* C:\Users\<YOUR\_USERNAME>\AppData\Roaming\ComfyUI

The above operations will not delete your following folders. If you need to delete corresponding files, please delete manually:

* models files
* custom nodes
* input/output directories

## Troubleshooting

### Display unsupported devices

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b698b91cdff0cca7232fa501f02d0cec" alt="ComfyUI Installation Steps - Unsupported Device" data-og-width="1646" width="1646" data-og-height="1070" height="1070" data-path="images/desktop/win-comfyui-desktop-0.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1ca5cf563dc51b4c4e394bebfdfe008a 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1e2d44b417e0b06763b23b42629efd9c 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=677fcc1cf15e7ff2035fe02f021a9a76 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=084e4529992f5e5cddb6373176a32594 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=63c01acbc8db2cb8191c2a0f5d9131df 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-0.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1344ae04a083b4f841bdf62debe5862b 2500w" />

Since ComfyUI Desktop (Windows) only supports **NVIDIA GPUs with CUDA**, you may see this screen if your device is not supported

* Please switch to a supported device
* Or consider using [ComfyUI Portable](/installation/comfyui_portable_windows) or through [manual installation](/installation/manual_install) to use ComfyUI

### ​Error identification​

If installation fails, you should see the following screen

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1b5506d072a12fec06e4e8109c07a81f" alt="ComfyUI Installation Failed" data-og-width="1514" width="1514" data-og-height="1103" height="1103" data-path="images/desktop/win-comfyui-desktop-7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4a3b8bc500b1469c23b4e30fcfbd36af 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7c5bae6de3fea5d44ebb66d0ad281cb4 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=49ae6c1de01b136e0da09938f24e4f4a 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0d7c698905502cfd34d159947c177959 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2a1e733756e94307541eee35a9f1eb48 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-7.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b4c1159b58a121228ac08e07eb0d2ca0 2500w" />

It is recommended to take these steps to find the error cause:

1. Click `Show Terminal` to view error output
2. Click `Open Logs` to view installation logs
3. Visit official forum to search for error reports
4. Click `Reinstall` to try reinstalling

Before submitting feedback, it's recommended to provide the **error output** and **log files** to tools like **GPT**

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8775711eafb69c06fd88c068d457d621" alt="ComfyUI Installation Failed - Error Log" data-og-width="1514" width="1514" data-og-height="1142" height="1142" data-path="images/desktop/win-comfyui-desktop-8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b3853195bb8599f8e620dba4b7114adb 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a8d720eea46760fadc849f19b6c2512c 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=81c7f420f2882f76da456df6ba22aaa5 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b2a08cedae959954fa063649352ef00e 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b64d43de6e3f62ea1f26da5e16e8b596 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-8.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d27bd134c83d62629986a9cbde62b707 2500w" />
<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=cac5f2c54db6f17fde50029a8fcfb315" alt="ComfyUI Installation Failed - GPT Feedback" data-og-width="1514" width="1514" data-og-height="1649" height="1649" data-path="images/desktop/win-comfyui-desktop-9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=16ecdec9dee3d9d55167ae26c7e8683b 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=67525d548b448d8b01d7cffe0ccf1a82 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2a722ef5654dcd3b9dc2f5da36077121 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c6c9aa98d5c10df15723b87e52826dc1 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=51ea56d56fc0e764a443515739d59c8d 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-9.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5c0d9cd9cf21c16c5d0caa84bdefebd6 2500w" />

As shown above, ask the GPT for the cause of the corresponding error, or remove ComfyUI completely and retry the installation.

### Feedback Installation Failure

If you encounter any errors during installation, please check if there are similar error reports or submit errors to us through:

* Github Issues: [https://github.com/Comfy-Org/desktop/issues](https://github.com/Comfy-Org/desktop/issues)
* Comfy Official Forum: [https://forum.comfy.org/](https://forum.comfy.org/)

When submitting error reports, please ensure you include the following logs and configuration files to help us locate and investigate the issue:

1. Log Files

| Filename    | Description                                                                                     | Location     |
| ----------- | ----------------------------------------------------------------------------------------------- | ------------ |
| main.log    | Contains logs related to desktop application and server startup from the Electron process       | {log_path_0} |
| comfyui.log | Contains logs related to ComfyUI normal operation, such as core ComfyUI process terminal output | {log_path_0} |

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b3d3056cd0203c90712562126a5c204d" alt="ComfyUI Log Files Location" data-og-width="1527" width="1527" data-og-height="987" height="987" data-path="images/desktop/win-comfyui-desktop-10-logs.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=aa2a640d0250582bbf4f5c34fe8ad8c0 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=26647edc8867c1690b6b0d3f3c0c03ce 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=891c9b6f0ec0bc7ee9147da24710ce1c 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2e74c76124371b826f0c8187cdbb2643 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=bd30a2c10ead50f539c4c31f7316e306 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-10-logs.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=45c116fa61178ae841afe93dd94a9c72 2500w" />

2. Configuration Files

| Filename                 | Description                                                                     | Location        |
| ------------------------ | ------------------------------------------------------------------------------- | --------------- |
| extra\_model\_paths.yaml | Contains additional paths where ComfyUI will search for models and custom nodes | {config_path_0} |
| config.json              | Contains application configuration. This file should not be edited directly     | {config_path_0} |

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=82fac333832e9222b4534b35131f856d" alt="ComfyUI Config Files Location" data-og-width="1527" width="1527" data-og-height="987" height="987" data-path="images/desktop/win-comfyui-desktop-11-config.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4391bf98168ae8cc7ba4e11b6d5f6b86 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=35a70d7105699657f74ef7797b520947 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0a21a2c57d59b28159d0f43982badc77 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e23b1a2612b2eb552eb6e1941ce446b2 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3bc2df5c167269238b188f5fd186740d 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/win-comfyui-desktop-11-config.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=643f71bd078606d366b131255ac6b9a4 2500w" />
