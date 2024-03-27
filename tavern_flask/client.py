import json as jsonlib
import logging
from urllib.parse import urlparse, urlencode

import flask
from tavern._core import exceptions
from tavern._core.dict_util import check_expected_keys
from tavern._core.extfunctions import import_ext_function
from typing import Dict
logger = logging.getLogger(__name__)


class FlaskTestSession:

    def __init__(self, **kwargs):
        expected_blocks = {
            "app": {
                "location",
            },
        }

        check_expected_keys(expected_blocks.keys(), kwargs)

        try:
            self._app_args = kwargs.pop("app", {})
            app_location = self._app_args["location"]
        except KeyError as e:
            msg = "Need to specify app location (in the form my.module:application)"
            logger.error(msg)
            raise exceptions.MissingKeysError(msg) from e

        self._flask_app: flask.Flask = import_ext_function(app_location)
        self._test_client = self._flask_app.test_client()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def make_request(self, url: str, verify:bool, method:str, headers:Dict=None, params: Dict=None, json: Dict=None, data=None):
        # This isn't used - won't be using SSL
        if not verify:
            logger.warning("'verify' has no use when using flask test client")

        # TODO
        # set host header with url?
        parsed = urlparse(url)
        route = parsed.path

        body = None

        if data:
            body = urlencode(data)

        if json:
            body = jsonlib.dumps(json)

        meth = getattr(self._test_client, method.lower())
        return meth(route, headers=headers, data=body, query_string=params)
