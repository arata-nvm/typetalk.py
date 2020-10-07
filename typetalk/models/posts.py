from . import common


class Post(object):
    def __init__(self, post):
        self.id = post['id']
        self.topic_id = post['topicId']
        self.reply_to = post['replyTo']
        self.message = post['message']
        self.contents = post['contents']
        self.account = Account(post['account'])
        self.mention = post['mention']
        self.mentions = [Mention(mention) for mention in post['mentions']]
        self.attachments = [Attachment(attachment)
                            for attachment in post['attachments']]
        self.likes = [Like(like) for like in post['likes']]
        self.talks = [Talk(talk) for talk in post['talks']]
        self.links = [Link(link) for link in post['links']]
        self.quoted_posts = [Post(post) for post in post['quotedPosts']]
        self.created_at = common.fromisoformat(post['createdAt'])
        self.updated_at = common.fromisoformat(post['updatedAt'])


class Attachment(object):
    def __init__(self, attachment):
        self.attachment = AttachmentDetail(attachment['attachment'])
        self.web_url = attachment['webUrl']
        self.api_url = attachment['apiUrl']
        if attachment.get('thumbnails'):
            self.thumbnails = [Thumbnail(thumbnail)
                               for thumbnail in attachment['thumbnails']]


class AttachmentDetail(object):
    def __init__(self, detail):
        self.content_type = detail['contentType']
        self.file_key = detail['fileKey']
        self.file_name = detail['fileName']
        self.file_size = detail['fileSize']


class Thumbnail(object):
    def __init__(self, thumbnail):
        self.type = thumbnail['type']
        self.file_size = thumbnail['fileSize']
        self.width = thumbnail['width']
        self.height = thumbnail['height']


class Like(object):
    def __init__(self, like):
        self.id = like['id']
        self.post_id = like['postId']
        self.topic_id = like['topicId']
        self.comment = like['comment']
        self.account = Account(like['account'])
        self.created_at = common.fromisoformat(like['createdAt'])


class Account(object):
    def __init__(self, account):
        self.id = account['id']
        self.name = account['name']
        self.full_name = account['fullName']
        self.suggestion = account['suggestion']
        self.image_url = account['imageUrl']
        self.is_bot = account['isBot']
        self.created_at = common.fromisoformat(account['createdAt'])
        self.updated_at = common.fromisoformat(account['updatedAt'])


class Link(object):
    def __init__(self, link):
        self.id = link['id']
        self.url = link['url']
        self.content_type = link['contentType']
        self.title = link['title']
        self.description = link['description']
        self.image_url = link['imageUrl']
        self.embed = link['embed']
        self.created_at = common.fromisoformat(link['createdAt'])
        self.updated_at = common.fromisoformat(link['updatedAt'])
