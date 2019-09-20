# pacman-game

##### pacmanMatrix
 This is configuration file for Pacman Board. 'p' is for pacman, 'g' for ghost, 'f' for fruit and '#' for obstacle. If you want to change the board, make sure that after changes, total characters (including spaces) in each line is same and '#' should be on the border of the board. Put spaces for empty positions. 
##### escape.py
  This file gives next position of ghosts such that it maximizes the current shortest distance form the pacman. It uses Breadth-first Search as a subroutine.
##### pacmanBFS.py
  This file does Breadth First Search from pacman position and finds the shortest path to each ghosts. The ghosts uses this path to reach pacman in minimum time.
##### pacman.py
  It is the main program or game. The game runs in the terminal.
  
  Some snapshots of the game
  

To run the game, execute the command `python3 pacmanGUI.py` on the terminal.

or

To make `pacman.py` executable, type the following

`chmod +x myscript.py`

Type `./pacman.py` to run.
