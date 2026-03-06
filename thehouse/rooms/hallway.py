"""Hallway.

Sides:
- FORWARD: the hall.
- RIGHT: door to the bedroom.
- BACKWARD: door to the studio.
- LEFT: door to the livingroom.
"""

from thehouse.helpers import print_pause, validate_input
from thehouse.helpers.constants import PASSEPARTOUT

from .room import Room


class Hallway(Room):
    """Hallway."""

    def blueprint(self) -> None:
        """Print the blueprint of the room."""
        print_pause(
            [
                "- In front of you, there is the hall of the house.",
                "- On your right, there is a small table and a door.",
                "- Behind you, there is a door.",
                "- On your left, there is a door and two paintings.",
            ]
        )

    def center(self):
        """Print welcome message and blueprint."""
        print_pause("You are in the hallway.")
        self.blueprint()
        return self.move()

    def backward(self):
        """Print content of the back side of the room."""
        studio = self.thehouse.rooms["studio"]

        if studio.door_locked or PASSEPARTOUT not in self.player.items:
            print_pause(
                [
                    "The door is locked!",
                    "It seems you need to find a key.",
                    "You go back.",
                ]
            )
            return str(self)
        else:
            print_pause("You open the door and enter the studio.")
            return "studio"

    def forward(self):
        """Move player to the hall."""
        return "hall"

    def right(self):
        """Move player to the bedroom."""
        if PASSEPARTOUT not in self.player.items:
            print_pause(
                [
                    "There is a small table and a door.",
                    "What do you want to do?",
                ]
            )

            # Using descriptive labels for the radio boxes
            choices_map = {
                "Check the table": "table",
                "Open the door": "door",
            }

            choice_label = validate_input(
                "Your choice: ",
                list(choices_map.keys()),
            )

            # Get the internal value from the mapping
            selected_key = next(k for k in choices_map if k.lower() == choice_label)
            choice = choices_map[selected_key]

            if choice == "door":
                print_pause("You open the door and enter the bedroom.")
                return "bedroom"
            else:
                return self.table()
        else:
            print_pause("You open the door and enter the bedroom.")
            return "bedroom"

    def table(self):
        """Let the user check if there's something inside the table."""
        print_pause(
            ["You open the drawer and find that it is empty.", "You go back."]
        )
        return str(self)

    def left(self):
        """Move player to the livingroom."""
        print_pause("You open the door and enter the living room.")
        return "livingroom"
