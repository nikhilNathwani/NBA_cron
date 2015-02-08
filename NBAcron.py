import time
import sys
from scrape import *

#writes a crontab to "nba_crontab.txt", with task times for each NBA
#game in the season that spans from the dates specified. Note that this
#is not a full crontab as a task needs to be defined. This can be 
#accomplished simply via the addTaskToCrontab function.
def genCronJob(initDay, initMonth, termDay, termMonth, termYear, task):
	task= ' '.join(task) #combine task into one string

	#get dates on which NBA games are played in a (month,day) list
	dates= getMonthDayTuples(initDay, initMonth, termDay, termMonth, termYear)

	#get list of gametimes for each game on each day in (time,day,month) format
	gts= [getGametimesForDay(x,y,termYear,gametimeDataFn) for (x,y) in dates]
	flat= [item for sublist in gts for item in sublist]

	#stable deduplication of gametime list (i.e. sort order is maintained)
	dedup= []
	for i in flat:
	  if i not in dedup:
	    dedup.append(i)

	#convert (time,day,month) tuples into crontab schedule format, and 
	#write them to 'nba_crontab.txt'
	reforms= map(reformatGametime,dedup)
	writeRowsToFile(reforms,'nba_crontab.txt')
	addTaskToCrontab('nba_crontab.txt',task)
	return



#crontab_fn is the filename of the crontab to add the task to
#scriptToRun is a string containing the script corresponding to the task
def addTaskToCrontab(crontab_fn, task):
	with open(crontab_fn, 'r') as f:
		#last character of x is a \n, so need to remove before adding task
	    rows=[''.join([x[:-1], task, '\n']) for x in f.readlines()]

	with open(crontab_fn, 'w') as f:
	    f.writelines(rows) 



if __name__ == "__main__":
	start= time.time()
	genCronJob(28, 10, 15, 4, 2015, sys.argv[1:])
	print "Time taken:", time.time()-start
