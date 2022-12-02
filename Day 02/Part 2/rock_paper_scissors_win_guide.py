# Calculate total points from input
# Key:
# A - Opponent Rock         X - Player LOSE
# B - Opponent Paper        Y - Player DRAW
# C - Opponent Scissors     Z - Player WIN

# Points:
# Player Rock - 1     Player Paper - 2       Player Scissors - 3
# WIN - 6   LOSE - 0    DRAW - 3

from os.path import realpath
#Enumerate WIN/DRAW/LOSE points
win = 6
draw = 3
# Don't need to add points in the event of a loss, so no need to enumerate it


total_points = 0

with open(realpath('Day 02\\input.txt'),'r') as f:
    for line in f:
        match line[2]:
           case 'X': # Player LOSE
               match line[0]:
                   case 'A': # Opponent Rock
                       # Play Scissors to lose
                       total_points += 3 # Shape points
                   case 'B': # Opponent Paper
                       # Play Rock to lose
                       total_points += 1 # Shape points
                   case 'C': # Opponent Scissors
                       # Play Paper to lose
                       total_points += 2 # Shape points
               # No points for losing
           case 'Y': # Player DRAW
               match line[0]:
                   case 'A': # Opponent Rock
                       # Play Rock to draw
                       total_points += 1 # Shape points
                   case 'B': # Opponent Paper
                       # Play Paper to draw
                       total_points += 2 # Shape points
                   case 'C': # Opponent Scissors
                       # Play Scissors to draw
                       total_points += 3 # Shape points
               total_points += draw
           case 'Z': # Player WIN
               match line[0]:
                   case 'A': # Opponent Rock
                       # Play Paper to draw
                       total_points += 2 # Shape points
                   case 'B': # Opponent Paper
                       # Play Scissors to draw
                       total_points += 3 # Shape points
                   case 'C': # Opponent Scissors
                       # Play Rock to draw
                       total_points += 1 # Shape points
               total_points += win

print(total_points)