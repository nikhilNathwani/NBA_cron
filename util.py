from bs4 import BeautifulSoup
import urllib2

monthToNumDays={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
allstar=[(2,13),(2,14),(2,15),(2,16),(2,17),(2,18)]

#fetches beautifulsoup-formatted data from given url
def grabSiteData(url):
    usock= urllib2.urlopen(url)
    data= usock.read()
    usock.close()
    return BeautifulSoup(data)



#writes data to rows file (helpful for script to use use the local data, which
#is much faster than unnecessariy querying the web on repeated runs).
def writeRowsToFile(rows,fn):
	with open(fn,'w') as f:
		for r in rows:
			f.write(r)
			f.write('\n')
	return


#returns list of (month,day) tuples of days in which games were played
#currently, days within the all star break are hardcoded as a global var
#initDay and initMonth comprise the date of the season-opening game, while
#termDay, termMonth, and termYear comprise the date of the season-ending game
def getMonthDayTuples(initDay, initMonth, termDay, termMonth, termYear):
	global monthToNumDays
	#account for leap years 
	if termYear%4==0: monthToNumDays[2]= 29
	tups= []
	currMonth= initMonth-1 #forcing 0-indexing
	currDay= initDay-1
	while currMonth+1!=termMonth or currDay+1!=termDay:
		tups.append((currMonth+1,currDay+1)) 
		#increment month at the end of the month and set day to 0
		#else just increment day
		if currDay+1==monthToNumDays[currMonth+1]:
			currMonth= (currMonth+1)%12
			currDay= 0
		else: 
			currDay= (currDay+1)%(monthToNumDays[currMonth+1])
	#append the final day of the season
	tups.append((currMonth+1, currDay+1))
	#remove days on which no games are player (for now, 
	#hard-coded days of all-star weekend into "allstar" list)
	tups= [x for x in tups if x not in allstar]
	return tups