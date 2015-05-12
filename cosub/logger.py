#!/usr/bin/env python

import os
import csv
from datetime import datetime
import urllib 
import urllib2

name = "history.csv"
fields = ["Time","Action","Data"]

logfile = None

writer = None
reader = None


def setup():
	global logfile
	## create file if it doesn't exist
	if not os.path.isfile(name):
	 	logfile = open(name, 'w')
	 	writer = csv.writer(logfile, delimiter=',', quotechar='"')
	 	writer.writerow(fields)
	 	logfile.close()

def write(d):
	logfile = open(name, 'a')
	d['Time'] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
	writer = csv.DictWriter(logfile, fieldnames=fields)
	writer.writerow(d)
	logfile.close()

def read():
	logfile = open(name, 'r')
	reader = csv.DictReader(logfile, fieldnames=fields)
	logfile.close()
	return "TODO"

def write_server(d):
	d['Time'] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
	post_d = urllib.urlencode({"data":d})
	path = d['Data']['server_log_path']

	req = urllib2.Request(path, post_d)
	response = urllib2.urlopen(req)