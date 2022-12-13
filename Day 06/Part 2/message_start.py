#I'm tired of forgetting this part

from os.path import realpath

# We'll just use the output to track the pointer number what ever it's called
output = 14
start_found = False
#Read the input file to a local list of the lines.
with open(realpath('Day 06\\input.txt'),'r') as f:
    for line in f:
        while not start_found:
            check_str = line[output-14:output]
            for char in check_str:
                num = check_str.count(char)
                if num > 1:
                    output += 1
                    break
            else:
                start_found = True

print(output)