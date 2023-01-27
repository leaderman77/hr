import os
import cv2
import json
import jsonpickle
from decouple import AutoConfig

from hr import HR
from utils import project_dir, get_diagonal, get_obj

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")
config = AutoConfig(search_path=CONFIG_DIR)
PROJECT_DIR = project_dir()


def test_json():
    """

    Returns
    -------
    Agar oldingan salqangan json fayl bilan berilgan rasmdan olingan json file ustam ust tushsa testdan o'tgan bo'ladi
    """
    with open("../tests/output.json") as f:
        expected = json.load(f)

    _path = "embedding/2022-11-02 18_59_59.jpg"
    image = cv2.imread(_path)
    app = HR(option_list=["all"])
    faces = app.get_face_data(image)
    dioganal_min = int(config("DIOGANAL_MIN"))
    dioganal_max = int(config("DIOGANAL_MAX"))

    facedata = {}
    for i in range(len(faces)):
        bbox = faces[i][0]
        diagonal = get_diagonal(bbox)
        if dioganal_min < diagonal < dioganal_max:
            facedata[str(i)] = get_obj(faces[i])
    objects = {}
    objects["objects"] = facedata
    generated_by_test = jsonpickle.encode(objects)
    assert expected == generated_by_test, "json fayllarda farq bor"
