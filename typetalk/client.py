import json
from urllib import request
from .models import topics

BASE_URL = 'https://typetalk.com/api/v1'


class Client(object):
    def __init__(self, token: str) -> None:
        self.token = token

    def getTopic(self, topic_id: int) -> topics.TopicDetails:
        url = f'{BASE_URL}/topics/{topic_id}'
        res_json = self._get(url)
        res = json.loads(res_json)
        topic_detail = topics.TopicDetails(res)
        return topic_detail

    def _get(self, url: str) -> str:
        headers = {'X-Typetalk-Token': self.token}
        req = request.Request(url, headers=headers)
        res = request.urlopen(req)
        return res.read().decode('utf-8')
