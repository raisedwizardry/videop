from data.recordings import Directory
import pytest
from conftest import testdata

@pytest.mark.parametrize("test_input,expected", [
    (testdata.linuxShow, "/Test/Directory/Videos/TV Shows/The 100/Season 06/The 100 (2014) - S06E01 - Sanctum.ts"), 
    (testdata.windowsShow, "D:/Test/Directory/Videos/TV Shows/The 100/Season 06/The 100 (2014) - S06E02 - Red Sun Rising.ts"), 
    (testdata.windowsYearShow, "D:/Test/Directory/Videos/TV Shows/Jeopardy (1984)/Season 35/Jeopardy (1964) - S35E179 - Teachers Tournament.ts"),
    (testdata.linuxRelease, "/Release/Directory/Videos/TV Shows/Fargo/Season 02/Fargo.S02E04.Fear.and.Trembling.mkv"),
    (testdata.windowsMovie, "D:/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)/The Boy and the Pirates (1960).ts"),
    (testdata.linuxMovie, "/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)/The Boy and the Pirates (1960).ts")])
def test_directory_full(test_input, expected):
    assert Directory(test_input).full == expected

@pytest.mark.parametrize("test_input,expected", [
    (testdata.linuxShow, "/Test/Directory/Videos/TV Shows/The 100/Season 06"), 
    (testdata.windowsShow, "D:/Test/Directory/Videos/TV Shows/The 100/Season 06"), 
    (testdata.windowsYearShow, "D:/Test/Directory/Videos/TV Shows/Jeopardy (1984)/Season 35"),
    (testdata.linuxRelease, "/Release/Directory/Videos/TV Shows/Fargo/Season 02"),
    (testdata.windowsMovie, "D:/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)"),
    (testdata.linuxMovie, "/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)")])
def test_directory_directory(test_input, expected):
    assert Directory(test_input).directory == expected

@pytest.mark.parametrize("test_input,expected", [
    (testdata.linuxShow, "The 100 (2014) - S06E01 - Sanctum"), 
    (testdata.windowsShow, "The 100 (2014) - S06E02 - Red Sun Rising"), 
    (testdata.windowsYearShow, "Jeopardy (1964) - S35E179 - Teachers Tournament"),
    (testdata.linuxRelease, "Fargo.S02E04.Fear.and.Trembling"),
    (testdata.windowsMovie, "The Boy and the Pirates (1960)"),
    (testdata.linuxMovie, "The Boy and the Pirates (1960)")])
def test_directory_simplename(test_input, expected):
    assert Directory(test_input).simplename == expected

@pytest.mark.parametrize("test_input,expected", [
    (testdata.linuxShow, "The 100 (2014) - S06E01 - Sanctum.ts"), 
    (testdata.windowsShow, "The 100 (2014) - S06E02 - Red Sun Rising.ts"), 
    (testdata.windowsYearShow, "Jeopardy (1964) - S35E179 - Teachers Tournament.ts"),
    (testdata.linuxRelease, "Fargo.S02E04.Fear.and.Trembling.mkv"),
    (testdata.windowsMovie, "The Boy and the Pirates (1960).ts"),
    (testdata.linuxMovie, "The Boy and the Pirates (1960).ts")])
def test_directory_filename(test_input, expected):
    assert Directory(test_input).filename == expected

@pytest.mark.parametrize("test_input,expected", [
    (testdata.linuxShow, "ts"), 
    (testdata.windowsShow, "ts"), 
    (testdata.windowsYearShow, "ts"),
    (testdata.linuxRelease, "mkv"),
    (testdata.windowsMovie, "ts"),
    (testdata.linuxMovie, "ts")])
def test_directory_extention(test_input, expected):
    assert Directory(test_input).extention == expected