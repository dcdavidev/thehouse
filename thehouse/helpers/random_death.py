"""random_death.

This function will print a random death from the DEATHS variable.
It uses the print_pause funtion
"""

import random
from rich.text import Text

from .print_pause import print_pause

DEATHS = [
    "Something utterly bad stabs you in the back. You died!",
    "A strange figure grabs you and kills you instantly!",
    "Something from the dark makes you so mad you die!",
]


def random_death():
    """Print a random death from DEATHS variable."""
    death_msg = random.choice(DEATHS)
    print_pause(Text(death_msg, style="red"), 3)
    print_pause(Text("\n\n=== GAME OVER ===\n\n", style="bold blink red"))
