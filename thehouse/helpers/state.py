"""Game state manager."""

class GameState:
    player = None
    current_room = "Bedroom"

    @classmethod
    def update(cls, player=None, room=None):
        if player:
            cls.player = player
        if room:
            cls.current_room = room
