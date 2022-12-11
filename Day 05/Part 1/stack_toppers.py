from os.path import realpath

output = ''

input_stage = 1

stacks = [[], [], [],   # Stack 0 - 2
		  [], [], [],   # Stack 3 - 5
		  [], [], []]   # Stack 6 - 8

#Maps the stack to it's number in the input string
stack_key = {0:1, 1:5, 2:9, 3:13, 4:17, 5:21, 6:25, 7:29, 8:33}

#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 
#0123456789

#Read the input file and see if the jobs overlap
with open(realpath('.\\Day 05\\input.txt'),'r') as f:
	for line in f:
		if line.strip() == '1   2   3   4   5   6   7   8   9':
			#Reading in the stacks is done
			input_stage = 0
			#Confirm stacks by printing them
			print(stacks)
			continue
		if input_stage:
			for k,v in stack_key.items():
				#Build the stacks.  Since reading is done top down,
				#each new line goes beneath the last.
				if line[v] != ' ':
					stacks[k].insert(0,line[v])
			continue
		else:
			cmd_vars = line.split()
			#cmd_vars[1]       - How many
			#(cmd_vars[3] - 1) - From where
			#(cmd_vars[5] - 1) - To where
			if len(cmd_vars):
				#Conversion time
				cmd_vars[1] = int(cmd_vars[1])
				cmd_vars[3] = int(cmd_vars[3])
				cmd_vars[5] = int(cmd_vars[5])
				while cmd_vars[1] > 0:
					box = stacks[(cmd_vars[3]-1)].pop()
					stacks[(cmd_vars[5]-1)].append(box)
					cmd_vars[1] -= 1

for stack in stacks:
	output += stack[-1]

print(output)
