import utils


def test_sql():
    print(utils.sql.format("select * from table;"))  # noqa


if __name__ == '__main__':
    test_sql()
