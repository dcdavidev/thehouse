"""Kitchen.

Sides:
- FORWARD: window
- RIGHT: door to the hall
- BACKWARD: drawers
- LEFT: drawers
"""

import random

from thehouse.helpers import print_pause, validate_input
from thehouse.helpers.constants import KNIFE

from .room import Room


class Kitchen(Room):
    """Kitchen."""

    def __init__(self, player, thehouse):
        """Initialize class.

        :param player: the instantiated Player class.
        :param thehouse: the instantiated TheHouse class.
        """
        super().__init__(player, thehouse)
        self.knife_in_drawer = random.randint(1, 3)
        self.knife_on_wall = random.choice(["left", "backward"])

    def blueprint(self) -> None:
        """Print the blueprint of the room."""
        print_pause(
            [
                "- In front of you, there is a window.",
                "- On your right, there is a door.",
                "- Behind you, there are some kitchen drawers.",
                "- On your left, there are more kitchen drawers.",
            ]
        )

    def center(self):
        """Print a welcome message."""
        print_pause("You are in the kitchen!")
        self.blueprint()
        return self.move()

    def forward(self):
        """Print the content of the front side of the room."""
        print_pause(
            [
                "You look out of the window.",
                "There is nothing but darkness to see...",
                "You go back.",
            ]
        )
        return str(self)

    def right(self):
        """Move the player to the hall."""
        print_pause("You open the door and enter the hall.")
        return "hall"

    def _search_drawers(self, wall):
        print_pause(
            ["There are three drawers here. You decide to check them all."]
        )
        return self.pick_a_drawer(wall)

    def left(self):
        """Show user the drawers."""
        return self._search_drawers("left")

    def backward(self):
        """Show user the drawers."""
        return self._search_drawers("backward")

    def pick_a_drawer(self, wall):
        """Let the user pick a drawer.

        :param wall: the wall where the knife is located.
        """
        drawer_options = {
            "Open the 1st drawer": 1,
            "Open the 2nd drawer": 2,
            "Open the 3rd drawer": 3,
            "Nevermind...": "back",
        }

        while True:
            choice_label = validate_input(
                "Which drawer do you want to open?",
                list(drawer_options.keys()),
            )

            # Get the internal value from the mapping
            selected_key = next(k for k in drawer_options if k.lower() == choice_label)
            choice = drawer_options[selected_key]

            if choice == "back":
                print_pause("You go back to the center of the room.")
                return str(self)
            else:
                print_pause("You dig through the kitchen tools, looking for something useful.")

                if wall == self.knife_on_wall and choice == self.knife_in_drawer:
                    if KNIFE in self.player.items:
                        print_pause(
                            [
                                "You already have the knife from this drawer.",
                                "There is nothing else inside.",
                            ]
                        )
                    else:
                        print_pause("You find a KNIFE!")
                        self.player.pick_an_item(KNIFE)
                else:
                    print_pause("You find nothing but old silverware and rusty tools.")
