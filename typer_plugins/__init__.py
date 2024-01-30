"""Register Typer CLI applications to a main application to make it more pluggable.

This small python module allows us to register Typer CLI applications by utilizing 
entry points.

https://packaging.python.org/en/latest/specifications/entry-points/

When using setuptools, you need to define the entry points like this:

```
from setuptools import setup

setup(
    name='plugin_a',
    install_requires=[
        'typer',
    ],
    entry_points='''
        [exampleapp.plugins]
        plugin-a=plugin_a.app:app
    ''',
)
```

If you are using Poetry, then you can simply create a plugin which will automatically register
the command with the entrypoint, add this into your pyproject.toml:

```
[tool.poetry.plugins."exampleapp.plugins"]
"plugin-a" = "plugin_a.app:app"
```

You must ensure plugins are defined as a string, so "exampleapp.plugins" with the speechmarks is correct.

For examples, take a look at the examples/ folder in the GitHub repository.
"""
import logging
from pkg_resources import iter_entry_points

import typer

from typer_plugins.errors import TyperCLIAlreadyRegistered


def register_plugins(app: typer.Typer, entrypoint: str) -> None:
    """Attempts to register plugins to a Typer CLI App.

    Args:
        app:            typer.Typer object.
        entrypoint:     Entrypoint path to discover plugins.
    """
    logging.debug("Attempting to load all Typer CLI plugins...")
    if not isinstance(app, typer.Typer):
        raise TypeError("You have not provided a Typer application.")

    registered_plugins = []

    plugins = iter_entry_points(group=entrypoint)
    for plugin in plugins:
        # Check if plugin is already registered with the same name, the name
        # is the initial entrypoint from the root Typer app so it must be unique.
        if plugin.name in registered_plugins:
            logging.error(f"Typer CLI Plugin '{plugin.name}' already exist.")
            raise TyperCLIAlreadyRegistered(plugin.name)

        try:
            resolved_plugin = plugin.load()
        except ModuleNotFoundError as err:
            resolved_plugin = typer.Typer(help=f"Failed to load plugin - {err.msg}")

        app.add_typer(resolved_plugin, name=plugin.name)
        registered_plugins.append(plugin.name)
        logging.info(f"Successfully loaded Typer CLI plugin '{plugin.name}'.")
