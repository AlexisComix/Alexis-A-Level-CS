#Skeleton Program for the AQA AS1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA AS1 Programmer Team
#developed in a Python 3 programming environment

#Version Number 1.0

import random

"""
I have noticed that this file uses 2 spaces for indents.
Yikes.
"""

def GetRowColumn(): # Get two integers as an input from the user
  print()           # Print a blank new line for some reason
  Column = int(input("Please enter column: "))  # Unchecked cast to int
  Row = int(input("Please enter row: "))        # Unchecked cast to int
  print()             # Print yet another blank line for some reason
  return Row, Column  # Return
            
def MakePlayerMove(Board, Ships): # Ships is not accessed
  """
  Function to make a player's move. Takes in the board as an arg
  and also takes in ships. Both are of unknown types. Messy.
  """
  Row, Column = GetRowColumn()    # Call to get the row and col input
  if Board[Row][Column] == "m" or Board[Row][Column] == "h":  # Checks misses and hits
    # A really wacky, long string formatting thingy. Ew.
    print("Sorry, you have already shot at the square (" + str(Column) + "," + str(Row) + "). Please try again.")
  elif Board[Row][Column] == "-": # If the shot misses
    print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.")
    Board[Row][Column] = "m"  # Mark as a miss
  else:
    print("Hit at (" + str(Column) + "," + str(Row) + ").")
    Board[Row][Column] = "h"  # Assumes that any other character is a hit. That could go wrong.
        
def SetUpBoard():
  """
  Make a 10x10 list of dashes marking empty tiles.
  numpy could have been a better choice.
  """
  Board = []                  # Blank board list
  for Row in range(10):       # For each row make a blank list
    BoardRow = []
    for Column in range(10):  # Add 10 dashes to the row
      BoardRow.append("-")    
    Board.append(BoardRow)    # Add the blank list to the board and repeat
  return Board                # Return the board

def LoadGame(Filename, Board):
  """
  Load a game from a file... It also takes a board arguement.
  The way this does it is messy, It should just be able to return
  a board that is loaded from a file.

  They are modifying the variable from what is passed in, which means
  that we could have a bad output from it making the code not work properly.
  As said, it should return a board instead if it is actually wanting to be
  a good program.
  """
  # with open(...) as ...: would have been better
  BoardFile = open(Filename, "r") # Open
  for Row in range(10):           # Read each row from the file
    Line = BoardFile.readline()
    for Column in range(10):      # Set the board's cols individually
      Board[Row][Column] = Line[Column]
  BoardFile.close() # Close 
    
def PlaceRandomShips(Board, Ships):
  """
  Place ships on the board randomly for the computer player.
  Takes in a board, and ships. Both are of unknown type, again.

  I think the ships are supposed to be a two dimensional list with a 
  ship type and a length.
  """
  # -------------------------------
  # Fix variables possibly unbound (Error Lens)
  # I added this so I didn't have a bunch of red dots and lines
  # in VSC. 
  Row = 0
  Column = 0
  Orientation = ""
  # -------------------------------
  for Ship in Ships:  # Iterate through the ships
    Valid = False     # Initialise a flag variable to false
    while not Valid:  # Use the flag in a while loop (kinda neat which is a surprise)
      Row = random.randint(0, 9) # Get a random row index candidate
      Column = random.randint(0, 9)   # Same for col
      # Get a random orientation (Horizontal or Vertical)
      HorV = random.randint(0, 1)
      if HorV == 0:
        Orientation = "v" 
      else:
        Orientation = "h" 
      # Check if the boat position is valid
      Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation)
    print("Computer placing the " + Ship[0])
    # Place the ship
    PlaceShip(Board, Ship, Row, Column, Orientation)

def PlaceShip(Board, Ship, Row, Column, Orientation):
  """
  Places the ship based on orientation.
  Changes bits in the list based on the length of the ship
  and the starting point of where it is placed.
  """
  if Orientation == "v":
    for Scan in range(Ship[1]):
      Board[Row + Scan][Column] = Ship[0][0]
  elif Orientation == "h":
    for Scan in range(Ship[1]):
      Board[Row][Column + Scan] = Ship[0][0]

