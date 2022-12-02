#I'm tired of forgetting this part

from os.path import realpath

input = []
output = None

#Read the input file to a local list of the lines.
with open(realpath('Day 02\\input.txt'),'r') as f:
    for line in f:
        input.append(line)

# MY CODE HERE

# Q: Why not just process each line as it's being read instead of reading all the lines,
#    then re-iterating over the list?

# A: I definitely could do that.  This is just a template. Until I know what the challenge
#    is, I don't know how I'll want to go about processing the input.

print(output)