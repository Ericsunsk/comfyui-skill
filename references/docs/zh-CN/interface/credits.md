> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# ComfyUI 积分管理

> 在本篇中我们将介绍 ComfyUI 的积分管理功能，包括积分的获取、使用、查看等操作。

积分系统是为了支持 `Partner Nodes` 节点而新增的，由于调用闭源 AI 模型需要消耗Token，所以对应的积分管理是很有必要的，在默认情况下积分界面并不会展示，请首先在`设置` -> `用户`中登录对应的 ComfyUI 账号，然后你就可以在 `设置` -> `积分` 中查看关联账号的积分信息了。

<img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5c862444d78a8887b8f8fd500bf1b1fd" alt="ComfyUI 积分界面" data-og-width="3358" width="3358" data-og-height="1820" height="1820" data-path="images/zh/interface/setting/menu-credits.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0078ad8fca746d13e7e37b7af88bc21a 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=be7a88754951017d38429846baff9550 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=48a3c32781b4e56cc5b8d3e22bfe616e 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=2e62b1f074c32757a1811ecacc0076b3 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=4bf7e88f24f09823f4f38eba62bdc9d0 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=505c573620b6b2f0af75aaf0ea33d89f 2500w" />

<Note>
  ComfyUI将始终保持完全开源，并对本地用户免费。
</Note>

## 如何购买积分?

下面是对应的积分购买演示视频：

<video controls className="w-full aspect-video" src="https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/Buy_Credits_Flow.mp4?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a339505a6c77545fbb91e03a7a627c8b" data-path="images/interface/setting/Buy_Credits_Flow.mp4" />

详细操作步骤如下：

