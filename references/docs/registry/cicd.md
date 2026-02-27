> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Node CI/CD

## Introduction

When making changes to custom nodes, it's not uncommon to break things in Comfy or other custom nodes. It is often unrealistic to test on every operating system and different configurations of Pytorch.

### Run Comfy Workflows using Github Actions

[Comfy-Action](https://github.com/Comfy-Org/comfy-action) allows you to run a Comfy workflow\.json file on Github Actions. It supports downloading models, custom nodes, and runs on Linux/Mac/Windows.

### Results

Output files are uploaded to the [CI/CD Dashboard](https://ci.comfy.org/) and can be viewed as a last step before committing new changes or publishing new versions of the custom node.

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=443608968123247168b89b026ed2ae0e" alt="ComfyCI" data-og-width="2526" width="2526" data-og-height="1722" height="1722" data-path="images/comfyci.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=bf00166a6e417a12b3afce2a3b70caac 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=8e6a0bfe6492622ae7c3b61c2946fb01 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=4381e7cb42aa617fdfaf2f0f51abd09c 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=64dd33fa30c0810d93e6c4415e847d6d 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ac6ecc93ae6dfc064445e7ca61e8351c 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=c458db2f48fa97f12f368c2adcd3de76 2500w" />
