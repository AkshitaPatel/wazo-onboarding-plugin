import logging

from wazo_calld.http import AuthResource
from wazo_amid.auth import required_acl

logger = logging.getLogger(__name__)


class OnboardingResource(AuthResource):
    def __init__(self, amid_client):
        self.amid_client = amid_client

    @required_acl("calld.onboarding.read")
    def get(self):
        logger.info("Hello!!!!!!!")
        return "Hello", 200

    def post(self, call_tech, call_id):
        response = self.amid_client.action(
            "Redirect",
            {
                "Channel": f"{call_tech}/{call_id}",
                "Exten": "3000",
                "Context": "xivo-extrafeatures",
                "Priority": "1",
            },
        )

        return response
