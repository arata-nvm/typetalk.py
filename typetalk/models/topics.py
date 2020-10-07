from . import common
from .organizations import Organization
from .posts import Post


class TopicDetails(object):
    def __init__(self, detail):
        self.my_space = Organization(detail['mySpace'])
        self.team = detail['team']
        self.topic = Topic(detail['topic'])
        self.favorite = detail['favorite']
        if detail.get('bookmark'):
            self.bookmark = Bookmark(detail['bookmark'])
        self.post_contents_settings = detail['postContentsSettings']
        self.posts = [Post(post) for post in detail['posts']]
        self.has_next = detail['hasNext']
        self.exceeds_attachemnt_limit = detail['exceedsAttachmentLimit']
        self.onboarding = detail['onboarding']
        if detail.get('myTopics'):
            self.my_topic = MyTopic(detail['myTopic'])


class Topic(object):
    def __init__(self, topic):
        self.id = topic['id']
        self.name = topic['name']
        self.suggestion = topic['suggestion']
        self.is_direct_message = topic['isDirectMessage']
        self.is_archived = topic['isArchived']
        self.last_posted_at = common.fromisoformat(topic['lastPostedAt'])
        self.created_at = common.fromisoformat(topic['createdAt'])
        self.updated_at = common.fromisoformat(topic['updatedAt'])
        self.description = topic['description']


class Bookmark(object):
    def __init__(self, bookmark):
        self.post_id = bookmark['postId']
        self.updated_at = common.fromisoformat(bookmark['updatedAt'])


class MyTopic(object):
    def __init__(self, my_topic):
        self.id = my_topic['id']
        self.topic_id = my_topic['topicID']
        self.account_id = my_topic['accountId']
        self.kind = my_topic['kind']
        self.topic_group_id = my_topic['topicGroupId']
        self.ex_topic_group_id = my_topic['exTopicGroupId']
        self.order_no = my_topic['orderNo']
        self.created_at = common.fromisoformat(my_topic['createdAt'])
        self.updated_at = common.fromisoformat(my_topic['updatedAt'])
