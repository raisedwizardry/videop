import re
from pathlib import Path, PurePath

class File():
    def __init__(self, file):
        self.file = file

class DirectoryFiles:
    def __init__(self, path):
        self.videoPath = path
        self.files = list()
        self.pattern = '**/*.ts'
        self.listAll()

    def listAll(self):
        videoDirectory = Path(self.videoPath)
        for videoFiles in videoDirectory.glob(self.pattern):
            self.files.append(File(videoFiles.as_posix()))

#TODO:make Filename an abstract base class to accomidate an episode and movie class they can inherit from
class Filename:
    def __init__(self, fullDirectoryFilename):
        self.full = fullDirectoryFilename
        pathparts = Directory(fullDirectoryFilename)
        self.fullFilename = pathparts.filename
        self.fullPath = pathparts.directory
        self.simpleFilename = pathparts.simplename
        self.extention = pathparts.extention
        self.isMovie = None
        seFind = self.matchSe(self.simpleFilename)
        if seFind:
            self.setEpisode(seFind)
        movieYearFind = self.matchYear(self.simpleFilename)
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
        self.title = self.simpleFilename.split(' - ')[2]
        self.show = self.excludeYear(self.simpleFilename)
        self.isMovie = False

    def setMovie(self, movieYearFind):
        self.movieTitle = movieYearFind.group(1).strip()
        self.movieYear = movieYearFind.group(2)
        self.isMovie = True

class Directory:
    def __init__(self, fullDirectoryFilename):
        path = PurePath(fullDirectoryFilename)
        self.full = path.as_posix()
        self.directory = path.parent.as_posix()
        self.filename = path.name
        self.simplename = PurePath(path.with_suffix("")).name
        self.extention = path.suffix.split('.', 1)[-1]