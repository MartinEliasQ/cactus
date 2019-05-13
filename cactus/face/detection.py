from cactus.face.strategy.dnn import dnn
from cactus.face.strategy.haar import haar
from cactus.face.strategy.hog import hog


class detection(object):
    def __init__(self, strategy=None):
        if strategy:
            self.detect = strategy

    def detect(self):
        print('No method was provided')
        raise Exception('No method was provided')


def detector(method="dnn"):
    if method is None or method.lower() not in ['dnn', 'haar', 'hog']:
        raise Exception('Method do not available')
    method = method.lower()
    print("Using {} method".format(method))
    return {
        'dnn': lambda: detection(dnn),
        'haar': lambda: detection(haar),
        'hog': lambda: detection(hog)
    }[method]()
