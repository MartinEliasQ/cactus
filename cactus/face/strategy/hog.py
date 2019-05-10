import dlib
from cactus.utils.image import (read, to_gray)
import numpy as np

FACE_DETECTOR = dlib.get_frontal_face_detector()


def hog(imagen):
    img = read(imagen)
    img_gray = to_gray(img)
    detected_faces = FACE_DETECTOR(img_gray, 1)
    boxes = list()

    for _, face_box in enumerate(detected_faces):
        x = face_box.left()
        y = face_box.top()
        w = face_box.right()
        h = face_box.bottom()

        box = (x, y, w, h)
        boxes.append(np.array(box))
    return boxes
