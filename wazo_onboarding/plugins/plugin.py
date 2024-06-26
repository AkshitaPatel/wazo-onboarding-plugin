import logging


logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        # registering API endpoint
        router = dependencies['router']
        router.add_get('/onboarding', self.onboarding)
        logger.info('Onboarding plugin loaded')

    def unload(self):
        logger.info('Onboarding Plugin unloaded')

    def onboarding(self, request):
        logger.info('Monkey')
        return 'Onboarding successful'
