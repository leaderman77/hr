# import cv2
from insightface.app import FaceAnalysis


app = FaceAnalysis(allowed_modules=["detection"])
app.prepare(ctx_id=0, det_size=(640, 640), det_thresh=0.7)


class HR:
    def __int__(self):
        pass

    def detection(self, img):
        print("detection f-ya")
        faces = app.get(img)
        for face in faces:
            print(face.bbox)
            # rasm koordinatalari shu yerda yuboriladi

    def agegender(self):
        print("age-gender f-ya")

    def recognation(self):
        print("recognation f-ya")


# myHR = HR()
# myHR.agegender()
# myHR.recognation()
