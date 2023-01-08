import os


class Services:
    def __init__(self, context):
        self.context = context
        self.services = {}

        self._parse_services()

        self.context.set('s', self)

    def __getattr__(self, item):
        if item in self.services:
            return self.services[item]

    def _parse_services(self):
        services = list(map(lambda x: x.split('.')[0], os.listdir('services')))

        for service in services:
            module = __import__('services.' + service, fromlist=[service])
            klass = getattr(module, service)
            self.services[klass.NAME] = klass(self.context)
