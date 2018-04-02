import os
import sys
import re
from plexapi.server import PlexServer

class show:
	
	def __init__(self, directory, filename):
		self.directory=directory
		self.filename=filename
		seasonpattern = re.compile(r'^[S,s]\d\d[E,e]\d\d$') #S03E20
		self.dirfilename = str(self.directory) + str(self.filename)
		self.filenamenoext  = self.filename.split('.ts')[0]
		split=str.split(self.filenamenoext)
		for i in range(0, len(split)): 
			if seasonpattern.match(split[i]) is not None:
				self.seasoninfo=split[i]
				self.season = int(self.seasoninfo[1:3])
				self.episode = int(self.seasoninfo[4:])
				titled=" ".join(split[:i])
				self.title= re.sub('\s[(]\d\d\d\d[)]\s-','',str(titled))

	def match(self):
		baseurl = 'http://mordor:32400'
		token = '357ny2ronBoJNay5iHPh'
		plex = PlexServer(baseurl, token)
		for video in plex.search(self.title):
			#add logic to check for multiple search results
			if video.TYPE=='show':
				lama=video.episode('',self.season,self.episode)
				#add logic to compare filename with plex found filename maybe use len(lama.locations))
				self.newfilename = '%s.%s.%s' % (lama.show().title, lama.seasonEpisode, lama.title)

		#create a working directory
		#create a log file
		#move target file into directory
