from pathlib import Path
import os
import shutil


def create(path):
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except:
        print("An error occured")


def delete(path: str):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
    except:
        print("An error occured")


def get_info(path: str):
    try:
        folder_list = next(os.walk(path))
        return (folder_list)
    except:
        print("An error occured")


def get_folders(path: str):
    return get_info(path)[1]


def get_files(path: str):
    return get_info(path)[2]


def create_multiple(paths: list):
    for path in paths:
        create(path)


def delete_multiple(paths: list):
    for path in paths:
        delete(path)


def get_paths_with_dest(origen, dest):
    root = get_folders(origen)
    all_files = list()

    for node in root:
        node_route = "{}/{}".format(origen, node)
        node_dest_route = "{}/{}".format(dest, node)

        files = get_files(node_route)
        files = list(map(lambda x: [
                     "{}/{}".format(node_route, x),
                     "{}/{}".format(node_dest_route, x)], files))
        all_files.append(files)
    return all_files
