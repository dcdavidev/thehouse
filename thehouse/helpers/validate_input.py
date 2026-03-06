"""validate_input.

This function will validate input.
"""
import sys
import questionary
from pyfiglet import Figlet
from rich.text import Text
from rich.console import Console
from rich.panel import Panel
from .ui import get_appbar

console = Console()

def validate_input(prompt, options):
    """Validate the input from the user using questionary."""
    try:
        # Show appbar before the prompt
        console.print(get_appbar())

        choices = []
        for opt in options:
            choices.append(opt.capitalize() if isinstance(opt, str) else str(opt))

        if "quit" not in options:
            choices.append("Quit")

        answer = questionary.select(
            prompt,
            choices=choices,
            style=questionary.Style([
                ('qmark', 'fg:#673ab7 bold'),
                ('question', 'bold'),
                ('answer', 'fg:#f44336 bold'),
                ('pointer', 'fg:#673ab7 bold'),
                ('highlighted', 'fg:#673ab7 bold'),
                ('selected', 'fg:#cc2722'),
                ('separator', 'fg:#cc5454'),
                ('instruction', ''),
                ('text', ''),
                ('disabled', 'fg:#858585 italic')
            ])
        ).ask()

        if answer is None or answer == "Quit":
            f = Figlet(font="catwalk")
            goodbye_text = f.renderText("BYE")
            console.print(Text(goodbye_text, style="bold yellow"))
            sys.exit(0)

        result = answer.lower()
        if result in options:
            return result
        return result

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
