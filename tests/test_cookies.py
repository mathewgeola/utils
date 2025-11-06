import utils


def test_cookies():
    cookies = {
        "cwb-utils": "hi"
    }
    print(utils.cookies.dict_to_str(cookies))


if __name__ == '__main__':
    test_cookies()
