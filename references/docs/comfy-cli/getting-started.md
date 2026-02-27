> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started

### Overview

`comfy-cli` is a [command line tool](https://github.com/Comfy-Org/comfy-cli) that makes it easier to install and manage Comfy.

### Install CLI

<CodeGroup>
  ```bash pip theme={null}
  pip install comfy-cli
  ```

  ```bash homebrew theme={null}
  brew tap Comfy-Org/comfy-cli
  brew install comfy-org/comfy-cli/comfy-cli
  ```
</CodeGroup>

To get shell completion hints:

```bash  theme={null}
comfy --install-completion
```

### Install ComfyUI

Create a virtual environment with any Python version greater than 3.9.

<CodeGroup>
  ```bash conda theme={null}
  conda create -n comfy-env python=3.11
  conda activate comfy-env
  ```

  ```bash venv theme={null}
  python3 -m venv comfy-env
  source comfy-env/bin/activate
  ```
</CodeGroup>

Install ComfyUI

```bash  theme={null}
comfy install
```

<Warning>You still need to install CUDA, or ROCm depending on your GPU.</Warning>

### Run ComfyUI

```bash  theme={null}
comfy launch
```

### Manage Custom Nodes

```bash  theme={null}
comfy node install <NODE_NAME>
```

We use `cm-cli` for installing custom nodes. See the [docs](https://github.com/ltdrdata/ComfyUI-Manager/blob/main/docs/en/cm-cli.md) for more information.

### Manage Models

Downloading models with `comfy-cli` is easy. Just run:

```bash  theme={null}
comfy model download <url> models/checkpoints
```

### Contributing

We encourage contributions to comfy-cli! If you have suggestions, ideas, or bug reports, please open an issue on our [GitHub repository](https://github.com/Comfy-Org/comfy-cli/issues). If you want to contribute code, fork the repository and submit a pull request.

Refer to the [Dev Guide](https://github.com/Comfy-Org/comfy-cli/blob/main/DEV_README.md) for further details.

### Analytics

We track usage of the CLI to improve the user experience. You can disable this by running:

```bash  theme={null}
comfy tracking disable
```

To re-enable tracking, run:

```bash  theme={null}
comfy tracking enable
```
