import os
import subprocess
import sys

class filelist:
	def showrecord(self):
		filelist=list()
		recordings = str("/mnt/d/Stuff/videop-dev-folder/Video/DVR/processing/plex-recordings")
		for root, directories, filenames in os.walk(recordings):
			directories[:] = [d for d in directories if not d.startswith('.')]
			for filename in filenames:
				filelist.append(os.path.join(root,filename))
		toencode=list()
		for i in range(0, len(filelist), 1):
			if filelist[i].lower().endswith('.ts'):
				toencode.append(filelist[i])
		return toencode

