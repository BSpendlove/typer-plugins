# typer-plugins

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![PyPI Version](https://img.shields.io/pypi/v/typer-plugins.svg)](https://pypi.python.org/pypi/typer-plugins)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Python Versions](https://img.shields.io/pypi/pyversions/typer-plugins.svg)](https://pypi.python.org/pypi/typer-plugins)
[![Actions status](https://github.com/BSpendlove/typer-plugins/workflows/ci/badge.svg)](https://github.com/BSpendlove/typer-plugins/actions)

Register Typer CLI applications to a main root application to make it more pluggable.

This is inspired by [click-plugins](https://github.com/click-contrib/click-plugins) so I have created a similar package to register Typer CLI based applications in a similar plugin format. It's slightly different how to use it and I'm still actively working on this project to improve the process of registering, detecting duplicate plugins. Natively running a plugin with broken code will not break the full application, only when someone attempts to execute that specific command.

But now you can manage your Typer CLI applications with plugin based architecture, managing separate sub-command groups in separate Git repositories.


## How to use

1. `pip install typer-plugins`
2. Import the package in your main application that you want to register all your plugins into

```python
import typer
from typer_plugins import register_plugins # Import the register_plugins function

app = typer.Typer(invoke_without_command=True)
register_plugins(app=app, entrypoint="exampleapp.plugins") # Run the function after creating your main `app`. This entrypoint should be used by all your applications.

if __name__ == "__main__":
    app()
```

3. Create your plugin(s) and ensure you either create an entrypoint, [here is an example using pyproject.toml with Poetry](/typer-plugins/examples/plugin_a/pyproject.toml):

```bash
[tool.poetry.plugins."exampleapp.plugins"]
"plugin-a" = "plugin_a.app:app"
```

This format assumes your plugin is called `plugin_a` and there is a python file called `app.py` with the Typer app created assigned to a variable named `app`. You can find a working example in the [examples directory](/typer-plugins/examples/plugin_a/plugin_a/app.py)

4. As long as your entrypoint matches up with the poetry plugin configured in the pyproject.toml file, you can now proceed to `pip install <your-plugin>` whether it be locally or via a package distributer. It will then register from your main application where you use the `register_plugins` function.

```bash
$ python my-app plugin-a --help
Usage: my-app plugin-a [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  root-command-a
  root-command-b
  some-commands
  some-other-commands
```

## Development / Contributing

TO-DO