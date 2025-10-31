import utils


def test_file():
    print(utils.file.compress("test_file", "zip"))
    print(utils.file.compress("test_file", "rar"))

    print(utils.file.decompress("test_file.rar", "test_file1"))
    print(utils.file.decompress("test_file.zip", "test_file2"))

    print(utils.file.get_file_paths_and_dir_paths("."))


if __name__ == '__main__':
    test_file()
