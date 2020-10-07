from . import common


class Organization(object):
    def __init__(self, org):
        self.space = Space(org['space'])
        self.my_role = org['myRole']
        self.is_payment_admin = org['isPaymentAdmin']
        self.invitable_roles = org['invitableRoles']
        self.my_plan = MyPlan(org['myPlan'])


class Space(object):
    def __init__(self, space):
        self.key = space['key']
        self.name = space['name']
        self.enabled = space['enabled']
        self.image_url = space['imageUrl']


class MyPlan(object):
    def __init__(self, my_plan):
        self.plan = Plan(my_plan['plan'])
        self.enabled = my_plan['enabled']
        self.trial = my_plan['trial']
        self.number_of_users = my_plan['numberOfUsers']
        self.number_of_allowed_addresses = my_plan['numberOfAllowedAddresses']
        self.total_attachment_size = my_plan['totalAttachmentSize']
        self.created_at = common.fromisoformat(my_plan['createdAt'])
        self.updated_at = common.fromisoformat(my_plan['updatedAt'])


class Plan(object):
    def __init__(self, plan):
        self.key = plan['key']
        self.name = plan['name']
        self.limit_number_of_users = plan['limitNumberOfUsers']
        self.limit_number_of_allowed_addressses = plan['limitNumberOfAllowedAddresses']
        self.limit_total_attachment_size = plan['limitTotalAttachmentSize']
