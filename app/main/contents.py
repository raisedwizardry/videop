import os
import subprocess
import sys

class filelist():
	files=list()
	recordings = str("/mnt/d/Stuff/plex-recordings/A.P. BIO/Season 01")
	for root, directories, filenames in os.walk(recordings):
		for filename in filenames:
			files.append(os.path.join(root,filename))