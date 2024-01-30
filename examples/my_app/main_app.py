import typer
from typer_plugins import register_plugins

app = typer.Typer()
register_plugins(app=app, entrypoint="exampleapp.plugins")

if __name__ == "__main__":
    app()
