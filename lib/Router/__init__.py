import os

from lib.Server.request import Request
from lib.Server.response import Response


class Router:
    def __init__(self, context):
        self.context = context
        self.routes = {}

        self._parse_routes()

    def _parse_routes(self):
        routes = list(map(lambda x: x.split('.')[0], os.listdir('controllers')))

        for route in routes:
            module = __import__('controllers.' + route, fromlist=[route])
            klass = getattr(module, route)
            self.routes[klass.NAME] = klass(self.context)

    def handle(self, route, method):
        if route in self.routes:
            getattr(self.routes[route], method)(
                Request(
                    method="GET",
                    url="http://localhost:8080/test",
                    headers={
                        "Host": "localhost:8080",
                        "User-Agent": "curl/7.64.1",
                        "Accept": "*/*",
                    },
                    body="",
                ),
                Response,
            )
        else:
            raise Exception('Route not found')
