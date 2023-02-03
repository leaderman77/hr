import math
import cv2
import requests
import base64
import datetime
import time
import json
import jsonpickle
import os
from decouple import AutoConfig

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")
config = AutoConfig(search_path=CONFIG_DIR)

from insightface.app import FaceAnalysis


class CameraProcessor:
    def __init__(self, config, option_list=["det"]):
        self.config = config
        self.option_list = option_list
        self.app = FaceAnalysis(allowed_modules=["detection"])
        self.app.prepare(ctx_id=0, det_size=(640, 640), det_thresh=0.5)
        cam_path = config("CAMERA_PATH")
        if config("CAMERA_PATH") == "0":
            cam_path = int(config("CAMERA_PATH"))
        self.cap = cv2.VideoCapture(cam_path)

    def get_image(self):
        """
        Extract a single image from the video capture object.

        Returns
        -------
        image : ndarray
            The extracted image.
        """
        ret, frame = self.cap.read()
        # startX, startY = self.config("startX", cast=int), self.config(
        #     "startY", cast=int
        # )
        # endX, endY = int(self.config("endX")), int(self.config("endX"))
        # return frame[startY:endY, startX:endX]
        return frame

    def get_diagonal(self, bbox):
        """
        Calculate the diagonal length of a bounding box.

        Parameters
        ----------
        face : objectq
            Object containing bounding box coordinates.

        Returns
        -------
        diagonal : float
            The calculated diagonal length.
        """
        return math.sqrt((bbox[0] - bbox[2]) ** 2 + (bbox[1] - bbox[3]) ** 2)

    def send_image(self, image):
        """
        Send image and face data to the API.

        Parameters
        ----------
        image : ndarray
            Image to send.
        face : object
            Object containing face data.
        """
        _, img_encoded = cv2.imencode(".jpg", image)
        api_url = self.config("TEST_URL")
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        json_data = {
            "camera_id": int(self.config("CAMERA_ID")),
            "image_encoded": str(base64.encodebytes(img_encoded), "utf-8"),
            "key": self.config("MERCHANT_KEY"),
            "location_id": int(self.config("LOCATION_ID")),
            "merchant_id": int(self.config("MERCHANT_ID")),
            "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
        }

        response = requests.post(api_url, headers=headers, json=json_data, verify=False)
        print(response.status_code)
        time.sleep(int(self.config("PER_SECOND")))

    def analyze_faces(self, image):
        """
        Analyze faces in the image and send to API if within specified size range.

        Parameters
        ----------
        app : object
            Object containing face detection methods.
        image : ndarray
            Image to analyze.
        """
        dioganal_min = int(self.config("DIOGANAL_MIN"))
        dioganal_max = int(self.config("DIOGANAL_MAX"))

        faces = self.app.get(image)

        for face in faces:
            diagonal = self.get_diagonal(face.bbox)
            if dioganal_min < diagonal < dioganal_max:
                self.send_image(image)

    def process(self):
        """
        Run the camera process indefinitely.

        Parameters
        ----------
        config : function
            Function to get configuration variables.
        """
        while True:
            try:
                # image = self.get_image()
                _path = "../tests/embedding/2022-11-02 18_59_59.jpg"
                image = cv2.imread(_path)
                # faces = self.app.get(image)
                # rimg = self.app.draw_on(image, faces)
                self.analyze_faces(image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
                # cv2.imshow("frame", rimg)

            except Exception as ex:
                print("xatolik ", ex)
        cv2.destroyAllWindows()


# ishlatilishiqq
processor = CameraProcessor(config)
while True:
    try:
        processor.process()
    except Exception as ex:
        print("xatolik ", ex)
