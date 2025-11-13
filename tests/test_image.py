import utils


def test_image():
    file_path1 = utils.url.to_file_path(
        "https://www.baidu.com/img/flexible/logo/pc/result@2.png",
        file_path="1.png"
    )
    print(file_path1)
    file_path1 = utils.image.to_jpg(file_path1)
    print(file_path1)

    file_path2 = utils.url.to_file_path(
        "https://www.baidu.com/img/flexible/logo/pc/result@2.png",
        file_path="2.png"
    )
    print(file_path2)
    file_path2 = utils.image.to_jpg(file_path2)
    print(file_path2)

    if file_path1 is not None and file_path2 is not None:
        file_path3 = utils.image.concat([file_path1, file_path2], "3.jpg", orientation="vertical")
        file_path4 = utils.image.concat([file_path1, file_path2], "4.jpg", orientation="horizontal")
        print(file_path3)
        print(file_path4)


if __name__ == '__main__':
    test_image()
