from lib.Context import Context
from lib.Server import Server


def main():
    server = Server({
        'port': 3000,
        'context': Context()
    })

    server.listen()


if __name__ == '__main__':
    main()
