from cactus.utils.image import (read, to_gray)
import cv2
import numpy as np

CASCADE_XML = "src/haarcascade_frontalface_alt2.xml"
FACE_DETECTOR = cv2.CascadeClassifier(CASCADE_XML)


def haar(imagen):
    img = read(imagen)
    img_width, img_height, _ = img.shape
    img_gray = to_gray(img)
    detected_faces = FACE_DETECTOR.detectMultiScale(img_gray, 1.3, 5)
    boxes = list()

    for (x, y, w, h) in detected_faces:
        center_x = x + (w/2)
        center_y = y + (h/2)
        b_dim = min(max(w, h)*1.3, img_width, img_height)
        box = ((center_x-b_dim/2), (center_y - b_dim/2),
               (center_x+b_dim/2), center_y + b_dim/2)

        boxes.append(np.array(box))
    return boxes
