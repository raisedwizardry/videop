from data.recordings import Filename
import pytest

linuxShow = "/Test/Directory/Videos/TV Shows/The 100/Season 06/The 100 (2014) - S06E01 - Sanctum.ts"
windowsShow = "D:\\Test\\Directory\\Videos\\TV Shows\\The 100\\Season 06\\The 100 (2014) - S06E02 - Red Sun Rising.ts"
windowsYearShow = "D:\\Test\\Directory\\Videos\\TV Shows\\Jeopardy (1984)\\Season 35\\Jeopardy (1964) - S35E179 - Teachers Tournament.ts"
linuxRelease = "/Release/Directory/Videos/TV Shows/Fargo/Season 02/Fargo.S02E04.Fear.and.Trembling.mkv"
windowsMovie = "D:\\Test/Directory\\Videos\\Movies\\The Boy and the Pirates (1960)\\The Boy and the Pirates (1960).ts"
linuxMovie = "/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)/The Boy and the Pirates (1960).ts"

@pytest.mark.parametrize("test_input,expected", [
    (linuxShow, False), 
    (windowsShow, False), 
    (windowsYearShow, False),
    #(linuxRelease, False),
    (windowsMovie, True),
    (linuxMovie, True)])
def test_filename_ismovie_bool(test_input, expected):
    assert Filename(test_input).isMovie == expected

@pytest.mark.parametrize("test_input,expected", [
    (linuxShow, "The 100"),
    (windowsShow, "The 100"),
    (windowsYearShow, "Jeopardy")
    #(linuxRelease, "Fargo"),
    #(windowsMovie, AttributeError),
    #(linuxMovie, AttributeError)
    ])
def test_filename_show(test_input, expected):
    assert Filename(test_input).show == expected

@pytest.mark.parametrize("test_input,expected", [
    #(linuxShow, "The 100"),
    #(windowsShow, "The 100"),
    #(windowsYearShow, "Jeopardy"),
    #(linuxRelease, "Fargo"),
    (windowsMovie, "The Boy and the Pirates"),
    (linuxMovie, "The Boy and the Pirates")])
def test_filename_movie_title(test_input, expected):
    assert Filename(test_input).movieTitle == expected

@pytest.mark.parametrize("test_input,expected", [
    #(linuxShow, "The 100"),
    #(windowsShow, "The 100"),
    #(windowsYearShow, "Jeopardy"),
    #(linuxRelease, "Fargo"),
    (windowsMovie, "1960"),
    (linuxMovie, "1960")])
def test_filename_movie_year(test_input, expected):
    assert Filename(test_input).movieYear == expected
