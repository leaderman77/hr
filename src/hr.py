import cv2
from insightface.app import FaceAnalysis
import os
import uuid

app = FaceAnalysis(allowed_modules=["detection"])
app.prepare(ctx_id=0, det_size=(640, 640), det_thresh=0.3)


class HR:
    def __int__(self):
        pass

    def detection(self, img):
        faces = app.get(img)
        all_detect_facees = []
        for face in faces:
            print(face.bbox)
            print(face.kps)
            x1 = int(face["bbox"][0])
            y1 = int(face["bbox"][1])
            x2 = int(face["bbox"][2])
            y2 = int(face["bbox"][3])
            crop_img = img[y1:y2, x1:x2]
            print(crop_img.shape)
            # test uchin ishlatildi
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # test papka yaratib osha joyga detection bogan rasmlarni saqlaymiz
            # cv2.imwrite("detect.jpg",crop_img)

            # rasm koordinatalari shu yerda yuboriladi
            all_detect_facees.append([face.bbox, face.kps, crop_img.shape])

        # test qilish uchun ishlatildi
        # full_filename = os.path.join("../tests/detection/", "test-det_score-0,3-"+str(uuid.uuid4())+".jpg")
        # cv2.imwrite(full_filename, img)

        return all_detect_facees

    def agegender(self):
        print("age-gender f-ya")

    def embeding(self):
        print("embeding f-ya")


# myHR = HR()
# myHR.agegender()
# myHR.recognation()
