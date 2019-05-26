import pytest
from server.instance import server

# Creates a fixture whose name is "app"
# and returns our flask server instance
@pytest.fixture
def app():
    app = server.app
    return app

class TestPath:
    def __init__(self):
        self.linuxShow = "/Test/Directory/Videos/TV Shows/The 100/Season 06/The 100 (2014) - S06E01 - Sanctum.ts"
        self.windowsShow = "D:\\Test\\Directory\\Videos\\TV Shows\\The 100\\Season 06\\The 100 (2014) - S06E02 - Red Sun Rising.ts"
        self.windowsYearShow = "D:\\Test\\Directory\\Videos\\TV Shows\\Jeopardy (1984)\\Season 35\\Jeopardy (1964) - S35E179 - Teachers Tournament.ts"
        self.linuxRelease = "/Release/Directory/Videos/TV Shows/Fargo/Season 02/Fargo.S02E04.Fear.and.Trembling.mkv"
        self.windowsMovie = "D:\\Test\\Directory\\Videos\\Movies\\The Boy and the Pirates (1960)\\The Boy and the Pirates (1960).ts"
        self.linuxMovie = "/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)/The Boy and the Pirates (1960).ts"

testdata = TestPath()