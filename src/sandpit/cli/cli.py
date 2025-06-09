import sys
from typing import Optional

import typer
from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

from sandpit.cli import dummy
from sandpit.version import get_version

# Remove no_args_is_help and add invoke_without_command to allow a version option without subcommand.
app = typer.Typer(
    help="Sandpit API Command Line Interface", invoke_without_command=True
)

# Register sub-commands
app.add_typer(dummy.app, name="admin", help="Dummy commands")

console = Console(
    theme=Theme(
        {
            "info": "cyan",
            "warning": "yellow",
            "error": "red bold",
            "success": "green bold",
            "command": "magenta bold",
            "subcommand": "cyan",
            "description": "white",
            "heading": "yellow bold",
        }
    )
)


def create_command_panel(command_name: str, commands: dict) -> Panel:
    """Create a panel for a command group"""
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Command", style="subcommand")
    table.add_column("Description", style="description")

    for cmd, desc in commands.items():
        table.add_row(cmd, desc)

    return Panel(
        table,
        title=f"[heading]{command_name} Commands",
        border_style="blue",
        box=box.ROUNDED,
    )


def show_welcome():
    """Display welcome message and version information"""
    version = get_version()

    welcome_panel = Panel(
        Text("Welcome to the NSLS-II API Command Line Interface", style="info"),
        subtitle=f"Version: {version}",
        border_style="cyan",
        box=box.DOUBLE,
    )
    console.print(welcome_panel)


def show_available_commands():
    """Display available commands in an organized layout"""
    command_groups = {
        "Dummy": {
            "dummy status": "Show current dummy status",
        },
    }

    panels = []
    for group, commands in command_groups.items():
        panels.append(create_command_panel(group, commands))

    console.print(Columns(panels, equal=True, expand=True))


def show_usage_tips():
    """Display usage tips"""
    tips_panel = Panel(
        "[info]Tips:\n"
        "• Use [command]-h[/command] or [command]--help[/command] with any command to see detailed usage\n"
        "• Set environment with [command]env switch[/command] before using other commands\n"
        "• Always [command]auth login[/command] before accessing protected resources",
        title="Usage Tips",
        border_style="green",
        box=box.ROUNDED,
    )
    console.print(tips_panel)


@app.callback()
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        is_eager=True,
    ),
):
    """
    NSLS-II API Command Line Interface
    """
    if version:
        version = get_version()
        console.print(f"[info]Sandpit API CLI version: {version}")
        raise typer.Exit()

    # Only show a welcome message and commands if no subcommand is specified
    if ctx.invoked_subcommand is None:
        show_welcome()
        console.print()
        show_available_commands()
        console.print()
        show_usage_tips()


def run():
    try:
        app()
    except Exception as e:
        console.print(f"[error]Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    run()
