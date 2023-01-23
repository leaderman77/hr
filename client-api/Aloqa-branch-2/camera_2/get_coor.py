import cv2
import time
import math
from insightface.app import FaceAnalysis


app = FaceAnalysis(allowed_modules=["detection"])
app.prepare(ctx_id=0, det_size=(640, 640), det_thresh=0.3)
_path = "../camera_2/test_rasmlari/Frame_ch_3.jpg"
img1 = cv2.imread(_path)


def Work():
    while True:
        try:
            start_point = (700, 450)
            end_point = (1600, 1430)
            startX, startY = start_point
            endX, endY = end_point

            # Blue color in BGR
            color = (255, 0, 0)

            # Line thickness of 2 px
            thickness = 2

            image = img1[startY:endY, startX:endX]
            faces = app.get(image)
            for face in faces:
                dioganal = math.sqrt(
                    (face.bbox[0] - face.bbox[2]) ** 2
                    + (face.bbox[1] - face.bbox[3]) ** 2
                )
                print(dioganal)
                image = cv2.rectangle(img1, start_point, end_point, color, thickness)
                break

            cv2.imshow("Frame", image)
            cv2.imwrite("crop_ch_3.jpg", image)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break
        except Exception as ex:
            print("xatolik ", ex)

    cv2.destroyAllWindows()
    # vs.release()


while True:
    try:
        Work()
    except Exception as ex:
        print(ex)
