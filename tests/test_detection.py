import os
import cv2
import glob
import numpy as np

from hr import HR
from utils import project_dir


PROJECT_DIR = project_dir()


def test_det():
    """
    Yuzni aniqlashni test qilish:
        - berilgan path bo'yicha barcha .jpg rasmlarni load qiladi
        - topilgan har bir yuz uchun yuz atrofida to'rtburchak chiziladi
    """
    hr = HR(name_model="buffalo_sc")
    imgs_path = os.path.join(
        PROJECT_DIR, "data", "drive", "rasmlar_kirish", "2022-11-02 18_59_59.jpg"
    )
    for img_path in glob.glob(imgs_path):
        img = cv2.imread(img_path)
        det_data = hr.detection(img)

        for data in det_data:
            bbox, kps, shape, det_score = data
            x1 = int(bbox[0])
            y1 = int(bbox[1])
            x2 = int(bbox[2])
            y2 = int(bbox[3])

            # draw bbox
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # print(bbox)

            # draw kps
            if kps is not None:
                kps = kps.astype(np.int_)
                for l in range(kps.shape[0]):
                    cv2.circle(img, (kps[l][0], kps[l][1]), 5, (0, 0, 255), -1)
            # cv2.imwrite("test_rasm.jpg", img)

            assert 220 < x1 < 320, "Xato"
            assert 150 < y1 < 250, "Xato"
            assert 300 < x2 < 400, "Xato"
            assert 200 < y2 < 350, "Xato"
