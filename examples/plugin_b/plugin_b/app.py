import typer

app = typer.Typer()


@app.command()
def root_command_a(data: str):
    print(f"This is root-command-a for plugin-b: {data}")


@app.command()
def root_command_b(data: str):
    print(f"This is root-command-b for plugin-b: {data}")
