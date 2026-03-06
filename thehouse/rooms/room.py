"""Room blueprint."""
from thehouse.helpers import print_pause, validate_input


class Room:
    """Room blueprint."""

    def __init__(self, player, thehouse):
        """Initialize the class.

        :param player: the instantiated Player class.
        :param thehouse: the instantiated TheHouse class.
        """
        self.player = player
        self.thehouse = thehouse

    def __str__(self):
        """Return the name of the room."""
        return self.__class__.__name__.lower()

    def blueprint(self) -> None:
        """Print all sides of the room.

        This method is called if the user chooses 'help'.
        """
        pass

    def right(self) -> str:
        """Print the content of the right side of the room."""
        return str(self)

    def left(self) -> str:
        """Print the content of the left side of the room."""
        return str(self)

    def backward(self) -> str:
        """Print the content of the back side of the room."""
        return str(self)

    def forward(self) -> str:
        """Print the content of the front side of the room."""
        return str(self)

    def move(self) -> str:
        """Let the user move inside or outside the room."""
        # Map descriptive labels to move actions
        move_options = {
            "Go forward": "forward",
            "Go right": "right",
            "Go backward": "backward",
            "Go left": "left",
            "Check the room (Help)": "help",
            "Check your pockets (Items)": "items",
        }

        while True:
            choice_label = validate_input(
                "Where do you want to go?",
                list(move_options.keys()),
            )

            # Get the internal value from the mapping
            selected_key = next(k for k in move_options if k.lower() == choice_label)
            choice = move_options[selected_key]

            if choice == "right":
                return self.right()
            elif choice == "left":
                return self.left()
            elif choice == "backward":
                return self.backward()
            elif choice == "forward":
                return self.forward()
            elif choice == "help":
                self.blueprint()
            elif choice == "items":
                self.player.print_items()
