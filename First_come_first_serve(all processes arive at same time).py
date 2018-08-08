#process = {'P1': 21,'P2':3,'P3':6,'P4':2}   Example
process = {}  # Process with Burst time
no_processes = int(input())  # Enter total number of processes

for i in range(no_processes):    
	value = int(input())
	process["P"+str(i)] = value

sol = {}    
sum = 0
for i in process:
	sol[i] = []
	sol[i].append(sum)
	sol[i].append(sum + process[i])
	sum = sol[i][1]

avrg_wait = 0
avrg_turn = 0
print("\n")
print("\tWaiting time of the process(Arrival time same): ")
print("_"*65)
print("processes\t| Burst time\t|Waiting time\t|Turn Around time ")
print("_"*65)
for i in process:
	print("\t{0}\t|\t{1}\t|\t{2}\t|\t{3}\t|".format(i,process[i],sol[i][0],(process[i]+sol[i][0])))
	avrg_wait = avrg_wait + sol[i][0]
	avrg_turn = avrg_turn + (process[i]+sol[i][0])
print("_"*65)
print("Average waiting time : {0}".format(avrg_wait/no_processes))
print("Average Turn around time : {0}".format(avrg_turn/no_processes))
