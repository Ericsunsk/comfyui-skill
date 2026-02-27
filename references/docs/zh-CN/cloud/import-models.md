> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 导入模型到 Comfy Cloud

> 了解如何从 Civitai 和 Hugging Face 导入模型到 Comfy Cloud

<Note>
  这是 **Comfy Cloud** 云端功能，仅在云端版本中可用，本地版本不支持此功能。了解更多关于 Comfy Cloud 的信息，请参阅 [Comfy Cloud](/zh-CN/get_started/cloud)。
</Note>

## 概述

Comfy Cloud 允许你直接从 Civitai 和 Hugging Face 导入模型。此功能仅对 **Creator** 及以上订阅用户开放。

## 要求

* **订阅等级**: Creator 或更高
* **支持来源**: Civitai 和 Hugging Face

## 如何导入模型

### 1. 导入功能入口

<img src="https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/import_model.png?fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=0621b50c1cc510ddcdd5bb69f96625b7" alt="Import" data-og-width="2140" width="2140" data-og-height="1034" height="1034" data-path="images/cloud/import_model/import_model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/import_model.png?w=280&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=5f657e5077a577b198693556aaf5ddea 280w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/import_model.png?w=560&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=3443ae3a5a20fa298bf2b3038448c283 560w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/import_model.png?w=840&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=0abfe48cd2e452be1044e0098a4e7941 840w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/import_model.png?w=1100&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=05e0b5cb9faaf5a502b18607c7aba62b 1100w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/import_model.png?w=1650&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=34bd624481d178e9bba1444d8906826a 1650w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/import_model.png?w=2500&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=e35979c149dbd0308c4f031938734d87 2500w" />

1. 点击左侧边栏的 **Models** 按钮打开模型库。
2. 在模型库弹窗中，点击 **Import** 按钮。

### 2. 粘贴链接

1. 粘贴你从 huggingface 或者 civitai 上获取的模型链接
   <img src="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-1.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=077d3bf113f8139db1ce9f94e3c42202" alt="Import Modal" data-og-width="1720" width="1720" data-og-height="1262" height="1262" data-path="images/cloud/import_model/import_model_modal-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-1.png?w=280&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=bfd4facf5bd4766cd35cdbc8989ca538 280w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-1.png?w=560&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=d16a654426335b2cc4890b4a2f13b005 560w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-1.png?w=840&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=320334450cbb11362eb65b6a24d960df 840w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-1.png?w=1100&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=f9e442c0aa5af203594f29d814470ac3 1100w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-1.png?w=1650&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=dfc95e5104345526513fef4396bbb750 1650w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-1.png?w=2500&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=b65d574b4a1828bf5aeb0deeeca72552 2500w" />

2. 如果链接有效，则你可以看到对应的通过标识，并可以点击 `Continue` 按钮进行下一步
   <img src="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-2.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=3b35abf880dc14c6d0186e1e6a104f92" alt="Import Modal" data-og-width="1720" width="1720" data-og-height="1262" height="1262" data-path="images/cloud/import_model/import_model_modal-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-2.png?w=280&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=ce9803997384278bad15c5ad1248502a 280w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-2.png?w=560&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=7f0fcb032544542081f629c7acbc0928 560w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-2.png?w=840&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=2bbb8d599bf6471c376c2ee5f3f7e3a6 840w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-2.png?w=1100&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=c3c87eea0f10bedc82bea685153472fc 1100w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-2.png?w=1650&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=698a5bf19b6198656737782931a0952b 1650w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-2.png?w=2500&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=3fc2faf528e5e83517cdd6a896b8452f 2500w" />

3. 选择导入的模型类型和对应的文件夹
   <img src="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-3.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=10c28ec6293b6d2658d2899ebbae072f" alt="Import Modal" data-og-width="1720" width="1720" data-og-height="1262" height="1262" data-path="images/cloud/import_model/import_model_modal-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-3.png?w=280&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=53e3bf80e01bf9f1b598d0410175b060 280w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-3.png?w=560&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=90daab9763a51ad165b081ca513b5c99 560w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-3.png?w=840&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=8820ca089aeb00a16808c0d3ae80d7d6 840w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-3.png?w=1100&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=8582401400f416024a7a444d73c7d0e9 1100w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-3.png?w=1650&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=139b6369666ab65b539cb2bc90f00b86 1650w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-3.png?w=2500&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=d221678399c1c06730de129279698941 2500w" />

