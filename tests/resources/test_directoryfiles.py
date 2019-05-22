from pathlib import Path, PurePath
from data.recordings import DirectoryFiles
#https://medium.com/testcult/intro-to-test-framework-pytest-5b1ce4d011ae
#https://www.linuxjournal.com/content/python-testing-pytest-fixtures-and-coverage
#https://code-maven.com/pytest-fixtures-temporary-directory
#


def test_directoryfiles_multiple_types(tmpdir):
    tempVideoPath = Path(tmpdir).as_posix()
    tmpdir.join('abc.ts').write("d")
    tmpdir.join('123.mpeg').write("d")
    tmpdir.join('123.mkv').write("d")
    expected = [(Path(tmpdir) / 'abc.ts').as_posix()]
    assert DirectoryFiles(tempVideoPath).files == expected

def test_directoryfiles_only_one(tmpdir):
    tempVideoPath = Path(tmpdir).as_posix()
    tmpdir.join('Going To The Show.ts').write("d")
    expected = [(Path(tmpdir) / 'Going To The Show.ts').as_posix()]
    assert DirectoryFiles(tempVideoPath).files == expected

def test_directoryfiles_single_type(tmpdir):
    tempVideoPath = Path(tmpdir).as_posix()
    tmpdir.join('Going To The Show.ts').write("d")
    tmpdir.join('At The Show.ts').write("d")
    expected = []
    expected.append((Path(tmpdir) / 'At The Show.ts').as_posix())
    expected.append((Path(tmpdir) / 'Going To The Show.ts').as_posix())
    assert DirectoryFiles(tempVideoPath).files == expected

def test_directoryfiles_no_type(tmpdir):
    tempVideoPath = Path(tmpdir).as_posix()
    tmpdir.join('Goodbye.json').write("d")
    tmpdir.join('Hello.txt').write("d")
    tmpdir.join('Backwards.cs').write("d")
    expected = []
    assert DirectoryFiles(tempVideoPath).files == expected
