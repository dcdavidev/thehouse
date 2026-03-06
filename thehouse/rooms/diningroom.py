"""Dining Room.

Sides:
- FORWARD: corpse
- RIGHT: corpse
- BACKWARD: corpse
- LEFT: door to the hall
"""
import random

from thehouse.helpers import print_pause
from thehouse.helpers.constants import HOUSE_KEY_2

from .room import Room


class Diningroom(Room):
    """Diningroom."""

    def __init__(self, player, thehouse):
        """Initialize class.

        :param player: the instantiated Player class.
        :param thehouse: the instantiated TheHouse class.
        """
        super().__init__(player, thehouse)
        self.key_in_corpse = random.choice(["forward", "left", "backward"])

    def blueprint(self) -> None:
        """Print the blueprint of the room."""
        print_pause(
            [
                "- In front of you, there is a corpse!",
                "- On your right, there is another corpse!",
                "- Behind you, there is a third corpse!",
                "- On your left, there is a door.",
            ]
        )

    def center(self):
        """Print a welcome message."""
        print_pause(
            [
                "You are in the dining room!",
                "There is a bloody mess here...",
                "Someone or something killed three people!",
            ]
        )
        self.blueprint()
        return self.move()

    def forward(self):
        """Describe the corpse."""
        print_pause(
            [
                "Something smashed its head!",
                "There is a lot of blood and a strange material on the corpse.",
                "You check its pockets.",
            ]
        )

        if self.key_in_corpse == "forward":
            if HOUSE_KEY_2 in self.player.items:
                print_pause(
                    ["You already checked its pockets and found a key.", "You go back."]
                )
            else:
                print_pause("You find a key!")
                self.player.pick_an_item(HOUSE_KEY_2)
        else:
            print_pause("There is nothing inside its pockets. You go back.")

        return str(self)

    def right(self):
        """Describe the corpse."""
        print_pause(["Something ripped its arms off!", "You check its pockets."])

        if self.key_in_corpse == "left":
            if HOUSE_KEY_2 in self.player.items:
                print_pause(
                    ["You already checked its pockets and found a key.", "You go back."]
                )
            else:
                print_pause("You find a key!")
                self.player.pick_an_item(HOUSE_KEY_2)
        else:
            print_pause("There is nothing inside its pockets. You go back.")

        return str(self)

    def backward(self):
        """Describe the corpse."""
        print_pause(
            [
                "There is a huge hole inside the chest of the corpse.",
                "Something ripped its heart out!",
                "You check its pockets.",
            ]
        )

        if self.key_in_corpse == "backward":
            if HOUSE_KEY_2 in self.player.items:
                print_pause(
                    ["You already checked its pockets and found a key.", "You go back."]
                )
            else:
                print_pause("You find a key!")
                self.player.pick_an_item(HOUSE_KEY_2)
        else:
            print_pause("There is nothing inside its pockets. You go back.")

        return str(self)

    def left(self):
        """Move player towards the hall."""
        print_pause("You open the door and enter the hall.")
        return "hall"
