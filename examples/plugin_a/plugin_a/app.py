import typer
from plugin_a.sub_commands_a import some_commands
from plugin_a.sub_commands_b import some_more_commands

app = typer.Typer()
app.add_typer(some_commands.app, name="some-commands")
app.add_typer(some_more_commands.app, name="some-other-commands")


@app.command()
def root_command_a(data: str):
    print(f"This is root-command-a for plugin-a: {data}")


@app.command()
def root_command_b(data: str):
    print(f"This is root-command-b for plugin-a: {data}")
