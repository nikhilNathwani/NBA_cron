from util import *

gametimeDataFn= "gametimeData.txt"
delay= 5 #schedule task for [delay] hrs after game begins


#appends lines of the form "[time] [am/pm] [day] [month]" into
#the file entitled 'gametimeData_ET.txt' for each game played
#on the given month and day, of the season ending in year "termYear"
def downloadGametimeData(month,day,termYear):
	#get gamtimes in the form (time,day,month)
	gts= scrapeGametimesForDay(month, day, termYear)
	#remove duplicate gametimes
	dedup= []
	for i in gts:
	  if i not in dedup:
	    dedup.append(i)
	#append to 'gametimeData_ET.txt' in format specified
	#in the pre-function comment
	with open('gametimeData_ET.txt','a') as f:
		for d in dedup:
			f.write(d[0][:d[0].rfind(' ')]+" "+str(d[1])+" "+str(d[2]))
			f.write('\n')



#scrapes NBA.com for game times on given month & day
#only needed until data is downloaded locally via 
#the downloadGametimeData function above
def scrapeGametimesForDay(month,day,termYear):
	#generate the proper URL for the given month, day, and termYear
	yr= termYear if month<9 else termYear-1
	urlAppend=str(yr)+str(month).zfill(2)+str(day).zfill(2)
	site= "http://www.nba.com/gameline/"+urlAppend

	#grab blocks of HTML within which the gametimes are contained.
	#for past games, gametimes live in a div with class "nbaFnlStatTxSm"
	#for future games, they live in h2's in a div w/ class "nbaPreMnStatus"
	soup= grabSiteData(site)
	times= soup.findAll("div",{"class" : "nbaFnlStatTxSm"})

	#for past games, "times" will be non-empty at this point, so return it
	if times!=[]:
		times= [elem.text.encode("ascii","ignore") for elem in times]
		return [(time,day,month) for time in times]

	#for future games, populate & return the "times" list
	timeDivs= soup.findAll("div",{"class" : "nbaPreMnStatus"})
	for div in timeDivs:
		parts= [x.text.encode("ascii","ignore") for x in div.findAll("h2")]
		times.append(parts[0]+" " +parts[1])
	return [(time,day,month) for time in times]



#reads from local data if available, else goes to web by
#relying on scrapeGametimesForDay function 
def getGametimesForDay(month,day,termYear,fn):
	if fn=="":
		return scrapeGametimesForDay(month,day,termYear)
	else:
		times= []
		f= open(fn,"r")
		line = f.readline()
		while line: #continues until no lines are left
			hr,am_pm,day,month= line.split() 
			times.append((hr+" "+am_pm + " et",day,month))
			line = f.readline() #read next line
		f.close() #close the file
		return times



#convert a game time of the form "xx:xx [AM/PM] EST" into crontab format: 
#"[minute] [hr] [day] [month] [day-of-week] [command-line-to-execute]"
#timeStr is of the format (time,day,month), from scrapeGametimesForDay function
def reformatGametime(timeStr):
	time,day,month= timeStr
	#remove "et", i.e. "eastern time", from time
	time= time[:time.rfind(' ')] 
	##hhmm is the time in hh:mm format, and isAfternoon is "am" or "pm"
	hhmm,isAfternoon= time.split()  
	#break hhmm into hour and minute. I str(int()) stuff to remove leading 0's
	hour,minute= [str(int(x)) for x in hhmm.split(':')] 
	#switch hour to military time, which is necessary for crontab
	hour= str(int(hour)+delay+12) if isAfternoon else str(int(hour+delay))
	#combine everything into crontab format
	return minute+' '+hour+' '+str(day)+' '+str(month)+' * '

