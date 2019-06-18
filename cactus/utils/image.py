import cv2
import numpy as np
from PIL import Image


def read(path: str):
    return Image.open(path)


def save(image, dest):
    try:
        image.save(dest)
    except:
        print("An error occured")


def to_numpy(image):
    return np.array(image)


def to_pillow(image):
    return Image.fromarray(image)


def to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def to_blob(image):
    return cv2.dnn.blobFromImage(cv2.resize(to_numpy(image), (300, 300)),
                                 1.0, (300, 300),
                                 (103.93, 116.77, 123.68))


def crop_box(path, box, size=(299, 299)):
    image = read(path)
    return image.crop(box).resize(size)

def crop_Image_rect(image, box, size):
    image = read(image)
    return image.crop(box).resize(size)

def save_Image(image, path):
    try:
        image.save(path)
        return True
    except:
        return False

def crop_and_save(origen, dest, box, size):
    cropped = crop_Image_rect(origen,box, size)
    save_Image(cropped, dest)
    
