import json
from src.hr import HR
import cv2
import os
import requests
import base64
import datetime

myHR = HR()


def det(img):
    """
    Bu f-ya:
        - kerakli rasmni load qiladi.
        - HR classi yordamida rasmdiagi har bir yuz uchun
            {
                "bbox":
                    {
                        "x1": 1265,
                        "y1": 897,
                        "x2": 1412,
                        "y2": 1078
                    },
                "kps":
                    {
                        "right_eye": [1303, 969],
                        "left_eye": [1358, 1041],
                        "nose": [1335, 1017],
                        "right_lip": [1307, 1037],
                        "left_lip": [1358, 1041]
                    },
                "shape":
                    {
                        "h": 181,
                        "w": 147,
                        "c": 3
                    }
            }
            ma'lumotlarni API orqali serverga yuboradi
    """

    faces = myHR.detection(img)
    det_result = {}
    print(type(faces))
    for i in range(len(faces)):
        bbox, kps, _shape = faces[i]
        x1 = int(bbox[0])
        y1 = int(bbox[1])
        x2 = int(bbox[2])
        y2 = int(bbox[3])

        # bbox
        b_box = {}
        b_box["x1"] = x1
        b_box["y1"] = y1
        b_box["x2"] = x2
        b_box["y2"] = y2

        # kps
        b_kps = {}
        b_kps["right_eye"] = (int(kps[0][0]), int(kps[0][1]))
        b_kps["left_eye"] = (int(kps[1][0]), int(kps[1][1]))
        b_kps["nose"] = (int(kps[2][0]), int(kps[2][1]))
        b_kps["right_lip"] = (int(kps[3][0]), int(kps[3][1]))
        b_kps["left_lip"] = (int(kps[4][0]), int(kps[4][1]))

        # shape
        b_shape = {}
        b_shape["h"] = _shape[0]
        b_shape["w"] = _shape[1]
        b_shape["c"] = _shape[2]

        # har bir topilgan yuz uchun
        obj = {}
        obj["bbox"] = b_box
        obj["kps"] = b_kps
        obj["shape"] = b_shape

        det_result["p" + str(i)] = obj

    det_json = json.dumps(det_result)
    print(det_json)
    print(type(det_json))
    return det_json
    # det_json API orqali jo'natiladi


def videoStream():
    """
    Bu f-yaning vazifasi
        - kameradan olingan rasmni det() f-yaga yuboradi va natijasini faces o'zgaruvchisiga yuklaydi
        - kamerning manzili boyicha olingan rasm
            {
                "merchant_id": 1,
                "location_id": 1,
                "camera_id": 1,
                "faces": faces,
                "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
                "frame": str(base64.encodebytes(img_encoded), "utf-8"),
            }
         ko'rinishida serverga yuboriladi
    """

    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)

    while cap.isOpened():
        # Press key q to stop
        if cv2.waitKey(1) == ord("q"):
            break
        try:
            ret, frame = cap.read()
            if not ret:
                break
            # frameni yuborish kerak
            faces = det(frame)

            # APIga yuboriladigan datalar shu yerdan ketadi
            addr = "http://3.74.85.246:85"
            test_url = addr + "/api/frame/create/"

            # prepare headers for http request
            # content_type = 'application/json'  # 'image/jpeg'
            # headers = {'content-type': content_type}
            _, img_encoded = cv2.imencode(".jpg", frame)

            response = requests.post(
                test_url,
                data={
                    "merchant_id": 1,
                    "location_id": 1,
                    "camera_id": 1,
                    "faces": faces,
                    "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
                    "frame": str(base64.encodebytes(img_encoded), "utf-8"),
                },
            )
            print(response.status_code)
            cv2.imshow("Detected Objects", frame)
        except Exception as e:
            print(e)


videoStream()
