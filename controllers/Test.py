class Test:
    NAME = 'test'

    def __init__(self, context):
        self.context = context

    def deneme(self, request, response):
        print('TEST:CONTROLLER --- deneme')
        self.context.s.test.deneme()
        print(self.context.db)
