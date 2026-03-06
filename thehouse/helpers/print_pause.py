"""print_pause.

This function will print a message and then it will pause the terminal
"""

import time
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from .ui import make_layout

console = Console()

def print_pause(content, sleep=1):
    """Print a message (or multiple) and pause the terminal with an appbar.

    :param content: a string or a list of strings to print.
    :param sleep: the amount of seconds the terminal should sleep as integer.
    """
    try:
        # Normalize content to a list
        if isinstance(content, (str, Text)):
            lines = [content]
        else:
            lines = content

        # Check if we are dealing with a banner
        is_banner = any("\n" in str(line).strip() for line in lines)

        if is_banner:
            for line in lines:
                # Banners are shown above the appbar
                console.print(make_layout(line))
                time.sleep(sleep)
        else:
            # Display lines one by one inside the same box
            accumulated_text = Text()
            
            # Live display makes it look truly persistent during the pause
            with Live(make_layout(Panel(accumulated_text, border_style="bright_blue", padding=(1, 2))), 
                      console=console, refresh_per_second=4, transient=True) as live:
                for i, line in enumerate(lines):
                    if i > 0:
                        accumulated_text.append("\n\n")
                    
                    accumulated_text.append(str(line))
                    live.update(make_layout(Panel(accumulated_text, border_style="bright_blue", padding=(1, 2))))
                    time.sleep(sleep)
            
            # Final print to keep it in terminal history
            console.print(make_layout(Panel(accumulated_text, border_style="bright_blue", padding=(1, 2))))

    except KeyboardInterrupt:
        f = Figlet(font="catwalk")
        banner = f.renderText("BYE")
        console.print(Text(banner, style="bold yellow"))
        quit()
