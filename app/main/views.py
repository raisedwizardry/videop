import os
import subprocess
import sys
import ntpath
from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import Listed,Userconfig
from . import main
from .forms import PlexForm
from .contents import show

@main.route('/', methods=['GET', 'POST'])
def index():
	form = PlexForm()
	directory = Userconfig.query.get(2)

	if form.validate_on_submit():
		#add check for input already in database and everwrite it if there. maybe this #concheck = Userconfig.query.filter_by(plexdir=form.directory.data).first()
		concheck = Userconfig(plexdir=form.directory.data)
		db.session.add(concheck)
		db.session.commit()
		return redirect(url_for('.index'))
	return render_template('index.html',
							form=form, 
							directory=directory)

#/mnt/d/Stuff/videop-dev-folder/Video/DVR/processing/plex-dvr/recordings/tv-shows/
#/mnt/d/Stuff/videop-dev-folder/Video/DVR/processing/plex-dvr/recordings/movies/
#/mnt/d/Stuff/videop-dev-folder/Video/DVR/processing/plex-dvr/archived/
@main.route('/list', methods=['GET','POST'])
def listfiles():
	files=list()
	directory = Userconfig.query.get(2)
	if directory is None:
		pass
	else:
		for root, directories, filenames in os.walk(str(directory.plexdir)):
			directories[:] = [d for d in directories if not d.startswith('.')]
			for filename in filenames:
				if filename.lower().endswith('.ts'):
					fill=show(root, filename)
					dircheck = Listed.query.filter_by(dirfilename=fill.dirfilename).first()
					if dircheck is None:
						show.commit(fill)
					files.append(str(fill.epname))
	return render_template('list.html', files=files, directory=directory)
#/srv/samba/E10TB/Video/DVR/processing/plex-recording/tv-shows/A.P. BIO/Season 01/A.P. Bio (2018) - S01E05 - Dating Toledoans.ts
#/mnt/d/Stuff/videop-dev-folder/Video/DVR/processing/plex-recordings/tv-shows/A.P. BIO/Season 01/A.P. Bio (2018) - S01E05 - Dating Toledoans.ts