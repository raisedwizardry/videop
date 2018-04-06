import os
import subprocess
import sys
import ntpath
from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import Listed,Userconfig
from ..email import send_email
from . import main
from .forms import NameForm
from .contents import show

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.directory.data)
            db.session.add(user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))

@main.route('/list',methods=['GET','POST'])
def listfiles():
    files=list()
    for root, directories, filenames in os.walk(str("/mnt/d/Stuff/videop-dev-folder/Video/DVR/processing/plex-recordings")):
        directories[:] = [d for d in directories if not d.startswith('.')]
        for filename in filenames:
            if filename.lower().endswith('.ts'):
                fill=show(root, filename)
                show.match(fill)
                dircheck = Listed.query.filter_by(dirfilename=fill.dirfilename).first()
                if dircheck is None:
                    show.commit(fill)
                files.append(str(fill.epname))


    return render_template('list.html', files=files)
#/srv/samba/E10TB/Video/DVR/processing/plex-recording/tv-shows/A.P. BIO/Season 01/A.P. Bio (2018) - S01E05 - Dating Toledoans.ts
#/mnt/d/Stuff/videop-dev-folder/Video/DVR/processing/plex-recordings/tv-shows/A.P. BIO/Season 01/A.P. Bio (2018) - S01E05 - Dating Toledoans.ts