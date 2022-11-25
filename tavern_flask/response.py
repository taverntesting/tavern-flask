from requests import Response
from tavern._plugins.rest.response import RestResponse


class FlaskResponse(RestResponse):
    """Flask response verifier"""

    def verify(self, response):
        """Wrap the Flask response into a Requests response and call the
        verifier for that. See docs for RestResponse for what this does and
        returns
        """

        wrapped_response = Response()
        wrapped_response.headers = response.headers
        wrapped_response.status_code = response._status_code
        wrapped_response._content = response.get_data()
        return super(FlaskResponse, self).verify(wrapped_response)
