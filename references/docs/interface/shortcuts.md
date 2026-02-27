> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI Keyboard Shortcuts and Custom Settings

> Keyboard and mouse shortcuts for ComfyUI and related settings

{/* TODO(yoland): Add this back to comfyUI readme page */}

Currently, ComfyUI supports custom keyboard shortcuts. You can set the shortcuts by clicking on `Settings (gear icon)` --> `Keybinding`.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ec261f919615b16c4b111e6370926543" alt="ComfyUI Shortcut Settings" data-og-width="1692" width="1692" data-og-height="1368" height="1368" data-path="images/interface/setting/keybinding.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=d48c51c47e759dae0d9c5ea611590165 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=622388e6fa819f8570231cb1a90f2055 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dcd5b6fc07a781a29421136ea1dca316 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=7b07e58fd0e676b1fe95dee3d2337138 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=50e401f316a5d73cbcf83c69ef04d452 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/keybinding.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=14a051c626877fa3d7b5059c3b94f711 2500w" />

In the corresponding menu, you can see all the current shortcut settings for ComfyUI. Click the `edit icon` before the corresponding command to customize the shortcut.

Below is the current list of shortcuts for ComfyUI, which you can customize as needed.

<Tabs>
  <Tab title="Windows/Linux">
    | Shortcut                        | Command                                                                                                            |
    | ------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
    | Ctrl + Enter                    | Queue prompt                                                                                                       |
    | Ctrl + Shift + Enter            | Queue prompt (Front)                                                                                               |
    | Ctrl + Alt + Enter              | Interrupt                                                                                                          |
    | Ctrl + Z / Ctrl + Y             | Undo/Redo                                                                                                          |
    | Ctrl + S                        | Save workflow                                                                                                      |
    | Ctrl + O                        | Load workflow                                                                                                      |
    | Ctrl + A                        | Select all nodes                                                                                                   |
    | Alt + C                         | Collapse/uncollapse selected nodes                                                                                 |
    | Ctrl + M                        | Mute/unmute selected nodes                                                                                         |
    | Ctrl + B                        | Bypass/unbypass selected nodes                                                                                     |
    | Delete<br />Backspace           | Delete selected nodes                                                                                              |
    | Backspace                       | Clear workflow                                                                                                     |
    | Space                           | Move canvas when holding and moving cursor                                                                         |
    | Ctrl + Click<br />Shift + Click | Add clicked node to selection                                                                                      |
    | Ctrl + C/Ctrl + V               | Copy and paste selected nodes (without maintaining connections to outputs of unselected nodes)                     |
    | Ctrl + C/Ctrl + Shift + V       | Copy and paste selected nodes (maintaining connections from outputs of unselected nodes to inputs of pasted nodes) |
    | Shift + Drag                    | Move multiple selected nodes at the same time                                                                      |
    | Ctrl + G                        | Add frame to selected nodes                                                                                        |
    | Ctrl + ,                        | Show settings dialog                                                                                               |
    | Alt + =                         | Zoom in (canvas)                                                                                                   |
    | Alt + -                         | Zoom out (canvas)                                                                                                  |
    | .                               | Fit view to selected nodes                                                                                         |
    | P                               | Pin/unpin selected items                                                                                           |
    | Q                               | Toggle queue sidebar                                                                                               |
    | W                               | Toggle workflow sidebar                                                                                            |
    | N                               | Toggle node library sidebar                                                                                        |
    | M                               | Toggle model library sidebar                                                                                       |
    | Ctrl + \`                       | Toggle log bottom panel                                                                                            |
    | F                               | Toggle focus mode (full screen)                                                                                    |
    | R                               | Refresh node definitions                                                                                           |
    | Double-Click LMB                | Quick search for nodes to add                                                                                      |
  </Tab>

  <Tab title="MacOS">
    | Shortcut                         | Command                                                                                                            |
    | -------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
    | Cmd ⌘ + Enter                    | Queue prompt                                                                                                       |
    | Cmd ⌘ + Shift + Enter            | Queue prompt (Front)                                                                                               |
    | Cmd ⌘ + Alt + Enter              | Interrupt                                                                                                          |
    | Cmd ⌘ + Z/Cmd ⌘ + Y              | Undo/Redo                                                                                                          |
    | Cmd ⌘ + S                        | Save workflow                                                                                                      |
    | Cmd ⌘ + O                        | Load workflow                                                                                                      |
    | Cmd ⌘ + A                        | Select all nodes                                                                                                   |
    | Opt ⌥ + C                        | Collapse/uncollapse selected nodes                                                                                 |
    | Cmd ⌘ + M                        | Mute/unmute selected nodes                                                                                         |
    | Cmd ⌘ + B                        | Bypass/unbypass selected nodes                                                                                     |
    | Delete<br />Backspace            | Delete selected nodes                                                                                              |
    | Backspace                        | Clear workflow                                                                                                     |
    | Space                            | Move canvas when holding and moving cursor                                                                         |
    | Cmd ⌘ + Click<br />Shift + Click | Add clicked node to selection                                                                                      |
    | Cmd ⌘ + C / Cmd ⌘ + V            | Copy and paste selected nodes (without maintaining connections to outputs of unselected nodes)                     |
    | Cmd ⌘ + C / Cmd ⌘ + Shift + V    | Copy and paste selected nodes (maintaining connections from outputs of unselected nodes to inputs of pasted nodes) |
    | Shift + Drag                     | Move multiple selected nodes at the same time                                                                      |
    | Cmd ⌘ + G                        | Add frame to selected nodes                                                                                        |
    | Cmd ⌘ + ,                        | Show settings dialog                                                                                               |
    | Opt ⌥ + =                        | Zoom in (canvas)                                                                                                   |
    | Opt ⌥ + -                        | Zoom out (canvas)                                                                                                  |
    | .                                | Fit view to selected nodes                                                                                         |
    | P                                | Pin/unpin selected items                                                                                           |
    | Q                                | Toggle queue sidebar                                                                                               |
    | W                                | Toggle workflow sidebar                                                                                            |
    | N                                | Toggle node library sidebar                                                                                        |
    | M                                | Toggle model library sidebar                                                                                       |
    | Cmd ⌘ + \`                       | Toggle log bottom panel                                                                                            |
    | F                                | Toggle focus mode (full screen)                                                                                    |
    | R                                | Refresh node definitions                                                                                           |
    | Double-Click LMB                 | Quick search for nodes to add                                                                                      |
  </Tab>
</Tabs>
