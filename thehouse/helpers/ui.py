"""UI components."""
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from .state import GameState

def get_appbar():
    """Create a persistent top appbar."""
    if not GameState.player:
        return Panel(Text("Loading...", style="dim"), border_style="bright_magenta")

    # Health bar with hearts
    health_stars = "❤" * GameState.player.health
    pt_lost = "o" * (GameState.player.max_health - GameState.player.health)
    
    health_text = Text("HP: ", style="bold")
    health_text.append(health_stars, style="red")
    health_text.append(pt_lost, style="dim white")

    # Items
    items_text = Text(" 📦 Items: ", style="bold")
    if not GameState.player.items:
        items_text.append("None", style="dim italic")
    else:
        items_text.append(", ".join(GameState.player.items), style="yellow")

    # Room
    room_text = Text(f" 🏠 {GameState.current_room.upper()}", style="bold cyan")

    # Create a grid for the appbar to align elements
    table = Table.grid(expand=True)
    table.add_column(justify="left", ratio=1)
    table.add_column(justify="center", ratio=2)
    table.add_column(justify="right", ratio=1)
    
    table.add_row(health_text, items_text, room_text)
    
    return Panel(table, border_style="bright_magenta", padding=(0, 1))

def make_layout(main_content):
    """Create the full screen layout with appbar at the top."""
    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main")
    )
    layout["header"].update(get_appbar())
    layout["main"].update(main_content)
    return layout
