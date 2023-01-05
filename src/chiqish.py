# Import Libraries
import math
from insightface.app import FaceAnalysis
import cv2
import os
import requests
import base64
import datetime
import time

app = FaceAnalysis(allowed_modules=["detection"], name="buffalo_sc")
app.prepare(ctx_id=0, det_size=(640, 640), det_thresh=0.3)


# img1 = cv2.imread("./rasmlar2/1_1_1_2022-10-09-17-37-25.jpg")
# 131
# 226
def Work():
    startTime = time.time()
    cap = cv2.VideoCapture(
        "rtsp://admin:L22F4A64@100.67.7.157:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif"
    )

    while True:
        try:
            ret, frame = cap.read()
            start_point = (950, 170)

            # Ending coordinate, here (220, 220)
            # represents the bottom right corner of rectangle
            end_point = (1800, 1400)

            startX, startY = start_point
            endX, endY = end_point

            # Blue color in BGR
            color = (255, 0, 0)

            # Line thickness of 2 px
            thickness = 2

            # Using cv2.rectangle() method
            # Draw a rectangle with blue line borders of thickness of 2 px
            # image = cv2.rectangle(img1, start_point, end_point, color, thickness)
            image = frame[startY:endY, startX:endX]
            # image = img1
            # cv2.imwrite("frame_out.jpg", image)
            faces = app.get(image)
            rimg = app.draw_on(image, faces)
            for face in faces:
                dioganal = math.sqrt(
                    (face.bbox[0] - face.bbox[2]) ** 2
                    + (face.bbox[1] - face.bbox[3]) ** 2
                )

                if dioganal > 125 and dioganal < 230:
                    endTime = time.time()
                    if endTime - startTime > 4:
                        startTime = time.time()
                        print("bor")
                        # print(face.bbox[0],face.bbox[1],face.bbox[2],face.bbox[3])
                        # start_point = (int(face.bbox[0]),int(face.bbox[1]))
                        # end_point = (int(face.bbox[2]),int(face.bbox[3]))
                        cv2.imwrite("frame_out.jpg", image)

                        # print(dioganal)
                        # image = cv2.rectangle(image,start_point, end_point, color, thickness)
                        addr = "http://3.74.85.246:85"
                        test_url = addr + "/api/frame/create/"

                        # prepare headers for http request
                        content_type = "application/json"  # 'image/jpeg'
                        headers = {"content-type": content_type}

                        img = cv2.imread(os.path.join("frame_out.jpg"))

                        _, img_encoded = cv2.imencode(".jpg", img)

                        img_str = str(base64.encodebytes(img_encoded))

                        response = requests.post(
                            test_url,
                            data={
                                "merchant_id": 1,
                                "location_id": 1,
                                "camera_id": 2,
                                "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
                                "frame": str(base64.encodebytes(img_encoded), "utf-8"),
                            },
                        )
                        print(response.status_code)
                        break
                        # time.sleep(1)
        except Exception as ex:
            print("xatolik chiqishda ", ex)
            continue
        # cv2.imshow("Frame", rimg)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    # vs.release()


while True:
    try:
        Work()
    except Exception as ex:
        print(ex)
