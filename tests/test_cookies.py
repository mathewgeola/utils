from utils import cookies as _cookies


def test_cookies():
    cookies = {
        "utils": "hi"
    }
    print(_cookies.dict_to_str(cookies))


if __name__ == '__main__':
    test_cookies()
