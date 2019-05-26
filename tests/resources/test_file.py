from data.recordings import File
import pytest
from conftest import testdata

@pytest.mark.parametrize("test_input,expected", [
    (testdata.linuxShow, "/Test/Directory/Videos/TV Shows/The 100/Season 06/The 100 (2014) - S06E01 - Sanctum.ts"), 
    (testdata.windowsShow, "D:\\Test\\Directory\\Videos\\TV Shows\\The 100\\Season 06\\The 100 (2014) - S06E02 - Red Sun Rising.ts"), 
    (testdata.windowsYearShow, "D:\\Test\\Directory\\Videos\\TV Shows\\Jeopardy (1984)\\Season 35\\Jeopardy (1964) - S35E179 - Teachers Tournament.ts"),
    (testdata.linuxRelease, "/Release/Directory/Videos/TV Shows/Fargo/Season 02/Fargo.S02E04.Fear.and.Trembling.mkv"),
    (testdata.windowsMovie, "D:\\Test\\Directory\\Videos\\Movies\\The Boy and the Pirates (1960)\\The Boy and the Pirates (1960).ts"),
    (testdata.linuxMovie, "/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)/The Boy and the Pirates (1960).ts")])
def test_file_file(test_input, expected):
    assert File(test_input).file == expected