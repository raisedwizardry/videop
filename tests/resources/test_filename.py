from data.recordings import Filename
import pytest
from conftest import testdata

@pytest.mark.parametrize("test_input,expected", [
    (testdata.linuxShow, False), 
    (testdata.windowsShow, False), 
    (testdata.windowsYearShow, False),
    #(testdata.linuxRelease, False),
    (testdata.windowsMovie, True),
    (testdata.linuxMovie, True)])
def test_filename_ismovie_bool(test_input, expected):
    assert Filename(test_input).isMovie == expected

@pytest.mark.parametrize("test_input,expected", [
    (testdata.linuxShow, "The 100"),
    (testdata.windowsShow, "The 100"),
    (testdata.windowsYearShow, "Jeopardy")
    #(testdata.linuxRelease, "Fargo"),
    #(testdata.windowsMovie, AttributeError),
    #(testdata.linuxMovie, AttributeError)
    ])
def test_filename_show(test_input, expected):
    assert Filename(test_input).show == expected

@pytest.mark.parametrize("test_input,expected", [
    #(testdata.linuxShow, "The 100"),
    #(testdata.windowsShow, "The 100"),
    #(testdata.windowsYearShow, "Jeopardy"),
    #(testdata.linuxRelease, "Fargo"),
    (testdata.windowsMovie, "The Boy and the Pirates"),
    (testdata.linuxMovie, "The Boy and the Pirates")])
def test_filename_movie_title(test_input, expected):
    assert Filename(test_input).movieTitle == expected

@pytest.mark.parametrize("test_input,expected", [
    #(testdata.linuxShow, "The 100"),
    #(testdata.windowsShow, "The 100"),
    #(testdata.windowsYearShow, "Jeopardy"),
    #(testdata.linuxRelease, "Fargo"),
    (testdata.windowsMovie, "1960"),
    (testdata.linuxMovie, "1960")])
def test_filename_movie_year(test_input, expected):
    assert Filename(test_input).movieYear == expected
