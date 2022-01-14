# This is an assignment for cse210, week 2.
# Tic-Tac-Toe
# Daniel Harris

"""Tic-Tac-Toe is played according to the following rules.

1. The game is played on a grid that is three squares by three squares.
2. Player one uses x's. Player two uses o's.
3. Players take turns putting their marks in empty squares.
4. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
5. If all nine squares are full and neither player has three in a row, the game ends in a draw."""

def main():
  # Functions go here
  player = current_player('')



def current_player(current_player):
  #determine who is the current player
  if current_player == '' or current_player == 'o':
    return 'x'
  else:
    return 'o'

if __name__=="__main__":
  main()