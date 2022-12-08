from os.path import realpath

output = 0

#Read the input file and see if the jobs overlap
with open(realpath('.\\Day 04\\input.txt'),'r') as f:
	for line in f:
		jobs = line.split(',')
		job_0 = jobs[0].split('-')
		job_1 = jobs[1].split('-')

		if int(job_0[0])<= int(job_1[0]) and int(job_0[1]) >= int(job_1[1]):
			# Job 0 starts before/at AND ends after/at job 2
			output += 1
		elif int(job_1[0])<= int(job_0[0]) and int(job_1[1]) >= int(job_0[1]):
			#Job 1 starts at/before Job 0 AND ends at/after Job 0
			output += 1
		
print(output)
