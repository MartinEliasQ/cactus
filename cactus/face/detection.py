from cactus.face.strategy.dnn import dnn
from cactus.face.strategy.haar import haar
from cactus.face.strategy.hog import hog
from cactus.utils.others import add_string_to_array
from cactus.utils.image import crop_box
from cactus.utils.folder import get_files, get_folders


class detection(object):
    def __init__(self, strategy=None):
        if strategy:
            self.detect = strategy

    def detect(self):
        print('No method was provided')
        raise Exception('No method was provided')

    def get_boxes_from_directory(self, path_batch):
        all_boxes = map(lambda x: add_string_to_array(
            x, self.detect(x)), path_batch)
        return list(all_boxes)

    def to_face(self, frames_folder="frames", dest_folder="faces"):

        pass


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
