> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Publishing Nodes

## Set up a Registry Account

Follow the steps below to set up a registry account and publish your first node.

### Watch a Tutorial

<iframe height="415" src="https://www.youtube.com/embed/WhOZZOgBggU?si=6TyvhJJadmQ65uXC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style={{ width: "100%", borderRadius: "0.5rem" }} />

### Create a Publisher

A publisher is an identity that can publish custom nodes to the registry. Every custom node needs to include a publisher identifier in the pyproject.toml [file]().

Go to [Comfy Registry](https://registry.comfy.org), and create a publisher account. Your publisher id is globally unique, and cannot be changed later because it is used in the URL of your custom node.

Your publisher id is found after the `@` symbol on your profile page.

<img className="block" src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=95e3271276938f1ec1226f172ffc020f" alt="Hero Dark" data-og-width="534" width="534" data-og-height="342" height="342" data-path="images/publisherid.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=aafd181c16f25d66961b717fb46b77e8 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=618357651a7a64a0f90d31227ba4295b 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=743c9a3f2b3c387aee9f668169e8b21f 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a2bd945881111904b91bde24daa733f3 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=511f7245307d7569caeedfd0781864cc 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=f2cc85d730f5fd90c59d8d198c2e623d 2500w" />

### Create a Registry Publishing API Key

<Note>
  **Important:** This API key is specifically for **publishing custom nodes to the Registry and ComfyUI-Manager**. If you're looking to use paid API nodes in your workflows instead, see [API Nodes Overview](/tutorials/partner-nodes/overview).
</Note>

Go [here](https://registry.comfy.org/nodes) and click on the publisher you want to create an API key for. This key will be used to publish custom nodes to the Registry (which powers ComfyUI-Manager) via the CLI or GitHub Actions.

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6f9c94583f78457419cfde793f49f387" alt="Create key for Specific Publisher" data-og-width="295" width="295" data-og-height="159" height="159" data-path="images/pat-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=11fb3f0cf7bb78bee430c7f46acdd856 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ab9b38ebab6988131e095f953b453b23 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=f1ab93bd727e4867871910d15dfcd8ac 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=593cbe8448b237f88b299862bb93603d 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=d16bea3a955600aa59999dfdd0abaa01 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=1367f355a0557b74b236392c35521a3e 2500w" />

Name the API key and save it somewhere safe. If you lose it, you'll have to create a new key.

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=490347389e83b978f4c65b0e6a7b5d33" alt="Create API Key" data-og-width="526" width="526" data-og-height="474" height="474" data-path="images/pat-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=9b69fd6494a9bb03f31ec26e4360ef88 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=b0aa3c4774cd80af6018e52f3decff9f 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3a7dd425166cabb9abbdcda3687a9dad 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=0bbe8642a1be3bd3d96659723590c5f9 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=994cdedbfa26a483463ccbaf65871e87 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=be07aee07dc86c5a196c5babb2da69ec 2500w" />

### Add Metadata

<Tip>Have you installed the comfy-cli? [Do that first](/comfy-cli/getting-started).</Tip>

```bash  theme={null}
comfy node init
```

This command will generate the following metadata:

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

Add this file to your repository. Check the [specifications](/registry/specifications) for more information on the pyproject.toml file.

## Publish to the Registry

### Option 1: Comfy CLI

Run the command below to manually publish your node to the registry.

```bash  theme={null}
comfy node publish
```

You'll be prompted for the API key.

```bash  theme={null}
API Key for publisher '<publisher id>': ****************************************************

...Version 1.0.0 Published. 
See it here: https://registry.comfy.org/publisherId/your-node
```

<Warning>
  Keep in mind that the API key is hidden by default.
</Warning>

<Warning>
  When copy-pasting, your API key might have an additional \x16 at the back when using CTRL+V (for Windows), eg: \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\x16.

  It is recommended to copy-paste your API key via right-clicking instead.
</Warning>

### Option 2: Github Actions

Automatically publish your node through github actions.

<Steps>
  <Step title="Set up a Github Secret">
    Go to Settings -> Secrets and Variables -> Actions -> Under Secrets Tab and Repository secrets -> New Repository Secret.

    Create a secret called `REGISTRY_ACCESS_TOKEN` and store your API key as the value.
  </Step>

  <Step title="Create a Github Action">
    Copy the code below and paste it here `/.github/workflows/publish_action.yml`

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

    <Warning>If your working branch is named something besides `main`, such as `master`, add the name under the branches section.</Warning>
  </Step>

  <Step title="Test the Github Action">
    Push an update to your `pyproject.toml`'s version number. You should see your updated node on the registry.

    <Tip>The github action will automatically run every time you push an update to your `pyproject.toml` file</Tip>
  </Step>
</Steps>
