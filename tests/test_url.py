import utils


def test_url():
    url = "https://releases.ubuntu.com/20.04/ubuntu-20.04.6-desktop-amd64.iso"
    url = "http://msapi.esgcc.com.cn/datacenter-file/file/download?id=245776836132106240"
    file_path = utils.url.to_file_path(url, use_tqdm=True)
    print(file_path)


if __name__ == '__main__':
    test_url()
