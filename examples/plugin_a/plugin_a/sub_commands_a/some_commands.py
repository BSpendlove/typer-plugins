import typer

app = typer.Typer()


@app.command()
def some_command():
    """This command probably does something for plugin-a."""
    print("Here is a sub-command under plugin-a")


@app.command()
def some_other_command():
    """This command is another command for plugin-a"""
    print("Here is another sub-command under plugin-a")
