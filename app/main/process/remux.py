import sys
import os.path
import subprocess
import xml.dom
import datetime
import re
from subprocess import check_output
from .chap import chap

class remux:
	
	def __init__(self, prop):
		self.houseKeep(prop)
		#self.createSrt(prop)
		#self.demuxVideo(prop)
		#self.createChap(prop)
		#self.muxVideo(prop)
		
	def houseKeep(self, prop):
		subprocess.call(["mkdir", str(prop.archivedir)])
		#subprocess.call(["cp",
		#	str(prop.dirfilename),
		#	str(prop.archivedir)]) #copy original file to mux dir

	def createSrt(self, prop):
		subprocess.call(["/opt/ccextractor/linux/ccextractor",
			str(prop.archivedir)+str(prop.filename), "-o", str(prop.archivedirfilename)+".srt"]) #runccextractor on copied file in mux dir
		subprocess.call(["rm", str(prop.archivedir)+str(prop.filename)]) #remove extracted copy file from the mux dir
		subprocess.call(["mv", str(prop.dirfilename), str(prop.episode)])

	def demuxVideo(self, prop):
		theids=self.getId(prop.episode)
		subprocess.call(["projectx", 
			"-demux", str(prop.episode),
			"-id", str(theids),
			"-out", str(prop.archivedir),
			"-name", str(prop.epname)+"."])

	def createChapter(self, prop):
		duration=self.getDuration(prop.episode)
		chap(duration, prop.archivedirfilename)

	def muxVideo(self, prop):
		fps=self.getFrame(str(prop.episode))
		mkvfps="0:"+str(fps)+"fps"
		subprocess.call(["mkvmerge",
			"-o", str(prop.archivedirfilename)+"-notrans.mkv", 
			"--default-duration",
			str(mkvfps), "--chapters",
			str(prop.archivedirfilename)+".txt",
			str(prop.archivedirfilename)+".m2v",
			str(prop.archivedirfilename)+".ac3",
			str(prop.archivedirfilename)+".srt"])

	def getId(self, filename):
		vid=check_output(["mediainfo", "--Inform=Video;%ID%\\n", str(filename)])
		vid=vid.decode("utf-8").strip('\n').split('\n')
		aid=check_output(["mediainfo", "--Inform=Audio;%ID%\\n", str(filename)])
		aid=aid.decode("utf-8").strip('\n').split('\n')
		theids=str(vid[0]) + "," + str(aid[0])
		return theids

	def getFrame(self, filename):
		out= subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0",
			"-show_entries", "stream=r_frame_rate", "-of", "default=noprint_wrappers=1:nokey=1",
			str(filename)])
		return str(out.decode("utf-8").split('\n')[0])

	def getDuration(self, filename):
		duration=check_output(["mediainfo", "--Inform=General;%Duration/String3%\\n", str(filename)])
		duration=duration.decode("utf-8").strip('\n').split('\n')
		return duration[0]