from utils import image as _image
from utils import url as _url


def test_image():
    if (file_path := _url.to_file_path("https://www.baidu.com/img/flexible/logo/pc/result@2.png")) is not None:
        print(_image.to_jpg(file_path))


if __name__ == '__main__':
    test_image()
