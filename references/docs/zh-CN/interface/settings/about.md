> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 关于页面

> ComfyUI 关于设置页详细说明

About 页面是 ComfyUI 设置系统中的一个信息展示面板，用于显示应用程序版本信息、相关链接和系统统计数据，这些设置在向我们提交反馈问题时，可以提供给我们一些非常关键的信息。

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6fdb66bb60546e4a894ea10c7d46340e" alt="about" data-og-width="2130" width="2130" data-og-height="1530" height="1530" data-path="images/interface/setting/settings-about.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a414ed9196a5440614e81b70f99d22af 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=8000c5d757bad85921092c07ce294f8c 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=7cf5d70ae1569afeff6a1bd7f663956d 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3e56877d6e2f9f978efbae9662acf9c4 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=95497cee7748c0bcb8fc99d85ab4ade9 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=fb20ec9f1d1477d715a8e7e464d49c66 2500w" />

### 版本信息徽章

About 页面显示以下核心版本信息：

* **ComfyUI 版本**：显示后端 ComfyUI 的版本号，链接到官方 GitHub 仓库
* **ComfyUI\_frontend 版本**：显示前端界面的版本号，链接到前端 GitHub 仓库
* **Discord 社区**：提供 ComfyOrg Discord 服务器的链接
* **官方网站**：链接到 ComfyOrg 官方网站

<Tip>
  由于这里的版本信息主要是对应稳定版本的信息，如果你正在使用的是 nightly 版本，那么这里并不会显示对应的 commit hash 等，如果你正在使用 nightly 版本，可以在对应的 ComfyUI 主目录中使用 `git log` 命令来查看对应的 commit hash 等信息。
  另外一个常见的问题是，不同的依赖包会在更新中失败回滚
</Tip>

### 自定义节点徽章

如果安装了自定义节点，About 页面还会显示自定义节点提供的额外徽章信息。这些徽章由各个自定义节点通过 `aboutPageBadges` 属性注册。

### 系统统计信息

页面底部显示详细的系统统计信息，包括：

* 硬件配置信息
* 软件环境信息
* 系统性能数据

## 扩展开发者指南

扩展开发者可以通过在扩展配置中添加 `aboutPageBadges` 属性来向 About 页面添加自定义徽章：

```javascript  theme={null}
app.registerExtension({
  name: 'MyExtension',
  aboutPageBadges: [
    {
      label: 'My Extension v1.0.0',
      url: 'https://github.com/myuser/myextension',
      icon: 'pi pi-github'
    }
  ]
})
```
