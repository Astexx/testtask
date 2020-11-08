from flask_restful import Resource, reqparse

from apps.api.settings import api, app
from apps.utils.request_handler import get_token, make_request


class ImageParser(Resource):
    """
    Getting image lists
    """

    def __init__(self):
        self.params = None
        self.token = get_token()

    def get(self):
        """
        GET implementation
        :return: Response
        """
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        args = parser.parse_args()
        page_num = args.get('page')
        if page_num:
            self.params = {'page': page_num}
        kwargs = {
            'url_prefix': '/images',
            'token': self.token,
            'api_params': self.params
        }
        response = make_request('get', **kwargs)
        try:
            if response.status_code != 200:
                app.logger.error(AssertionError(
                    f'Wrong status code received: {response.status_code} expected 200'
                ))
            return response.json()
        except (KeyError, AssertionError):
            exception = ConnectionResetError(response.content.decode())
            app.logger.error(exception)
            raise exception


class ImageDetail(Resource):
    """
    Getting detailed image information
    """

    def __init__(self):
        self.token = get_token()

    def get(self, _id):
        """
        GET implementation
        :param _id: Image id
        :return: Response
        """
        kwargs = {
            'url_prefix': f'/images/{_id}',
            'token': self.token,
        }
        response = make_request('get', **kwargs)
        try:
            if response.status_code != 200:
                app.logger.error(AssertionError(
                    f'Wrong status code received: {response.status_code} expected 200'
                ))
            return response.json()
        except (KeyError, AssertionError):
            exception = ConnectionResetError(response.content.decode())
            app.logger.error(exception)
            raise exception


api.add_resource(ImageParser, '/images')
api.add_resource(ImageDetail, '/images/<int:_id>')
