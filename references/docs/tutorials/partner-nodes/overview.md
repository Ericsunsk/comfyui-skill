> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Partner Nodes

> In this article, we will introduce ComfyUI's Partner Nodes and related information.

Partner Nodes are ComfyUI's new way of calling closed-source models through API requests, providing ComfyUI users with access to external state-of-the-art AI models without complex API key setup.

## What are Partner Nodes?

Partner Nodes are a set of special nodes that connect to external API services, allowing you to use closed-source or third-party hosted AI models directly in your ComfyUI workflows. These nodes are designed to seamlessly integrate the capabilities of external models while maintaining the open-source nature of ComfyUI's core.

Currently supported models include:

* **Black Forest Labs**: Flux 1.1\[pro] Ultra, Flux .1\[pro], Flux .1 Kontext Pro, Flux .1 Kontext Max, Flux.1 Canny Control, Flux.1 Depth Control, Flux.1 Expand, Flux.1 Fill
* **Google**: Veo2, Veo 3.0, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini Image
* **Ideogram**: V3, V2, V1
* **Kling**: 2.0, 1.6, 1.5, v1, v2-1, v2-1-master, v2-maser & Various Effects
* **Luma**: Photon, Ray2, Ray1.6, Ray-flash-2, Photo-flash-1
* **MiniMax**: Text-to-Video, Image-to-Video, Hailuo-02, T2V-01, I2V-01
* **Moonvalley**: Image-to-Video, Text-to-Video, Video-to-Video
* **OpenAI**: o1, o1-pro, o3, o4-mini, gpt-4o, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-5, gpt-5-mini, gpt-5-nano, DALL·E 2, DALL·E 3, GPT-Image-1
* **PixVerse**: V4 & Effects
* **Pika**: 2.2
* **Recraft**: V3, V2 & Various Tools
* **Hunyuan 3D**: Text-to-3D, Image-to-3D, Multi-view-to-3D
* **Rodin**: 3D Generation
* **Runway**: Text-to-Image, First-Last-Frame to Video, Image to Video (Gen3a Turbo, Gen4 Turbo)
* **Stability AI**: Stable Image Ultra, Stable Diffusion 3.5 Large, Stable Diffusion 3.5 Medium, Image Upscale
* **Tripo**: v1-4, v2.0, v2.5
* **Vidu**: Image-to-Video, Reference Video, Start-End to Video, Text-to-Video

## Prerequisites for Using API Nodes

To use API Nodes, the following requirements must be met:

### 1. ComfyUI Version Requirements

Please update your ComfyUI to the latest version, as we may add more API support in the future, and corresponding nodes will be updated, so please keep your ComfyUI up to date.

<Tip>
  Please note the distinction between nightly and release versions. We recommend using the `nightly` version (which is the latest code commit), as the release version may not be updated in a timely manner.
  This refers to the development version and the stable version, and since we are still rapidly iterating, this document may not be updated promptly, so please pay attention to the version differences.
</Tip>

### 2. Account and Credits Requirements

You need to be logged into your ComfyUI with a [Comfy account](/interface/user) and have a credit balance of [credits](/interface/credits) greater than 0.

Log in via `Settings` -> `User`:

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=066170b38e0b9ead026029685e00fa65" alt="ComfyUI User Interface" data-og-width="3358" width="3358" data-og-height="1828" height="1828" data-path="images/interface/setting/user.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c7f1a017e9b00c6224a440f83d121a59 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=92b830f85f4393d802f7f33bdce81634 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e294573cc054158fb3a108d10bc67087 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=5160ea18d19dfdde201bbf41dbb1af0b 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=463f4645799b84ea5dcd4879ed3b87ca 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e52e827f35eddf444e91e5ed4f11b331 2500w" />

Go to `Settings` -> `Credits` to purchase credits
<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/purchase-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=a324b33ce2d6dce5bf2d0e895ac0d1eb" alt="Credits Interface" data-og-width="3358" width="3358" data-og-height="1828" height="1828" data-path="images/interface/setting/purchase-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/purchase-1.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3be3740eb5ebef1f96177e261d356394 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/purchase-1.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=639eca3dce7544af869871fbc50187a8 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/purchase-1.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e36ad4124f9eaeeb5ac3c83481c55eef 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/purchase-1.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=05042870ef1f4b2270c6053b3903018e 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/purchase-1.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=06ae7e8245f405be7e80c80808a50dbe 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/purchase-1.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=3544af87748d5ef4b2a4966d08a2bcdd 2500w" />

Please refer to the corresponding documentation for account and credits to ensure this requirement:

