> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 属性

## 节点是属性的容器

节点通常具有 ***属性***。也称为 ***参数*** 或 ***特性***，节点属性是可以更改的变量。一些属性可以通过用户手动调整，使用称为 ***小部件*** 的数据输入字段。其他属性可以通过连接到属性 ***输入插槽*** 或端口的其他节点自动驱动。通常，属性可以在小部件和输入之间转换，从而允许用户手动或自动控制属性值。

属性可以采取多种形式，并包含多种不同类型的信息。例如，**加载检查点** 节点具有一个属性：生成模型检查点文件的文件路径。**KSampler** 节点具有多个属性，例如采样 **步骤**、**CFG** 比例、**采样器名称** 等等。

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2121d646aef4f1386f1f09162312785b" alt="节点属性" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/concepts/core-concepts_properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2cefc8007c7898e676ff75bf00c6ba92 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=14dfbe18d40d717bdd05b708f9a8510a 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a1c89860f0b232aea917a1ce47b61d2f 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f1ba7ae145baeba3b8bed3b62ba6afa0 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=bf77af55bac39bb412df4cac93054fd9 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ed41455e1d24854be6db7dcec66f09d2 2500w" />

## 数据类型

信息可以以多种不同形式出现，称为 ***数据类型***。例如，字母数字文本称为 ***字符串***，整数称为 ***整数***，带小数点的数字称为 ***浮点数*** 或 ***浮点***。新的数据类型总是被添加到 ComfyUI 中。

ComfyUI 是用 Python 脚本语言编写的，该语言对数据类型非常宽容。相比之下，ComfyUI 环境是非常 ***强类型*** 的。这意味着不同的数据类型不能混合。例如，我们不能将图像输出连接到整数输入。这对用户来说是一个巨大的好处，指导他们正确构建工作流程并防止程序错误。