<Steps>
  <Step title="登录你的 ComfyUI 账号">
    在 `设置` -> `用户` 中登录你的 ComfyUI 账号
    <img src="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=156baae110c5223431a8692840481c27" alt="登录界面" data-og-width="3358" width="3358" data-og-height="1828" height="1828" data-path="images/zh/interface/setting/user.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=280&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=599786bda9ebbaa358ec6e968249e733 280w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=560&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=931837dd5ad64512911fd24ea12400f8 560w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=840&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=ee58e29fb4c99d7cf6a99471589b364d 840w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=1100&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=c53f39f9677914ad476c33e574e83ace 1100w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=1650&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=fc990161f80fa5a5aca616209fda2f6d 1650w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?w=2500&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=0fbc5469bb6f9bf527ca70d9f32e2869 2500w" />
  </Step>

  <Step title="前往 `设置` -> `积分` 中对积分进行购买">
    在登录后你应该可以看到对应的菜单增加了 `积分（Credits）` 选项

    前往 `设置` -> `积分` 中对积分进行购买
    <img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/purchase-1.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3abd5716f8e8dd5f1e52a969cb73667d" alt="积分界面" data-og-width="3358" width="3358" data-og-height="1820" height="1820" data-path="images/zh/interface/setting/purchase-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/purchase-1.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d5b82af578de5d6ee9c56e4997620e84 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/purchase-1.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ca98c6bd787a559021ff376a1656354a 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/purchase-1.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c3f1abd5b72ad92430c5254bcf21bad8 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/purchase-1.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=138a476827eab9b971e7e18a5761ec33 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/purchase-1.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=30c5b1fe0087dbc069a3a48d172cf653 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/purchase-1.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f4010325b7e1195d89bddcc4b68f9064 2500w" />
  </Step>

  <Step title="设置购买积分的金额">
    <img src="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/buy.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1509ad064fcc11da8b662544793a0503" alt="设置购买金额" data-og-width="3354" width="3354" data-og-height="1828" height="1828" data-path="images/zh/interface/setting/buy.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/buy.jpg?w=280&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5576a2c343454eb5bb432d2e50eeccc0 280w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/buy.jpg?w=560&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b153ea26116b391efec87236a72eadae 560w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/buy.jpg?w=840&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c4047b32db976566b92ea93d829d49ab 840w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/buy.jpg?w=1100&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=991b103b66342df97ccc8f4c29ce1171 1100w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/buy.jpg?w=1650&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a3f1f1eb45983cbf20e95d65e4daa6d8 1650w, https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/buy.jpg?w=2500&fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=29851737f50c4a40d0848c9e94c254da 2500w" />
    在弹窗中设置购买金额，并点击 `购买`按钮
  </Step>

  <Step title="在 Stripe 中进行支付">
    <img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/stripe_payment.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=2f50a9b77c2e20986184a934e664881d" alt="stripe 支付页面" data-og-width="4000" width="4000" data-og-height="2203" height="2203" data-path="images/interface/setting/stripe_payment.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/stripe_payment.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=809687e3675146d778f288a67d59007e 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/stripe_payment.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=dbe0830f4fe51572189fdf285cfb6f5c 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/stripe_payment.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=eaa1e0ae4bddcfc7826bdbd33363e2bb 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/stripe_payment.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=b59d0398e3b84686dc6a7cd28c1855d5 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/stripe_payment.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=86926a7fc4f302e016ce96041856bf20 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/stripe_payment.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e02dd6e259df06d387ed680874f3b8e4 2500w" />
    在支付页面请进行以下步骤：

    1. 选择用于支付的币种
    2. 确认对应的邮箱是你在 ComfyUI 中的注册邮箱
    3. 选择对应的支付方式

    * 信用卡
    * 微信（仅在选择使用 Comfy Credits 支付时才支持）
    * 支付宝（仅在选择使用 Comfy Credits 支付时才支持）

    4. 点击 `Pay` 按钮或者`Generate QR Code` 按钮完成对应的支付流程
  </Step>

  <Step title="完成支付，并检查积分余额">
    <img src="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/purchase-2.jpg?fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=dbd346fb31f6fefd993347d7af7966b6" alt="支付成功" data-og-width="3310" width="3310" data-og-height="1828" height="1828" data-path="images/zh/interface/setting/purchase-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/purchase-2.jpg?w=280&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=8ef2c3dda55c855ec4efff27908c5091 280w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/purchase-2.jpg?w=560&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=7322a3fce80c5da149aed0a1cd248a1f 560w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/purchase-2.jpg?w=840&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=73c0df1d86bac422b3cae47c0dc7c608 840w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/purchase-2.jpg?w=1100&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=ec4ef51b361b0e222bdb6042fc147856 1100w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/purchase-2.jpg?w=1650&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=c0fa533a27443bca3ef2fb643e22e5d8 1650w, https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/purchase-2.jpg?w=2500&fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=0460eb0b3d575cca9ca2bfc0a964397e 2500w" />
    在支付动作完成后，请返回`菜单` -> `积分` 检查你的余额是否已经更新，请试着刷新界面或者重启
  </Step>
</Steps>

## 常见问题

<AccordionGroup>
  <Accordion title="是否支持积分出现负数？">
    不支持，当积分为负数时你将无法运行 Partner Nodes
  </Accordion>

  <Accordion title="如果我有没有用完的积分支持退款吗？">
    目前我们暂不支持退款
  </Accordion>

  <Accordion title="我要如何查看当前余额和使用量？">
    点击`设置` -> `积分` 即可在对应页面看淡当前余额和`积分历史`的入口
  </Accordion>

  <Accordion title="我的积分可以和其他用户共享吗？">
    我们可以在多个设备间登录同一个账号，但是不支持共享积分给其它用户
  </Accordion>

  <Accordion title="我要如何知道每次消耗了多少积分？">
    由于不同尺寸的图像和生成数量，每次消耗的`Token` 和 `积分`是不一样的，在 `设置` -> `积分` 中，你可以看到每次消耗的积分，以及对应的积分历史
  </Accordion>

  <Accordion title="为什么没有支付宝微信支付选项？">
    请确保你选择了 Comfy Credits 支付，目前微信支付宝等仅在 Comfy Credits 支付时才支持
  </Accordion>

  <Accordion title="积分会过期吗？">
    会的，过期时间取决于积分类型：

    * **月度积分**：在账单周期结束时过期
    * **充值积分**：在购买之日起1年后过期
  </Accordion>
</AccordionGroup>
