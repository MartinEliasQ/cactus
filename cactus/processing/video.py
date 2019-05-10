from cactus.utils import (folder, image, metrics)

import cv2
from datetime import datetime


def to_frames(path: str = None, dest: str = None, rate=1):
    video = cv2.VideoCapture(path)
    n_frames = number_frames(video)
    count = 0
    success, frame = video.read()
    while success:
        video.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
        cv2.imwrite('{}/{}.jpg'
                    .format(dest, str(datetime.now())), frame)
        success, frame = video.read()
        count += rate


def number_frames(video):
    return int(video.get(cv2.CAP_PROP_FRAME_COUNT))
