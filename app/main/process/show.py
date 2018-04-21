import os
import sys
import re
import arrow
from plexapi.server import PlexServer
from config import Config
from ...models import Listed
from ... import db

class show:	
	
	def __init__(self, directory, filename):
		self.directory=directory
		self.filename=filename
		seasonpattern = re.compile(r'^[S,s]\d\d[E,e]\d\d$') #S03E20
		self.dirfilename = str(self.directory) + '/' + str(self.filename)
		self.filenamenoext  = self.filename.split('.ts')[0]
		split=str.split(self.filenamenoext)
		for i in range(0, len(split)): 
			if seasonpattern.match(split[i]) is not None:
				self.seasoninfo=split[i]
				self.epseason = int(self.seasoninfo[1:3])
				self.epnum = int(self.seasoninfo[4:])
				titled=" ".join(split[:i])
				self.epshow= re.sub('\s[(]\d\d\d\d[)]\s-','',str(titled))

	@property
	def epname(self):
		plex = PlexServer(str(Config.PLEX_URL), str(Config.PLEX_TOKEN))
		for video in plex.search(self.epshow):
			#add logic to check for multiple search results
			
			if video.TYPE=='show':
				lama=video.episode('',self.epseason,self.epnum)
				plexdirfilename=lama.locations
				#logic to compare filename with plexapi found filename
				#if not plexdirfilename:
					# add conditon to handle this
				#if len(plexdirfilename)>1:
					# add condition to handle this
				if len(plexdirfilename)>0:
					plexdirfilename=lama.locations[0]
					if self.filename == os.path.basename(plexdirfilename): #if str(plexdirfilename) == str(self.dirfilename)
						return '%s %s %s' % (lama.show().title, lama.seasonEpisode, lama.title)
				
	def commit(self):
		writedb=Listed( directory=self.directory, dirfilename=self.dirfilename, 
						filename=self.filename, filenamenoext=self.filenamenoext,
						epnum=self.epnum, epseason=self.epseason,
						epshow=self.epshow, epname=self.epname)
		db.session.add(writedb)
		db.session.commit()
	
	def isplaying(self):
		plex = PlexServer(str(Config.PLEX_URL), str(Config.PLEX_TOKEN))
		playing= plex.isPlayingMedia(includePaused=True)
		
	def retrieve(self, dirfilename):
		entry=Listed.query.filter_by(dirfilename=str(dirfilename)).first()
		if entry:
			self.directory = entry.directory
			self.dirfilename = entry.dirfilename
			self.filename = entry.filename
			self.filenamenoext = entry.filenamenoext
			self.epnum = entry.epnum
			self.epseason = entry.epseason
			self.epshow = entry.epshow
			self.epname = entry.epname
	
	def setarchive(self, archivedir):
		today= arrow.utcnow().format('YYYYMMDD HHmmss')
		self.archivedir = str(archivedir) + str(today) + " " + str(self.epname) + "/"
		self.archivedirfilename= str(self.archivedir) + str(self.epname)
		self.episode= str(self.archivedirfilename)+".ts"
		

		#create a working directory
		#create a log file
		#move target file into directory
