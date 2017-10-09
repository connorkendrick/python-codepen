# MODULE COMMENT: FILL IN DURING DOCUMENTATION PROCESS
import requests


class _CodePen(object):
    # CLASS COMMENT: FILL IN DURING DOCUMENTATION PROCESS

    def __init__(self):
        #FILL IN DURING DOCUMENTATION PROCESS
        self.__base_uri = 'https://cpv2api.com'
        self._default_category = 'popular'

    def __get_complete_url(self, path):
        # FLL IN DURING DOCUMENTATION PROCESS
        return '{base_uri}/{path}'.format(base_uri=self.__base_uri, path=path)

    def _get_category(self, category):
        # FILL IN DURING DOCUMENTATION PROCESS
        if category is None:
            category = self._default_category
        return category

    def _request(self, path, params=None):
        # FILL IN DURING DOCUMENTATION PROCESS
        url = self.__get_complete_url(path)

        if params is None:
            params = {}

        # Convert query values to strings so Requests can parse
        for key in params:
            params[key] = str(params[key])

        response = requests.get(url, params=params)
        return response.json()['data']
