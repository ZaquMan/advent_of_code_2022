# Calculate total points from input
# Key:
# A - Opponent Rock         X - Player Rock
# B - Opponent Paper        Y - Player Paper
# C - Opponent Scissors     Z - Player Scissors

# Points:
# X - 1     Y - 2       Z - 3
# WIN - 6   LOSE - 0    DRAW - 3

from os.path import realpath
#Enumerate WIN/DRAW/LOSE points
win = 6
draw = 3
# Don't need to add points in the event of a loss, so no need to enumerate it

total_points = 0
with open(realpath('Day 02\\input.txt'),'r') as f:
    for line in f:
        total_points += ord(line[2]) - 87 # Add points for player's shape
        # Python 3.10 finally added switch/case style conditional statements!
        match line[0]:
            case 'A': # Opponent Rock
                if line[2] == 'Y': # Player Paper
                    total_points += win
                elif line[2] == 'X': # Player Rock
                    total_points += draw
            case 'B': # Opponent Paper
                if line[2] == 'Z': # Player Scissors
                    total_points += win
                elif line[2] == 'Y': # Player Paper
                    total_points += draw
            case 'C': # Opponent Scissors
                if line[2] == 'X': # Player Rock
                    total_points += win
                elif line[2] == 'Z': # Player Scissors
                    total_points += draw

print(total_points)