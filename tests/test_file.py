import utils


def test_file():
    print(utils.file.compress(".", "tests.zip"))
    print(utils.file.decompress("tests.zip", "tests"))
    print(utils.file.get_file_paths_and_dir_paths("."))


if __name__ == '__main__':
    test_file()
