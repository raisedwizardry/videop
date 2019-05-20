from data.recordings import Directory

def test_directory_show_linux():
    path = "/Test/Directory/Videos/TV Shows/The 100/Season 06/The 100 (2014) - S06E01 - Sanctum.ts"
    setupObject = Directory(path)
    assert setupObject.full == "/Test/Directory/Videos/TV Shows/The 100/Season 06/The 100 (2014) - S06E01 - Sanctum.ts"
    assert setupObject.directory == "/Test/Directory/Videos/TV Shows/The 100/Season 06"
    assert setupObject.filename == "The 100 (2014) - S06E01 - Sanctum.ts"
    assert setupObject.extention == ".ts"

def test_directory_show_windows():
    path = "D:\\Test\\Directory\\Videos\\TV Shows\\The 100\\Season 06\\The 100 (2014) - S06E02 - Red Sun Rising.ts"
    setupObject = Directory(path)
    assert setupObject.full == "D:/Test/Directory/Videos/TV Shows/The 100/Season 06/The 100 (2014) - S06E02 - Red Sun Rising.ts"
    assert setupObject.directory == "D:/Test/Directory/Videos/TV Shows/The 100/Season 06"
    assert setupObject.filename == "The 100 (2014) - S06E02 - Red Sun Rising.ts"
    assert setupObject.extention == ".ts"

def test_directory_dateshow_windows():
    path = "D:\\Test\\Directory\\Videos\\TV Shows\\Jeopardy (1984)\\Season 35\\Jeopardy (1964) - S35E179 - Teachers Tournament.ts"
    setupObject = Directory(path)
    assert setupObject.full == "D:/Test/Directory/Videos/TV Shows/Jeopardy (1984)/Season 35/Jeopardy (1964) - S35E179 - Teachers Tournament.ts"
    assert setupObject.directory == "D:/Test/Directory/Videos/TV Shows/Jeopardy (1984)/Season 35"
    assert setupObject.filename == "Jeopardy (1964) - S35E179 - Teachers Tournament.ts"
    assert setupObject.extention == ".ts"

def test_directory_release_linux():
    path = "/Release/Directory/Videos/TV Shows/Fargo/Season 02/Fargo.S02E04.Fear.and.Trembling.mkv"
    setupObject = Directory(path)
    assert setupObject.full == "/Release/Directory/Videos/TV Shows/Fargo/Season 02/Fargo.S02E04.Fear.and.Trembling.mkv"
    assert setupObject.directory == "/Release/Directory/Videos/TV Shows/Fargo/Season 02"
    assert setupObject.filename == "Fargo.S02E04.Fear.and.Trembling.mkv"
    assert setupObject.extention == ".mkv"

def test_directory_movie_windows():
    path = "D:\\Test/Directory\\Videos\\Movies\\The Boy and the Pirates (1960)\\The Boy and the Pirates (1960).ts"
    setupObject = Directory(path)
    assert setupObject.full == "D:/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)/The Boy and the Pirates (1960).ts"
    assert setupObject.directory == "D:/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)"
    assert setupObject.filename == "The Boy and the Pirates (1960).ts"
    assert setupObject.extention == ".ts"

def test_directory_movie_linux():
    path = "/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)/The Boy and the Pirates (1960).ts"
    setupObject = Directory(path)
    assert setupObject.full == "/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)/The Boy and the Pirates (1960).ts"
    assert setupObject.directory == "/Test/Directory/Videos/Movies/The Boy and the Pirates (1960)"
    assert setupObject.filename == "The Boy and the Pirates (1960).ts"
    assert setupObject.extention == ".ts"
