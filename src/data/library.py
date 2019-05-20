from server.configuration import settings
from data.recordings import Filename
from plexapi.server import PlexServer

class Connect:
    def __init__(self):
        self.plex = PlexServer(settings['plex']['baseurl'], settings['plex']['token'])

class Match:
    def __init__(self, path):
        server = Connect().plex
        file = Filename(path)
        if file.isMovie:
            shows = server.library.section('Movies')
        else:
            shows = server.library.section('TV Shows')
            showInfo = shows.get(file.show)
            self.showMatch = showInfo.episode(season=file.seasonNumber, episode=file.episodeNumber)