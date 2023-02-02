import os

import typer
import toml
from rich.console import Console


app = typer.Typer(help="shefcraft - Package Management for Cairo")
_console = Console()


@app.command()
def deploy():

    pass

if __name__ == "__main__":
    app()
