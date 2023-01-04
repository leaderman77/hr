# Import Libraries
import math
from insightface.app import FaceAnalysis
import cv2
import os
import requests
import base64
import datetime
import time
from decouple import config

app = FaceAnalysis(allowed_modules=["detection"])
app.prepare(ctx_id=0, det_size=(640, 640), det_thresh=0.3)
# img1 = cv2.imread("./rasmlar/1_1_1_2022-10-09-17-32-26.jpg")


def videoStream():
    cap = cv2.VideoCapture(int(config("CAMERA_PATH")))
    # 80
    # 226
    while True:
        ret, frame = cap.read()
        # boundryni chegarasi
        start_point = (1150, 120)
        end_point = (1650, 900)
        startX, startY = start_point
        endX, endY = end_point

        # Blue color in BGR
        color = (255, 0, 0)

        # Line thickness of 2 px
        thickness = 2

        image = frame
        # cv2.imwrite("frame_out.jpg", image)
        faces = app.get(image)
        # rimg = app.draw_on(image, faces)
        for face in faces:
            dioganal = math.sqrt(
                (face.bbox[0] - face.bbox[2]) ** 2 + (face.bbox[1] - face.bbox[3]) ** 2
            )

            if dioganal > 80 and dioganal < 115:
                # print(face.bbox[0],face.bbox[1],face.bbox[2],face.bbox[3])
                # start_point = (int(face.bbox[0]),int(face.bbox[1]))
                # end_point = (int(face.bbox[2]),int(face.bbox[3]))

                # print(dioganal)
                # image = cv2.rectangle(image,start_point, end_point, color, thickness)
                addr = "http://3.74.85.246:85"
                test_url = addr + "/api/frame/create/"

                # prepare headers for http request
                # content_type = 'application/json'  # 'image/jpeg'
                # headers = {'content-type': content_type}

                _, img_encoded = cv2.imencode(".jpg", image)

                img_str = str(base64.encodebytes(img_encoded))

                response = requests.post(
                    test_url,
                    data={
                        "merchant_id": config("MERCHANT_ID"),
                        "location_id": config("LOCATION_ID"),
                        "camera_id": config("CAMERA_ID"),
                        "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
                        "frame": str(base64.encodebytes(img_encoded), "utf-8"),
                    },
                )
                print(response.status_code)
                time.sleep(config("PER_SECOND"))
                break

        cv2.imshow("Frame", image)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    # vs.release()


videoStream()
