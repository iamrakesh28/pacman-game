# Pacman Game

##### pacmanMatrix
 This is configuration file for Pacman Board. 'p' is for pacman, 'g' for ghost, 'f' for fruit and '#' for obstacle. If you want to change the board, make sure that after changes, total characters (including spaces) in each line is same and '#' should be on the border of the board. Put spaces for empty positions. 
##### escape.py
  This file gives next position of ghosts such that it maximizes the current shortest distance form the pacman. It uses Breadth-first Search as a subroutine.
##### pacmanBFS.py
  This file does Breadth First Search from pacman position and finds the shortest path to each ghosts. The ghosts uses this path to reach pacman in minimum time.
##### pacman.py
  It is the main program or game. The game runs in the terminal.
  
##### visualPac.py
  It takes board matrix, ghosts, fruits and pacman positions as input and displays in the shell. This program creates visualization in the terminal.
  
  Some snapshots of the game
  
#	![Pacman1](https://github.com/iamrakesh28/Games/blob/master/images/pacman1.png)
#	![Pacman2](https://github.com/iamrakesh28/pacman-game/blob/gui/Images/pacman-old.gif)

To run the game, execute the command `python3 pacman.py` on the terminal.

or

To make `pacman.py` executable, type the following

`chmod +x myscript.py`

Type `./pacman.py` to run.
##### pacmanGUI.py
  It is the main program or game. The game runs in a graphical interface and pygame module is needed for it.
  
  Some snapshots of the game
  
  ![Pacman1](https://github.com/iamrakesh28/pacman-game/blob/gui/Images/pac-game1.png) 
  
  ![Pacman2](https://github.com/iamrakesh28/pacman-game/blob/gui/Images/pacman.gif)

# Installation

The game requires pygame module to run. To install pygame for python, do this on a terminal (Ctrl+Alt+t)

#### python2
`sudo apt-get install python-pygame`
or

`pip install pygame`

#### python3
`sudo apt-get install python3-pygame`
or

`pip3 install pygame`

To run the game, execute the command (choose suitable python interpreter) `python pacmanGUI.py` on the terminal.

or

`pacmanGUI` is a executable file. Run the game from this file.

or

Create standalone executable file for `pacmanGUI.py`. To create standalone executable, do these

## Installing PyInstaller
PyInstaller can be installed using Pip, the Python package manager

`pip install pyinstaller`

## Building the Executable

Now, build the executable

`pyinstaller --onefile --windowed pacmanGUI.py`
