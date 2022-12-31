from os.path import realpath

output = 0

# A directory is a dictionary, right?
# EX
# - / (dir)
#   - a (dir)
#    - e (dir)
#      - i (file, size=584)
# = {'/': {'a': {'e': {'i': 584}}}}

file_tree = {'/': {}}
active_dir = file_tree['/']

def up_dir(tree):
    if active_dir in tree.values():
        # Active Dir is already at the top of the tree
        return dir
    for v in tree.values():
        return up_dir(v)

#Read the input file to a local list of the lines.
with open(realpath('Day 07\\input.txt'),'r') as f:
    for line in f:
        input = line.split()
        if input[0] == '$':
            # line is a command
            match input[1]:
                case 'cd':
                    match input[2]:
                        case '..':
                            # Go up 1 dir
                            up_dir(file_tree)
                            continue
                        case '/':
                            active_dir = file_tree['/']
                        case _:
                            if input[2] in active_dir:
                                active_dir = active_dir[input[2]]
                            else:
                                raise('Bad input')
                case 'ls':
                    # There isn't actually anything to do
                    continue
        elif input[0].isnumeric():
            # Files start with their size
            active_dir[input[1]] = int(input[0])
        elif input[0] == 'dir':
            # Dirs start with 'dir'
            active_dir[input[1]] = {}




print(output)