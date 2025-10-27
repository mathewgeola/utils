from utils import list as _list


def test_list():
    print(_list.split(list(range(8)), 3))
    print(_list.flatten([1, 2, [3, 4], [5, 6, 7]]))


if __name__ == '__main__':
    test_list()
