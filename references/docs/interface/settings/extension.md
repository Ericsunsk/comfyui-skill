> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Extension Settings

> Detailed description of ComfyUI extension management and setting options

The Extension settings panel is a special management panel in the ComfyUI frontend settings system, specifically used to manage the enable/disable status of frontend extension plugins. Unlike Custom Nodes, this panel is only used to manage frontend extensions registered by custom nodes, not to disable custom nodes themselves.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=351dc6d25afbe287ed94c4bf39db91a1" alt="extension" data-og-width="1910" width="1910" data-og-height="1248" height="1248" data-path="images/interface/setting/extension/extension.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a34f411c79daef19b975794c98e095fc 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=12e4f6f41641a0e9a7600c55a9364fde 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0ee3665ed976865e6315f14b151282d5 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=98fb5076a9297011e4ab0993327a06da 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9ef00ebcc6e38e996ffa577618bfcb82 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/extension/extension.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c2e919422f54efaa23027110369dc014 2500w" />

These frontend extension plugins are used to enhance the ComfyUI experience, such as providing shortcuts, settings, UI components, menu items, and other features.

Extension status changes require a page reload to take effect:

## Extension Settings Panel Features

### 1. Extension List Management

Displays all registered extensions, including:

* Extension Name
* Core extension identification (displays "Core" label)
* Enable/disable status

### 2. Search Functionality

Provides a search box to quickly find specific extensions:

### 3. Enable/Disable Control

Each extension has an independent toggle switch:

### 4. Batch Operations

Provides right-click menu for batch operations:

* Enable All extensions
* Disable All extensions
* Disable 3rd Party extensions (keep core extensions)

## Notes

* Extension status changes require a page reload to take effect
* Some core extensions cannot be disabled
* The system will automatically disable known problematic extensions
* Extension settings are automatically saved to the user configuration file

This Extension settings panel is essentially a "frontend plugin manager" that allows users to flexibly control ComfyUI's functional modules.
