import logging

from wazo_calld.http import AuthResource
from wazo_amid.auth import required_acl

from wazo_calld.ari_ import CoreARI as AriClient

logger = logging.getLogger(__name__)


class OnboardingResource(AuthResource):
    def __init__(self, ari, amid_client):
        self.ari = ari
        self.amid_client = amid_client

    @required_acl("calld.onboarding.read")
    def get(self):
        logger.info("Hello!!!!!!!")
        return "Hello", 200

    @required_acl("calld.onboarding.update")
    def put(self, call_tech, call_id):

        channels = self.ari.channels.list()
        logger.info("Channels!!!")
        if (len(channels) == 0):
            logger.info("No channels currently")
        else:
            logger.info("Current Channels : ")
            for channel in channels:
                logger.info("Channel: %s", channel)
            # channel = self.ari.channels.get(channels[0])
            # logger.info("Channel name: %s ", channel['name'])
            response = self.amid_client.action(
                "Redirect",
                {
                    "Channel": f"{call_tech}/{call_id}",
                    "Exten": "3000",
                    "Context": "xivo-extrafeatures",
                    "Priority": "1",
                },
            )

        return response, channels

# not pass channel names and detect current calls witout passing it as arguments
# use ari interface , we used ami , can use amid
# reinstate required acl and make it work with alphas token

# remove call_id autodetect form list of channels
# play monkeys
# hangup after few seconds
