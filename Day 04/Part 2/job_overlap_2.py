from os.path import realpath

output = 0

#Read the input file and see if the jobs overlap at all
with open(realpath('.\\Day 04\\input.txt'),'r') as f:
	for line in f:
		jobs = line.split(',')
		job_0 = jobs[0].split('-')
		job_1 = jobs[1].split('-')

		if int(job_0[0]) < int(job_1[0]) and int(job_0[1]) < int(job_1[0]):
			# 123...  Job 0 is completely
			# ...456  before Job 1
			continue
		elif int(job_1[0]) < int(job_0[0]) and int(job_1[1]) < int(job_0[0]):
			# ...456  Job 0 is completely
			# 123...  after Job 1
			continue
		output += 1

print(output)