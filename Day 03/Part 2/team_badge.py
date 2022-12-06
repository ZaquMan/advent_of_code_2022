from os.path import realpath

input = []
output = 0

#Read the input file to a local list of the lines.
with open(realpath('input.txt'),'r') as f:
	for line in f:
		input.append(line)

for x in range(0,int(len(input)/3)):
	elf_0 = input.pop(0)
	elf_2 = input.pop(0)
	elf_3 = input.pop(0)
	
	dups = []
	for char in elf_0:
		if char in elf_2:
			dups.append(char)
	for char in dups:
		if char in elf_3:
			if char.islower():
				output += (ord(char) - 96)
			else:
				output += (ord(char) - 38)
			break

print(output)
