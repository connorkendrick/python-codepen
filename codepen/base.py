import requests

class CodePen(object):
    def __init__(self):
        self.base_uri = 'https://cpv2api.com'
        self.default_category = 'popular'

    def _get_category(self, category):
        if category is None:
            category = self.default_category
        return category

    def _get_complete_url(self, path):
        return '{base_uri}/{path}'.format(base_uri=self.base_uri, path=path)

    def _GET(self, path, params={}):
        url = self._get_complete_url(path)

        for key in params:
            params[key] = str(params[key])
        
        response = requests.get(url, params=params)
        return response.json()['data']
