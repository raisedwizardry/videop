#!/usr/bin/python3

import sys
import os.path
import subprocess
import xml.dom
import datetime
import re
from subprocess import check_output

def houseKeep():
	subprocess.call(["mkdir", str(fill.archivedir)])
	if os.path.isfile(str(fill.archivedir)+fill.filename) is False:
		subprocess.call(["cp",
			str(fill.dirfilename),
			str(fill.archivedir)]) #copy original file to mux dir

def createSrt():
	subprocess.call(["/opt/ccextractor/linux/ccextractor",
		str(fill.dirfilename),
		"-o", str(fill.epname)]) #runccextractor on copied file in mux dir
	subprocess.call(["rm", str(fill.archivedirfilename)+".ts"]) #remove extracted copy file from the mux dir
	subprocess.call(["mv", str(fill.dirfilename), str(fill.archivedir)])

def demuxVideo():
	theids=getId(fill.episode)
	subprocess.call(["projectx", 
		"-demux", str(fill.episode),
		"-id", str(theids),
		"-out", str(fill.archivedir),
		"-name", str(fill.epname)])

def muxVideo():
	fps=getFrame(str(fill.episode))
	mkvfps="0:"+str(fps)+"fps"
	subprocess.call(["mkvmerge",
		"-o", str(fill.archivedirfilename)+"-notrans.mkv", 
		"--default-duration",
		str(mkvfps),
		str(fill.archivedirfilename)+".m2v",
		str(fill.archivedirfilename)+".ac3"])

def getId(filename):
	vid=check_output(["mediainfo", "--Inform=Video;%ID%\\n", str(filename)])
	vid=vid.decode("utf-8").strip('\n').split('\n')
	aid=check_output(["mediainfo", "--Inform=Audio;%ID%\\n", str(filename)])
	aid=aid.decode("utf-8").strip('\n').split('\n')
	theids=str(vid[0]) + "," + str(aid[0])
	return theids

def getFrame(filename):
	out= subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0",
		"-show_entries", "stream=r_frame_rate", "-of", "default=noprint_wrappers=1:nokey=1",
		str(filename)])
	return str(out.decode("utf-8").split('\n')[0])

