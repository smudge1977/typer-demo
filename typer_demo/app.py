#!/usr/bin/env python3
"""
Copyright <<year>> <<insert publisher name>>
DESCRIPTION:
    this is a sample Typer CLI layout
USAGE EXAMPLE:
    > python template_simple_cli.py example_cmd
"""
import logging
from typing import Optional

import typer

import typer_demo


# from .files_app import app

log = logging.getLogger(__name__)

app = typer.Typer(add_completion=True)
app = typer.Typer(help=__doc__)


# Typer app for 'files' sub application
# files_app = typer.Typer(name="files", help="Manage files")

# 'files' as sub-app to the main app
# app.add_typer(files.app, name="files", help="File management commands")


def opener():
    with open("file", "r") as f:
        f.read()


def summer(a: int, b: int) -> int:
    return a + b


@app.command()
def hello(name: Optional[str] = None):
    if name:
        typer.echo(f"Hello {name}")
    else:
        typer.echo("Hello World!")


@app.command()
def bye(name: Optional[str] = None):
    if name:
        typer.echo(f"Bye {name}")
    else:
        typer.echo("Goodbye!")


@app.command()
def version():
    """get the version of the package"""
    # version = pkg_resources.get_distribution(PKG_NAME).version
    typer.echo(typer_demo.__version__)


@app.command()
def create(username: str):
    """
    Create a new user with USERNAME.
    """
    typer.echo(f"Creating user: {username}")


@app.command()
def delete(
    username: str,
    force: bool = typer.Option(
        ...,
        prompt="Are you sure you want to delete the user?",
        help="Force deletion without confirmation.",
    ),
):
    """
    Delete a user with USERNAME.

    If --force is not used, will ask for confirmation.
    """
    if force:
        typer.echo(f"Deleting user: {username}")
    else:
        typer.echo("Operation cancelled")


@app.command()
def delete_all(
    force: bool = typer.Option(
        ...,
        prompt="Are you sure you want to delete ALL users?",
        help="Force deletion without confirmation.",
    )
):
    """
    Delete ALL users in the database.

    If --force is not used, will ask for confirmation.
    """
    if force:
        typer.echo("Deleting all users")
    else:
        typer.echo("Operation cancelled")


@app.command()
def init():
    """
    Initialize the users database.
    """
    typer.echo("Initializing user database")


@app.command()
def greet2(
    name: str = typer.Argument("world", help="The name to greet", show_default=True)
):
    """Example of default values
    The doc string is the best place to document the command!
    More so than the <help> attrib on the Arg which only shows
    in `typer-demo greet2 --help` help for setting"""
    typer.echo(f"Hello, {name}!")


@app.callback()
def before_command_callback():
    """This runs before a command to help with data validation"""
    # Define a callback function to be executed before a command is invoked
    typer.echo("Before command")


@app.command()
def greet3(name: str):
    typer.echo(f"Hello, {name}!")


@app.command()
def backup(database: str, output_dir: str, force: bool = False):
    """Example of switches
    --force / --no-force  [default: no-force]
    """
    if force:
        typer.echo("Forced backup requested!")
    else:
        typer.echo("Regular backup requested.")
    typer.echo(f"Database: {database}")
    typer.echo(f"Output directory: {output_dir}")


# typer.progressbar()
# launch websites automatically — typer.launch("https://google.com")
# prompt users for input — typer.prompt("What is your name?")
# gracefully terminate a program — raise typer.Exit()
def main():
    log.debug("APP Main debug")
    log.info("APP Info - started...")
    app()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    FORMAT = "%(levelname)-8s %(module)-10s:%(lineno)-6s %(message)s"
    logging.basicConfig(format=FORMAT)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    # TODO: if cli -v walk one level of loggers setting to INFO
    # if -vv walk two levels etc.
    # You only get debug if running the module directly.

    log.info("App running...")

    main()
