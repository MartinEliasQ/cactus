from cactus.face.strategy.dnn import dnn
from cactus.face.strategy.haar import haar
from cactus.face.strategy.hog import hog
from cactus.utils.others import add_string_to_array
from cactus.utils.image import crop_box, save_Image
from cactus.utils.folder import create, get_files, get_folders


class detection(object):
    def __init__(self, strategy=None):
        if strategy:
            self.detect = strategy

    def detect(self):
        print('No method was provided')
        raise Exception('No method was provided')

    def get_boxes_from_directory(self, path_batch):
        all_boxes = map(lambda x: add_string_to_array(
            x, self.detect(x)),
            path_batch)
        return list(all_boxes)

    def to_face(self, frames_folder="frames", dest_folder="faces"):
        create(dest_folder)
        labels = get_folders(frames_folder)
        labels_files = [(label,
                         get_files("{}/{}".format(frames_folder,
                                                  label)))
                        for label
                        in labels]

        list_return = []
        for label, lfiles in labels_files:
            print("Detecting {}'s faces".format(label))

            list_of_files = list(map(lambda x: "{}/{}/{}".format(
                frames_folder, label, x
            ), lfiles))
            
            create("{}/{}".format(dest_folder, label))

            list_of_files = [image_file 
                            for image_file 
                            in list_of_files 
                            if len(image_file) > 0]
            
            list_of_files = [image]
            gbfd = self.get_boxes_from_directory(list_of_files)


            list_return.append(gbfd)
        return list_return


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
