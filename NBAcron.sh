#!/bin/bash

echo $@
python NBAcron.py $@
crontab NBA_crontab.txt