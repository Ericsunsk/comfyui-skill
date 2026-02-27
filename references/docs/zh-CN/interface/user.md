> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 账号管理

> 在本篇中我们将介绍 ComfyUI 的账号管理功能，包括账号的登录、注册、注销等操作。

账号系统是为了支持 `API Nodes` 节点而新增的，`API Nodes`支持了对闭源模型 API 的调用，这大大扩展了 ComfyUI 的可能性，由于对应的 API 调用需要消耗 Token，所以我们增加了对应的用户系统。

当前我们支持以下几种登录方式：

* 邮箱登录
* Google 登录
* Github 登录
* API Key 登录(非白名单网站授权使用)

登录要求相关及说明，我们在本篇文档中会进行对应说明

## ComfyUI 版本要求

你可能至少需要使用 [ComfyUI v0.3.0](https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.30) 版本才能使用账号系统,确保对应前端版本至少为`1.17.11`,有时候前端可能会安装失败而导致回滚到旧版本，所以请在`设置` -> `关于` 查看前端版本是否大于`1.17.11`

在部分地区可能会因为网络限制无法正常访问登录 API 导致登录超时或者失败， 在登录前请**确保你的网络环境不会被限制对应 API 的访问**，保证能够正常访问 Google 或者 Github 等网站。

<Tip>
  由于我们仍在快速迭代更新，所以相关功能可能会有变动，如果没有特殊情况，请尽量更新到最新版本以获取相关功能支持。
</Tip>

## 网络要求

要使用API，你必须处于安全的网络环境中：

* 允许从`127.0.0.1`或`localhost`访问。
* 不支持使用`--listen`参数通过局域网访问API节点。
* 在未启用 SSL 证书即非 `https` 开头的站点你可能无法成功登录
* 你可能无法在不在我们白名单的站点中登录（可以通过 API Key 登录）
* 确保你能够正常连接我们的服务（在某些地区可能需要代理来访问）。

## 如何进行登录

在 `设置` -> `用户` 中进行登录：

<img src="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=156baae110c5223431a8692840481c27" alt="ComfyUI 用户界面" data-og-width="3358" width="3358" data-og-height="1828" height="1828" data-path="images/zh/interface/setting/user.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=280&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=599786bda9ebbaa358ec6e968249e733 280w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=560&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=931837dd5ad64512911fd24ea12400f8 560w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=840&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=ee58e29fb4c99d7cf6a99471589b364d 840w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=1100&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=c53f39f9677914ad476c33e574e83ace 1100w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=1650&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=fc990161f80fa5a5aca616209fda2f6d 1650w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=2500&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=0fbc5469bb6f9bf527ca70d9f32e2869 2500w" />

## 登录方式

<img src="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user-login.jpg?fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=488ac4c4d44ec739af66f07f08033bb7" alt="user-login" data-og-width="3354" width="3354" data-og-height="1850" height="1850" data-path="images/zh/interface/setting/user-login.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user-login.jpg?w=280&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=b7aa4d45d82da0d655a53a696a6ebef4 280w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user-login.jpg?w=560&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=f0a9663c3c1d02986f714c6292582696 560w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user-login.jpg?w=840&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=d05893f189be730b76cfff93f4ad0205 840w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user-login.jpg?w=1100&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=8c5a5902c8a16b6f5c12b886a9a9151c 1100w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user-login.jpg?w=1650&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=19458045b0c23df97194c5adeddc1a21 1650w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user-login.jpg?w=2500&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=e8b686b358c40a693c88202ae551b922 2500w" />

如果是首次登录，请首先创建一个账户。

<Card title="使用 API Key 进行登录" icon="key" href="/zh-CN/account/login#使用-api-key-进行登录">
  对于非白名单网站或局域网环境，你可以使用 API Key 登录。请查看账户登录文档中的详细指南。
</Card>

## 登录后状态

登录后在 CofmyUI 界面顶部菜单栏显示登录按钮，并可以通过该按钮打开对应的登录界面，并可以在设置菜单中退出对应的账号

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=b23d8df619e6a9bf132ebb2184a8f96c" alt="user-logged" data-og-width="884" width="884" data-og-height="238" height="238" data-path="images/interface/setting/user-logged.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6513231322c210692fd491202e111e7f 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=f376347fb12608a390e12e5a2c13e356 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=5bd461139043f7801d4c167e2b4b74f8 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e97426ca6cfea8d2f9723f7762198c2b 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=1d2af01cd57d73a66db70fbf17623f1a 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=05267f070d7950ebc8d928b5df12bcef 2500w" />

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-user-logged.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f1355762418eddba66d524ceee7dc234" alt="menu-user-logged" data-og-width="3358" width="3358" data-og-height="1820" height="1820" data-path="images/zh/interface/setting/menu-user-logged.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-user-logged.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=624f02cdf3ad0886f773c29c9dcaa8a4 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-user-logged.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ad7589720c8a4ab523c592e97476d78e 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-user-logged.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=356735f6c7d2cddb596df001cbe81a7f 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-user-logged.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7073088cb177bbb91e8b1091d76e9225 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-user-logged.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=863c9b1624a8b2a624a8b0abab0ece9d 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-user-logged.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0f450cbdccc77df1cf42441138df5efe 2500w" />

## 常见问题

<AccordionGroup>
  <Accordion title="是否存在登录设备限制？">
    我们不会对登录设备进行限制，你可以在任何设备上登录你的账号，但是请注意，你的账号信息可能会被其他设备访问，所以请不要在公共设备上登录你的账号。
  </Accordion>

  <Accordion title="局域网内要如何登录？">
    目前局域网内仅支持通过 API Key 登录，如果你是通过局域网访问 ComfyUI 相关服务，请使用 API Key 来进行登录。
  </Accordion>

  <Accordion title="在一些网站为什么没法登录？">
    由于我们的登录服务设置了白名单，所以你可能在一些服务端上部署的 ComfyUI 无法正常登录，对于此类情况，你可以使用 API Key 登录来解决。
  </Accordion>
</AccordionGroup>
