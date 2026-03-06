"""Living Room.

Sides:
- FORWARD: safe
- RIGHT: door to the hallway
- BACKWARD: window
- LEFT: window
"""

import random

from thehouse.characters import Monster
from thehouse.helpers import print_pause, validate_input, validate_text_input
from thehouse.helpers.constants import HOUSE_KEY_3, KNIFE, PASSEPARTOUT

from .room import Room


class Livingroom(Room):
    """Livingroom."""

    def __init__(self, player, thehouse):
        """Initialize class.

        :param player: the instantiated Player class.
        :param thehouse: the instantiated TheHouse class.
        """
        super().__init__(player, thehouse)
        self.monster = Monster(self.player)
        self.tries = random.randint(3, 6)
        self.safe_open = False
        self.safe_combination = random.randint(1, 9999)

    def blueprint(self) -> None:
        """Print blueprint of the room."""
        print_pause(
            [
                "- In front of you, there is a painting.",
                "- On your right, there is a door.",
                "- Behind you, there is a window.",
                "- On your left, there is another window.",
            ]
        )

    def center(self):
        """Print welcome message."""
        if self.monster.is_alive:
            print_pause(
                [
                    "There is a terrible monster!",
                    "It is half human and half something indescribable!",
                    "Luckily, it is slow, but one of its tentacles tries to grab you!",
                ]
            )
            return self.fight_or_escape()
        else:
            print_pause("You are in the living room!")
            self.blueprint()
            return self.move()

    def fight_or_escape(self):
        """Let user choose between fighting or escaping."""
        choice = validate_input(
            "Do you want to fight or escape?",
            ["fight", "escape"],
        )

        if choice == "fight":
            return self.fight()
        else:
            return self.escape()

    def fight(self):
        """Let the user fight the monster."""
        if self.monster.is_alive and self.player.is_alive:
            print_pause("It is your turn to deal damage!")

            if KNIFE not in self.player.items:
                damage = 1
                print_pause("It seems like you need something to deal more damage!")
            else:
                damage = random.randint(2, 4)

            print_pause(f"You deal {damage} damage.")
            self.monster.lose_health(damage)

            if self.monster.is_alive:
                print_pause("It is the monster's turn to deal damage!")
                self.monster.deal_damage()

                if self.player.is_alive:
                    return self.fight_or_escape()
                else:
                    return str(self)
            else:
                print_pause(
                    [
                        "You successfully kill the monster!",
                        "The monster drops a key.",
                    ]
                )
                self.player.pick_an_item(PASSEPARTOUT)
                self.thehouse.rooms["studio"].door_locked = False
                return self.center()
        return str(self)

    def escape(self):
        """Let the user try to escape the monster."""
        print_pause("You are trying to escape the monster!")

        choice = validate_input(
            "Quick, choose a path!",
            ["Path 1", "Path 2", "Path 3", "Path 4", "Path 5", "Path 6"],
        )

        # Get the digit from "Path X"
        path_num = int(choice.split()[-1])

        if path_num == random.randint(1, 6):
            print_pause("You successfully escape the monster!")
            return "hallway"
        else:
            print_pause("You panic and cannot escape the fight.")
            self.tries -= 1

            if self.tries <= 0:
                print_pause("The monster reaches you!")
                self.monster.deal_damage()
                self.tries = random.randint(3, 6)

                if self.player.is_alive:
                    return self.fight_or_escape()
                else:
                    return str(self)
            else:
                return self.fight_or_escape()

    def right(self):
        """Move the user towards the hallway."""
        print_pause("You open the door and enter the hallway.")
        return "hallway"

    def backward(self):
        """Move the user towards the window."""
        print_pause(
            [
                "There is a window and you look outside.",
                "There is a car! Maybe you can use it to escape from this house!",
                "You go back.",
            ]
        )
        return str(self)

    def left(self):
        """Move the user towards left."""
        print_pause(
            [
                "There is a balcony.",
                "Outside, there is a garden.",
                "The low lights make the garden look bleak.",
                "You go back.",
            ]
        )
        return str(self)

    def forward(self):
        """Move the user towards the safe."""
        if self.safe_open:
            print_pause(
                [
                    "You already opened the safe and picked THE HOUSE KEY 3.",
                    "You go back.",
                ]
            )
            return str(self)
        else:
            print_pause(
                [
                    "There is a painting...",
                    "You look closely and see there is something behind it!",
                    "You move the painting and reveal a safe!",
                    "Maybe you can break it open!",
                ]
            )

            return self.break_open()

    def break_open(self):
        """Let the user break open the safe."""
        print_pause("You need a combination!")

        while True:
            choice = validate_text_input(
                "Enter the combination (4 digits), or type 'back': "
            )

            if choice.lower() == "back":
                return str(self)
            else:
                if choice == str(self.safe_combination).zfill(4) or choice == str(self.safe_combination):
                    print_pause(
                        ["You successfully open the safe!", "Inside, there is a key!"]
                    )
                    self.player.pick_an_item(HOUSE_KEY_3)
                    self.safe_open = True

                    return str(self)
                else:
                    print_pause("The combination is wrong! Try again!")
