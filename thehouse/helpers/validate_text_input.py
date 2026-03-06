"""validate_text_input.

This function will validate text input.
"""
import sys
import questionary
from pyfiglet import Figlet
from rich.text import Text
from rich.console import Console
from rich.panel import Panel

console = Console()

def validate_text_input(prompt):
    """Validate the text input from the user using questionary."""
    try:
        answer = questionary.text(prompt).ask()

        if answer is None:
            f = Figlet(font="catwalk")
            goodbye_text = f.renderText("BYE")
            console.print(Text(goodbye_text, style="bold yellow"))
            sys.exit(0)

        return answer
    except (EOFError, PermissionError):
        console.print(Panel(
            "[bold red]Error: Interactive terminal required.[/bold red]\n\n"
            "This game requires an interactive terminal to run.\n"
            "If you are using Docker, please run it with the [bold]-it[/bold] flags:\n\n"
            "  [bold cyan]docker run -it dcdavidev/thehouse[/bold cyan]",
            title="System Error",
            border_style="red"
        ))
        sys.exit(1)
    except KeyboardInterrupt:
        f = Figlet(font="catwalk")
        goodbye_text = f.renderText("BYE")
        console.print(Text(f"\n{goodbye_text}", style="bold yellow"))
        sys.exit(0)
