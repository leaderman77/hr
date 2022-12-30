import cv2
from src.hr import HR
import glob
import os
import uuid


def test_det():
    hr = HR()
    imgs_path = "../../data/drive/rasmlar_kirish/*.jpg"

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

            assert 120 < x1 < 140, "Xato"
            assert 120 < y1 < 140, "Xato"
            assert 120 < y2 < 140, "Xato"
            assert 120 < y2 < 140, "Xato"

            # draw kps
            # please put here
        filename = os.path.join("", "test-det_score-" + str(uuid.uuid4()) + ".jpg")
        print(filename)
        cv2.imwrite(filename, img)



