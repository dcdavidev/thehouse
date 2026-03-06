"""Character blueprint."""
import random

from rich.text import Text

from thehouse.helpers import print_pause


class Character:
    """Character blueprint."""

    def __init__(self):
        """Set max_health and health."""
        self.max_health = random.randint(5, 10)
        self.health = self.max_health

    @property
    def is_alive(self) -> bool:
        """Return whether the character is alive or not."""
        return True if self.health > 0 else False

    def lose_health(self, damage=1) -> None:
        """Take an amount of damage and substract it to health.

        :param damage: the amount of damage as integer the character takes.
        """
        self.health -= damage
        # Sound the terminal bell ONLY on damage
        if damage > 0:
            print("\a", end="", flush=True)
        self.print_health()

    def restore_health(self) -> None:
        """Restore the health to the maximum health of the character."""
        self.health = self.max_health
        self.print_health()

    def print_health(self) -> None:
        """Print a bar with the current health."""
        # Use rich Text for health bar coloring
        health_stars = "*" * self.health
        pt_lost = "-" * (self.max_health - self.health)
        
        health_text = Text("Health: ", style="bold")
        health_text.append(health_stars, style="red")
        health_text.append(pt_lost, style="dim")
        
        print_pause(health_text)
