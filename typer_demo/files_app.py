#!/usr/bin/env python3
"""
Copyright
DESCRIPTION:
    this is a the files sub applicaiton
USAGE EXAMPLE:
    files_app move --help

"""
import logging

import typer


# from typing import Optional


log = logging.getLogger(__name__)

app = typer.Typer(add_completion=True)
app = typer.Typer(help=__doc__)


@app.command(name="move", help="Move files")
def move_files(src_path: str, dest_path: str):
    # shutil.move(src_path, dest_path)
    typer.echo(f"Moved files from '{src_path}' to '{dest_path}'")


@app.command(name="delete", help="Delete files")
def delete_files(file_path: str):
    # shutil.rmtree(file_path)
    typer.echo(f"Deleted files at '{file_path}'")


@app.command()
def main():
    print("Inside Files App")
    app()


if __name__ == "__main__":
    main()
