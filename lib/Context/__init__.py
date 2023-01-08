class Context:
    DEFAULT = {
        's': None,
        'm': None,
        'db': None,
    }

    def __init__(self, **kwargs):
        self.context = self.DEFAULT
        self.context.update(self._kwargs(kwargs))

    def __getattr__(self, item):
        if item in self.context:
            return self.context[item]

    def _kwargs(self, kwargs):
        for key in kwargs:
            if key in self.context:
                if self.context[key] is None:
                    self.context[key] = kwargs[key]
                else:
                    raise KeyError(f'Context: {key} is already defined')
        return kwargs

    def set(self, key, value):
        self.context.update(self._kwargs({key: value}))
