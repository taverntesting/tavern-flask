import json as jsonlib
import logging

try:
    from urllib.parse import urlencode, urlparse
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode

from future.utils import raise_from
from tavern.schemas.extensions import import_ext_function
from tavern.util import exceptions
from tavern.util.dict_util import check_expected_keys

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
            raise_from(exceptions.MissingKeysError(msg), e)

        self._flask_app = import_ext_function(app_location)
        self._test_client = self._flask_app.test_client()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def make_request(
        self, url, verify, method, headers=None, params=None, json=None, data=None
    ):
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
