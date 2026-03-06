## 2.7.0 (2026-03-06)

### Feat

- trigger release cycle

### Fix

- resolve version inconsistencies and remove redundant __version__ from __init__.py
- handle non-interactive environments and update README
- use rebase before pushing release to handle concurrent changes
- simplify release process and ensure tags are pushed
- explicit tag pushing and enable annotated tags
- ensure automated release pushes both commits and tags

## 2.6.1 (2026-03-06)

### Fix

- synchronize release tagging and simplify publish triggers

## 2.6.0 (2026-03-06)

### Feat

- UI overhaul with rich, pyfiglet, and persistent appbar
- setup automated release with poetry, poethepoet and commitizen
- expose main function for entry point

### Fix

- make automated release non-interactive and reset version to last tag
- update version to 3.0.1 in project metadata
- spelling

## 2.5.0 (2023-03-16)

## 2.4.1 (2023-02-21)

## 2.4.0 (2022-06-27)

## 2.3.1 (2022-06-25)

### Feat

- add play again
- add items. now you can check your pockets!
- add print_items

### Fix

- gracefully quit the game if user interrupts it
- add PASSEPARTOUT
- add back when users is asked to pick a combination for the safe
- fix item name

## 2.3.0 (2022-06-24)

### Feat

- **livingroom**: add a strong combination
- **room**: add items
- add magic methods

### Fix

- fix items
- fix item names
- **room**: remove items
- export Monster
- **monster**: fix deal_damage
- fix validate_input

### Refactor

- delete old file
- **diningroom**: add documentation and blueprint
- **kitchen**: add documentation and blueprint
- **hall**: add documentation and blueprint
- add documentation and blueprint
- add a note for future content
- **hallway**: update methods and add PASSEPARTOUT
- **studio**: add documentation
- improve Room parent class
- fix imports
- add player the TheHouse class
- add intro of thehouse
- add helpers and documentation
- init thehouse class
- create a backup of the old thehouse
- make is_alive as a class property

## 2.2.0 (2022-06-20)

### Feat

- **thehouse**: add gameover

### Fix

- **character**: fix restore_health
- **livingroom**: fix escape

## 2.1.2 (2022-06-19)

### Fix

- move if __name__ on the __main__ module

## 2.1.1 (2022-06-19)

### Fix

- **pyproject**: fix scripts

## 2.1.0 (2022-06-19)

## 2.0.7 (2022-06-19)

## 2.0.6 (2022-06-19)

## 2.0.5 (2022-06-19)

### Fix

- **pyproject**: fix scripts

## 2.0.3 (2022-06-19)

### Refactor

- move play function inside the thehouse file

## 2.0.2 (2022-06-19)

## 2.0.1 (2022-06-19)

### Fix

- add hyphens to the destinations

## 2.0.0 (2022-06-19)

### Feat

- **diningroom**: add content of the room
- **diningroom**: add content to the center method
- **diningroom**: initialize
- **hall**: add forward method content
- **kitchen**: hide the knife in a random drawer
- **kitchen**: add forward and right methods
- **kitchen**: initialize
- **livingroom**: add the escape method
- **livingroom**: add fight
- **monster**: initialize class
- **character**: init class
- **livingroom**: initialize room
- **bedroom**: add pick a drawer
- **bedroom**: add the content on the method left
- **bedroom**: add content on the right method
- **bedroom**: display three dots while resting
- **bedroom**: add the backword content
- **bedroom**: put more content in the center method

### Fix

- more fixes
- **bedroom**: hopefully fix pick a drawer prompt
- fix import
- **thehouse**: better intro
- **studio**: improve and hopefully fix key
- **thehouse**: add more space to the title
- **livingroom**: add damage to deals_damage
- import monster
- **hallway**: fix the position of the bedroom
- fix import and whitespace

### Refactor

- follow schema F > R > B > L

## 1.3.0 (2022-06-18)

### Feat

- **bedroom**: initialize
- **player**: add restore_health and print_health
- **studio**: randomize where the key is
- **hall**: init
- **hallway**: add the backward content
- **studio**: move to the hallway
- add items to Player class
- **room**: add parent class room
- **hallway**: add more content
- **studio**: change the position of the window and the desk

### Fix

- imports
- **hall**: remove "where do you want to go" from the center method
- move "Where do you wanna go" into the move function
- **studio**: fix the lock of the door
- fix typo

### Refactor

- **play**: call the play function

## 1.2.3 (2022-06-18)

## 1.2.2 (2022-06-18)

## 1.2.1 (2022-06-18)

### Refactor

- move the play function in play.py

## 1.2.0 (2022-06-18)

### Feat

- randomly select a room to start with
- init hallway
- add current_room
- add random_death
- add forward content
- add the left content
- add right and backward content
- add play_again
- add health bar
- add Player class
- **rooms**: prompt the user to turn the lights on if they're off
- initialize the studio room
- initialize game engine
- **helpers**: add validate_input
- **helpers**: add print_pause

### Fix

- remove the hallway from the rooms available
- check if door is locked
- create an intro of the game, moved from the studio
- change how the game will be run and add play again
- check if player is still alive
- improve play_game
- ask the user to pick another book
- move to the center of the room only if player is still alive
- now the game checks properly for the player's health
- check the player health and quit the game if health is 0
- fix paths

### Refactor

- rename game_engine into thehouse
