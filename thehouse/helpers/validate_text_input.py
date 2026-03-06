"""validate_text_input.

This function will validate text input.
"""
import questionary
from termcolor import colored

from .print_pause import print_pause


def validate_text_input(prompt):
    """Validate the text input from the user using questionary."""
    try:
        answer = questionary.text(prompt).ask()

        if answer is None:
            print_pause(colored("Goodbye!", "yellow"))
            quit()

        return answer
    except KeyboardInterrupt:
        print_pause(colored("\nGoodbye!", "yellow"))
        quit()
