> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Account Management

> In this document, we will introduce the account management features of ComfyUI, including account login, registration, and logout operations.

The account system was added to support `API Nodes`, which enable calls to closed-source model APIs, greatly expanding the possibilities of ComfyUI. Since these API calls consume tokens, we have added a corresponding user system.

Currently, we support the following login methods:

* Email login
* Google login
* Github login
* API Key login (for non-whitelisted site authorization)

We will provide relevant login requirements and explanations in this document.

## ComfyUI Version Requirements

You may need to use at least [ComfyUI v0.3.0](https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.30) to use the account system. Ensure that the corresponding frontend version is at least `1.17.11`. Sometimes the frontend may fail to install and revert to an older version, so please check if the frontend version is greater than `1.17.11` in `Settings` -> `About`.

In some regions, network restrictions may prevent normal access to the login API, causing timeouts or failures. Before logging in, please **ensure that your network environment does not restrict access to the corresponding API**, and make sure you can access sites like Google or Github.

<Tip>
  Since we are still in rapid iterative updates, related functions may change. If there are no special circumstances, please try to update to the latest version to get support for relevant functions.
</Tip>

## Network Requirements

To login to ComfyUI account, you must be in a secure network environment:

* Only allow access from `127.0.0.1` or `localhost`.
* Do not support using the `--listen` parameter to access the API node through a local network.
* If you are using a non-SSL certificate or a site that does not start with `https`, you may not be able to successfully log in.
* You may not be able to log in on a site that is not in our whitelist (but you can log in using an API Key now).
* Ensure you can connect to our service normally (some regions may require a proxy).

## How to Log In

Log in via `Settings` -> `User`:

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=066170b38e0b9ead026029685e00fa65" alt="ComfyUI User Interface" data-og-width="3358" width="3358" data-og-height="1828" height="1828" data-path="images/interface/setting/user.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c7f1a017e9b00c6224a440f83d121a59 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=92b830f85f4393d802f7f33bdce81634 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e294573cc054158fb3a108d10bc67087 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=5160ea18d19dfdde201bbf41dbb1af0b 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=463f4645799b84ea5dcd4879ed3b87ca 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e52e827f35eddf444e91e5ed4f11b331 2500w" />

## Login Methods

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-login.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=70d1bb2128baed57bcd3d87d0744eb46" alt="user-login" data-og-width="3450" width="3450" data-og-height="1914" height="1914" data-path="images/interface/setting/user-login.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-login.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c2d53b9870525d895c8fa81f0e538e3d 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-login.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=cd42ecbdbdf6125483de8371898b3fbd 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-login.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=43374539ccc89e2c0280ebfc993ac99b 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-login.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=35f4abe40eebf63264c33bb3683f11c2 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-login.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=8eff64dceb83f2aab2b6ba22102e2136 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-login.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=78a146c092c4a8b51f9839a395151aa3 2500w" />

If this is your first login, please create an account first.

<Card title="Logging in with an API Key" icon="key" href="/account/login#logging-in-with-an-api-key">
  For non-whitelisted sites or LAN environments, you can use API Key login. See the detailed guide in the account login documentation.
</Card>

## Post-Login Status

After logging in, a login button is displayed in the top menu bar of the ComfyUI interface. You can open the corresponding login interface through this button and log out of the corresponding account in the settings menu.

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=b23d8df619e6a9bf132ebb2184a8f96c" alt="user-logged" data-og-width="884" width="884" data-og-height="238" height="238" data-path="images/interface/setting/user-logged.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6513231322c210692fd491202e111e7f 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=f376347fb12608a390e12e5a2c13e356 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=5bd461139043f7801d4c167e2b4b74f8 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e97426ca6cfea8d2f9723f7762198c2b 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=1d2af01cd57d73a66db70fbf17623f1a 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-logged.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=05267f070d7950ebc8d928b5df12bcef 2500w" />

<img src="https://mintcdn.com/dripart/i-QzV1V5IIRkC9tt/images/interface/setting/menu-user-logged.jpg?fit=max&auto=format&n=i-QzV1V5IIRkC9tt&q=85&s=114285c984763119766644a35dab4002" alt="menu-user-logged" data-og-width="4266" width="4266" data-og-height="3230" height="3230" data-path="images/interface/setting/menu-user-logged.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/i-QzV1V5IIRkC9tt/images/interface/setting/menu-user-logged.jpg?w=280&fit=max&auto=format&n=i-QzV1V5IIRkC9tt&q=85&s=5b42fd498d1796c9962de0aa1635e957 280w, https://mintcdn.com/dripart/i-QzV1V5IIRkC9tt/images/interface/setting/menu-user-logged.jpg?w=560&fit=max&auto=format&n=i-QzV1V5IIRkC9tt&q=85&s=f8306bcbf6161cc9e1983be741f689a6 560w, https://mintcdn.com/dripart/i-QzV1V5IIRkC9tt/images/interface/setting/menu-user-logged.jpg?w=840&fit=max&auto=format&n=i-QzV1V5IIRkC9tt&q=85&s=54745182bde2201633475e6a3839aa4a 840w, https://mintcdn.com/dripart/i-QzV1V5IIRkC9tt/images/interface/setting/menu-user-logged.jpg?w=1100&fit=max&auto=format&n=i-QzV1V5IIRkC9tt&q=85&s=00fb3349320582961915354a6e167394 1100w, https://mintcdn.com/dripart/i-QzV1V5IIRkC9tt/images/interface/setting/menu-user-logged.jpg?w=1650&fit=max&auto=format&n=i-QzV1V5IIRkC9tt&q=85&s=55e09b7785d7ae4d00c9a1aedff6e8d7 1650w, https://mintcdn.com/dripart/i-QzV1V5IIRkC9tt/images/interface/setting/menu-user-logged.jpg?w=2500&fit=max&auto=format&n=i-QzV1V5IIRkC9tt&q=85&s=18259c2d6696a984912e03d4a4889102 2500w" />

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Are there any login device restrictions?">
    We do not restrict login devices. You can log in to your account on any device, but please note that your account information may be accessed by other devices, so do not log in to your account on public devices.
  </Accordion>

  <Accordion title="How to log in in a LAN environment?">
    Currently, only API Key login is supported in a LAN environment. If you are accessing ComfyUI services through a LAN, please use API Key to log in.
  </Accordion>

  <Accordion title="Why can't I log in on some websites?">
    Our login service has a whitelist, so you may not be able to log in to ComfyUI deployed on some servers, for this case, you can use API Key login to solve it.
  </Accordion>
</AccordionGroup>
