#     Pacman Bot
Pacman Bot trained using Q-Learning algorithm to play the Arcade Pacman.
##### 1. pacmanMatrix
  This is configuration file for Pacman Board. 'p' is for pacman, 'g' for ghost, 'f' for fruit and '#' for obstacle. If you want to change the board, make sure that after changes, total characters (including spaces) in each line is same and '#' should be on the border of the board. Put spaces for empty positions. 
##### 2. escape.py
  This file gives next position of ghosts such that it maximizes the current shortest distance form the pacman. It uses Breadth-first Search as a subroutine.
##### 3. pacmanBFS.py
  This file does Breadth First Search from pacman position and finds the shortest path to each ghosts. The ghosts uses this path to reach pacman in minimum time.
##### 4. train.py
  Q-Learning is implemented in this file. It takes the following input:
  
    a. Current and previus positions of ghosts and pacman (previous position is used for calculating velocity)
    b. Number of fruits and change in fruit number
    c. Who is chasing whom
    d. Minimum distance of fruit and ghost from pacman
    e. The game is over or not. If over, then is it a lose or win
    
 Reward function is based on the above inputs. All these data are stored as a state. States are stored in python dicitionary. 
### Shell Version
##### 5. visualPac.py
  It takes board matrix, ghosts, fruits and pacman positions as input and displays in the shell.
##### 6. trainPacman.py
  It is the game executable file for shell. It takes board input from the pacmanMatrix.txt file. Displays the board using visualPac.py. Takes the input from the user or bot about its action. Gets the next position of ghosts from escape.py or pacmanBFS.py files. Gives the required inputs to the train.py file. train.py takes the optimal action (when the bot is playing) and send it back to trainPacman.py. Each time the file is run, it takes the previously learned Q-values, actions, states, etc from Q, action, memo, state, etc. files. Each time the game is played, it learns and stores the values in these files.
#	![Pacman training](https://github.com/iamrakesh28/Games/blob/master/images/trainPacman.png)
 If you have changed the board configuration in the `pacmanMatrix`, then uncomment the line 124 (`train.E.init()`) and set `num = 10000` (line 123). `train.E.init()` set every values (Q-values, actions, states) to initail value and num is the number of episodes the game is trained for. After that uncomment the line 123 and set `num` to smaller value (>5) . This enables the program to train each time the game is played.
 To run the game in shell, use `python3 trainPacman.py` in shell.
 
 ### GUI Version
 ##### pacmanGUI.py
  It is the GUI version of the game. The Bot game runs in a graphical interface and pygame module is needed for it.
  
  Some snapshots of the game
  
  ![Pacman1](https://github.com/iamrakesh28/pacman-game/blob/gui/Images/pac-game1.png) 
 

# Installation

The Bot Game requires pygame module to run. To install pygame for python, do this on a terminal (Ctrl+Alt+t)

#### python2
`sudo apt-get install python-pygame`
or

`pip install pygame`

#### python3
`sudo apt-get install python3-pygame`
or

`pip3 install pygame`

To run the game, execute the command `python pacmanGUI.py` on the terminal.

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
