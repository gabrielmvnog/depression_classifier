from depression_classifier import app
from sys import argv


def start():
    print(__package__, ' started.')
    app.run(host='0.0.0.0', port=argv[1], debug=argv[2])


if __name__ == '__main__':
    start()
