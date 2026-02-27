> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Properties

## Nodes are containers for properties

Nodes usually have ***properties***. Also known as ***parameters*** or ***attributes***, node properties are variables that can be changed. Some properties can be adjusted manually by the user, using a data entry field called a ***widget***. Other properties can be driven automatically by other nodes connected to the property ***input slot*** or port. Usually, a property can be converted from widget to input and vice versa, allowing users to control property values manually or automatically.

Properties can take many forms and hold many different types of information. For example, a **Load Checkpoint** node has a single property:  the file path to the generative model checkpoint file. A **KSampler** node has multiple properties such as the number of sampling **steps**, **CFG** scale, **sampler\_name**, etc.

<img src="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2121d646aef4f1386f1f09162312785b" alt="node properties" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/concepts/core-concepts_properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=280&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2cefc8007c7898e676ff75bf00c6ba92 280w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=560&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=14dfbe18d40d717bdd05b708f9a8510a 560w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=840&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=a1c89860f0b232aea917a1ce47b61d2f 840w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=1100&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=f1ba7ae145baeba3b8bed3b62ba6afa0 1100w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=1650&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=bf77af55bac39bb412df4cac93054fd9 1650w, https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?w=2500&fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ed41455e1d24854be6db7dcec66f09d2 2500w" />

## Data types

Information can come in many different forms, called ***data types***. For example, alphanumeric text is known as a ***string***, a whole number is an ***integer***, and a number with a decimal point is known as a ***floating point*** number or ***float***. New data types are always being added to ComfyUI.

ComfyUI is written in the Python scripting language, which is very forgiving about data types. By contrast, the ComfyUI environment is very ***strongly typed***. This means that different data types can’t be mixed up. For example, we can’t connect an image output to an integer input. This is a huge benefit to users, guiding them to proper workflow construction and preventing program errors.
