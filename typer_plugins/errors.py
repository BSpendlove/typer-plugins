"""Errors/Exceptions for typer-plugins."""


class TyperCLIAlreadyRegistered(Exception):
    """Explictly used when a Typer App has already been registered with a specific root command."""

    def __init__(self, name: str) -> None:
        super().__init__(
            f"A TyperCLI application with name '{name}' has already been registered."
        )
