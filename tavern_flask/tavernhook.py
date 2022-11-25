from os.path import abspath, dirname, join

import yaml
from tavern.util.dict_util import format_keys

from .client import FlaskTestSession
from .request import FlaskRequest
from .response import FlaskResponse

session_type = FlaskTestSession

request_type = FlaskRequest
request_block_name = "request"


def get_expected_from_request(stage, test_block_config, _):
    r_expected = stage["response"]
    f_expected = format_keys(r_expected, test_block_config["variables"])
    return f_expected


verifier_type = FlaskResponse
response_block_name = "response"

schema_path = join(abspath(dirname(__file__)), "schema.yaml")
with open(schema_path, "r") as schema_file:
    schema = yaml.load(schema_file, Loader=yaml.Loader)
