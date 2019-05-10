import os
import fnmatch
from server.configuration import settings

class files:
    def listDirectoryTs():
        files= list()
        listOfFiles = os.listdir(settings['Common']['videopath'])
        pattern = "*.ts"
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                    files.append(entry)
        return files
