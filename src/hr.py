# import cv2
from insightface.app import FaceAnalysis


class HR:
    def __init__(self, module="detection", det_size=(640, 640), det_thresh=0.3):
        self.app = FaceAnalysis(allowed_modules=[module])
        self.app.prepare(ctx_id=0, det_size=det_size, det_thresh=det_thresh)

    def detection(self, img):
        faces = self.app.get(img)
        all_detect_faces = []
        for face in faces:
            x1 = int(face["bbox"][0])
            y1 = int(face["bbox"][1])
            x2 = int(face["bbox"][2])
            y2 = int(face["bbox"][3])
            crop_img = img[y1:y2, x1:x2]

            # rasm koordinatalari shu yerda aniqlanadi
            all_detect_faces.append([face.bbox, face.kps, crop_img.shape])

        return all_detect_faces

    def agegender(self):
        print("age-gender f-ya")

    def embeding(self):
        print("embeding f-ya")


# myHR = HR()
# myHR.agegender()
# myHR.recognation()
