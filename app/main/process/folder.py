import sys
import os.path
import subprocess
import xml.dom
import datetime
import re
from subprocess import check_output
from .contents import createChap

def houseKeep():
	subprocess.call(["mkdir", str(fill.archivedir)])
	subprocess.call(["cp",
		str(fill.dirfilename),
		str(fill.archivedir)]) #copy original file to mux dir

def createSrt():
	subprocess.call(["/opt/ccextractor/linux/ccextractor",
		str(fill.archivedir)+str(fill.filename), "-o", str(fill.archivedirfilename)+".srt"]) #runccextractor on copied file in mux dir
	subprocess.call(["rm", str(fill.archivedir)+str(fill.filename)]) #remove extracted copy file from the mux dir
	subprocess.call(["mv", str(fill.dirfilename), str(fill.episode)])

def demuxVideo():
	theids=getId(fill.episode)
	subprocess.call(["projectx", 
		"-demux", str(fill.episode),
		"-id", str(theids),
		"-out", str(fill.archivedir),
		"-name", str(fill.epname)+"."])

def createChapter():
	duration=getDuration(fill.episode)
	createChap(duration, fill.archivedirfilename)

def muxVideo():
	fps=getFrame(str(fill.episode))
	mkvfps="0:"+str(fps)+"fps"
	subprocess.call(["mkvmerge",
		"-o", str(fill.archivedirfilename)+"-notrans.mkv", 
		"--default-duration",
		str(mkvfps), "--chapters",
		str(fill.archivedirfilename)+".txt",
		str(fill.archivedirfilename)+".m2v",
		str(fill.archivedirfilename)+".ac3",
		str(fill.archivedirfilename)+".srt"])

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

def getDuration(filename):
	duration=check_output(["mediainfo", "--Inform=General;%Duration/String3%\\n", str(filename)])
	duration=duration.decode("utf-8").strip('\n').split('\n')
	return duration[0]