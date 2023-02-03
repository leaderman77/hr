import os
import cv2
import numpy as np
from hr import HR
from utils import project_dir

PROJECT_DIR = project_dir()


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


def det():
    """
    Rasmlardan yuzlarni aniqlash:
        - berilgan path bo'yicha barcha .jpg rasmlarni load qiladi
        - topilgan har bir yuz uchun yuz atrofida to'rtburchak chiziladi
    """
    hr = HR(det_thresh=0.5)
    imgs_path = os.path.join(
        PROJECT_DIR,
        "data",
        "s3_v0.1.1",
        "merchant_1",
        "location_1",
    )

    folders = os.listdir(imgs_path)
    for folder in folders:
        camera = os.path.join(imgs_path, folder)
        fayllar = os.listdir(camera)
        for _joy_fayl in fayllar:
            _joy2 = os.path.join(camera, _joy_fayl)
            _joy2_fayllar = os.listdir(_joy2)
            for _joy2_fayl in _joy2_fayllar:
                _joy3 = os.path.join(_joy2, _joy2_fayl)
                img_path = _joy3
                img = cv2.imread(img_path)
                print(img)
                det_data = hr.detection(img)

                for data in det_data:
                    bbox, kps, _shape, det_score = data
                    x1 = int(bbox[0])
                    y1 = int(bbox[1])
                    x2 = int(bbox[2])
                    y2 = int(bbox[3])

                    # draw bbox
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(
                        img,
                        f"{det_score:.2f}",
                        (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 225),
                        2,
                        cv2.LINE_AA,
                    )
                    # print(bbox)

                    # draw kps
                    if kps is not None:
                        kps = kps.astype(np.int_)
                        for l in range(kps.shape[0]):
                            cv2.circle(img, (kps[l][0], kps[l][1]), 5, (0, 0, 255), -1)
                    cv2.imwrite(name_change(img_path), img)


det()
