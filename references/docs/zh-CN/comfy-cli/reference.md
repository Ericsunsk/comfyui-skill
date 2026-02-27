> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# 参考

# CLI

## 节点

**用法**:

```console  theme={null}
$ comfy node [OPTIONS] COMMAND [ARGS]...
```

**选项**:

* `--install-completion`: 为当前 shell 安装自动补全功能。
* `--show-completion`: 显示当前 shell 的自动补全功能，可用于复制或自定义安装。
* `--help`: 显示此消息并退出。

**命令**:

* `deps-in-workflow`
* `disable`
* `enable`
* `fix`
* `install`
* `install-deps`
* `reinstall`
* `restore-dependencies`
* `restore-snapshot`
* `save-snapshot`: 保存当前 ComfyUI 环境的快照...
* `show`
* `simple-show`
* `uninstall`
* `update`

### `deps-in-workflow`

**用法**:

```console  theme={null}
$ deps-in-workflow [OPTIONS]
```

**选项**:

* `--workflow TEXT`: 工作流文件 (.json/.png)  \[必需]
* `--output TEXT`: 输出文件 (.json/.png)  \[必需]
* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `disable`

**用法**:

```console  theme={null}
$ disable [OPTIONS] ARGS...
```

**参数**:

* `ARGS...`: 禁用自定义节点  \[必需]

**选项**:

* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `enable`

**用法**:

```console  theme={null}
$ enable [OPTIONS] ARGS...
```

**参数**:

* `ARGS...`: 启用自定义节点  \[必需]

**选项**:

* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `fix`

**用法**:

```console  theme={null}
$ fix [OPTIONS] ARGS...
```

**参数**:

* `ARGS...`: 修复指定自定义节点的依赖项  \[必需]

**选项**:

* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `install`

**用法**:

```console  theme={null}
$ install [OPTIONS] ARGS...
```

**参数**:

* `ARGS...`: 安装自定义节点  \[必需]

**选项**:

* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `install-deps`

**用法**:

```console  theme={null}
$ install-deps [OPTIONS]
```

**选项**:

* `--deps TEXT`: 依赖项规范文件 (.json)
* `--workflow TEXT`: 工作流文件 (.json/.png)
* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `reinstall`

**用法**:

```console  theme={null}
$ reinstall [OPTIONS] ARGS...
```

**参数**:

* `ARGS...`: 重新安装自定义节点  \[必需]

**选项**:

* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `restore-dependencies`

**用法**:

```console  theme={null}
$ restore-dependencies [OPTIONS]
```

**选项**:

* `--help`: 显示此消息并退出。

### `restore-snapshot`

**用法**:

```console  theme={null}
$ restore-snapshot [OPTIONS] PATH
```

**参数**:

* `PATH`: \[必需]

**选项**:

* `--help`: 显示此消息并退出。

### `save-snapshot`

保存当前 ComfyUI 环境的快照。

**用法**:

```console  theme={null}
$ save-snapshot [OPTIONS]
```

**选项**:

* `--output TEXT`: 指定输出文件路径 (.json/.yaml)。
* `--help`: 显示此消息并退出。

### `show`

**用法**:

```console  theme={null}
$ show [OPTIONS] ARGS...
```

**参数**:

* `ARGS...`: \[installed|enabled|not-installed|disabled|all|snapshot|snapshot-list]  \[必需]

**选项**:

* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `simple-show`

**用法**:

```console  theme={null}
$ simple-show [OPTIONS] ARGS...
```

**参数**:

* `ARGS...`: \[installed|enabled|not-installed|disabled|all|snapshot|snapshot-list]  \[必需]

**选项**:

* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `uninstall`

**用法**:

```console  theme={null}
$ uninstall [OPTIONS] ARGS...
```

**参数**:

* `ARGS...`: 卸载自定义节点  \[必需]

**选项**:

* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

### `update`

**用法**:

```console  theme={null}
$ update [OPTIONS] ARGS...
```

**参数**:

* `ARGS...`: 更新自定义节点  \[必需]

**选项**:

* `--channel TEXT`: 指定操作模式
* `--mode TEXT`: \[remote|local|cache]
* `--help`: 显示此消息并退出。

## 模型

**用法**:

```console  theme={null}
$ comfy model [OPTIONS] COMMAND [ARGS]...
```

**选项**:

* `--install-completion`: 为当前 shell 安装自动补全功能。
* `--show-completion`: 显示当前 shell 的自动补全功能，可用于复制或自定义安装。
* `--help`: 显示此消息并退出。

**命令**:

* `download`: 下载模型到指定的相对路径...
* `list`: 显示当前所有已下载模型的列表...
* `remove`: 删除一个或多个已下载的模型，...

### `download`

如果模型尚未下载，则将其下载到指定的相对路径。

**用法**:

```console  theme={null}
$ download [OPTIONS]
```

**选项**:

* `--url TEXT`: 模型下载的 URL  \[必需]
* `--relative-path TEXT`: 从当前工作区到安装模型的相对路径。  \[默认值: models/checkpoints]
* `--help`: 显示此消息并退出。

### `list`

以表格格式显示当前已下载的所有模型列表。

**用法**:

```console  theme={null}
$ list [OPTIONS]
```

**选项**:

* `--relative-path TEXT`: 从当前工作区到存储模型的相对路径。  \[默认值: models/checkpoints]
* `--help`: 显示此消息并退出。

### `remove`

通过直接指定或交互式选择，删除一个或多个已下载的模型。

**用法**:

```console  theme={null}
$ remove [OPTIONS]
```

**选项**:

* `--relative-path TEXT`: 从当前工作区到存储模型的相对路径。  \[默认值: models/checkpoints]
* `--model-names TEXT`: 要删除的模型文件名列表，用空格分隔。
* `--help`: 显示此消息并退出。
