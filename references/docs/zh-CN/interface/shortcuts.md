> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 的快捷键及自定义设置

> ComfyUI 的键盘和鼠标快捷键及相关设置

目前 ComfyUI 已经支持快捷键自定义，你可以在点击 `设置（齿轮图标）` --> `快捷键`  中进行快捷键的设置。

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ec261f919615b16c4b111e6370926543" alt="ComfyUI 快捷键设置" data-og-width="1692" width="1692" data-og-height="1368" height="1368" data-path="images/interface/setting/keybinding.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d48c51c47e759dae0d9c5ea611590165 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=622388e6fa819f8570231cb1a90f2055 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dcd5b6fc07a781a29421136ea1dca316 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=7b07e58fd0e676b1fe95dee3d2337138 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=50e401f316a5d73cbcf83c69ef04d452 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=14a051c626877fa3d7b5059c3b94f711 2500w" />

在对应菜单中，你可以看到目前 ComfyUI 所有的快捷键设置，点击对应命令之前的`编辑图标`，就可以对快捷键进行自定义。

<Tabs>
  <Tab title="Windows/Linux">
    | 快捷键                             | 命令                             |
    | ------------------------------- | ------------------------------ |
    | Ctrl + Enter                    | 执行提示词                          |
    | Ctrl + Shift + Enter            | 执行提示词（前端）                      |
    | Ctrl + Alt + Enter              | 中断                             |
    | Ctrl + Z / Ctrl + Y             | 撤销/重做                          |
    | Ctrl + S                        | 保存工作流                          |
    | Ctrl + O                        | 加载工作流                          |
    | Ctrl + A                        | 选择所有节点                         |
    | Alt + C                         | 折叠/展开选定节点                      |
    | Ctrl + M                        | 静音/取消静音选定节点                    |
    | Ctrl + B                        | 忽略/取消忽略选定节点                    |
    | Delete<br />Backspace           | 删除选定节点                         |
    | Backspace                       | 清除工作流                          |
    | Space                           | 按住并移动光标时移动画布                   |
    | Ctrl + Click<br />Shift + Click | 将点击的节点添加到选择中                   |
    | Ctrl + C/Ctrl + V               | 复制并粘贴选定节点（不保持与未选定节点输出的连接）      |
    | Ctrl + C/Ctrl + Shift + V       | 复制并粘贴选定节点（保持未选定节点输出到粘贴节点输入的连接） |
    | Shift + Drag                    | 同时移动多个选定节点                     |
    | Ctrl + G                        | 添加框到选中节点                       |
    | Ctrl + ,                        | 显示设置对话框                        |
    | Alt + =                         | 放大（画布）                         |
    | Alt + -                         | 缩小（画布）                         |
    | .                               | 适应视图到选中节点                      |
    | P                               | 固定/取消固定选中项                     |
    | Q                               | 切换执行队列侧边栏                      |
    | W                               | 切换工作流侧边栏                       |
    | N                               | 切换节点库侧边栏                       |
    | M                               | 切换模型库侧边栏                       |
    | Ctrl + \`                       | 切换日志底部面板                       |
    | F                               | 切换焦点模式（全屏）                     |
    | R                               | 刷新节点定义                         |
    | 双击左键                            | 快速搜索要添加的节点                     |
  </Tab>

  <Tab title="MacOS">
    | 快捷键                              | 说明                             |
    | -------------------------------- | ------------------------------ |
    | Cmd ⌘ + Enter                    | 执行提示词                          |
    | Cmd ⌘ + Shift + Enter            | 执行提示词（前端）                      |
    | Cmd ⌘ + Alt + Enter              | 中断                             |
    | Cmd ⌘ + Z/Cmd ⌘ + Y              | 撤销/重做                          |
    | Cmd ⌘ + S                        | 保存工作流                          |
    | Cmd ⌘ + O                        | 加载工作流                          |
    | Cmd ⌘ + A                        | 选择所有节点                         |
    | Opt ⌥ + C                        | 折叠/展开选定节点                      |
    | Cmd ⌘ + M                        | 静音/取消静音选定节点                    |
    | Cmd ⌘ + B                        | 忽略/取消忽略选定节点                    |
    | Delete<br />Backspace            | 删除选定节点                         |
    | Backspace                        | 清除工作流                          |
    | Space                            | 按住并移动光标时移动画布                   |
    | Cmd ⌘ + Click<br />Shift + Click | 将点击的节点添加到选择中                   |
    | Cmd ⌘ + C / Cmd ⌘ + V            | 复制并粘贴选定节点（不保持与未选定节点输出的连接）      |
    | Cmd ⌘ + C / Cmd ⌘ + Shift + V    | 复制并粘贴选定节点（保持未选定节点输出到粘贴节点输入的连接） |
    | Shift + Drag                     | 同时移动多个选定节点                     |
    | Cmd ⌘ + G                        | 添加框到选中节点                       |
    | Cmd ⌘ + ,                        | 显示设置对话框                        |
    | Opt ⌥ + =                        | 放大（画布）                         |
    | Opt ⌥ + -                        | 缩小（画布）                         |
    | .                                | 适应视图到选中节点                      |
    | P                                | 固定/取消固定选中项                     |
    | Q                                | 切换执行队列侧边栏                      |
    | W                                | 切换工作流侧边栏                       |
    | N                                | 切换节点库侧边栏                       |
    | M                                | 切换模型库侧边栏                       |
    | Cmd ⌘ + \`                       | 切换日志底部面板                       |
    | F                                | 切换焦点模式（全屏）                     |
    | R                                | 刷新节点定义                         |
    | 双击左键                             | 快速搜索要添加的节点                     |
  </Tab>
</Tabs>
