"""Studio.

Sides:
- FORWARD: door to the hallway
- RIGHT: window
- BACKWARD: desk
- LEFT: shelf
"""

import random

from thehouse.helpers import print_pause, validate_input
from thehouse.helpers.constants import PASSEPARTOUT, STUDIO_KEY

from .room import Room


class Studio(Room):
    """Studio class."""

    def __init__(self, player, thehouse):
        """Initialize class.

        :param player: the instantiated Player class.
        :param thehouse: the instantiated TheHouse class.
        """
        super().__init__(player, thehouse)
        self.door_locked = True
        self.lights = random.choice([True, False])
        self.key_in_book = random.randint(1, 3)

    def prompt_light(self):
        """Ask the user to turn the lights on."""
        print_pause(
            [
                "You hear something lurking in the dark.",
                "You lose some health while turning the lights on.",
            ]
        )
        self.player.lose_health()
        self.lights = True

    def blueprint(self) -> None:
        """Print blueprint of the room."""
        print_pause(
            [
                "- In front of you, there is a closed door.",
                "- On your right, there is a window.",
                "- Behind you, there is a desk with some papers on it.",
                "- On your left, there is a shelf with many books on it.",
            ]
        )

    def center(self) -> str:
        """Print center of the room."""
        lights = "on" if self.lights else "off"

        print_pause(f"You find yourself in a room with the lights {lights}.")

        if not self.lights:
            self.prompt_light()

        if self.player.is_alive:
            print_pause("You are in the middle of a studio.")
            self.blueprint()
            return self.move()

        return str(self)

    def right(self) -> str:
        """Print the content of the right side."""
        print_pause(
            [
                "Behind the desk, there is a window.",
                "You glance outside, but it is pitch black.",
                "You cannot see anything interesting here.",
                "You go back.",
            ]
        )
        return str(self)

    def backward(self) -> str:
        """Print the content of the back side."""
        combination = self.thehouse.rooms["livingroom"].safe_combination

        print_pause(
            [
                "The desk is full of papers.",
                "There is a note on the desk.",
                f"It says: {combination:04d}",
                "You go back.",
            ]
        )
        return str(self)

    def left(self) -> str:
        """Print the content of the left side."""
        print_pause(
            [
                "On your left, there is a shelf full of books.",
                "You run your finger along the dusty spines "
                "and quickly read the titles.",
                "There are so many books on this shelf.",
                "You wonder if you have ever read this many books.",
            ]
        )

        return self.pick_a_book()

    def book_divine_comedy(self):
        """Print content of the Divine Comedy book."""
        if self.key_in_book == 1 and (STUDIO_KEY not in self.player.items):
            self.pick_the_key()
        else:
            print_pause(
                [
                    "Amor, ch’a nullo amato amar perdona,",
                    "mi prese del costui piacer sì forte,",
                    "che, come vedi, ancor non m’abbandona",
                ]
            )

    def book_the_king_in_yellow(self):
        """Print content of The King in Yellow book."""
        if self.key_in_book == 2 and (STUDIO_KEY not in self.player.items):
            self.pick_the_key()
        else:
            print_pause(
                [
                    "for I knew that the King in Yellow",
                    "had opened his tattered mantle",
                    "and there was only God to cry to now.",
                ]
            )

    def book_arkhams_secrets(self):
        """Print content of Arkham's secrets book."""
        if self.key_in_book == 3 and (STUDIO_KEY not in self.player.items):
            self.pick_the_key()
        else:
            print_pause(
                [
                    "West of Arkham the hills rise wild,",
                    "and there are valleys with deep",
                    "woods that no axe has ever cut.",
                ]
            )

    def pick_the_key(self):
        """Add the key into the player's items."""
        print_pause("You open the book and a key falls onto the ground.")
        self.player.pick_an_item(STUDIO_KEY)

    def pick_a_book(self) -> str:
        """Let the user choose a book."""
        book_options = {
            "Divine Comedy": "1",
            "The King in Yellow": "2",
            "Arkham's Secrets": "3",
            "Nevermind...": "back",
        }

        while True:
            choice_label = validate_input(
                "Which book do you want to pick?",
                list(book_options.keys()),
            )

            selected_key = next(k for k in book_options if k.lower() == choice_label)
            choice = book_options[selected_key]

            if choice == "1":
                self.book_divine_comedy()
            elif choice == "2":
                self.book_the_king_in_yellow()
            elif choice == "3":
                self.book_arkhams_secrets()
            elif choice == "back":
                print_pause("You go back to the center of the room.")
                return str(self)

    def forward(self) -> str:
        """Print content of the front side of the house."""
        if not self.door_locked:
            print_pause("You open the door and enter the hallway.")
            return "hallway"
        else:
            print_pause(
                [
                    "There is a closed door in front of you.",
                    "Do you want to try to open it?",
                ]
            )

            choice = validate_input("Your choice:", ["yes", "no"])

            if choice == "yes":
                if (
                    STUDIO_KEY in self.player.items
                    or PASSEPARTOUT in self.player.items
                ):
                    self.door_locked = False
                    print_pause(
                        ["You use a key to unlock the door.", "You exit the studio."]
                    )
                    return "hallway"
                else:
                    print_pause(
                        [
                            "The door is locked.",
                            "It seems you need a key to open it!",
                            "You go back.",
                        ]
                    )
                    return str(self)
            else:
                print_pause(
                    [
                        "You hear a scratching sound from the other side of the door!",
                        "You instantly jump back in fear!",
                    ]
                )
                self.player.lose_health()
                return str(self)
