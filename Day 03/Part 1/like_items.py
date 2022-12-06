from os.path import realpath

input = []
output = 0

#Read the input file to a local list of the lines.
with open(realpath('input.txt'),'r') as f:
	for line in f:
		#Split line in two halves
		line_1 = line[:int(len(line)/2)]
		line_2 = line[int(len(line)/2):]
        
		#For each letter in half 1, check if it's in half 2
		for char in line_1:
			if char in line_2:
				if char.islower():
					output += (ord(char) - 96)
				else:
					output += (ord(char) - 38)
				break


print(output)
