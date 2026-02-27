> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# MacOS Desktop Version

> This article introduces how to download, install and use ComfyUI Desktop for MacOS

export const log_path_0 = "~/Library/Logs/ComfyUI"

export const config_path_0 = "~/Library/Application Support/ComfyUI"

**ComfyUI Desktop** is a standalone installation version that can be installed like regular software.
It supports quick installation and automatic configuration of the **Python environment and dependencies**, and supports one-click import of existing ComfyUI settings, models, workflows, and files.

ComfyUI Desktop is an open source project, please visit the full code [here](https://github.com/Comfy-Org/desktop).

<Note>ComfyUI Desktop (MacOS) only supports Apple Silicon</Note>

This tutorial will guide you through the software installation process and explain related configuration details.

<Warning>As **ComfyUI Desktop** is still in **Beta** status, the actual installation process may change</Warning>

## ComfyUI Desktop (MacOS) Download

Please click the button below to download the installation package for MacOS **ComfyUI Desktop**

<a className="prose" href="https://download.comfy.org/mac/dmg/arm64" style={{ display: 'inline-block', backgroundColor: '#0078D6', color: '#ffffff', padding: '10px 20px', borderRadius: '8px', borderColor: "transparent", textDecoration: 'none', fontWeight: 'bold'}}>
  <p className="prose" style={{ margin: 0, fontSize: "0.8rem" }}>Download for MacOS</p>
</a>

## Install via Homebrew

ComfyUI Desktop can also be installed via [Homebrew](https://brew.sh/):

```
brew install comfyui
```

## ComfyUI Desktop Installation Steps

Double-click the downloaded installation package file. As shown in the image, drag the **ComfyUI** application into the **Applications** folder following the arrow

<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0.png?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=fa83e96d6f26f6b34a71cc103eb38108" alt="ComfyUI Installation Package" data-og-width="883" width="883" data-og-height="698" height="698" data-path="images/desktop/mac-comfyui-desktop-0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0.png?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=fa13c212b5933b36385bb6da53d70a61 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0.png?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=46b7c62de74bb178a0153ab028f7b268 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0.png?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=108cb198b2970fd1745a65163178c246 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0.png?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=70f9b144f45fb6cf10826834d6daa0f6 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0.png?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=0330ac481b350cd691482040000a98b9 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0.png?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=080c2f8dc4a84bd44b11f79e8dcd3008 2500w" />

If your folder shows as below with a prohibition sign on the icon after opening the installation package, it means your current system version is not compatible with **ComfyUI Desktop**
<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0-1.png?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=fe9e4f24ccff7e80553955b6c944d6be" alt="ComfyUI logo" data-og-width="883" width="883" data-og-height="622" height="622" data-path="images/desktop/mac-comfyui-desktop-0-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0-1.png?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3477e8f38233451c9a7df68d0093f024 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0-1.png?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=82d77610a192557cf1fee352deaf9639 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0-1.png?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=cc4b9f5bb63072b70779b7ce3d1822a7 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0-1.png?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=887e714dfa49c83db3fde090359d5884 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0-1.png?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d42ee07a848d3bd61bc405a9c63fdb48 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-0-1.png?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=6896aa942c971fa98062f8239410cfc1 2500w" />

Then find the **ComfyUI icon** in **Launchpad** and click it to enter ComfyUI initialization settings
<img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-1.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a315ed6d739f9a0590a93da64981b32b" alt="ComfyUI Lanchpad" data-og-width="2880" width="2880" data-og-height="1620" height="1620" data-path="images/desktop/mac-comfyui-desktop-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-1.jpg?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4c2285474e2708685f01d74ebdbcf27d 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-1.jpg?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8c500b8fca9d8450a88e74b26a5b5ee4 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-1.jpg?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=344b1b0a40ace630b6dba8a0abbcc049 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-1.jpg?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=9877f40a7db4dc573f9f7ece9cdb7f3c 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-1.jpg?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=cbfe213d92634c15455eb7715b6fe18f 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-1.jpg?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=897e72547a9a9429970b3f31ec7456ea 2500w" />

## ComfyUI Desktop Initialization Process

<Steps>
  <Step title="Start Screen">
    <Tabs>
      <Tab title="Normal Start">
                <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-2.png?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=e9795a772f7cb2d26ddf2de4a111048d" alt="ComfyUI Installation Steps - Start" data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/desktop/mac-comfyui-desktop-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-2.png?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=16930b1bf7346da56bbe2387667d8181 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-2.png?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1745ef37e70f4fae1516a605c250fe2e 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-2.png?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=213e53f6e58625fe8a7eab82b90f640c 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-2.png?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c1e2b9e34fc572a00e08d8b912aadb31 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-2.png?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=00a1747c5b38d51a5b5d34b4517874f3 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-2.png?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=aa9cbfaa0071e65b8cc6e0569a361762 2500w" />

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
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-3.png?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=145a5d5a12bebb15a09f6fda3bca6565" alt="ComfyUI Installation Steps - GPU Selection" data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/desktop/mac-comfyui-desktop-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-3.png?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ffc04c74298a3d9be74786bc32771fed 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-3.png?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8f9825571425df2e1679da68dda2e57c 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-3.png?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b489b601596da8ff6f496366109e8fce 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-3.png?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=76008549ff4e093ee6a20d041f5d6588 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-3.png?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a1d0189f1fdc62b4b1fe339602904d44 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-3.png?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=965f050a4dcb8bf6d77e5bcac6a2bf53 2500w" />

    The three options are:

    1. **MPS (Recommended):** Metal Performance Shaders (MPS) is an Apple framework that uses GPUs to accelerate computing and machine learning tasks on Apple devices, supporting frameworks like PyTorch.
    2. **Manual Configuration:** You need to manually install and configure the python runtime environment. Don't select this unless you know how to configure
    3. **Enable CPU Mode:** For developers and special cases only. Don't select this unless you're sure you need it

    Unless there are special circumstances, please select **MPS** as shown and click **Next** to proceed
  </Step>

  <Step title="Install location">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-4.png?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=29b0e4ee60b6991d5fff478c2f4028bf" alt="ComfyUI Installation Steps - Installation Location" data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/desktop/mac-comfyui-desktop-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-4.png?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3d73b9e85f245091387b95ff1afe29fb 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-4.png?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b2cadffd88abc71d4472c4460b1142fe 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-4.png?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c7a0ce651e528d1adc144994813bacf5 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-4.png?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f5e767661e569c98fea58dba785fac69 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-4.png?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1b43dcfdbf61d62779943b3a05560e02 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-4.png?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=3eaf8a9217a4e2723a6526f0a854f20b 2500w" />

    In this step, you will select the installation location for the following related content of ComfyUI:

    * **Python Environment**
    * **Models Model Files**
    * **Custom Nodes Custom Nodes**

    Recommendations:

    * Please create a separate empty folder as the installation directory for ComfyUI
    * Please ensure that the disk has at least **5G** of disk space to ensure the normal installation of **ComfyUI Desktop**

    <Note>Not all files are installed in this directory, some files will be located in the MacOS system directory, you can refer to the uninstallation section of this guide to complete the uninstallation of the ComfyUI desktop version</Note>
  </Step>

  <Step title="Migrate from Existing Installation (Optional)">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-5.png?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ebd173fbc75978d91f05cab02823fd22" alt="ComfyUI Installation Steps - File Migration" data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/desktop/mac-comfyui-desktop-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-5.png?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d6b54ec77697e1da0b456a22a3affcd9 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-5.png?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c44898a8b41e63d5f6d69d363d6a6564 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-5.png?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=6a9a4a799e132a2406eb075b6d435451 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-5.png?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=20d689d3d5016d8ee24834766a514d5a 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-5.png?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=69e19a8beb0daceed5560180543cf2dd 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-5.png?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=af0c6afcedbd7bd41bb3fc7b23865239 2500w" />

    In this step you can migrate your existing ComfyUI installation content to ComfyUI Desktop. Select your existing ComfyUI installation directory, and the installer will automatically recognize:

    * **User Files**
    * **Models:** Will not be copied, only linked with desktop version
    * **Custom Nodes:** Nodes will be reinstalled

    Don't worry, this step won't copy model files. You can check or uncheck options as needed. Click **Next** to continue
  </Step>

  <Step title="Desktop Settings">
        <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-6.png?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5b0980bf4e43f4b21c4bae613935f59a" alt="ComfyUI Installation Steps - Desktop Settings" data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/desktop/mac-comfyui-desktop-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-6.png?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=8479828672aa40c53a242c988a28b67d 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-6.png?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=34cdd9999fb5fbca40055d03c0a46920 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-6.png?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b0041376f45c6ea72fb1d529f93107ee 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-6.png?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=ced87efe8dedea7e5ed1e70ec7d46a31 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-6.png?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=af40e071cfd4c7e68800526d6b1eb48f 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-6.png?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=b5c515f256bf1733652b550f4c62df8d 2500w" />

    These are preference settings:

    1. **Automatic Updates:** Whether to set automatic updates when ComfyUI updates are available
    2. **Usage Metrics:** If enabled, we will collect **anonymous usage data** to help improve ComfyUI
    3. **Mirror Settings:** Since the program needs internet access to download Python and complete environment installation, if you see a red ❌ during installation indicating this may cause installation failure, please follow the steps below

    <img src="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-7.png?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=5ade3ebbc9231bf38c886abaa26c3e92" alt="ComfyUI Installation Steps - Mirror Settings" data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/desktop/mac-comfyui-desktop-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-7.png?w=280&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=21a5375021f1666eb5f9ce3635296b59 280w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-7.png?w=560&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c8666bf4827f5c69deb2317c879424a4 560w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-7.png?w=840&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4ba0b3e9aa45c78c8cc71d6ac2992dba 840w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-7.png?w=1100&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c8136cef6df6c6d59bc7bc70c45d0f41 1100w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-7.png?w=1650&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=65f2f0bd058e434d07ab700bfe4a11e8 1650w, https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/desktop/mac-comfyui-desktop-7.png?w=2500&fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=4a9febf4d9f6b59a596c265b0d99253b 2500w" />
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

For **ComfyUI Desktop**, you can directly delete **ComfyUI** from the **Applications** folder

If you want to completely remove all **ComfyUI Desktop** files, you can manually delete these folders:

```
~/Library/Application Support/ComfyUI
```

The above operations will not delete your following folders. If you need to delete corresponding files, please delete manually:

* models files
* custom nodes
* input/output directories

## Troubleshooting

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
