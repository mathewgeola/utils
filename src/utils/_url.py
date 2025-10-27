import os
import re
import sys
from typing import Any, Final
from urllib import parse

import httpx
import tldextract
from furl import furl
from typing_extensions import Literal
from w3lib.url import canonicalize_url

from utils._headers import _headers


# noinspection PyShadowingNames
class _url:
    @staticmethod
    def get_furl_obj(url: str) -> furl:
        return furl(url)

    @staticmethod
    def get_parse_result(url: str) -> parse.ParseResult:
        parse_result = parse.urlparse(url)
        return parse_result

    @staticmethod
    def get_origin_path(url: str) -> str:
        """
        >>> _url.get_origin_path("https://github.com/search?q=owner%3Amathewgeola+utils&type=repositories")
        'https://github.com/search'

        Args:
            url:

        Returns:

        """
        furl_obj = _url.get_furl_obj(url)
        origin_path = str(furl_obj.origin) + str(furl_obj.path)
        return origin_path

    @staticmethod
    def is_valid(url: str) -> bool:
        """
        >>> _url.is_valid("https://www.baidu.com/")
        True

        Args:
            url:

        Returns:

        """
        try:
            parse_result = _url.get_parse_result(url)
            scheme, netloc = parse_result.scheme, parse_result.netloc
            if not scheme:
                return False
            if not netloc:
                return False
            if scheme not in ("http", "https"):
                return False
            return True
        except ValueError:
            return False

    @staticmethod
    def quote(
            url: str,
            safe: str | None = None,
            encoding: str = "utf-8",
            quote_type: Literal["encodeURI", "encodeURIComponent", "browser"] | None = "browser"
    ) -> str:
        """
        >>> _url.quote("https://www.baidu.com/s?wd=你好")
        'https://www.baidu.com/s?wd=%E4%BD%A0%E5%A5%BD'

        Args:
            url:
            safe:
            encoding:
            quote_type:

        Returns:

        """
        if quote_type == "encodeURI":
            safe = ";/?:@&=+$,-_.!~*'()#"
        elif quote_type == "encodeURIComponent":
            safe = "-_.~"
        elif quote_type == "browser":
            safe = ";/?:@&=+$,-_.!~*'()"
            parsed = parse.urlparse(url)
            path = parse.quote(parsed.path, safe=safe)
            query_pairs = parse.parse_qsl(parsed.query, keep_blank_values=True)
            encoded_query = "&".join(
                f"{k}={parse.quote(v, safe='-_.~', encoding=encoding)}"
                for k, v in query_pairs
            )
            fragment = parse.quote(parsed.fragment, safe='-_.~', encoding=encoding)
            return parse.urlunparse((
                parsed.scheme,
                parsed.netloc,
                path,
                parsed.params,
                encoded_query,
                fragment
            ))
        else:
            if safe is None:
                safe = "/"

        return parse.quote(url, safe=safe, encoding=encoding)

    @staticmethod
    def unquote(url: str, encoding: str = "utf-8") -> str:
        """
        >>> _url.unquote("https://www.baidu.com/s?wd=%E4%BD%A0%E5%A5%BD")
        'https://www.baidu.com/s?wd=你好'

        Args:
            url:
            encoding:

        Returns:

        """
        return parse.unquote(url, encoding=encoding)

    @staticmethod
    def encode(params: dict[str, Any]) -> str:
        """
        >>> _url.encode({"a": "1", "b": "2"})
        'a=1&b=2'

        Args:
            params:

        Returns:

        """
        return parse.urlencode(params)

    @staticmethod
    def decode(url: str) -> dict[str, str]:
        """
        >>> _url.decode("xxx?a=1&b=2")
        {'a': '1', 'b': '2'}

        Args:
            url:

        Returns:

        """
        params = dict()

        lst = url.split("?", maxsplit=1)[-1].split("&")
        for i in lst:
            key, value = i.split("=", maxsplit=1)
            params[key] = _url.unquote(value)

        return params

    @staticmethod
    def join_url(base_url: str, url: str) -> str:
        """
        >>> _url.join_url("https://www.baidu.com/", "/s?ie=UTF-8&wd=utils")
        'https://www.baidu.com/s?ie=UTF-8&wd=utils'

        Args:
            base_url:
            url:

        Returns:

        """
        return parse.urljoin(base_url, url)

    @staticmethod
    def join_params(url: str, params: dict[str, Any]) -> str:
        """
        >>> _url.join_params("https://www.baidu.com/s", {"wd": "你好"})
        'https://www.baidu.com/s?wd=%E4%BD%A0%E5%A5%BD'

        Args:
            url:
            params:

        Returns:

        """
        if not params:
            return url

        params = _url.encode(params)
        separator = "?" if "?" not in url else "&"
        return url + separator + params

    @staticmethod
    def get_params(url: str) -> dict[str, str]:
        """
        >>> _url.get_params("https://www.baidu.com/s?wd=utils")
        {'wd': 'utils'}

        Args:
            url:

        Returns:

        """
        furl_obj = _url.get_furl_obj(url)
        params = dict(furl_obj.query.params)
        return params

    @staticmethod
    def get_param(url: str, key: str, default: Any | None = None) -> Any:
        """
        >>> _url.get_param("https://www.baidu.com/s?wd=utils", "wd")
        'utils'

        Args:
            url:
            key:
            default:

        Returns:

        """
        params = _url.get_params(url)
        param = params.get(key, default)
        return param

    @staticmethod
    def get_url_params(url: str) -> tuple[str, dict[str, str]]:
        """
        >>> _url.get_url_params("https://www.baidu.com/s?wd=utils")
        ('https://www.baidu.com/s', {'wd': 'utils'})

        Args:
            url:

        Returns:

        """
        root_url = ""
        params = dict()

        if "?" in url:
            root_url = url.split("?", maxsplit=1)[0]
            params = _url.get_params(url)
        else:
            if re.search("[&=]", url) and not re.search("/", url):
                params = _url.get_params(url)
            else:
                root_url = url

        return root_url, params

    @staticmethod
    def get_domain(url: str) -> str:
        """
        >>> _url.get_domain("https://image.baidu.com/search/index?word=utils")
        'baidu'

        Args:
            url:

        Returns:

        """
        er = tldextract.extract(url)
        domain = er.domain
        return domain

    @staticmethod
    def get_subdomain(url: str) -> str:
        """
        >>> _url.get_subdomain("https://image.baidu.com/search/index?word=utils")
        'image'

        Args:
            url:

        Returns:

        """
        er = tldextract.extract(url)
        subdomain = er.subdomain
        return subdomain

    @staticmethod
    def canonicalize(url: str) -> str:
        """
        >>> _url.canonicalize("https://www.baidu.com/s?wd=utils")
        'https://www.baidu.com/s?wd=utils'

        Args:
            url:

        Returns:

        """
        return canonicalize_url(url)

    @staticmethod
    def to_file_path(
            url: str,
            headers: dict[str, str] | None = None,
            file_path: str | None = None,
            dir_path: str | None = None,
            file_name: str | None = None,
            file_prefix: str | None = None,
            file_suffix: str | None = None,
            use_cache: bool = True,
            chunk_size: int = 64 * 1024
    ) -> str | None:
        if not _url.is_valid(url):
            return None

        if headers is None:
            headers = _headers.get_default()

        if file_path is None:
            if dir_path is None:
                sys_argv0 = sys.argv[0]
                if not os.path.isfile(sys_argv0):
                    return None
                dir_path = os.path.dirname(sys_argv0)
            if file_name is None:
                if file_prefix is not None and file_suffix is not None:
                    file_name = file_prefix + file_suffix
                else:
                    if file_prefix is None:
                        file_prefix, _ = os.path.splitext(_url.get_furl_obj(url).path.segments[-1])
                    if file_suffix is None:
                        _, file_suffix = os.path.splitext(_url.get_furl_obj(url).path.segments[-1])
                        if file_suffix is None or file_suffix == "":
                            response = httpx.head(url, headers=headers)
                            if (content_type := response.headers.get("content-type")) is not None:
                                # todo：Add more content_type.
                                content_type_to_file_suffix: Final[dict[str, str]] = {
                                    "image/png": "png",
                                    "image/gif": "gif",
                                    "text/html;charset=utf-8": "html",
                                    "text/javascript; charset=utf-8": "js",
                                }
                                file_ext = content_type_to_file_suffix[content_type]
                                file_suffix = "." + file_ext
                    file_name = file_prefix + file_suffix
            file_path = os.path.join(dir_path, file_name)

        file_path = os.path.abspath(file_path)

        if use_cache:
            if os.path.exists(file_path):
                return file_path

        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        try:
            with httpx.Client(timeout=None, follow_redirects=True) as client:
                with client.stream("GET", url, headers=headers) as response:
                    response.raise_for_status()
                    with open(file_path, "wb") as file:
                        for chunk in response.iter_bytes(chunk_size=chunk_size):
                            file.write(chunk)
        except Exception as e:  # noqa
            file_path = None

        return file_path


__all__ = [
    "_url"
]