def ValidateBoatPosition(Board, Ship, Row, Column, Orientation):
  """
  Function to validate the board position.

  Uses a big mess of guard clauses.
  """
  if Orientation == "v" and Row + Ship[1] > 10:
    # Check if the row index plus the ship length is out of bounds
    return False
  elif Orientation == "h" and Column + Ship[1] > 10:
    # Checks if the column plus the ship length is out of bounds
    return False
  else:
    # Here, It checks if where the ship could be placed is blank.
    # If not, it returns that its not valid.
    if Orientation == "v":
      for Scan in range(Ship[1]):
        if Board[Row + Scan][Column] != "-":
          return False
    elif Orientation == "h":
      for Scan in range(Ship[1]):
        if Board[Row][Column + Scan] != "-":
          return False
  # If none of the guard clauses return, the program assumes it is valid.
  return True

def CheckWin(Board):
  """
  Goes over the board and checks if there are any ship tiles.
  """
  # I believe this could be condensed to one for loop.
  for Row in range(10):
    for Column in range(10):
      if Board[Row][Column] in ["A","B","S","D","P"]:
        return False
  return True
 
def PrintBoard(Board):
  """
  Prints the board really messily. I am not sure why they use blank print
  statements for newlines, it looks really ugly and wastes time. \n would
  be much nicer if they really needed it.
  """
  print()
  print("The board looks like this: ")  
  print()
  print (" ", end="")
  # Prints the board for the player to see.
  for Column in range(10):
    print(" " + str(Column) + "  ", end="")
  # Prints the whole board of all the ships included, row by
  # row but uses the name Column for some reason.
  print()

  # Here, It places a blank tile for the user to simulate
  # not being able to see the opponents ships... even though
  # they are shown it just before...
  for Row in range(10):
    print (str(Row) + " ", end="")
    for Column in range(10):
      if Board[Row][Column] == "-":
        print(" ", end="")
      elif Board[Row][Column] in ["A","B","S","D","P"]:
        print(" ", end="")                
      else:
        print(Board[Row][Column], end="")
      if Column != 9: # Prints pretty lines between each tile
        print(" | ", end="")
    print()
       
def DisplayMenu():
  """
  Display the main menu.
  Not many gripes except for the blank prints.
  """
  print("MAIN MENU")
  print()
  print("1. Start new game")
  print("2. Load training game")
  print("9. Quit")
  print()
    
def GetMainMenuChoice():
  # Gets choice from the main menu
  print("Please enter your choice: ", end="")
  # Can't be sure an input is an int but it casts anyway
  # yolo
  Choice = int(input())
  print()
  return Choice

def PlayGame(Board, Ships):
  """
  Plays the game. Basically just calls things that call things
  in a loop that finishes if the game is over.
  I don't think this game has a lose state?? You just keep 
  playing until you win. 
  Not much to comment about with inlines.
  """
  GameWon = False
  while not GameWon:
    PrintBoard(Board)
    MakePlayerMove(Board, Ships)
    GameWon = CheckWin(Board)
    if GameWon:
      print("All ships sunk!")
      print()

if __name__ == "__main__":
  """
  Main game stuff.
  """
  TRAININGGAME = "Training.txt" # Constant with a local path to a file
  MenuOption = 0  # Initialise
  while not MenuOption == 9:  # While the player is not quitting
    Board = SetUpBoard()      # Set up the board
    # Load the Ships structure. This could easily be a constant but whatever.
    Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2]]
    DisplayMenu()     # Displays the options
    MenuOption = GetMainMenuChoice()  # Gets the choice from the main menu
    if MenuOption == 1:               # Play a normal game
      PlaceRandomShips(Board, Ships)
      PlayGame(Board,Ships)
    if MenuOption == 2:               # Play a game with a predefined board
      LoadGame(TRAININGGAME, Board)
      PlayGame(Board, Ships)   

"""
I think that all of this code is really messy and badly put together.
It is not robust at all, and usually very unsafe.

Also, why does it not use pep8? It's not that hard.
"""