> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 发布节点

## 设置注册表账户

按照以下步骤设置注册表账户并发布您的第一个节点。

### 观看教程

<iframe height="415" src="https://www.youtube.com/embed/WhOZZOgBggU?si=6TyvhJJadmQ65uXC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style={{ width: "100%", borderRadius: "0.5rem" }} />

### 创建发布者

发布者是一个可以向注册表(registry)发布自定义节点的身份。每个自定义节点都需要在 pyproject.toml [文件]() 中包含发布者标识符。

访问 [Comfy Registry](https://registry.comfy.org)，创建一个发布者账户。您的发布者 ID 是全球唯一的，并且之后不能更改，因为它用于您的自定义节点的 URL 中。

您的发布者 ID 可以在个人资料页面上 `@` 符号后面找到。

<img className="block" src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=95e3271276938f1ec1226f172ffc020f" alt="Hero Dark" data-og-width="534" width="534" data-og-height="342" height="342" data-path="images/publisherid.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=aafd181c16f25d66961b717fb46b77e8 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=618357651a7a64a0f90d31227ba4295b 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=743c9a3f2b3c387aee9f668169e8b21f 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a2bd945881111904b91bde24daa733f3 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=511f7245307d7569caeedfd0781864cc 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=f2cc85d730f5fd90c59d8d198c2e623d 2500w" />

### 创建注册表发布 API Key

<Note>
  **重要提示:** 此 API 密钥专门用于**将自定义节点发布到注册表和 ComfyUI-Manager**。如果您想在工作流中使用付费 API 节点,请参阅 [API 节点总览](/zh-CN/tutorials/partner-nodes/overview)。
</Note>

访问[这里](https://registry.comfy.org/nodes)并点击你想要为其创建 API 密钥的发布者。此密钥将用于通过 CLI 或 GitHub Actions 将自定义节点发布到注册表（为 ComfyUI-Manager 提供支持）。

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6f9c94583f78457419cfde793f49f387" alt="为特定发布者创建密钥" data-og-width="295" width="295" data-og-height="159" height="159" data-path="images/pat-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=11fb3f0cf7bb78bee430c7f46acdd856 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ab9b38ebab6988131e095f953b453b23 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=f1ab93bd727e4867871910d15dfcd8ac 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=593cbe8448b237f88b299862bb93603d 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=d16bea3a955600aa59999dfdd0abaa01 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=1367f355a0557b74b236392c35521a3e 2500w" />

为 API 密钥命名并将其安全保存。如果密钥丢失了它，请重新创建一个新的密钥。

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=490347389e83b978f4c65b0e6a7b5d33" alt="创建 API 密钥" data-og-width="526" width="526" data-og-height="474" height="474" data-path="images/pat-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=9b69fd6494a9bb03f31ec26e4360ef88 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=b0aa3c4774cd80af6018e52f3decff9f 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3a7dd425166cabb9abbdcda3687a9dad 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=0bbe8642a1be3bd3d96659723590c5f9 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=994cdedbfa26a483463ccbaf65871e87 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=be07aee07dc86c5a196c5babb2da69ec 2500w" />

### 添加元数据

<Tip>
  安装 comfy-cli了吗？
  如果没有请 [先安装它](/zh-CN/comfy-cli/getting-started)。
</Tip>

```bash  theme={null}
comfy node init
```

这个命令将会生成下面这样的元数据：

```toml  theme={null}
# pyproject.toml
[project]
name = "" # Unique identifier for your node. Immutable after creation.
description = ""
version = "1.0.0" # Custom Node version. Must be semantically versioned.
license = { file = "LICENSE.txt" }
dependencies  = [] # Filled in from requirements.txt

[project.urls]
Repository = "https://github.com/..."

[tool.comfy]
PublisherId = "" # TODO (fill in Publisher ID from Comfy Registry Website).
DisplayName = "" # Display name for the Custom Node. Can be changed later.
Icon = "https://example.com/icon.png" # SVG, PNG, JPG or GIF (MAX. 800x400px)
```

将此文件添加到您的仓库中。查看[规范](/zh-CN/registry/specifications)以获取有关 pyproject.toml 文件的更多信息。

## 发布到注册表(registry)

### 选项 1: Comfy CLI

运行下面的命令手动将您的节点发布到注册表。

```bash  theme={null}
comfy node publish
```

会被提示要求输入 API 密钥。

```bash  theme={null}
API Key for publisher '<publisher id>': ****************************************************

...Version 1.0.0 Published. 
See it here: https://registry.comfy.org/publisherId/your-node
```

<Warning>
  请记住，API 密钥默认是隐藏的。
</Warning>

<Warning>
  当使用 CTRL+V 复制粘贴时，您的 API 密钥可能会有一个额外的 \x16 在后面，例如： \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\x16。

  建议通过右键点击复制粘贴您的 API 密钥。
</Warning>

### 选项 2: Github Actions

通过 Github Actions 自动发布您的节点。

<Steps>
  <Step title="设置一个 Github Secret">
    前往 Settings -> Secrets and Variables -> Actions -> Under Secrets Tab and Repository secrets -> New Repository Secret.

    创建一个名为 `REGISTRY_ACCESS_TOKEN` 的 secret 并存储您的 API 密钥作为值。
  </Step>

  <Step title="创建一个 Github Action">
    复制下面的代码并粘贴到 `/.github/workflows/publish_action.yml`

    ```bash  theme={null}
    name: Publish to Comfy registry
    on:
      workflow_dispatch:
      push:
        branches:
          - main
        paths:
          - "pyproject.toml"

    jobs:
      publish-node:
        name: Publish Custom Node to registry
        runs-on: ubuntu-latest
        steps:
          - name: Check out code
            uses: actions/checkout@v4
          - name: Publish Custom Node
            uses: Comfy-Org/publish-node-action@main
            with:
              personal_access_token: ${{ secrets.REGISTRY_ACCESS_TOKEN }} ## Add your own personal access token to your Github Repository secrets and reference it here.
    ```

    <Warning>
      如果您的分支名称不是 `main`，例如 `master`，请在 branches 部分添加名称。
    </Warning>
  </Step>

  <Step title="测试 Github Action">
    推送到您的 `pyproject.toml` 的版本号。您应该在注册表中看到您的更新节点。

    <Tip>Github Action 会自动在您每次推送 `pyproject.toml` 文件的更新时运行。</Tip>
  </Step>
</Steps>
