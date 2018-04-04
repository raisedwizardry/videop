import os
import sys
import re
from plexapi.server import PlexServer
from config import Config

class show:
	
	def __init__(self, directory, filename):
		self.directory=directory
		self.filename=filename
		seasonpattern = re.compile(r'^[S,s]\d\d[E,e]\d\d$') #S03E20
		self.dirfilename = str(self.directory) + '/' str(self.filename)
		self.filenamenoext  = self.filename.split('.ts')[0]
		split=str.split(self.filenamenoext)
		for i in range(0, len(split)): 
			if seasonpattern.match(split[i]) is not None:
				self.seasoninfo=split[i]
				self.epseason = int(self.seasoninfo[1:3])
				self.epnum = int(self.seasoninfo[4:])
				titled=" ".join(split[:i])
				self.epshow= re.sub('\s[(]\d\d\d\d[)]\s-','',str(titled))

	def match(self):
		plex = PlexServer(str(Config.PLEX_URL), str(Config.PLEX_TOKEN))
		for video in plex.search(self.epshow):
			#add logic to check for multiple search results
			if video.TYPE=='show':
				lama=video.episode('',self.epseason,self.epnum)
				self.plexdirfilename=lama.locations
				
				#add logic to compare filename with plex found filename maybe use len(lama.locations))
				self.epname = '%s.%s.%s' % (lama.show().title, lama.seasonEpisode, lama.title)

		#create a working directory
		#create a log file
		#move target file into directory
