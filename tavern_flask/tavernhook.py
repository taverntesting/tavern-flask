import logging
from os.path import join, abspath, dirname

import yaml

from future.utils import raise_from

from tavern.util.dict_util import format_keys
from tavern.util import exceptions

from .request import FlaskRequest
from .response import FlaskResponse
from .client import FlaskTestSession


logger = logging.getLogger(__name__)


session_type = FlaskTestSession

request_type = FlaskRequest
request_block_name = "request"

def get_expected_from_request(stage, test_block_config, session):
    # pylint: disable=unused-argument
    try:
        r_expected = stage["response"]
    except KeyError as e:
        logger.error("Need a 'response' block if a 'request' is being sent")
        raise_from(exceptions.MissingSettingsError, e)

    f_expected = format_keys(r_expected, test_block_config["variables"])
    return f_expected

verifier_type = FlaskResponse
response_block_name = "response"

schema_path = join(abspath(dirname(__file__)), "schema.yaml")
with open(schema_path, "r") as schema_file:
    schema = yaml.load(schema_file)
