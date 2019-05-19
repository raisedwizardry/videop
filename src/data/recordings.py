import re
import os
from pathlib import PurePath
import fnmatch
from server.configuration import settings

class DirectoryFiles:
    def __init__(self):
        self.files = list()
        self.pattern = "*.ts"
        self.listAll()

    def listAll(self):
        for root, directories, filenames in os.walk(settings['common']['videopath']):
            for filename in fnmatch.filter(filenames, self.pattern):
                join = PurePath(root) / filename
                self.files.append(join.as_posix())

class Filename:
    def __init__(self, fullDirectoryFilename):
        self.full = fullDirectoryFilename
        split = Directory(fullDirectoryFilename)
        self.fullFilename = split.filename
        self.fullPath = split.directory
        self.extention = split.extention
        self.isMovie = None
        seFind = self.matchSe(self.fullFilename)
        if seFind:
            self.setEpisode(seFind)
        movieYearFind = self.matchYear(self.fullFilename)
        if movieYearFind and self.isMovie is not False:
            self.setMovie(movieYearFind)

    def matchSe(self, matchParse):
        seasonPattern = re.compile(r'[S,s](\d\d)([E,e](\d\d\d?))+')  # S06E02
        return seasonPattern.search(matchParse)

    def excludeYear(self, matchParse):
        episodeYear = self.matchYear(matchParse.split(' - ')[0])
        if episodeYear:
            return episodeYear.group(1).strip()
        else:
            return matchParse.split(' - ')[0]
    
    def matchYear(self, matchParse):
        yearPattern = re.compile(r'(.*)[\s\(](\d{4})[\)]')
        return yearPattern.search(matchParse)

    def setEpisode(self, seFind):
        self.seInfo = seFind.group()
        self.seasonNumber = int(seFind.group(1))
        self.episodeNumber = int(seFind.group(3))
        self.title = self.fullFilename.split('.', 1)[-2].split(' - ')[2]
        self.show = self.excludeYear(self.fullFilename)
        self.isMovie = False

    def setMovie(self, movieYearFind):
        self.movieTitle = movieYearFind.group(1)
        self.movieYear = movieYearFind.group(2)
        self.isMovie = True

class Directory:
    def __init__(self, fullDirectoryFilename):
        path = PurePath(fullDirectoryFilename)
        self.full = path.as_posix()
        self.directory = path.parent.as_posix()
        self.filename = path.name
        self.extention = path.suffix