4. 等待模型下载完成
   <img src="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-4.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=d80d9bb488937b1b2493dfc4929b7a17" alt="Import Modal" data-og-width="1720" width="1720" data-og-height="1242" height="1242" data-path="images/cloud/import_model/import_model_modal-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-4.png?w=280&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=0bbdafa56859a71d9930adef4ec816e6 280w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-4.png?w=560&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=bf1632e3f8276b4bd441a93104250bc7 560w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-4.png?w=840&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=06a9b47598662ce0534f8fb035d2a567 840w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-4.png?w=1100&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=14ab41b161450a6a090123c098d98551 1100w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-4.png?w=1650&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=236b62033e1f6956cf4ae7815212c43f 1650w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/import_model_modal-4.png?w=2500&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=8784339a22f8eab32afd6757012d58a7 2500w" />

5. 下载完成后即可在模型库中找到对应的模型

## 如何查看已导入的模型

在模型库中，在下拉筛选中，选择 “My Models” 即可筛选出你导入的模型

<img src="https://mintcdn.com/dripart/506FEUHoNW04mqdV/images/cloud/import_model/imported_model.png?fit=max&auto=format&n=506FEUHoNW04mqdV&q=85&s=9e0b5c5f1a200c7337f94aa67d7ffd36" alt="Imported Models" data-og-width="1703" width="1703" data-og-height="964" height="964" data-path="images/cloud/import_model/imported_model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/506FEUHoNW04mqdV/images/cloud/import_model/imported_model.png?w=280&fit=max&auto=format&n=506FEUHoNW04mqdV&q=85&s=26a407917d666ed6051d7a9116b769e8 280w, https://mintcdn.com/dripart/506FEUHoNW04mqdV/images/cloud/import_model/imported_model.png?w=560&fit=max&auto=format&n=506FEUHoNW04mqdV&q=85&s=c9fb004bc14dd3eb324ca7e0b642b2a8 560w, https://mintcdn.com/dripart/506FEUHoNW04mqdV/images/cloud/import_model/imported_model.png?w=840&fit=max&auto=format&n=506FEUHoNW04mqdV&q=85&s=b4dd7f9409c05d629b71fe2ec4e4db1f 840w, https://mintcdn.com/dripart/506FEUHoNW04mqdV/images/cloud/import_model/imported_model.png?w=1100&fit=max&auto=format&n=506FEUHoNW04mqdV&q=85&s=b1288d5cbb36a412e742bf4cd1aed1b6 1100w, https://mintcdn.com/dripart/506FEUHoNW04mqdV/images/cloud/import_model/imported_model.png?w=1650&fit=max&auto=format&n=506FEUHoNW04mqdV&q=85&s=db878ea76469d0a179768f77ec2dc816 1650w, https://mintcdn.com/dripart/506FEUHoNW04mqdV/images/cloud/import_model/imported_model.png?w=2500&fit=max&auto=format&n=506FEUHoNW04mqdV&q=85&s=f3640ac6ddb63290a6cb39ee63fb5421 2500w" />

## 如何获取导入模型链接

### 1. 从 Civitai 获取链接

