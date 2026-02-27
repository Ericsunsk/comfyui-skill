> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 外观设置

> ComfyUI 外观设置选项的详细说明

这部分的设置主要用于自定义 ComfyUI 的外观，包括色彩主题、背景图片、节点样式等。

## 色彩主题

自定义 ComfyUI 外观的主要方式是通过内置的调色板系统。

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=206dbb5bcf19ba1923bd722e20ba868e" alt="色彩主题" data-og-width="1180" width="1180" data-og-height="174" height="174" data-path="images/interface/setting/appearance/color-palette.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c9a9689322656132fe0cc942ded1b06e 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0fafde84e9684d46ce7818b09ffa3a59 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=0d114e91564c4155e8667de6aa562976 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=806613c3883910fb1d6ae75e7a85e601 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=168dfc4fdd621f263fa7ad9432f08a6c 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/color-palette.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bf2a301c7a1fb756bf9ba53d3ce96906 2500w" />

1. 切换 ComfyUI 主题
2. 将当前选中的主题导出为 JSON 格式
3. 从Json文件中载入自定义主题配置
4. 删除自定义主题配置

<Note>
  对于调色板无法满足的外观需求，你可以通过 [user.css](#使用user-css进行高级外观自定义) 文件进行高级外观自定义
</Note>

### 如何自定义颜色主题

调色板允许您修改许多特定属性。以下是一些最常自定义的元素，颜色采用十六进制表示：

<Tip>
  1. 下面的 JSON 注释只是为了注释说明，实际使用请不要复制下面的内容进行修改，否则将会导致主题无法正常使用
  2. 由于我们仍在频繁迭代，下面的这些内容可能会随着 ComfyUI 前端的更新而有所调整，如果需要修改，请从设置中导出主题配置，然后进行修改
</Tip>

```json  theme={null}
{
  "id": "dark",                     // 必须是唯一的，不能和其它主题的id相同
  "name": "Dark (Default)",         // 主题名称,显示在主题选择器中
  "colors": {
    "node_slot": {                  // 节点连接槽的颜色配置
      "CLIP": "#FFD500",            // CLIP 模型连接槽颜色
      "CLIP_VISION": "#A8DADC",     // CLIP Vision 模型连接槽颜色
      "CLIP_VISION_OUTPUT": "#ad7452", // CLIP Vision 输出连接槽颜色
      "CONDITIONING": "#FFA931",     // 条件控制连接槽颜色
      "CONTROL_NET": "#6EE7B7",     // ControlNet 模型连接槽颜色
      "IMAGE": "#64B5F6",           // 图像数据连接槽颜色
      "LATENT": "#FF9CF9",          // 潜在空间连接槽颜色
      "MASK": "#81C784",            // 蒙版数据连接槽颜色
      "MODEL": "#B39DDB",           // 模型连接槽颜色
      "STYLE_MODEL": "#C2FFAE",     // 风格模型连接槽颜色
      "VAE": "#FF6E6E",             // VAE 模型连接槽颜色
      "NOISE": "#B0B0B0",           // 噪声数据连接槽颜色
      "GUIDER": "#66FFFF",          // 引导器连接槽颜色
      "SAMPLER": "#ECB4B4",         // 采样器连接槽颜色
      "SIGMAS": "#CDFFCD",          // Sigmas 数据连接槽颜色
      "TAESD": "#DCC274"            // TAESD 模型连接槽颜色
    },
    "litegraph_base": {             // LiteGraph 基础界面配置
      "BACKGROUND_IMAGE": "",        // 背景图片,默认为空
      "CLEAR_BACKGROUND_COLOR": "#222", // 主画布背景色
      "NODE_TITLE_COLOR": "#999",    // 节点标题文本颜色
      "NODE_SELECTED_TITLE_COLOR": "#FFF", // 选中节点的标题颜色
      "NODE_TEXT_SIZE": 14,          // 节点文本大小
      "NODE_TEXT_COLOR": "#AAA",     // 节点文本颜色
      "NODE_TEXT_HIGHLIGHT_COLOR": "#FFF", // 节点文本高亮颜色
      "NODE_SUBTEXT_SIZE": 12,       // 节点子文本大小
      "NODE_DEFAULT_COLOR": "#333",   // 节点默认颜色
      "NODE_DEFAULT_BGCOLOR": "#353535", // 节点默认背景色
      "NODE_DEFAULT_BOXCOLOR": "#666", // 节点默认边框颜色
      "NODE_DEFAULT_SHAPE": 2,        // 节点默认形状
      "NODE_BOX_OUTLINE_COLOR": "#FFF", // 节点边框轮廓颜色
      "NODE_BYPASS_BGCOLOR": "#FF00FF", // 节点旁路背景色
      "NODE_ERROR_COLOUR": "#E00",    // 节点错误状态颜色
      "DEFAULT_SHADOW_COLOR": "rgba(0,0,0,0.5)", // 默认阴影颜色
      "DEFAULT_GROUP_FONT": 24,       // 分组默认字体大小
      "WIDGET_BGCOLOR": "#222",       // 小部件背景色
      "WIDGET_OUTLINE_COLOR": "#666", // 小部件轮廓颜色
      "WIDGET_TEXT_COLOR": "#DDD",    // 小部件文本颜色
      "WIDGET_SECONDARY_TEXT_COLOR": "#999", // 小部件次要文本颜色
      "WIDGET_DISABLED_TEXT_COLOR": "#666", // 小部件禁用状态文本颜色
      "LINK_COLOR": "#9A9",          // 连接线颜色
      "EVENT_LINK_COLOR": "#A86",    // 事件连接线颜色
      "CONNECTING_LINK_COLOR": "#AFA", // 正在连接时的连接线颜色
      "BADGE_FG_COLOR": "#FFF",      // 徽章前景色
      "BADGE_BG_COLOR": "#0F1F0F"    // 徽章背景色
    },
    "comfy_base": {                  // ComfyUI 基础界面配置
      "fg-color": "#fff",            // 前景色
      "bg-color": "#202020",         // 背景色
      "comfy-menu-bg": "#353535",    // 菜单背景色
      "comfy-menu-secondary-bg": "#303030", // 次级菜单背景色
      "comfy-input-bg": "#222",      // 输入框背景色
      "input-text": "#ddd",          // 输入文本颜色
      "descrip-text": "#999",        // 描述文本颜色
      "drag-text": "#ccc",           // 拖拽文本颜色
      "error-text": "#ff4444",       // 错误文本颜色
      "border-color": "#4e4e4e",     // 边框颜色
      "tr-even-bg-color": "#222",    // 表格偶数行背景色
      "tr-odd-bg-color": "#353535",  // 表格奇数行背景色
      "content-bg": "#4e4e4e",       // 内容区背景色
      "content-fg": "#fff",          // 内容区前景色
      "content-hover-bg": "#222",    // 内容区悬停背景色
      "content-hover-fg": "#fff",    // 内容区悬停前景色
      "bar-shadow": "rgba(16, 16, 16, 0.5) 0 0 0.5rem" // 栏阴影效果
    }
  }
}
```

## 画布

### 背景图片

* 版本要求：ComfyUI 前端版本 1.20.5 或更新版本
* 功能：为画布设置自定义背景图片，提供更加个性化的工作空间，你可以上传图片或者使用网络图片来为画布设置背景图片

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=f393d494dfdc8b7b84997d58735d2f86" alt="设置背景图片" data-og-width="1768" width="1768" data-og-height="1524" height="1524" data-path="images/interface/setting/appearance/set-as-bg.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dacd49bd08e941c09260bb001b26c550 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=8ec0fa6b65c0a433e89c0c045fa9e3ea 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=3fbacb928e83bc685e3a4f605bfe53a2 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=cdae7e2939628dd6fe287d0047f6e0a5 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=da1e7e8201256f1366cfe5a8be6e0f21 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/set-as-bg.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bb134d3708f6686aaf75574993159389 2500w" />

## 节点

### 节点不透明度

* 功能：设置节点的不透明度，0表示完全透明，1表示完全不透明

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=43e2a908124028996938fedd96869b25" alt="节点不透明度" data-og-width="956" width="956" data-og-height="594" height="594" data-path="images/interface/setting/appearance/node-opacity.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=73e58f2a90eb80dbdbb6d88b640313e7 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=5f19cd8413e15ada7f0edb8879fbad67 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=48b086d7d3915e66759f570816d4aec2 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9d1dea85356595670653779100d27dc1 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=10ebc6b715728a77bdd47d252c31fa12 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/node-opacity.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=623b9f92d33cd47608e41d886ca089ad 2500w" />

## 节点组件

### 文本域小部件字体大小\*\*

* **范围**：8 - 24
* **功能**：设置文本域小部件中的字体大小，调整文本输入框中文字的显示大小，提升可读性
  <img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=2406917ddcec26ddb4e882202d433d0a" alt="文本域小部件字体大小" data-og-width="1206" width="1206" data-og-height="650" height="650" data-path="images/interface/setting/appearance/textarea-font-size.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=748bc7d69219db388d4e496c6407ac99 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=b6afebc4fc8ccdc5a25ee657455bccf0 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=1b4fbbeb51d63345733f67171f080d12 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e0c1551690d00900d20bd90ffce4e24c 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=cff057ffc84f96a9bbc8ad0a3517c1dc 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/textarea-font-size.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=bec2e089f63f4dbbd58e81ce9c535ea0 2500w" />

## 侧边栏

### 统一侧边栏宽度

* **功能**：启用后，当你在不同的侧边栏之间切换时，侧边栏的宽度将统一为一致的宽度，如果禁用，不同的侧边栏的宽度在切换时可以保持自定义的宽度

### 侧边栏大小

* **功能**：控制侧边栏的尺寸大小，可以设置为正常或者小

### 侧边栏位置

* **功能**：控制侧边栏显示在界面的左侧还是右侧，允许用户根据使用习惯调整侧边栏位置

### 侧边栏样式

* **功能**：控制侧边栏的视觉样式。选项包括：
  * **连接式（Connected）**：侧边栏与界面边缘连接显示。
  * **悬浮式（Floating）**：侧边栏以悬浮面板形式显示，与界面边缘有视觉分隔。

<img src="https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=c2bba9162ac584f219d9be2e912076b3" alt="侧边栏样式" data-og-width="615" width="615" data-og-height="707" height="707" data-path="images/interface/setting/appearance/sidbar_style.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=280&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=37cd6956187b453c751d229c037e20b4 280w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=560&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=f7cbb94120daca9e14c4efde3be83761 560w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=840&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=f10cab8d13b945d978a47fc0680bff09 840w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=1100&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=7bde7bdebbeef44bb92bf3c139e4eebe 1100w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=1650&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=10a5d01d6361b39a1e46ae8f034c7312 1650w, https://mintcdn.com/dripart/0LfkiFdUyOZfrZN7/images/interface/setting/appearance/sidbar_style.jpg?w=2500&fit=max&auto=format&n=0LfkiFdUyOZfrZN7&q=85&s=d785a83a7efd094c3a4a66130fea102f 2500w" />

## 树形浏览器

### 树形浏览器项目内边距

* **功能**：设置树形浏览器（侧边栏面板）中项目的内边距，调整树形结构中各项目之间的间距

<img src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=9fb818218a4713f0a88700de25633a8c" alt="树形浏览器项目内边距" data-og-width="1254" width="1254" data-og-height="650" height="650" data-path="images/interface/setting/appearance/padding.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=280&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=fac0725c9684e0bd4385aff8276b11ee 280w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=560&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4c41178c5e11f3c6365307177bf5417b 560w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=840&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=c8de042df86c3c648b36a7096fc5503a 840w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=1100&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=1e4e5e8b6bdfa9d6fdf9ce9101a4cf26 1100w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=1650&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=4c83f423b1b54e709a77874c402218a8 1650w, https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/appearance/padding.jpg?w=2500&fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=dc01878bc2e7ad3ce2b33214c506feab 2500w" />

## 使用user.css进行高级外观自定义

对于调色板不能提供足够控制的情况，您可以通过 user.css 文件使用自定义 CSS。此方法推荐给需要自定义调色板系统中不可用元素的高级用户。

### 要求

* ComfyUI 前端版本 1.20.5 或更新版本

### 设置 user.css

1. 在 ComfyUI 用户目录（与工作流和设置相同位置 - 请参阅下面的位置详细信息）中创建一个名为 `user.css` 的文件
2. 在此文件中添加您的自定义 CSS 规则
3. 重启 ComfyUI 或刷新页面以应用更改

### 用户目录位置

ComfyUI 用户目录是存储您的个人设置、工作流和自定义内容的地方。位置取决于您的安装类型：

<AccordionGroup>
  <Accordion title="桌面版Windows">
    ```
    C:\Users\<你的用户名>\AppData\Roaming\ComfyUI\user
    ```
  </Accordion>

  <Accordion title="桌面版macOS">
    ```
    ~/<ComfyUI 安装路径>/ComfyUI/user
    ```
  </Accordion>

  <Accordion title="手动安装">
    用户目录位于您的 ComfyUI 安装文件夹中：

    ```
    <ComfyUI_安装路径>/user/
    ```

    例如，如果您将 ComfyUI 克隆到 `C:\ComfyUI`，您的用户目录将是 `C:\ComfyUI\user\default`（或者如果您设置了自定义用户名，则为 `C:\ComfyUI\user\john`）。

    <Note>
      ComfyUI 支持每个安装支持多个用户。如果您没有配置自定义用户名，默认为 "default"。每个用户在 `user` 文件夹内都有自己的子目录。
    </Note>
  </Accordion>

  <Accordion title="便携版">
    用户目录位于您的 ComfyUI 便携版文件夹中：

    ```
    <ComfyUI_windows_portable>/ComfyUI/user/
    ```

    例如：`ComfyUI_windows_portable/ComfyUI/user/default`

    <Note>
      ComfyUI 支持每个安装支持多个用户。如果您没有配置自定义用户名，默认为 "default"。每个用户在 `user` 文件夹内都有自己的子目录。
    </Note>
  </Accordion>
</AccordionGroup>

此位置包含您的工作流、设置和其他用户特定文件。

找到上述文件夹位置后，请将对应的 Css 文件复制到对应的用户目录中如默认用户文件夹为`ComfyUI/user/default`，然后重启 ComfyUI 或刷新页面以应用更改

### user.css 示例及相关说明

`user.css` 文件会在启动的早期就进行加载。所以能需要在 CSS 规则中使用 `!important` 来确保它们覆盖默认样式。

**user.css 自定义示例**

```css  theme={null}
/* 增加输入框和菜单中的字体大小以提高可读性 */
.comfy-multiline-input, .litecontextmenu .litemenu-entry {
    font-size: 20px !important;
}

/* 使上下文菜单项更大，便于选择 */
.litegraph .litemenu-entry,
.litemenu-title {
  font-size: 24px !important; 
}

/* 为调色板中不可用的特定元素自定义样式 */
.comfy-menu {
    border: 1px solid rgb(126, 179, 189) !important;
    border-radius: 0px 0px 0px 10px !important;
    backdrop-filter: blur(2px);
}
```

**最佳实践**

1. **首先使用调色板**进行大多数自定义
2. **仅在必要时使用 user.css**，用于调色板未涵盖的元素
3. **在进行重大更改前导出您的主题**，以便在需要时恢复
4. **与社区分享您的主题**，以启发他人

**故障排除**

* 如果您的调色板更改没有显示，尝试刷新页面
* 如果 CSS 自定义不起作用，检查您是否使用前端版本 1.20.5+
* 尝试在未应用的 user.css 规则中添加 `!important`
* 保留您的自定义备份，以便轻松恢复
