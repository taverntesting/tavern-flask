import importlib
import json as jsonlib
import logging
from urllib.parse import urlencode, urlparse

from tavern._core.dict_util import check_expected_keys

logger = logging.getLogger(__name__)


class FlaskTestSession:
    def __init__(self, **kwargs):
        expected_blocks = {
            "app": {
                "location",
            },
        }

        check_expected_keys(expected_blocks.keys(), kwargs)

        self._app_args = kwargs.pop("app", {})
        app_location = self._app_args["location"]

        self._flask_app = importlib.import_module(app_location).create_app()
        self._test_client = self._flask_app.test_client()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def make_request(
        self, url, verify, method, params=None, json=None, data=None, **kwargs
    ):
        if kwargs.get("stream"):
            raise NotImplementedError
        kwargs.pop("stream")

        if data and json:
            raise NotImplementedError

        parsed = urlparse(url)
        route = parsed.path

        body = None
        if data:
            body = urlencode(data)
        elif json:
            body = jsonlib.dumps(json)

        meth = getattr(self._test_client, method.lower())
        return meth(route, data=body, query_string=params, **kwargs)
