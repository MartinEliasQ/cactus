from cactus.utils import (folder, image, metrics)

import cv2
from datetime import datetime


def to_frames(path: str = None, dest: str = "faces", rate=1):
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


def folder_to_frames(input="videos", output="frames", rate=1):
    folder.delete(output)
    folder.create(output)
    labels = folder.get_folders(input)
    labels_files = [(label, folder.get_files("{}/{}".format(input, label)))
                    for label
                    in labels]

    for label, label_files in labels_files:
        for lfile in label_files:
            print("Converting {}'s videos into frames".format(label))
            input_video = "{}/{}/{}".format(input, label, lfile)
            output_folder = "{}/{}".format(output, label)
            folder.create(output_folder)
            to_frames(input_video, output_folder, rate)

    return "Done"


def number_frames(video):
    return int(video.get(cv2.CAP_PROP_FRAME_COUNT))
