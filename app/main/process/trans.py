import sys
import os.path
import subprocess
import xml.dom
import datetime
import re
from subprocess import check_output
from pytvdbapi import api
import omdb

def getWidth(filename):
	width=check_output(["mediainfo", "--Inform=Video;%Width%\\n", str(filename)])
	return str(width.decode("utf-8").strip('\n').split('\n')[0])

def getRate(filename):
	out= subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0",
		"-show_entries", "stream=r_frame_rate", "-of", "default=noprint_wrappers=1:nokey=1",
		str(filename)])
	fps=str(out.decode("utf-8").split('\n')[0])
	rate= fps.split('/')
	rate= str(format(float(rate[0])/float(rate[1]),'.5g'))
	return rate

def getFormat(rate, width):
	if float(rate) == 29.97:
		if int(width) > 1280:
			format= "fullthirty"
		elif int(width) == 1280:
			format= "hdthirty"
		elif int(width) < 1280:
			format= "sdthirty"
	elif float(rate) == 59.94:
		if int(width) > 1280:
			format= "fullsixty"
		elif int(width) == 1280:
			format= "hdsixty"
		elif int(width) < 1280:
			format= "sdsixty"
	else:
		format="strange"
	return format