* [Comfy account](/interface/user): Find the `User` section in the settings menu to log in.
* [Credits](/interface/credits): After logging in, the settings interface will show a credits menu where you can purchase credits. We use a prepaid system, so there will be no unexpected charges.

### 3. Network Environment Requirements

API access requires that your current requests are based on a secure network environment. The current requirements for API access are as follows:

* The local network only allows access from `127.0.0.1` or `localhost`, and you can directly use the login function.
* If you are accessing from a local area network or a website that is not on the whitelist, please log in with an API Key. Please refer to [Log in with an API Key](/interface/user#logging-in-with-an-api-key).
* You should be able to access our API service normally (in some regions, you may need to use a proxy service).
* Access should be carried out in an `https` environment to ensure the security of the requests.

<Note>
  Accessing in an insecure context poses significant risks, which may result in the following consequences:

  1. Authentication may be stolen, leading to the leakage of your account information.
  2. Your account may be maliciously used, resulting in financial losses.

  Even if we open this restriction in the future, we strongly advise against accessing API services through insecure network requests due to the high risks involved.
</Note>

### 4. Using the Corresponding Nodes

**Add to Workflow**: Add the API node to your workflow just like you would with other nodes.
**Run**: Set the parameters and then run the workflow.

<img src="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=91c9219b9648e55c19a95359060eeb56" alt="API Nodes" data-og-width="784" width="784" data-og-height="773" height="773" data-path="images/tutorial/api_nodes/sidebar.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=280&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7179545b60c6a046bd0d309914a0000f 280w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=560&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f92ab198e88fa7e15fd03ec421214ac9 560w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=840&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b3384e5b0bd6a825865c30d169abcea0 840w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=1100&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=c41b83cf96aea58cef7d0191e35ec278 1100w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=1650&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f3f4d2d7183c91491b8ba7672906950f 1650w, https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/sidebar.jpg?w=2500&fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=4485b5b141edfc6f27a421e9d91f6eeb 2500w" />

## Log in with ComfyUI Account API Key on non-whitelisted websites

Currently, we have set up a whitelist to restrict the websites where you can log in to your ComfyUI account.
If you need to log in to your ComfyUI account on some non-whitelisted websites, please refer to the account management section to learn how to log in using an API Key.
In this case, the corresponding website does not need to be on our whitelist.

<Card title="Account Management" icon="book" href="/interface/user#logging-in-with-an-api-key">
  Learn how to log in with ComfyUI Account API Key
</Card>

<img src="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdb8d99a4bd52a6cc1de1b3453e8cfda" alt="Select Comfy API Key Login" data-og-width="3450" width="3450" data-og-height="1914" height="1914" data-path="images/interface/setting/user/user-login-api-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=280&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=84683bcf8e9b1f53885f54175cd83b87 280w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=560&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ae30f89ae6d9a7b97e41f69d3ae0e9f6 560w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=840&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=4dce9815e1729742abd819ce400429ad 840w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=1100&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=148e2ee529690c7985999f64841f8fcd 1100w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=1650&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=dca8a17b4e613ba65ee0d1dca67f4b28 1650w, https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?w=2500&fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=0d1ab01184bd504d62531abfb88abb57 2500w" />

## Use ComfyUI Account API Key Integration to call paid model Partner nodes

Currently, we support accessing our services through ComfyUI API Key Integration to call paid model Partner nodes. Please refer to the API Key Integration section to learn how to use API Key Integration to call paid model Partner nodes.

<Note>
  **Important:** The API key discussed here is your **ComfyUI Account API Key** (used for accessing paid Partner nodes in workflows). This is **NOT** the same as the **Registry Publishing API Key** used by developers to publish custom nodes to the registry. If you're looking to publish custom nodes, see [Publishing Nodes](/registry/publishing).
</Note>

<Card title="API Key Integration" icon="link" href="/development/comfyui-server/api-key-integration">
  Please refer to the API Key Integration section to learn how to use API Key Integration to call paid model Partner nodes
</Card>

## Advantages of Partner Nodes

Partner Nodes provide several important advantages for ComfyUI users:

* **Access to closed-source models**: Use state-of-the-art AI models without having to deploy them yourself
* **Seamless integration**: Partner nodes are fully compatible with other ComfyUI nodes and can be combined to create complex workflows
* **Simplified experience**: No need to manage API keys or handle complex API requests
* **Controlled costs**: The prepaid system ensures you have complete control over your spending with no unexpected charges

## Pricing

<Card title="Partner Node Pricing" icon="coin" href="/tutorials/partner-nodes/pricing">
  Please refer to the pricing page for the corresponding Partner pricing
</Card>

## About Open Source and Opt-in

It's important to note that **Partner Nodes are completely optional**. ComfyUI will always remain fully open-source and free for local users. Partner nodes are designed as an "opt-in" feature, providing convenience for those who want access to external SOTA (state-of-the-art) models.

## How to disable partner nodes completely

You can add the `--disable-api-nodes` launch argument to disable all partner nodes in ComfyUI. This argument will also prevent the frontend from communicating with the internet.

**For manual install:**

```bash  theme={null}
python main.py --disable-api-nodes
```

**For portable users (Windows):**

Update your `run_xxx.bat` file:

```batch  theme={null}
.\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build --disable-api-nodes
pause
```

## Use Cases

A powerful application of Partner Nodes is combining the output of external models with local nodes. For example:

* Using GPT-Image-1 to generate a base image, then transforming it into video with a local `wan` node
* Combining externally generated images with local upscaling or style transfer nodes
* Creating hybrid workflows that leverage the advantages of both closed-source and open-source models

This flexibility makes ComfyUI a truly universal generative AI interface, integrating various AI capabilities into a unified workflow, opening up more possibilities

## FAQs

<AccordionGroup>
  <Accordion title="Why can't I find the API nodes?">
    Please update your ComfyUI to the latest version (the latest commit or the latest [desktop version](https://www.comfy.org/download)).
    We may add more API support in the future, and the corresponding nodes will be updated, so please keep your ComfyUI up to date.

    <Tip>
      Please note that you need to distinguish between the nightly version and the release version.
      In some cases, the latest `release` version may not be updated in time compared to the `nightly` version.
      Since we are still iterating quickly, please ensure you are using the latest version when you cannot find the corresponding node.
    </Tip>
  </Accordion>

  <Accordion title="Why can't I use / log in to the API Nodes?">
    API access requires that your current request is based on a secure network environment. The current requirements for API access are as follows:

    * The local network only allows access from `127.0.0.1` or `localhost`, which may mean that you cannot use the API Nodes in a ComfyUI service started with the `--listen` parameter in a LAN environment.
    * Able to access our API service normally (a proxy service may be required in some regions).
    * Your account does not have enough [credits](/interface/credits).
  </Accordion>

  <Accordion title="Why can't I use API node even after logging in, or why does it keep asking me to log in while using?">
    * Currently, only `127.0.0.1` or `localhost` access is supported.
    * Ensure your account has enough credits.
  </Accordion>

  <Accordion title="Can API Nodes be used for free?">
    API Nodes require credits for API calls to closed-source models, so they do not support free usage.
  </Accordion>

  <Accordion title="How to purchase credits?">
    Please refer to the following documentation:

    1. [Comfy Account](/interface/user): Find the `User` section in the settings menu to log in.
    2. [Credits](/interface/credits): After logging in, the settings interface will show the credits menu. You can purchase credits in `Settings` → `Credits`. We use a prepaid system, so there will be no unexpected charges.
    3. Complete the payment through Stripe.
    4. Check if the credits have been updated. If not, try restarting or refreshing the page.
  </Accordion>

  <Accordion title="Are unused credits refundable?">
    Currently, we do not support refunds for credits.
    If you believe there is an error resulting in unused balance due to technical issues, please [contact support](mailto:support@comfy.org).
  </Accordion>

  <Accordion title="Can credits go negative?">
    Credits are not intended to be used as a negative balance or credit line. However, due to race conditions where partner nodes don't always report costs before execution, a single execution may consume more credits than your remaining balance and temporarily result in a negative balance after completion. When your balance is negative, you will not be able to run Partner Nodes until you top up and restore a positive balance. Please ensure you have enough credits before making API calls.
  </Accordion>

  <Accordion title="Where can I check usage and expenses?">
    Please visit the [Credits](/interface/credits) menu after logging in to check the corresponding credits.
  </Accordion>

  <Accordion title="Is it possible to use my own API Key?">
    Currently, the API Nodes are still in the testing phase and do not support this feature yet, but we have considered adding it.
  </Accordion>

  <Accordion title="Do credits expire?">
    No, your credits do not expire.
  </Accordion>

  <Accordion title="Can credits be transferred or shared?">
    No, your credits cannot be transferred to other users and are limited to the currently logged-in account, but we do not restrict the number of devices that can log in.
  </Accordion>

  <Accordion title="Can I use the same account on different devices?">
    We do not limit the number of devices that can log in; you can use your account anywhere you want.
  </Accordion>

  <Accordion title="How can I request for my account or information to be deleted??">
    Email a request to [support@comfy.org](mailto:support@comfy.org) and we will delete your information
  </Accordion>
</AccordionGroup>