1. 前往 [Civitai](https://civitai.com/) 找到你想导入的模型。
2. 使用鼠标右键点击下载按钮，选择"复制链接地址"，即可获取对应的模型下载链接

<img src="https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/copy_civitai_link.png?fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=48e3791d2dda7a9df235b1b4e73b0942" alt="Copy Civitai Link" data-og-width="1385" width="1385" data-og-height="729" height="729" data-path="images/cloud/import_model/copy_civitai_link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/copy_civitai_link.png?w=280&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=2086a0d20b4dcb921fd93215a2274939 280w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/copy_civitai_link.png?w=560&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=81c3b8606acb72ee6880e0ddfa13cd41 560w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/copy_civitai_link.png?w=840&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=cbd590ab4e100d6c077b7cebcd705db8 840w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/copy_civitai_link.png?w=1100&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=e7cf803627816eed795a0927921105dc 1100w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/copy_civitai_link.png?w=1650&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=0c1d6e78ffe77a6780611493b2ab9140 1650w, https://mintcdn.com/dripart/-QDp41xfxDglkAeZ/images/cloud/import_model/copy_civitai_link.png?w=2500&fit=max&auto=format&n=-QDp41xfxDglkAeZ&q=85&s=7f40ee22fef7441bab44df2e2c88b7cd 2500w" />

### 2. 从 Hugging Face 获取链接

1. 前往 [Hugging Face](https://huggingface.co/) 找到你想导入的模型仓库。
2. 进入模型文件页面通常受支持的格式是 “.safetensor”, ".sft" 的模型，你可以节点具体的模型名称进入对应详情页面

<img src="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-1.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=786214df669fd53613b295e6bd6e8cef" alt="Copy Huggingface model link" data-og-width="1276" width="1276" data-og-height="1059" height="1059" data-path="images/cloud/import_model/copy_huggingface_link-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-1.png?w=280&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=8ed5de8a1425e9bbc1b38f7096d0aa5c 280w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-1.png?w=560&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=1b224bdfaa379426cdd4ce0e7a1f1bee 560w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-1.png?w=840&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=6dedf5b816b329df930d96f33080bd8d 840w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-1.png?w=1100&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=630fd3595b11f960fdbb88cefe2a380e 1100w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-1.png?w=1650&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=2e499e38ba8f7cd9692566207ca5cff5 1650w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-1.png?w=2500&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=bde383c28644a40a010930e10c339d46 2500w" />

3. 在详情页面点击 `Copy Download Link` 按钮即可获取到模型下载链接

<img src="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-2.png?fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=4681f3e56576eb36ad4e26287bebc65b" alt="Copy Huggingface model link" data-og-width="1276" width="1276" data-og-height="815" height="815" data-path="images/cloud/import_model/copy_huggingface_link-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-2.png?w=280&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=7a4bc995b86feee0cee624f568c5eed1 280w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-2.png?w=560&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=77eb224abc5896ebedc3d738430e6bf7 560w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-2.png?w=840&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=e75e2d2cd52766f484b0ca7a4724e542 840w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-2.png?w=1100&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=25bbfc0154d2ef0c9f45bc619f77daf0 1100w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-2.png?w=1650&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=50fd53897ea197f7d6419f47a53e3197 1650w, https://mintcdn.com/dripart/04-EVgSb3UFO1T4M/images/cloud/import_model/copy_huggingface_link-2.png?w=2500&fit=max&auto=format&n=04-EVgSb3UFO1T4M&q=85&s=e5660d03f85b2e579ff2597210ea0763 2500w" />

## 导入私有模型

如果你想从 Hugging Face 或 Civitai 导入私有模型，需要先配置你的 API 密钥。

### 1. 生成 API 密钥

首先，你需要从对应平台生成 API 密钥：

<Tabs>
  <Tab title="Civitai">
    1. 登录 Civitai 后访问 [https://civitai.com/user/account](https://civitai.com/user/account)。
    2. 在账户设置中生成 API 密钥。

        <img src="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/civitai_key-1.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=50e93b8937fe90a70f7aec140db65d30" alt="Civitai API Key" data-og-width="4132" width="4132" data-og-height="3264" height="3264" data-path="images/cloud/import_model/civitai_key-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/civitai_key-1.png?w=280&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=d618a195b96c3f655c02610533f48c8b 280w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/civitai_key-1.png?w=560&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=c2981f8a20ff53498b27efc7c0b3a534 560w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/civitai_key-1.png?w=840&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=c63bf8f26ae41791d11d57f50e449e11 840w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/civitai_key-1.png?w=1100&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=38bc990399a606c799a77522fc68ae5c 1100w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/civitai_key-1.png?w=1650&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=440919333d344c4cdd784eba2a0235ee 1650w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/civitai_key-1.png?w=2500&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=c43a0f879c44e99517246b6ba833ba93 2500w" />
  </Tab>

  <Tab title="Hugging Face">
    1. 访问 [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)。
    2. 生成你的 API token。

        <img src="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-1.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=32729b7a20a9ebe16d546c4836b92b49" alt="Hugging Face API Key" data-og-width="4132" width="4132" data-og-height="3264" height="3264" data-path="images/cloud/import_model/huggingface_key-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-1.png?w=280&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=85dd55f4cbc577e5e2391919783f49dd 280w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-1.png?w=560&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=af6d6642ec371af4875dad6d3112d815 560w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-1.png?w=840&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=2fc3d12b844142706d977f8e2012c6e6 840w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-1.png?w=1100&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=c855d74fa9156691dcb0980bd3fa744e 1100w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-1.png?w=1650&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=b9f902237e29c3618460d4488af9c45a 1650w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-1.png?w=2500&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=40957311e8f4e867744f4eeb089643a2 2500w" />

    3. 确保你的 token 具有对应私有模型仓库的读取权限。

        <img src="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-2.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=2ae808aa8052e3cc98e8d91b5fde551c" alt="Hugging Face Token 权限" data-og-width="4132" width="4132" data-og-height="3264" height="3264" data-path="images/cloud/import_model/huggingface_key-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-2.png?w=280&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=3fe992caa75128f82ef337e2ed7a1f5f 280w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-2.png?w=560&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=58e5e350ed9433c05ce25ee2e1c414e1 560w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-2.png?w=840&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=8ca174e9351c1e93078187330458da6b 840w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-2.png?w=1100&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=e4cab0afab2f165b84c13fa0b66c0a09 1100w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-2.png?w=1650&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=d30a30790c0c9fe296849611a73f3ac1 1650w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/huggingface_key-2.png?w=2500&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=1bde7a3cd5fa7b3f58f765a153e53d8f 2500w" />
  </Tab>
</Tabs>

### 2. 保存 API 密钥

1. 前往 [Comfy Cloud 设置](https://cloud.comfy.org)，进入 **Secrets** 部分。

<img src="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-1.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=15ea8a8aeeb50da9bedc00429c9c05b1" alt="Settings Secrets" data-og-width="4268" width="4268" data-og-height="3774" height="3774" data-path="images/cloud/import_model/setting_secerts-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-1.png?w=280&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=dbf904f84866d064444c33fe27a40282 280w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-1.png?w=560&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=67acef525df9af679650865590d7e3b3 560w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-1.png?w=840&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=17a253ea9fedcb14db8144bbe8dd7549 840w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-1.png?w=1100&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=df9b7f47d26b506412cd98469a4e8663 1100w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-1.png?w=1650&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=5b2ffac0ac6046117309f86a6098f4fb 1650w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-1.png?w=2500&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=afb2ac69e0b68c5e54948a955b4643e3 2500w" />

2. 点击添加你的 API 密钥（密钥名称可以自由命名）：

<img src="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-2.png?fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=b87a3c87203a4e3929ae41295281a823" alt="添加 Secret Key" data-og-width="4268" width="4268" data-og-height="3774" height="3774" data-path="images/cloud/import_model/setting_secerts-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-2.png?w=280&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=fd6263d6abf52b59140a29b342670abc 280w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-2.png?w=560&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=e22b3032564774a95e73078e3044c98e 560w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-2.png?w=840&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=88659881dd51b2e16b0b6412c6a151af 840w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-2.png?w=1100&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=576f6c18c5c6e89b151d162ae1f0ed12 1100w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-2.png?w=1650&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=b06fde8b570eb9655fe43b3609f812a5 1650w, https://mintcdn.com/dripart/dkKbceCnXIcxFyjM/images/cloud/import_model/setting_secerts-2.png?w=2500&fit=max&auto=format&n=dkKbceCnXIcxFyjM&q=85&s=4a6fcbea7a986f99b1027bb1ebdb1553 2500w" />

3. 确保你的 API 密钥具有访问你想导入的私有模型的权限。

### 3. 导入私有模型

配置好 API 密钥后，你可以使用与公开模型相同的流程导入私有模型：

1. 从 Hugging Face 或 Civitai 获取模型链接。
2. 在导入弹窗中粘贴链接。
3. 系统会自动使用你保存的 API 密钥来访问私有模型。

<Note>
  请确保你的 API 密钥具有访问特定私有模型所需的权限。
</Note>

## 常见问题

<AccordionGroup>
  <Accordion title="上传的模型有什么限制？">
    有。仅支持 **safetensor** 文件格式。文件大小基本没有限制（最大 100GB）。
  </Accordion>

  <Accordion title="我上传的模型是私有的还是公开的？">
    你导入的模型是**私有的**。只有你自己可以在模型库中看到这些模型。
  </Accordion>

  <Accordion title="我可以从本地硬盘上传自定义模型吗？">
    目前，你需要先将模型上传到**公开的 Hugging Face 或 Civitai 仓库**，然后再从这些平台导入。
  </Accordion>

  <Accordion title="我可以上传分块的模型文件吗？">
    不可以。你需要先将分块的模型文件合并成一个文件后再导入。
  </Accordion>

  <Accordion title="这个功能包含在我当前的云订阅中吗？">
    此功能仅适用于 **Creator** 和 **Pro** 订阅计划。
  </Accordion>

  <Accordion title="这个功能在桌面版或便携版 Comfy 上可用吗？">
    不可以。这是**仅限云端**的功能。
  </Accordion>

  <Accordion title="我可以删除已上传的模型吗？">
    可以。你可以删除自己导入的模型。请注意，Comfy 内部团队上传的模型无法删除。
  </Accordion>
</AccordionGroup>
