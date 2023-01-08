import os


class Models:
    def __init__(self, context):
        self.context = context
        self.models = {}

        self._parse_models()
        self.context.set('m', self)

    def __getattr__(self, item):
        if item in self.models:
            return self.models[item]

    def _parse_models(self):
        models = list(map(lambda x: x.split('.')[0], os.listdir('models')))

        for model in models:
            module = __import__('models.' + model, fromlist=[model])
            klass = getattr(module, model)
            self.models[klass.NAME] = klass(self.context)
