> ## Documentation Index
> Fetch the complete documentation index at: https://docs.comfy.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Reference

# CLI

## Nodes

**Usage**:

```console  theme={null}
$ comfy node [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `deps-in-workflow`
* `disable`
* `enable`
* `fix`
* `install`
* `install-deps`
* `reinstall`
* `restore-dependencies`
* `restore-snapshot`
* `save-snapshot`: Save a snapshot of the current ComfyUI...
* `show`
* `simple-show`
* `uninstall`
* `update`

### `deps-in-workflow`

**Usage**:

```console  theme={null}
$ deps-in-workflow [OPTIONS]
```

**Options**:

* `--workflow TEXT`: Workflow file (.json/.png)  \[required]
* `--output TEXT`: Workflow file (.json/.png)  \[required]
* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `disable`

**Usage**:

```console  theme={null}
$ disable [OPTIONS] ARGS...
```

**Arguments**:

* `ARGS...`: disable custom nodes  \[required]

**Options**:

* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `enable`

**Usage**:

```console  theme={null}
$ enable [OPTIONS] ARGS...
```

**Arguments**:

* `ARGS...`: enable custom nodes  \[required]

**Options**:

* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `fix`

**Usage**:

```console  theme={null}
$ fix [OPTIONS] ARGS...
```

**Arguments**:

* `ARGS...`: fix dependencies for specified custom nodes  \[required]

**Options**:

* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `install`

**Usage**:

```console  theme={null}
$ install [OPTIONS] ARGS...
```

**Arguments**:

* `ARGS...`: install custom nodes  \[required]

**Options**:

* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `install-deps`

**Usage**:

```console  theme={null}
$ install-deps [OPTIONS]
```

**Options**:

* `--deps TEXT`: Dependency spec file (.json)
* `--workflow TEXT`: Workflow file (.json/.png)
* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `reinstall`

**Usage**:

```console  theme={null}
$ reinstall [OPTIONS] ARGS...
```

**Arguments**:

* `ARGS...`: reinstall custom nodes  \[required]

**Options**:

* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `restore-dependencies`

**Usage**:

```console  theme={null}
$ restore-dependencies [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `restore-snapshot`

**Usage**:

```console  theme={null}
$ restore-snapshot [OPTIONS] PATH
```

**Arguments**:

* `PATH`: \[required]

**Options**:

* `--help`: Show this message and exit.

### `save-snapshot`

Save a snapshot of the current ComfyUI environment

**Usage**:

```console  theme={null}
$ save-snapshot [OPTIONS]
```

**Options**:

* `--output TEXT`: Specify the output file path. (.json/.yaml)
* `--help`: Show this message and exit.

### `show`

**Usage**:

```console  theme={null}
$ show [OPTIONS] ARGS...
```

**Arguments**:

* `ARGS...`: \[installed|enabled|not-installed|disabled|all|snapshot|snapshot-list]  \[required]

**Options**:

* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `simple-show`

**Usage**:

```console  theme={null}
$ simple-show [OPTIONS] ARGS...
```

**Arguments**:

* `ARGS...`: \[installed|enabled|not-installed|disabled|all|snapshot|snapshot-list]  \[required]

**Options**:

* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `uninstall`

**Usage**:

```console  theme={null}
$ uninstall [OPTIONS] ARGS...
```

**Arguments**:

* `ARGS...`: uninstall custom nodes  \[required]

**Options**:

* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

### `update`

**Usage**:

```console  theme={null}
$ update [OPTIONS] ARGS...
```

**Arguments**:

* `ARGS...`: update custom nodes  \[required]

**Options**:

* `--channel TEXT`: Specify the operation mode
* `--mode TEXT`: \[remote|local|cache]
* `--help`: Show this message and exit.

## Models

**Usage**:

```console  theme={null}
$ comfy model [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `download`: Download a model to a specified relative...
* `list`: Display a list of all models currently...
* `remove`: Remove one or more downloaded models,...

### `download`

Download a model to a specified relative path if it is not already downloaded.

**Usage**:

```console  theme={null}
$ download [OPTIONS]
```

**Options**:

* `--url TEXT`: The URL from which to download the model  \[required]
* `--relative-path TEXT`: The relative path from the current workspace to install the model.  \[default: models/checkpoints]
* `--help`: Show this message and exit.

### `list`

Display a list of all models currently downloaded in a table format.

**Usage**:

```console  theme={null}
$ list [OPTIONS]
```

**Options**:

* `--relative-path TEXT`: The relative path from the current workspace where the models are stored.  \[default: models/checkpoints]
* `--help`: Show this message and exit.

### `remove`

Remove one or more downloaded models, either by specifying them directly or through an interactive selection.

**Usage**:

```console  theme={null}
$ remove [OPTIONS]
```

**Options**:

* `--relative-path TEXT`: The relative path from the current workspace where the models are stored.  \[default: models/checkpoints]
* `--model-names TEXT`: List of model filenames to delete, separated by spaces
* `--help`: Show this message and exit.
