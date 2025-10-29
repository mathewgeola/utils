from utils import sql as _sql


def test_sql():
    print(_sql.format("select * from table;"))  # noqa


if __name__ == '__main__':
    test_sql()
