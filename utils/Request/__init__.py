class Request:
    def __init__(self, method, url, headers, body):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"{self.method} {self.url}"
