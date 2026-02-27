> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 扩展设置

> ComfyUI 扩展管理和设置选项的详细说明

扩展设置面板是 ComfyUI 前端设置系统中的一个特殊管理面板，专门用于管理前端扩展插件的启用/禁用状态，区别于自定义节点（Custom Node），这个面板只是用于管理自定义节点注册的前端扩展，而不是禁用自定义节点。

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=351dc6d25afbe287ed94c4bf39db91a1" alt="extension" data-og-width="1910" width="1910" data-og-height="1248" height="1248" data-path="images/interface/setting/extension/extension.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a34f411c79daef19b975794c98e095fc 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=12e4f6f41641a0e9a7600c55a9364fde 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0ee3665ed976865e6315f14b151282d5 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=98fb5076a9297011e4ab0993327a06da 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9ef00ebcc6e38e996ffa577618bfcb82 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c2e919422f54efaa23027110369dc014 2500w" />

这些前端扩展插件是用于增强 ComfyUI 的体验，比如提供快捷键、设置、UI 组件、菜单项等功能。

扩展状态更改后需要重新加载页面才能生效：

## Extension 设置面板功能

### 1. 扩展列表管理

显示所有已注册的扩展，包括：

* 扩展名称
* 核心扩展标识（显示 "Core" 标签）
* 启用/禁用状态

### 2. 搜索功能

提供搜索框快速查找特定扩展：

### 3. 启用/禁用控制

每个扩展都有独立的切换开关：

### 4. 批量操作

提供右键菜单进行批量操作：

* 启用所有扩展
* 禁用所有扩展
* 禁用第三方扩展（保留核心扩展）

## 注意事项

* 扩展状态更改需要重新加载页面才能生效
* 某些核心扩展无法被禁用
* 系统会自动禁用已知有问题的扩展
* 扩展设置会自动保存到用户配置文件中

这个 Extension 设置面板本质上是一个"前端插件管理器"，让用户可以灵活控制 ComfyUI 的功能模块。
