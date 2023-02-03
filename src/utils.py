import os
import math
import cv2 as cv
import jsonpickle
import numpy as np


def name_change(nom):
    """
    Appends "_det" to the end of the file name
    Parameters
    ----------
    nom : str

    Returns
    -------
    str
    """

    return nom[0 : len(nom) - 4] + "_det" + nom[len(nom) - 4 :]


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


def resize_face(crop_img, crop_kps, target_size=(112, 112)):
    """Function to resize cropped face, face's kps to the desired size

    Parameters
    ----------
    crop_img : obj:`Array`
        cropped face image
    crop_kps : obj:`Array`
        adjusted kps according to cropped face
    target_size : obj:`Tuple`
        object contains target size for resizing

    Returns
    -------
    img : Array
        resized crop image
    list: Array
        resized kps
    """
    resized_crop = cv.resize(crop_img, target_size)
    ratio_x = target_size[0] / float(crop_img.shape[1])
    ratio_y = target_size[1] / float(crop_img.shape[0])
    crop_kps[:, 0] *= ratio_x
    crop_kps[:, 1] *= ratio_y

    return resized_crop, crop_kps


def crop_face(img, kps, bbox):
    """Function to crop face img & obtain cropped img kps

    Parameters
    ----------
    img : obj:`Array`
        input location image
    kps : obj:`Array`
        face kps found on loc image
    bbox : obj:`Array`
        face bbox found on loc image

    Returns
    -------
    img : Array
        cropped face image
    list
        the list of adjusted kps
    """
    x1 = int(bbox[0])
    y1 = int(bbox[1])
    x2 = int(bbox[2])
    y2 = int(bbox[3])
    crop_img = img[y1:y2, x1:x2]

    # recalculate kps for cropped img
    crop_kps = []
    for i in range(5):
        kps_1 = kps[i][0] - x1
        kps_2 = kps[i][1] - y1
        crop_kps.append([kps_1, kps_2])

    # converting list to np array
    crop_kps = np.array(crop_kps)

    return crop_img, crop_kps
