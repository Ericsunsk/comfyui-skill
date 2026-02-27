> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Customizing ComfyUI Appearance

> Learn how to customize the appearance of ComfyUI using color palettes and advanced CSS options

ComfyUI offers flexible appearance customization options that allow you to personalize the interface to your preferences.

## Color Palette System

The primary way to customize ComfyUI's appearance is through the built-in color palette system.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=206dbb5bcf19ba1923bd722e20ba868e" alt="Color Palette" data-og-width="1180" width="1180" data-og-height="174" height="174" data-path="images/interface/setting/appearance/color-palette.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c9a9689322656132fe0cc942ded1b06e 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0fafde84e9684d46ce7818b09ffa3a59 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0d114e91564c4155e8667de6aa562976 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=806613c3883910fb1d6ae75e7a85e601 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=168dfc4fdd621f263fa7ad9432f08a6c 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bf2a301c7a1fb756bf9ba53d3ce96906 2500w" />

This allows you to:

1. Switch ComfyUI themes
2. Export the currently selected theme as JSON format
3. Load custom theme configuration from JSON file
4. Delete custom theme configuration

<Note>
  For appearance needs that cannot be satisfied by the color palette, you can perform advanced appearance customization through the [user.css](#advanced-customization-with-user-css) file
</Note>

### How to Customize Color Themes

The color palette allows you to modify many specific properties. Here are some of the most commonly customized elements, with colors represented in hexadecimal format:

<Tip>
  1. The JSON comments below are for illustration only. Do not copy the content below for modification as it will cause the theme to malfunction.
  2. Since we are still iterating frequently, the content below may change with ComfyUI frontend updates. If you need to modify, please export the theme configuration from settings and then modify it.
</Tip>

```json  theme={null}
{
  "id": "dark",                     // Must be unique, cannot be the same as other theme IDs
  "name": "Dark (Default)",         // Theme name, displayed in theme selector
  "colors": {
    "node_slot": {                  // Node connection slot color configuration
      "CLIP": "#FFD500",            // CLIP model connection slot color
      "CLIP_VISION": "#A8DADC",     // CLIP Vision model connection slot color
      "CLIP_VISION_OUTPUT": "#ad7452", // CLIP Vision output connection slot color
      "CONDITIONING": "#FFA931",     // Conditioning control connection slot color
      "CONTROL_NET": "#6EE7B7",     // ControlNet model connection slot color
      "IMAGE": "#64B5F6",           // Image data connection slot color
      "LATENT": "#FF9CF9",          // Latent space connection slot color
      "MASK": "#81C784",            // Mask data connection slot color
      "MODEL": "#B39DDB",           // Model connection slot color
      "STYLE_MODEL": "#C2FFAE",     // Style model connection slot color
      "VAE": "#FF6E6E",             // VAE model connection slot color
      "NOISE": "#B0B0B0",           // Noise data connection slot color
      "GUIDER": "#66FFFF",          // Guider connection slot color
      "SAMPLER": "#ECB4B4",         // Sampler connection slot color
      "SIGMAS": "#CDFFCD",          // Sigmas data connection slot color
      "TAESD": "#DCC274"            // TAESD model connection slot color
    },
    "litegraph_base": {             // LiteGraph base interface configuration
      "BACKGROUND_IMAGE": "",        // Background image, default is empty
      "CLEAR_BACKGROUND_COLOR": "#222", // Main canvas background color
      "NODE_TITLE_COLOR": "#999",    // Node title text color
      "NODE_SELECTED_TITLE_COLOR": "#FFF", // Selected node title color
      "NODE_TEXT_SIZE": 14,          // Node text size
      "NODE_TEXT_COLOR": "#AAA",     // Node text color
      "NODE_TEXT_HIGHLIGHT_COLOR": "#FFF", // Node text highlight color
      "NODE_SUBTEXT_SIZE": 12,       // Node subtext size
      "NODE_DEFAULT_COLOR": "#333",   // Node default color
      "NODE_DEFAULT_BGCOLOR": "#353535", // Node default background color
      "NODE_DEFAULT_BOXCOLOR": "#666", // Node default border color
      "NODE_DEFAULT_SHAPE": 2,        // Node default shape
      "NODE_BOX_OUTLINE_COLOR": "#FFF", // Node border outline color
      "NODE_BYPASS_BGCOLOR": "#FF00FF", // Node bypass background color
      "NODE_ERROR_COLOUR": "#E00",    // Node error state color
      "DEFAULT_SHADOW_COLOR": "rgba(0,0,0,0.5)", // Default shadow color
      "DEFAULT_GROUP_FONT": 24,       // Group default font size
      "WIDGET_BGCOLOR": "#222",       // Widget background color
      "WIDGET_OUTLINE_COLOR": "#666", // Widget outline color
      "WIDGET_TEXT_COLOR": "#DDD",    // Widget text color
      "WIDGET_SECONDARY_TEXT_COLOR": "#999", // Widget secondary text color
      "WIDGET_DISABLED_TEXT_COLOR": "#666", // Widget disabled state text color
      "LINK_COLOR": "#9A9",          // Connection line color
      "EVENT_LINK_COLOR": "#A86",    // Event connection line color
      "CONNECTING_LINK_COLOR": "#AFA", // Connecting line color
      "BADGE_FG_COLOR": "#FFF",      // Badge foreground color
      "BADGE_BG_COLOR": "#0F1F0F"    // Badge background color
    },
    "comfy_base": {                  // ComfyUI base interface configuration
      "fg-color": "#fff",            // Foreground color
      "bg-color": "#202020",         // Background color
      "comfy-menu-bg": "#353535",    // Menu background color
      "comfy-menu-secondary-bg": "#303030", // Secondary menu background color
      "comfy-input-bg": "#222",      // Input field background color
      "input-text": "#ddd",          // Input text color
      "descrip-text": "#999",        // Description text color
      "drag-text": "#ccc",           // Drag text color
      "error-text": "#ff4444",       // Error text color
      "border-color": "#4e4e4e",     // Border color
      "tr-even-bg-color": "#222",    // Table even row background color
      "tr-odd-bg-color": "#353535",  // Table odd row background color
      "content-bg": "#4e4e4e",       // Content area background color
      "content-fg": "#fff",          // Content area foreground color
      "content-hover-bg": "#222",    // Content area hover background color
      "content-hover-fg": "#fff",    // Content area hover foreground color
      "bar-shadow": "rgba(16, 16, 16, 0.5) 0 0 0.5rem" // Bar shadow effect
    }
  }
}
```

## Canvas

### Background Image

* **Requirements**: ComfyUI frontend version 1.20.5 or newer
* **Function**: Set a custom background image for the canvas to provide a more personalized workspace. You can upload images or use web images to set the background for the canvas.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f393d494dfdc8b7b84997d58735d2f86" alt="Set Background Image" data-og-width="1768" width="1768" data-og-height="1524" height="1524" data-path="images/interface/setting/appearance/set-as-bg.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dacd49bd08e941c09260bb001b26c550 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=8ec0fa6b65c0a433e89c0c045fa9e3ea 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=3fbacb928e83bc685e3a4f605bfe53a2 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=cdae7e2939628dd6fe287d0047f6e0a5 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=da1e7e8201256f1366cfe5a8be6e0f21 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bb134d3708f6686aaf75574993159389 2500w" />

## Node

### Node Opacity

* **Function**: Set the opacity of nodes, where 0 represents completely transparent and 1 represents completely opaque.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=43e2a908124028996938fedd96869b25" alt="Node Opacity" data-og-width="956" width="956" data-og-height="594" height="594" data-path="images/interface/setting/appearance/node-opacity.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=73e58f2a90eb80dbdbb6d88b640313e7 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=5f19cd8413e15ada7f0edb8879fbad67 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=48b086d7d3915e66759f570816d4aec2 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9d1dea85356595670653779100d27dc1 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=10ebc6b715728a77bdd47d252c31fa12 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=623b9f92d33cd47608e41d886ca089ad 2500w" />

## Node Widget

### Textarea Widget Font Size

* **Range**: 8 - 24
* **Function**: Set the font size in textarea widgets. Adjusts the text display size in text input boxes to improve readability.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2406917ddcec26ddb4e882202d433d0a" alt="Textarea Widget Font Size" data-og-width="1206" width="1206" data-og-height="650" height="650" data-path="images/interface/setting/appearance/textarea-font-size.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=748bc7d69219db388d4e496c6407ac99 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b6afebc4fc8ccdc5a25ee657455bccf0 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=1b4fbbeb51d63345733f67171f080d12 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e0c1551690d00900d20bd90ffce4e24c 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=cff057ffc84f96a9bbc8ad0a3517c1dc 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bec2e089f63f4dbbd58e81ce9c535ea0 2500w" />

## Sidebar

### Unified Sidebar Width

* **Function**: When enabled, the sidebar width will be unified to a consistent width when switching between different sidebars. If disabled, different sidebars can maintain their custom widths when switching.

### Sidebar Size

* **Function**: Control the size of the sidebar, can be set to normal or small.

### Sidebar Location

* **Function**: Control whether the sidebar is displayed on the left or right side of the interface, allowing users to adjust the sidebar position according to their usage habits.

### Sidebar Style

* **Function**: Control the visual style of the sidebar. Options include:
  * **Connected**: The sidebar appears connected to the edge of the interface.
  * **Floating**: The sidebar appears as a floating panel with visual separation from the interface edge.

<img src="https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=c2bba9162ac584f219d9be2e912076b3" alt="Sidebar Style" data-og-width="615" width="615" data-og-height="707" height="707" data-path="images/interface/setting/appearance/sidbar_style.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=280&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=37cd6956187b453c751d229c037e20b4 280w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=560&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=f7cbb94120daca9e14c4efde3be83761 560w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=840&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=f10cab8d13b945d978a47fc0680bff09 840w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=1100&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=7bde7bdebbeef44bb92bf3c139e4eebe 1100w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=1650&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=10a5d01d6361b39a1e46ae8f034c7312 1650w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=2500&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=d785a83a7efd094c3a4a66130fea102f 2500w" />

## Tree Explorer

### Tree Explorer Item Padding

* **Function**: Set the padding of items in the tree explorer (sidebar panel), adjusting the spacing between items in the tree structure.

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9fb818218a4713f0a88700de25633a8c" alt="Tree Explorer Item Padding" data-og-width="1254" width="1254" data-og-height="650" height="650" data-path="images/interface/setting/appearance/padding.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=fac0725c9684e0bd4385aff8276b11ee 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4c41178c5e11f3c6365307177bf5417b 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c8de042df86c3c648b36a7096fc5503a 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=1e4e5e8b6bdfa9d6fdf9ce9101a4cf26 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4c83f423b1b54e709a77874c402218a8 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dc01878bc2e7ad3ce2b33214c506feab 2500w" />

## Advanced Customization with user.css

For cases where the color palette doesn't provide enough control, you can use custom CSS via a user.css file. This method is recommended for advanced users who need to customize elements that aren't available in the color palette system.

### Requirements

* ComfyUI frontend version 1.20.5 or newer

### Setting Up user.css

1. Create a file named `user.css` in your ComfyUI user directory (same location as your workflows and settings - see location details below)
2. Add your custom CSS rules to this file
3. Restart ComfyUI or refresh the page to apply changes

### User Directory Location

The ComfyUI user directory is where your personal settings, workflows, and customizations are stored. The location depends on your installation type:

<Tabs>
  <Tab title="Desktop - Windows">
    ```
    C:\Users\<your username>\AppData\Roaming\ComfyUI\user
    ```
  </Tab>

  <Tab title="Desktop - macOS">
    ```
    ~/<ComfyUI installation path>/ComfyUI/user
    ```
  </Tab>

  <Tab title="Desktop - Linux">
    ```
    ~/.config/ComfyUI/user
    ```
  </Tab>

  <Tab title="Manual Install">
    The user directory is located in your ComfyUI installation folder:

    ```
    <ComfyUI installation path>/user
    ```

    For example, if you cloned ComfyUI to `C:\ComfyUI`, your user directory would be `C:\ComfyUI\user\default` (or `C:\ComfyUI\user\john` if you've set up a custom username).

    <Note>
      ComfyUI supports multiple users per installation. If you haven't configured a custom username, it defaults to "default". Each user gets their own subdirectory within the `user` folder.
    </Note>
  </Tab>

  <Tab title="Portable">
    The user directory is located in your ComfyUI portable folder:

    ```
    <ComfyUI_windows_portable>/ComfyUI/user
    ```

    For example: `ComfyUI_windows_portable/ComfyUI/user/default`

    <Note>
      ComfyUI supports multiple users per installation. If you haven't configured a custom username, it defaults to "default". Each user gets their own subdirectory within the `user` folder.
    </Note>
  </Tab>
</Tabs>

This location contains your workflows, settings, and other user-specific files.

After finding the above folder location, please copy the corresponding CSS file to the corresponding user directory, such as the default user folder being `ComfyUI/user/default`, then restart ComfyUI or refresh the page to apply changes.

### user.css Examples and Related Instructions

The `user.css` file is loaded early in the application startup process. So you may need to use `!important` in your CSS rules to ensure they override the default styles.

**user.css Customization Examples**

```css  theme={null}
/* Increase font size in inputs and menus for better readability */
.comfy-multiline-input, .litecontextmenu .litemenu-entry {
    font-size: 20px !important;
}

/* Make context menu entries larger for easier selection */
.litegraph .litemenu-entry,
.litemenu-title {
  font-size: 24px !important; 
}

/* Custom styling for specific elements not available in the color palette */
.comfy-menu {
    border: 1px solid rgb(126, 179, 189) !important;
    border-radius: 0px 0px 0px 10px !important;
    backdrop-filter: blur(2px);
}
```

**Best Practices**

1. **Start with the color palette** for most customizations
2. Use **user.css only when necessary** for elements not covered by the color palette
3. **Export your theme** before making significant changes so you can revert if needed
4. **Share your themes** with the community to inspire others

**Troubleshooting**

* If your color palette changes don't appear, try refreshing the page
* If CSS customizations don't work, check that you're using frontend version 1.20.5+
* Try adding `!important` to user.css rules that aren't being applied
* Keep backups of your customizations to easily restore them
