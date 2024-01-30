from uuid import uuid4

from typer.testing import CliRunner

from examples.my_app.main_app import app

runner = CliRunner()


def test_root_app():
    result = runner.invoke(app=app, args=["--help"])
    assert result.exit_code == 0
    assert "Options" in result.stdout
    assert "Commands" in result.stdout

def test_root_app_registered_plugins():
    assert app.registered_groups
    assert [group.name for group in app.registered_groups] == ["plugin-a", "plugin-b"]
    
def test_root_app_plugins_have_commands():
    for group in app.registered_groups:
        assert group.typer_instance.registered_commands

def test_root_app_plugin_a():
    uid = uuid4()
    result = runner.invoke(app=app, args=["plugin-a", "root-command-a", str(uid)])
    assert result.exit_code == 0
    assert str(uid) in result.stdout

def test_root_app_plugin_a_sub_command():
    result = runner.invoke(app=app, args=["plugin-a", "some-commands", "some-command"])
    assert result.exit_code == 0
    assert "Here is a sub-command under plugin-a" in result.stdout

def test_root_app_plugin_b_sub_command_no_command():
    result = runner.invoke(app=app, args=["plugin-a", "some-commands", "some-command", "bad-command"])
    assert result.exit_code == 2
    assert "No such command 'bad-command'" in result.stdout

def test_root_app_plugin_a_syntax_error():
    result = runner.invoke(app=app, args=["plugin-a", "some-other-commands", "and-another-command"])
    assert result.exit_code == 1
    t, exc, _ = result.exc_info

    assert t == NameError
    assert exc.args[0] == "name 'bad' is not defined"

def test_root_app_plugin_b():
    uid = uuid4()
    result = runner.invoke(app=app, args=["plugin-b", "root-command-a", str(uid)])
    assert result.exit_code == 0
    assert str(uid) in result.stdout

def test_root_app_plugin_b_sub_command_no_command():
    result = runner.invoke(app=app, args=["plugin-b", "some-commands", "some-command"])
    assert result.exit_code == 2
    assert "No such command 'some-commands'" in result.stdout