import typer

app = typer.Typer()


@app.command()
def another_command():
    """This command does something."""
    print("Here is a sub-command under plugin-b")


@app.command()
def and_another_command():
    """This command also does something, however notice here there is a syntax error.
    
    The plugin will still work (and other plugins), that is quite neat... :-)

    $ python /main_app.py plugin-a some-other-commands and-another-command
    Traceback (most recent call last):

    File "/home/brandon/typer-testing/typer-plugins/examples/my_app/main_app.py", line 8, in <module>
        app()

    File "/home/brandon/typer-testing/typer-plugins/examples/plugin_a/plugin_a/sub_commands_b/some_more_commands.py", line 18, in and_another_command
        bad-syntax-error-here

    NameError: name 'bad' is not defined
    """
    bad-syntax-error-here
    print("Here is another sub-command under plugin-b")
