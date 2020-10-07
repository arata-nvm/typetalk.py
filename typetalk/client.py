from urllib import request

BASE_URL = 'https://typetalk.com/api/v1'


class Client(object):
    def __init__(self, token):
        self.token = token

    def _get(self, url):
        headers = {'X-Typetalk-Token': self.token}
        req = request.Request(url, headers=headers)
        res = request.urlopen(req)
        return res.read().decode('utf-8')
