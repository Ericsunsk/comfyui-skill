> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# How to install ComfyUI manually in different systems

For the installation of ComfyUI, it is mainly divided into several steps:

1. Create a virtual environment(avoid polluting the system-level Python environment)
2. Clone the ComfyUI code repository
3. Install dependencies
4. Start ComfyUI

You can also refer to [ComfyUI CLI](/comfy-cli/getting-started) to install ComfyUI, it is a command line tool that can easily install ComfyUI and manage its dependencies.

## Create a virtual environment

<Tip>
  Independent virtual environments are necessary because ComfyUI's dependencies may conflict with other dependencies on the system, and it can also avoid polluting the system-level Python environment.
</Tip>

[Install Miniconda](https://docs.anaconda.com/free/miniconda/index.html#latest-miniconda-installer-links). This will help you install the correct versions of Python and other libraries needed by ComfyUI.

Create an environment with Conda.

```
conda create -n comfyenv
conda activate comfyenv
```

## Clone the ComfyUI code repository

You need to ensure that you have installed [Git](https://git-scm.com/downloads) on your system. First, you need to open the terminal (command line), then clone the code repository.

<Tabs>
  <Tab title="Windows">
    <Warning>If you have not installed Microsoft Visual C++ Redistributable, please install it [here.](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)</Warning>
  </Tab>

  <Tab title="Linux">
    Open Terminal application.
  </Tab>

  <Tab title="MacOS">
    Open [Terminal application](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac).
  </Tab>
</Tabs>

```bash  theme={null}
git clone git@github.com:comfyanonymous/ComfyUI.git
```

## Install GPU and ComfyUI dependencies

<Steps>
  <Step title="Install GPU dependencies">
    Install GPU Dependencies

    <Accordion title="Nvidia">
      ```
      conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
      ```

      Alternatively, you can install the nightly version of PyTorch.

      <Accordion title="Install Nightly">
        <Warning>Install Nightly version (might be more risky)</Warning>

        ```
        conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch-nightly -c nvidia
        ```
      </Accordion>
    </Accordion>

    <Accordion title="AMD">
      ```
      pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0
      ```

      Alternatively, you can install the nightly version of PyTorch.

      <Accordion title="Install Nightly">
        <Warning>Install Nightly version (might be more risky)</Warning>

        ```
        pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.0
        ```
      </Accordion>
    </Accordion>

    <Accordion title="Mac ARM Silicon">
      ```bash  theme={null}
      conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly
      ```
    </Accordion>
  </Step>

  <Step title="Install ComfyUI dependencies">
    ```bash  theme={null}
    cd ComfyUI
    pip install -r requirements.txt
    ```
  </Step>

  <Step title="Start ComfyUI">
    Start the application

    ```
    cd ComfyUI
    python main.py
    ```
  </Step>
</Steps>

## How to update ComfyUI

<Steps>
  <Step title="pull the latest code">
    Use the command line to enter the installation path of ComfyUI, then pull the latest code.

    ```bash  theme={null}
    cd <installation path>/ComfyUI
    git pull
    ```
  </Step>

  <Step title="install the dependencies">
    Use the command line to enter the installation path of ComfyUI, then install the dependencies.

    <Warning>
      You need to ensure that the current Python environment is the ComfyUI virtual environment, otherwise the dependencies will be installed to the system-level Python environment, polluting the system-level Python environment.
    </Warning>

    ```bash  theme={null}
        pip install -r requirements.txt
    ```
  </Step>
</Steps>

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
