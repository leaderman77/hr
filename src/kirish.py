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


def work():
    """
    Ushbu f-ya .env filedan quydagi ma'lumotlarni load qiladi:
        - boundry size (startX,startY,endX,endY)
        - API adress yani post qilish uchun server pathini (api_url)
        - face dioganali chegarasini (dioganal_min, dioganal_max)
        - camera pathini (cam_path)
        - tashkilot IDsini (merchant_id)
        - o'sha tashkilot branch IDsini (location_id)
        - barnchdagi camera IDsini (camera_id)
        - shartni qanotlarnitgan dioganalli face aniqlanishi bilan serverga osha rasm yuboriladi va osha vaqtda time.sleep beriladi (per_second)
    :return:
    """
    # boundry size
    startX, startY = int(config("startX")), int(config("startY"))
    endX, endY = int(config("endX")), int(config("endX"))

    # API url
    api_url = config("TEST_URL")

    # face dioganal
    dioganal_min = int(config("DIOGANAL_MIN"))
    dioganal_max = int(config("DIOGANAL_MAX"))

    # appni tayyorlash
    app = FaceAnalysis(allowed_modules=["detection"], name="buffalo_sc")
    app.prepare(ctx_id=0, det_size=(640, 640), det_thresh=0.3)

    # camerani tayyoralsh yani 0 bosa webcamera aks holda camera pathi yoziladi
    cam_path = config("CAMERA_PATH")
    if config("CAMERA_PATH") == "0":
        cam_path = int(config("CAMERA_PATH"))

    cap = cv2.VideoCapture(cam_path)
    while True:
        try:
            ret, frame = cap.read()
            image = frame[startY:endY, startX:endX]
            faces = app.get(image)
            rimg = app.draw_on(image, faces)
            for face in faces:
                dioganal = math.sqrt(
                    (face.bbox[0] - face.bbox[2]) ** 2
                    + (face.bbox[1] - face.bbox[3]) ** 2
                )

                if dioganal > dioganal_min and dioganal < dioganal_max:
                    _, img_encoded = cv2.imencode(".jpg", image)

                    response = requests.post(
                        api_url,
                        data={
                            "merchant_id": int(config("MERCHANT_ID")),
                            "location_id": int(config("LOCATION_ID")),
                            "camera_id": int(config("CAMERA_ID")),
                            "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
                            "frame": str(base64.encodebytes(img_encoded), "utf-8"),
                        },
                    )
                    print(response.status_code)
                    time.sleep(int(config("PER_SECOND")))
                    break
            cv2.imshow("Frame", rimg)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break
        except Exception as ex:
            print("xatolik ", ex)

    cv2.destroyAllWindows()
    # vs.release()


while True:
    try:
        work()
    except Exception as ex:
        print(ex)
