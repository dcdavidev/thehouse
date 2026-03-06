"""thehouse.

This class wraps all rooms and play the game
"""
import random

from pyfiglet import Figlet
from rich.text import Text

import thehouse.rooms as rooms
from thehouse.helpers import print_pause, random_death
from thehouse.helpers.state import GameState


class TheHouse:
    """TheHouse."""

    def __init__(self, player):
        """Inizialize class.

        :param player: the instantiated player class.
        """
        self.player = player

        # Rooms
        self.rooms = {
            "bedroom": rooms.Bedroom(self.player, self),
            "diningroom": rooms.Diningroom(self.player, self),
            "hall": rooms.Hall(self.player, self),
            "hallway": rooms.Hallway(self.player, self),
            "kitchen": rooms.Kitchen(self.player, self),
            "livingroom": rooms.Livingroom(self.player, self),
            "studio": rooms.Studio(self.player, self),
        }

        self.current_room = "bedroom"
        # Initial state update
        GameState.update(player=self.player, room=self.current_room)

    def introduction(self):
        f = Figlet(font="catwalk")
        banner_text = f.renderText("THE HOUSE")
        banner = Text(banner_text, style="bold dim green")
        print_pause(banner, 3)

        print_pause([
            "Someone, or something hit you and you faint.",
            "You hear that this someone or something drags you to someplace.",
            "You open your eyes and find yourself lying on the floor.",
            "Your head is pounding and it hurts.",
            "With a lot of effort you stand up."
        ], 2)

    def play(self):
        """Play engine."""
        self.introduction()

        while not self.player.escaped and self.player.is_alive:
            # Update state before entering room
            GameState.update(room=self.current_room)
            
            # a room's center() method returns the next room
            next_room = self.rooms[self.current_room].center()
            self.current_room = next_room

            # Check if player is still alive
            if not self.player.is_alive:
                random_death()
                print_pause(Text("\n=== GAME OVER ===\n", style="bold red"), 3)
                break

            # Check if player has escaped
            if self.player.escaped:
                f = Figlet(font="catwalk")
                victory_text = f.renderText("VICTORY")
                victory = Text(victory_text, style="bold yellow")
                print_pause(victory)
                break
