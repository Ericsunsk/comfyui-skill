> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom nodes (new UI)

> Install, update, and manage custom nodes with ComfyUI-Manager using the new interface

<Note>
  If you're not using the new UI, refer to the [Switch between new and legacy UI](/manager/install) section to learn how to switch.
</Note>

## New UI overview

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b169a5dbcb0607bf29e499278a901dc2" alt="New UI" data-og-width="1219" width="1219" data-og-height="726" height="726" data-path="images/manager/new_ui_labeled.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=17ef42ac1136967d4f33afea60d9ff3f 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=8fc3b485e13b3a925181f2dadb70f11c 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=512e0c9466fc4e29ef5ce6eb4f87a4e3 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=5220e0f5374cc2b48f902c8f470fe4de 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b1eeadfb15d485a33f5fe3a3a98688e7 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=8520c22b56c9ccd156f4cdfa3200e445 2500w" />

1. **Left sidebar (Filters)**: Filter installed nodes, nodes in workflow, missing nodes, updatable nodes, etc.
2. **Top search bar**: Search node packs (Node Pack) or individual nodes (Node), switch search type using the Filter dropdown
3. **Right detail panel**: Click a node to display detailed information including description, enable status, version information, etc. The Description tab contains repository information, and the Nodes tab previews all nodes

## Node management

Learn how to use the new ComfyUI Manager to manage custom nodes

### Search nodes

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=39b734a9514bce3d14ec83ff053f2c99" alt="Filter" data-og-width="1544" width="1544" data-og-height="935" height="935" data-path="images/manager/new_ui_filter.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=8a57d14b27b4f5bc98fb35d88bbe8fe8 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c877977d988b6f765f72e1f4bdb66535 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f94d93853c5d5571609b25d1123d0da3 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=257911ad7a2125f334f2bad1fdfbcce9 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=cda7af0ef69f8c8c6c255d786aa56724 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=3b6965e4d34880a7b3a03b5c3fe494b5 2500w" />

The Manager supports searching for node packs and individual nodes separately. As shown above, you can switch search types by toggling the filter.

* Node Pack: A complete custom node pack
* Individual Node: Search for individual nodes within node packs

### Install nodes

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7968ebd2eb538909882c4b2f2efdf83d" alt="Install nodes" data-og-width="1800" width="1800" data-og-height="1125" height="1125" data-path="images/manager/new_ui_install_pack.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c219e6ca8061de11b4689563195ec107 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=2cd1646fc769226c40058df0f18b1f04 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f1a03caf56182b973a52b4f792cfb55b 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=aca4454e7bb097cc625029304a058c06 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=04ff6622c7a408a0ea917e4f2ae7928c 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=349f2e5c6ec9b1af0b60a77ab3ee2053 2500w" />

1. Select the corresponding node card
2. Click **Install** in the expanded node information
3. Or select a specific version in **Version** to install

### Update nodes

Under the **Update available** filter, you can filter nodes that have updates available in the current node list
<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=439f256ae789bbfee69e81ff0a87dfb9" alt="Update nodes" data-og-width="1800" width="1800" data-og-height="1125" height="1125" data-path="images/manager/new_ui_update_pack.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=bd96222fb1a8ffae0ca2e71842f0268a 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=91d756659360575608e148e574af69d6 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=358a661fbff8db73869a713eae21fad5 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b236128fd811b3057b604ca266b703e3 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=e19c7983f2c19ffc57f42a76e7d16784 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7743652420255512662afed1e2968f42 2500w" />

1. Updatable nodes will display an update arrow indicator
2. Select a specific version in **Version**
3. Click the **Update** button after selecting a version to update

### Find missing nodes

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=48daeed1ac09b0f725dc311be5c60871" alt="Find missing nodes" data-og-width="1800" width="1800" data-og-height="1135" height="1135" data-path="images/manager/new_ui_missing_packs_prompt.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7b769a9dbbac052fe16184708341f42e 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f5bec442a31db2918c46890b8051c0f4 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b875580b659298a30d032681dec171f0 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f5b7c1113f0594791de0e48025ebce91 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=77628b6d29f36e756e0085e1020b2843 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=dea4f5b56405defdeaecbce5b80b72c9 2500w" />
If your ComfyUI Manager is properly installed, a prompt will appear when loading a workflow with missing nodes

1. You can choose **Install All** to install all nodes at once
2. Or choose **Open Manager** to open the manager and browse details before installing

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c800b0999e45d8f3f45ceead054a9dbc" alt="Find missing nodes" data-og-width="1800" width="1800" data-og-height="1106" height="1106" data-path="images/manager/new_ui_missing_pack.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=44697dea932a4739013422e475c2a222 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=96aabd6fdc05b15fb7dedd8a7c843062 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=913c754a4d27ea8b12670194ac3689e8 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=368c1765d78e9cfaa0d371e1ff93afe4 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7f2b52d08f501231cdacf55ee3902a91 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=3b40d5d30656efa0bb4646f30846100f 2500w" />
To find missing nodes in a workflow, select the corresponding node, then click the **Missing** button in the preview panel to find missing nodes

### Uninstall nodes

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f40ab0c5454f6646566c887db41d2559" alt="Uninstall nodes" data-og-width="1800" width="1800" data-og-height="1125" height="1125" data-path="images/manager/new_ui_uninstall_pack.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c7028cdf8fa1d2310f8d264426aa009d 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=2222b38211412d34755ae703d7108447 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=68f11005751eb105cb97ac07ac86e1db 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7f746fdebe019be7210cdcd6cdcf2f1a 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f11f929dee2a17c3d5069e9c54b4cc2c 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=68880f1888f8581fbf7c6b892d616a8d 2500w" />
To uninstall an installed node, select the corresponding node, then click the **Uninstall** button in the preview panel to uninstall

## Common questions

1. Why can't I find the node I need?
   The new Manager only supports installing nodes from the [registry](/registry/overview). If your node is not registered in the registry, please register it in the Manager first.

2. Why can't I find the option to install via git?
   For security and stability of the ComfyUI user system, the new UI does not support installing nodes via git. Please refer to [Manually install custom nodes](/installation/install_custom_node) to learn how to manually install custom nodes.
