"""
Yuzni aniqlashni test qilish:
    - berilgan path bo'yicha barcha .jpg rasmlarni load qiladi
    - har bir rasmni HR classidagi detection f-ya yordamida barcha yuzlarni aniqlaydi( f-yaga bazi parametrlarni berish mumkin, masalan: module, det_size va det_thresh)
    - topilgan har bir yuz uchun yuz atrofida to'rtburchak chiziladi
"""
import cv2
from src.hr import HR
import glob
import os
import uuid


def test_det():
    hr = HR()
    # imgs_path = "../../data/drive/rasmlar_kirish/*.jpg"
    imgs_path = "../data/drive/rasmlar_chiqish/1_1_1_2022-10-09-17-38-10.jpg"

    for img_path in glob.glob(imgs_path):
        img = cv2.imread(img_path)
        det_data = hr.detection(img)

        for data in det_data:
            bbox, kps, _shape = data
            x1 = int(bbox[0])
            y1 = int(bbox[1])
            x2 = int(bbox[2])
            y2 = int(bbox[3])
            # draw bbox
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # print(bbox)

            assert 1100 < x1 < 1400, "Xato"
            assert 800 < y1 < 1000, "Xato"
            assert 1200 < y2 < 1600, "Xato"
            assert 900 < y2 < 1200, "Xato"

            # draw kps
            # please put here
        # filename = os.path.join("", "test-det_score-" + str(uuid.uuid4()) + ".jpg")
        # print(filename)
        # cv2.imwrite(filename, img)
