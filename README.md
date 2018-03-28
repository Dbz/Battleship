# Battleship

This is a simple python program that lets the user play against an AI oponent. 

## Features 
* Provide a simple way to play a fun game.
* Easy to install and play. Works on any system that can run python.
* Good example of how to make a simple game using python.

## Installation

To install Battleship, you will need to have python installed. Download python [here](https://www.python.org/downloads/).
![alt text](https://github.com/Dbz/Battleship/blob/master/markdown/py1.JPG)

**This program will not run on python 3. So download the Python 2.7 package.** 
Once you have downloaded the Python 2.7 executable, run it and go through the installer. 
Now with python installed, we can download and run the game! To download the game just hit the green button labled Clone or download and then hit the Zip folder button. ![alt text](https://github.com/Dbz/Battleship/blob/master/markdown/down1.JPG)


Once the zipped folder is downloaded, You can extract the files. This is different for every operating system, for windows I recomemnd [7-zip](https://www.7-zip.org/). After unziping the files, just double click on the file BattleShip.py.

## How to play

Once you've started the python script, the game should run immediately. If you see a window pop up and then close, you're probably using python 3. Make sure to run this game using python 2.7.x. This game is exactly like the board game battleship. On the left side is your view of your AI opponent's board. On the right side is your board and battleships. The battleships are represented by the brackets and plus symbols. Each ship can be vertical or horrizontal. Each player gets five ships. One size five ship, one size four ship, two size three ships, and one size two ships. The ships are arranaged on a ten by ten grid. The top left corner being row zero column zero and the bottom right corner being row nine column nine. 

The object of the game is simple, sink all of the enemy ships before they can sink all of yours. Each player turn, you get to fire one shot based on the coordinate you input. Then the AI will take their turn. When an AI hits you, they will try to hit around that spot to try and find the rest of your ship. When they do, the game will print out the version of your board that they can see. To understand the board, we'll explain each symbol. The symbol X represents a spot that has already been shot at but was just a miss. The symbol O represents a spot that has not been hit by anything. Lastly the * symbol represents part of a ship that has been hit. Once either you, or the AI has one the game will end. To play again simply restart the program.

## Contribute
* Issue Tracker: https://github.com/Dbz/Battleship/issues
* Source Code: https://github.com/Dbz/Battleship/blob/master/BattleShip.py
* Wiki: https://github.com/Dbz/Battleship/wiki
* Roadmap: https://github.com/Dbz/Battleship/wiki/Roadmap

## Imporovememnt ideas
* Port to python 3.
* Add a two player mode.
* Code cleanup to make the program easier to read.
* Add some error handling for certain invalid inputs.
* Allow a user to place their battleships.
* Add functionality to start a new game without exiting the program.
* Add numbers to board so it is easier to tell the coordinates.
* Debug features seem to be showing during gameplay. Need to remove them. 

## License
This project is licensed under the MIT license.
