from os.path import realpath
import pdb

input = []
output = 0

#Read the input file to a local list of the lines.
with open(realpath('input.txt'),'r') as f:
	for line in f:
		pdb.set_trace()
		jobs = line.split(',')
		job_0 = jobs[0].split('-')
		job_1 = jobs[1].split('-')

		if int(job_0[1]) - int(job_0[0]) > int(job_1[1]) - int(job_1[0]):
			#job_0 covers more space than job_1
			if job_0[0] <= job_1[0] and job_0[1] >= job_1[1]:
				#job_0 starts before and ends after job_1
				output += 1
		else:
			#job_1 covers more space than job_0, or they have the same space
			if job_1[0] <= job_0[0] and job_1[1] >= job_0[1]:
				#job_1 starts before and ends after job_0
				output += 1
print(output)
