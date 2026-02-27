> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 遮罩编辑器 - 在 ComfyUI 中创建和编辑遮罩

> 讲解 ComfyUI 中遮罩编辑器（Mask Editor）的使用方法，以及对应设置等

遮罩编辑器是 ComfyUI 中一个非常实用的功能，它可以帮助用户在图像中创建和编辑遮罩，而不需要在其它应用程序中进行操作。

遮罩编辑器目前通过 `Load image` 节点来触发，当你上传图像后，可以在节点上右键通过菜单 `Open in MaskEditor` 来打开遮罩编辑器。

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=6c44553609b2b549c343953f385b8cdd" alt="ComfyUI 遮罩编辑器" data-og-width="1082" width="1082" data-og-height="1344" height="1344" data-path="images/interface/maskeditor/maskeditor.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=b7a2ade26914299fde3f421992fa025e 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=072c660a1bbe4281601134eea338b020 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=ef3be676f03b0cf1d61aa34db0dbad82 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=bb36cbf201a785197c0e74dd7b1b6376 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=32af9df2f2b4bdc5a6f5ed7395a3e789 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=d15a19e80d97f1b3be68ce9fb5e29752 2500w" />

<img src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor_ui.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=1327b9215d2c5772abebcdfd3e9840aa" alt="ComfyUI 遮罩编辑器" data-og-width="1500" width="1500" data-og-height="1099" height="1099" data-path="images/interface/maskeditor/maskeditor_ui.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor_ui.jpg?w=280&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=961bf01136c869ca408f8022b9aa9aa4 280w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor_ui.jpg?w=560&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=35969fb3d0d3e904efebb89d836b606b 560w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor_ui.jpg?w=840&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4fbe1c6649a551caf87f046093c78ca0 840w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor_ui.jpg?w=1100&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=353eb8b8cd54cfe6a2fb6863995b2123 1100w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor_ui.jpg?w=1650&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=86bec6fe11b95d0a6b3771b496487135 1650w, https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor_ui.jpg?w=2500&fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=3ff864180319d3a3f2d9896b88676353 2500w" />

然后你就可以通过鼠标在图像上点击来创建和编辑遮罩了。

## 演示视频

<video controls>
  <source src="https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/maskeditor/maskeditor.mp4?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=f2f905b202074a6f51d1021e799d894d" type="video/mp4" data-path="images/interface/maskeditor/maskeditor.mp4" />

  你的浏览器不支持 video 标签。
</video>
