> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# About Page

> Detailed description of ComfyUI About settings page

The About page is an information display panel in the ComfyUI settings system, used to show application version information, related links, and system statistics. These settings can provide us with critical information when you submit feedback or report issues.

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6fdb66bb60546e4a894ea10c7d46340e" alt="about" data-og-width="2130" width="2130" data-og-height="1530" height="1530" data-path="images/interface/setting/settings-about.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a414ed9196a5440614e81b70f99d22af 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=8000c5d757bad85921092c07ce294f8c 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=7cf5d70ae1569afeff6a1bd7f663956d 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3e56877d6e2f9f978efbae9662acf9c4 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=95497cee7748c0bcb8fc99d85ab4ade9 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/settings-about.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=fb20ec9f1d1477d715a8e7e464d49c66 2500w" />

### Version Information Badges

The About page displays the following core version information:

* **ComfyUI Version**: Shows the backend ComfyUI version number, linked to the official GitHub repository
* **ComfyUI\_frontend Version**: Shows the frontend interface version number, linked to the frontend GitHub repository
* **Discord Community**: Provides a link to the ComfyOrg Discord server
* **Official Website**: Links to the ComfyOrg official website

<Tip>
  Since the version information here mainly corresponds to stable version information, if you are using the nightly version, the corresponding commit hash will not be displayed here. If you are using the nightly version, you can use the `git log` command in the corresponding ComfyUI main directory to view the corresponding commit hash and other information.
  Another common issue is that different dependency packages may fail and rollback during updates.
</Tip>

### Custom Node Badges

If custom nodes are installed, the About page will also display additional badge information provided by custom nodes. These badges are registered by each custom node through the `aboutPageBadges` property.

### System Info

The bottom of the page displays detailed system statistics, including:

* Hardware configuration information
* Software environment information
* System performance data

## Extension Developer Guide

Extension developers can add custom badges to the About page by adding the `aboutPageBadges` property to their extension configuration:

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
