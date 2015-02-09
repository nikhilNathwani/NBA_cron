NBA_cron
==========

This tool is a task scheduler that automatically runs scripts after each NBA game. For instance, if you're maintaining a database of NBA game data and have scripts to refresh your data from the web, NBA_cron will enable you to automatically have that script run after new data is made available online. 

NBA_cron is backed by [cron](http://en.wikipedia.org/wiki/Cron), a time-based job scheduler for Unix-based/Unix-like systems (meaning users of this tool are required to have such a system). 

##How to run the script
1) **Get the files**, which can be done by downloading the zip file of this repo on GitHub

2) **Run the code** by invoking the bash script, i.e. by entering the following into your terminal:
```
./NBAcron.sh [script to schedule]
```
If you get some sort of "Permission denied" message, try entering the following before running the above bash script:
```
sudo chmod +x
```

If you want to run the code directly instead of using the bash script, then enter the following into you terminal:
```
python NBAcron.py [script to schedule]
crontab nba_crontab.txt
```

When the tool's finished executing, the specified script will be scheduled to run 5 hours after each NBA game begins (a baked-in delay to allow for online data to update -- experimentation is needed to ensure that 5 hours is a good amount of time) for the entirety of the regular season (postseason games will be added to the crontab when playoff series schedules are released). 

A couple of quick notes:
- All gametimes in the crontab are in Eastern Time
- Any file that is referred to in your script must be specified with its full path (a guideline required by cron for security reasons)


##Next steps
- Perform some experimentation to determine an appropriate amount of delay after each game before new data becomes available online.
- Add postseason games to crontab when playoff series schedules are released
- Programmatically scrape off-days (currently hard-coded) to enable scaling to future seasons
