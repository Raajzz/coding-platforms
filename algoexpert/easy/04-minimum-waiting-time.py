# METHOD 1 | To find the lease possible waiting time we have to put the 

def minimumWaitingTime(queries):
	queries = sorted(queries)
	sum_of_time = 0
	waiting_time = 0
	if(len(queries) == 1):
		return waiting_time
	else:
		for idx in range(len(queries)-1):
			sum_of_time += queries[idx]
			waiting_time += sum_of_time
		return waiting_time

print(minimumWaitingTime([3,2,1,2,6]))