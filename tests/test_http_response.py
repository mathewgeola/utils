import requests

import utils


def test_http_response():
    text = """jQuery5346819({"username":"cwb-utils"})"""
    print(utils.http.response.jsonp_to_json(text)["username"])

    text = """jsonp_31515591963415254({"username":"cwb-utils"})"""
    print(utils.http.response.jsonp_to_json(text)["username"])

    url = "https://api.flickr.com/services/feeds/photos_public.gne?format=json&jsoncallback=handleFlickr"
    text = requests.get(url).text
    print(utils.http.response.jsonp_to_json(text))


if __name__ == '__main__':
    test_http_response()
