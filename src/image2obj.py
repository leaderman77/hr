import os
import io
import cv2
import json
import base64
import jsonpickle
from PIL import Image

from utils import project_dir
from hr import HR

PROJECT_DIR = project_dir()
app = HR(option_list=["all"])


def img_convertor(img_byte):
    """
    rasmni byte ko'rinishida keladi, rasmga decode qilinadi va undan  yuzlarni qirqib olib embedding, age va genderni
     aniqlab json ko'rinishida natija sifatida qaytaradi.
    Parameters
    ----------
    img_path: str

    Returns
    -------
    facedata: json
    """

    img = Image.open(io.BytesIO(base64.decodebytes(bytes(img_byte, "utf-8"))))
    img.save("dummy_img.jpg")
    img = cv2.imread("dummy_img.jpg")
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
    json_data = json.dumps(facedata)
    os.remove("dummy_img.jpg")

    return json_data


# s3 dagi rasm manzili yoki local manzil
_path = os.path.join(PROJECT_DIR, "tests", "embedding", "2022-11-02 18_59_59.jpg")
image = cv2.imread(_path)
_, img_encoded = cv2.imencode(".jpg", image)
img_convertor(str(base64.encodebytes(img_encoded), "utf-8"))
