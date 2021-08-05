## Project Name: The Maze Game
Presented By: Ammar Ahmad Rizvi, Rumaisa Kamran, Mikail Faroouqi

**HOW TO MOVE:**
* Use UP and DOWN arrow keys to move around the screen and settings. 
* Enter kep is used to select an option.
* Setttings can be changed by using right and left keys.

**GRID SIZE:**
 * The size can be changed from 10 - 35 units. 

**SIDE LENGTH:**
 * Size of the screen can be changed from 10 - 15 units.

**GAME MODES:**

*1. Solo*
 * Time is recorded for the player till the player reaches to end point.

*2. Two Player*
 * In this mode, both the players start from opposite ends and tries to reach their opponent's start point. The player one is indicarted by Green colour and uses the arrow
keys and the Player two is indicated by WASD to move.


**NOTES:**
 * Once the game is finished, the settings will be at default again.
 * ESC key can be clicked to exit the game.

# CODE STRUCTURE
**main.py:** 
 * This contains how the game works and the mechanism of the graph.

**character.py:**
 * This contains the movement of character fulfilling the game objectives. 

**ui_file.py:**
 * This contains the interface setting which includes the main menu, start game and end game visualization with the linkage of main file.

**graph.py**
 * The generation of the maze.

# HOW TO RUN
1. Pygame package has to be installed and by calling 'sudo pip3 install pygame' it will run.
2. It is run by calling 'python3 main.py' in terminal.

# Contribution:
Ammar: Main.py + Graph.py
Rumaisa: UI_File + Character.py
Mikail: No specific contribution in the code.
