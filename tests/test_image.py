import utils


def test_image():
    if (file_path := utils.url.to_file_path("https://www.baidu.com/img/flexible/logo/pc/result@2.png")) is not None:
        print(utils.image.to_jpg(file_path))


if __name__ == '__main__':
    test_image()
