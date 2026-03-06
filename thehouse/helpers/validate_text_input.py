"""validate_text_input.

This function will validate text input.
"""
import questionary
from pyfiglet import Figlet
from rich.text import Text
from rich.console import Console

console = Console()

def validate_text_input(prompt):
    """Validate the text input from the user using questionary."""
    try:
        answer = questionary.text(prompt).ask()

        if answer is None:
            f = Figlet(font="catwalk")
            goodbye_text = f.renderText("BYE")
            console.print(Text(goodbye_text, style="bold yellow"))
            quit()

        return answer
    except KeyboardInterrupt:
        f = Figlet(font="catwalk")
        goodbye_text = f.renderText("BYE")
        console.print(Text(f"\n{goodbye_text}", style="bold yellow"))
        quit()
