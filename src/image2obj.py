import os
import io
import cv2
import base64
import jsonpickle
from PIL import Image

from hr import HR

app = HR(option_list=["all"])


def img_convertor(img_path):
    img = cv2.imread(img_path)
    faces = app.get_face_data(img)
    facedata = {}
    for index, face in enumerate(faces):
        bbox, kps, embedding, gender, age, crop_face_img, img_shape = face
        obj = {}
        obj["embedding"] = jsonpickle.encode(embedding.tolist())
        obj["gender"] = int(gender)
        obj["age"] = age
        obj["img_obj"] = jsonpickle.encode(bbox.tolist())
        facedata[str(index)] = obj
    print(facedata)


# s3 dagi rasm manizli
_path = "../tests/embedding/2022-11-02 18_59_59.jpg"
img_convertor(_path)
