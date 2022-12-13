#I'm tired of forgetting this part

from os.path import realpath

# We'll just use the output to track the pointer number what ever it's called
output = 4
start_found = False
#Read the input file to a local list of the lines.
with open(realpath('Day 06\\input.txt'),'r') as f:
    for line in f:
        while not start_found:
            check_str = line[output-4:output]
            if check_str[0] in check_str[1:]:
                #char repeats so this is not the start tag
                output += 1
            elif check_str[1] in check_str[2:]:
                #char repeats so this is not the start tag
                output += 1
            elif check_str[2] in check_str[3:]:
                #char repeats so this is not the start tag
                output += 1
            else:
                #There are no repeating chars
                break


print(output)