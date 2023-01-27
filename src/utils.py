import os
import math
import jsonpickle
import numpy as np


def compute_sim(feat1, feat2):
    """Function to compute cosine similarity between two embedding vectors

    Parameters
    ----------
    feat1 : :obj:`Array`
        The first parameter. Vector
    feat2 : :obj:`Array`
        The second parameter. Vector

    Returns
    -------
    The method returns similarity score in float32 data type
    """

    feat1 = feat1.ravel()
    feat2 = feat2.ravel()
    sim = np.dot(feat1, feat2) / (np.linalg.norm(feat1) * np.linalg.norm(feat2))

    return sim


def project_dir():
    """
    Returns path to the project root
    Returns
    -------
    Path
        Return path to the project root
    """
    return os.path.dirname(os.path.dirname(__file__))


def get_diagonal(bbox):
    """
    Calculate the diagonal length of a bounding box.

    Parameters
    ----------
    face : objectq
        Object containing bounding box coordinates.

    Returns
    -------
    diagonal : float
        The calculated diagonal length.
    """
    return math.sqrt((bbox[0] - bbox[2]) ** 2 + (bbox[1] - bbox[3]) ** 2)


def get_obj(face):
    """
    Convert face data to JSON format.

    Parameters
    ----------
    face : object
        Object containing face data.

    Returns
    -------
    json_data : dict
        Dictionary containing face data in JSON format.
    """
    bbox, kps, embedding, gender, age, crop_face_img, img_shape = face

    x1 = int(bbox[0])
    y1 = int(bbox[1])
    x2 = int(bbox[2])
    y2 = int(bbox[3])

    # bbox
    b_box = {}
    b_box["x1"] = x1
    b_box["y1"] = y1
    b_box["x2"] = x2
    b_box["y2"] = y2

    # kps
    b_kps = {}
    b_kps["right_eye"] = [int(kps[0][0]), int(kps[0][1])]
    b_kps["left_eye"] = [int(kps[1][0]), int(kps[1][1])]
    b_kps["nose"] = [int(kps[2][0]), int(kps[2][1])]
    b_kps["right_lip"] = [int(kps[3][0]), int(kps[3][1])]
    b_kps["left_lip"] = [int(kps[4][0]), int(kps[4][1])]

    # embedding
    b_embedding = {}
    b_embedding["embedding_vek"] = jsonpickle.encode(embedding.tolist())

    # gender
    b_gender = {}
    b_gender["gender_f"] = int(gender)

    # age
    b_age = {}
    b_age["age_f"] = age

    # crop img shape
    b_crop_shape = {}
    b_crop_shape["h"] = crop_face_img[0]
    b_crop_shape["w"] = crop_face_img[1]
    b_crop_shape["c"] = crop_face_img[2]

    # har bir topilgan yuz uchun
    obj = {}
    obj["bbox"] = b_box
    obj["kps"] = b_kps
    obj["embedding"] = b_embedding
    obj["gender"] = b_gender
    obj["age"] = b_age
    obj["shape"] = b_crop_shape

    return obj
