> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Manager 自定义节点（新版 UI）管理

> 使用 ComfyUI-Manager 新界面安装、更新和管理自定义节点

<Note>
  如果你不是新版 UI 请参考 [切换新旧版UI](/zh-CN/manager/install) 部分了解如何进行切换
</Note>

你可以通过一下方式

## 新版界面说明

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b169a5dbcb0607bf29e499278a901dc2" alt="新版本 UI " data-og-width="1219" width="1219" data-og-height="726" height="726" data-path="images/manager/new_ui_labeled.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=17ef42ac1136967d4f33afea60d9ff3f 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=8fc3b485e13b3a925181f2dadb70f11c 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=512e0c9466fc4e29ef5ce6eb4f87a4e3 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=5220e0f5374cc2b48f902c8f470fe4de 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b1eeadfb15d485a33f5fe3a3a98688e7 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=8520c22b56c9ccd156f4cdfa3200e445 2500w" />

1. **左侧筛选器**：筛选已安装、工作流中的节点、缺失节点、可更新节点等
2. **顶部搜索栏**：搜索节点包（Node Pack）或单个节点（Node），Filter 可切换搜索类型
3. **右侧详情面板**：点击节点后显示详情信息，包括介绍、启用状态、版本信息等。Description 标签页包含仓库信息，Nodes 标签页预览所有节点

## 节点管理

了解如何使用新版本 ComfyUI Manager 进行自定义节点的管理

### 搜索节点

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=39b734a9514bce3d14ec83ff053f2c99" alt="筛选器" data-og-width="1544" width="1544" data-og-height="935" height="935" data-path="images/manager/new_ui_filter.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=8a57d14b27b4f5bc98fb35d88bbe8fe8 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c877977d988b6f765f72e1f4bdb66535 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f94d93853c5d5571609b25d1123d0da3 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=257911ad7a2125f334f2bad1fdfbcce9 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=cda7af0ef69f8c8c6c255d786aa56724 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=3b6965e4d34880a7b3a03b5c3fe494b5 2500w" />

在 Manager 中支持单独搜索节点包和单个节点，如上图，通过切换筛选器（filter）可以切换搜索类型

* 节点包：一个完整的自定义节点包
* 单个节点： 搜索节点内的单个节点

### 安装节点

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7968ebd2eb538909882c4b2f2efdf83d" alt="安装节点" data-og-width="1800" width="1800" data-og-height="1125" height="1125" data-path="images/manager/new_ui_install_pack.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c219e6ca8061de11b4689563195ec107 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=2cd1646fc769226c40058df0f18b1f04 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f1a03caf56182b973a52b4f792cfb55b 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=aca4454e7bb097cc625029304a058c06 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=04ff6622c7a408a0ea917e4f2ae7928c 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=349f2e5c6ec9b1af0b60a77ab3ee2053 2500w" />

1. 选中对应节点卡片
2. 在展开的节点信息点击 **安装（install）**
3. 或者在**版本（version）** 选择特定版本进行安装

### 更新节点

在 **Update available** 筛选器下，可以筛选出当前节点列表中可更新的节点
<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=439f256ae789bbfee69e81ff0a87dfb9" alt="更新节点" data-og-width="1800" width="1800" data-og-height="1125" height="1125" data-path="images/manager/new_ui_update_pack.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=bd96222fb1a8ffae0ca2e71842f0268a 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=91d756659360575608e148e574af69d6 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=358a661fbff8db73869a713eae21fad5 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b236128fd811b3057b604ca266b703e3 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=e19c7983f2c19ffc57f42a76e7d16784 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7743652420255512662afed1e2968f42 2500w" />

1. 对应可更新节点会显示一个可更新的箭头标志
2. 在 **version** 选择特定版本
3. 选择版本后点击 **Update** 按钮进行更新

### 查找缺失节点

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=48daeed1ac09b0f725dc311be5c60871" alt="查找缺失节点" data-og-width="1800" width="1800" data-og-height="1135" height="1135" data-path="images/manager/new_ui_missing_packs_prompt.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7b769a9dbbac052fe16184708341f42e 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f5bec442a31db2918c46890b8051c0f4 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b875580b659298a30d032681dec171f0 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f5b7c1113f0594791de0e48025ebce91 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=77628b6d29f36e756e0085e1020b2843 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=dea4f5b56405defdeaecbce5b80b72c9 2500w" />
如果你的 ComfyUI Manager 正确安装，那么在加载工作流出现节点缺失的时候则会出现弹窗提示安装缺失节点信息

1. 你可选择 **安装全部（Install All）** 一次性安装全部节点
2. 也可以选择 **打开管理器（Open Manager）** 打开管理器后浏览详情后进行安装

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c800b0999e45d8f3f45ceead054a9dbc" alt="查找缺失节点" data-og-width="1800" width="1800" data-og-height="1106" height="1106" data-path="images/manager/new_ui_missing_pack.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=44697dea932a4739013422e475c2a222 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=96aabd6fdc05b15fb7dedd8a7c843062 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=913c754a4d27ea8b12670194ac3689e8 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=368c1765d78e9cfaa0d371e1ff93afe4 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7f2b52d08f501231cdacf55ee3902a91 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=3b40d5d30656efa0bb4646f30846100f 2500w" />
如果想要查找工作流缺失节点，则选中对应节点后，在预览界面点击\*\*查找缺失节点（Missing）\*\*按钮即可进行查找缺失节点

### 卸载节点

<img src="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f40ab0c5454f6646566c887db41d2559" alt="卸载节点" data-og-width="1800" width="1800" data-og-height="1125" height="1125" data-path="images/manager/new_ui_uninstall_pack.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=280&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c7028cdf8fa1d2310f8d264426aa009d 280w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=560&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=2222b38211412d34755ae703d7108447 560w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=840&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=68f11005751eb105cb97ac07ac86e1db 840w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=1100&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7f746fdebe019be7210cdcd6cdcf2f1a 1100w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=1650&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f11f929dee2a17c3d5069e9c54b4cc2c 1650w, https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?w=2500&fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=68880f1888f8581fbf7c6b892d616a8d 2500w" />
如果想要卸载已安装的节点，则选中对应节点后，在预览界面点击\*\*卸载（Uninstall）\*\*按钮即可进行卸载

## 常见问题

1. 为什搜索不到我需要的节点？
   目前新版 Manager 仅支持从 [registry](/zh-CN/registry/overview) 上安装节点，如果你的节点未在 registry 注册请先在 Manager 进行注册

2. 为什么找不到通过 git 安装的选项了？
   考虑 ComfyUI 用户系统的安全性和稳定性，新版本 UI 不支持通过 git 安装节点，请参考 [手动安装自定义节点](/zh-CN/installation/install_custom_node) 了解如何手动安装自定义节点
