import logging

from wazo_amid_client import Client as AmidClient
from .http import OnboardingResource
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wazo_calld.ari_ import CoreARI as AriClient

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        # registering API endpoint
        api = dependencies['api']
        ari: AriClient = dependencies['ari']
        config = dependencies['config']
        token_changed_subscribe = dependencies['token_changed_subscribe']

        amid_client = AmidClient(**config['amid'])

        token_changed_subscribe(amid_client.set_token)

        api.add_resource(
            OnboardingResource, '/onboarding/<call_tech>/<call_id>', resource_class_args=[ari.client, amid_client]
        )
