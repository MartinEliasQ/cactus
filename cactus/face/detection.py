from cactus.face.strategy.dnn import dnn
from cactus.face.strategy.haar import haar
from cactus.face.strategy.hog import hog
from cactus.utils.others import add_string_to_array
from cactus.utils.image import crop_box, save_Image, crop_and_save
from cactus.utils.folder import create, get_files, get_folders, delete


import numpy as np
import math
from sklearn.model_selection import train_test_split
class detection(object):
    def __init__(self, strategy=None):
        if strategy:
            self.detect = strategy

    def detect(self):
        print('No method was provided')
        raise Exception('No method was provided')

    def get_boxes_from_directory(self, path_batch):

        all_boxes = []
        for file in path_batch:
            temp = add_string_to_array(file, self.detect(file))
            temp = np.array(temp)

            if len(temp) > 0:
                for tempi in temp:
                    all_boxes.append(tempi)
        
        return all_boxes

    def to_face(self, frames_folder="frames", dest_folder="faces"):
        train = "train"
        test = "test"
        val = "val"

        dataset_train = "{}/{}".format(dest_folder, train)
        dataset_test = "{}/{}".format(dest_folder, test)
        dataset_val = "{}/{}".format(dest_folder, val)


        delete(dest_folder)

        create(dest_folder)
        create(dataset_test)
        create(dataset_train)
        create(dataset_val)

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

            # Create folder to label
            delete("{}/{}".format(dataset_train, label))
            delete("{}/{}".format(dataset_test, label))
            delete("{}/{}".format(dataset_val, label))

            create("{}/{}".format(dataset_train, label))
            create("{}/{}".format(dataset_test, label))
            create("{}/{}".format(val, label))

            #### 
            gbfd = self.get_boxes_from_directory(list_of_files)

            image_boxes = [image_file 
                            for image_file 
                            in gbfd
                            if len(image_file) > 0]

            image_boxes = [[image_file[0],  # Origin
                            image_file[0].replace(frames_folder,dest_folder), # Dest, all images
                            image_file[0].replace(frames_folder,dataset_train), # Train folder
                            image_file[0].replace(frames_folder,dataset_test), # test folder
                            image_file[1]]                                     # Image box
                            for image_file 
                            in image_boxes]

            label_images = np.array(image_boxes)
            np.random.shuffle(label_images)
            # split image 70% train - 30% test
            index_splot = math.floor(len(label_images)*0.7)

            for i, l_image in enumerate(label_images):
                dir_file = l_image[0]
                dir_dest = l_image[1]
                train_folder = l_image[2]
                test_folder = l_image[3]
                box = l_image[4]

                crop_and_save(dir_file, dest_folder, box)

                if i <= index_splot:
                    crop_and_save(dir_file, train_folder, box)
                else:
                    crop_and_save(dir_file, test_folder, box)
                
            list_return.append(image_boxes)
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
