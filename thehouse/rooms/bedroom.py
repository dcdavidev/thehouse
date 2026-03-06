"""Bedroom.

Sides:
- FORWARD: dresser
- RIGHT: window
- BACKWARD: bed
- LEFT: door to the hallway
"""

import random

from thehouse.helpers import print_pause, validate_input
from thehouse.helpers.constants import HOUSE_KEY_1

from .room import Room


class Bedroom(Room):
    """Bedroom."""

    def __init__(self, player, thehouse):
        """Initialize the class.

        :param player: the instantiated Player class.
        :param thehouse: the instantiated TheHouse class.
        """
        super().__init__(player, thehouse)
        self.key_in_drawer = random.randint(1, 5)

    def blueprint(self) -> None:
        """Print the blueprint of the room."""
        print_pause(
            [
                "- In front of you, there is a dresser.",
                "- On your right, there is a window.",
                "- Behind you, there is a bed.",
                "- On your left, there is a door.",
            ]
        )

    def center(self):
        """Print welcome message."""
        print_pause("You are in the bedroom!")
        self.blueprint()
        return self.move()

    def left(self):
        """Move player to the left side of the room."""
        print_pause("You open the door and enter the hallway.")
        return "hallway"

    def backward(self):
        """Move player to the back side of the room."""
        print_pause(["You look tired.", "Do you want to rest a little?"])

        choice = validate_input("Type yes or no: ", ["yes", "no"])

        if choice == "yes":
            print_pause(["You decide to rest.", ".", ".", "."], 2)
            self.player.restore_health()
        else:
            print_pause("You go back.")

        return str(self)

    def right(self):
        """Print content of the right side of the room."""
        print_pause(
            [
                "You look out the window.",
                "Outside, it is pitch black!",
                "Something is moving in the darkness.",
                "It moves so fast that you can barely see it...",
                "You wonder how you can escape this house.",
                "And if it is even safe outside...",
                "You go back.",
            ],
            3,
        )

        return str(self)

    def forward(self):
        """Print content of the front side of the room."""
        print_pause(["There are five drawers."])
        return self.pick_a_drawer()

    def pick_a_drawer(self):
        """Let the user pick a drawer."""
        # Mapping labels to drawer numbers
        drawer_options = {
            "Open 1st drawer": 1,
            "Open 2nd drawer": 2,
            "Open 3rd drawer": 3,
            "Open 4th drawer": 4,
            "Open 5th drawer": 5,
            "You give up": "back",
        }

        while self.player.is_alive:
            choice_label = validate_input(
                "Choose wisely: ",
                list(drawer_options.keys()),
            )

            # Get the internal value from the mapping
            selected_key = next(k for k in drawer_options if k.lower() == choice_label)
            choice = drawer_options[selected_key]

            if choice == "back":
                print_pause("You go back to the center of the room.")
                return str(self)
            else:
                print_pause(
                    "There are some clothes in it. You dig through them to find something..."
                )

                if choice == self.key_in_drawer:
                    if HOUSE_KEY_1 in self.player.items:
                        print_pause(
                            [
                                "You already found a key in this drawer!",
                                "There is nothing more in it.",
                            ]
                        )
                    else:
                        print_pause("You find a key!")
                        self.player.pick_an_item(HOUSE_KEY_1)
                else:
                    print_pause(
                        [
                            "There is nothing among the clothes.",
                            "Something outside is moving...",
                        ]
                    )
                    self.player.lose_health()
        return str(self)
