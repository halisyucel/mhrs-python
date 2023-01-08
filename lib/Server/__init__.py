import os
import sqlite3

from lib.Context import Context
from lib.Models import Models
from lib.Router import Router
from lib.Services import Services


class Server:
    def __init__(self, options):
        self.connection = None
        self.options = self._options(options)
        self.router = Router(self.options['context'])
        self.services = Services(self.options['context'])
        self.models = Models(self.options['context'])

        self._db()

    @staticmethod
    def _options(options):
        if options is None:
            return {
                'port': 3000,
                'database': 'database.db',
                'context': Context(),
            }

        if 'port' not in options:
            options['port'] = 3000

        if 'database' not in options:
            options['database'] = 'database.db'

        if 'context' not in options:
            options['context'] = Context()

        if not isinstance(options['context'], Context):
            raise TypeError('SERVER: context must be an instance of Context')

        if not isinstance(options['port'], int):
            raise TypeError('SERVER: port must be an integer')

        if not isinstance(options['database'], str):
            raise TypeError('SERVER: database must be a string')

        if not os.path.isfile(os.path.join(os.getcwd(), options['database'])):
            raise FileNotFoundError('SERVER: database file not found')

        return options

    def _db(self):
        self.connection = sqlite3.connect(os.path.join(os.getcwd(), self.options['database']))
        self.options['context'].set('db', self.connection.cursor())

        print(f'SERVER: connecting to database "{self.options["database"]}"')

    def listen(self):
        print('SERVER: listening on port', self.options['port'])

        self._handle('test/deneme')

    def _handle(self, request):
        request = request.split('/')
        self.router.handle(request[0], request[1])
