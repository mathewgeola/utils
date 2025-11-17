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

    urls = [
        "http://images.esgcc.com.cn/images/spu/788C331B24AF68E4082E29DFF12F60A5/341775E2E3B5ADA379E8204CD019D5AC.jpg",
        "http://images.esgcc.com.cn/images/spu/788C331B24AF68E4082E29DFF12F60A5/F15AF3184BCFBA6738BF4020F00B2C6A.jpg"
    ]
    file_paths = []
    for url in urls:
        file_path = utils.url.to_file_path(url)
        print(file_path)
        if file_path is not None:
            file_path = utils.image.to_jpg(file_path)
            print(file_path)
            if file_path is not None:
                file_paths.append(file_path)

    file_path = utils.image.concat(
        file_paths, "5.jpg", orientation="vertical"
    )
    print(file_path)
    file_path = utils.image.concat(
        file_paths, "6.jpg", orientation="horizontal"
    )
    print(file_path)

    urls = [
        'http://images.esgcc.com.cn/images/spu/6A0EBD90BAF3DF8C055DC26C7AFC3169/5867DBF6E022A357C9BB3087D06DE8A6.png',
        'http://images.esgcc.com.cn/images/spu/6A0EBD90BAF3DF8C055DC26C7AFC3169/BCFAA29EF8D487C7C2506AEDECAE35B6.png',
        'http://images.esgcc.com.cn/images/spu/6A0EBD90BAF3DF8C055DC26C7AFC3169/F5332504375276F6E5035FC153EF0E82.png',
        'http://images.esgcc.com.cn/images/spu/6A0EBD90BAF3DF8C055DC26C7AFC3169/FC49C25E21007580F639C841FA03492C.png'
    ]

    file_paths = []
    for url in urls:
        file_path = utils.url.to_file_path(url)
        print(file_path)
        if file_path is not None:
            file_path = utils.image.to_jpg(file_path)
            print(file_path)
            if file_path is not None:
                file_paths.append(file_path)

    file_path = utils.image.concat(
        file_paths, "7.tiff", orientation="vertical"
    )
    print(file_path)
    file_path = utils.image.concat(
        file_paths, "8.jpg", orientation="horizontal"
    )
    print(file_path)


if __name__ == '__main__':
    test_image()
