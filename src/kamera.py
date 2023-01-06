import math
import cv2
import requests
import base64
import datetime
import time
from decouple import config

from hr import HR

class CameraProcessor:
    def init(self, config):
        self.config = config
        self.app = HR()
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
        startX, startY = self.config("startX", cast=int), self.config("startY", cast=int)
        endX, endY = int(self.config("endX")), int(self.config("endX"))
        return frame[startY:endY, startX:endX]

    def get_diagonal(self, face):
        """
        Calculate the diagonal length of a bounding box.

        Parameters
        ----------
        face : object
            Object containing bounding box coordinates.

        Returns
        -------
        diagonal : float
            The calculated diagonal length.
        """
        return math.sqrt((face.bbox[0] - face.bbox[2]) ** 2 + (face.bbox[1] - face.bbox[3]) ** 2)

    def face2json(self, face):
        """
        Convert face data to JSON format.

        Parameters
        ----------
        face : object
            Object containing face data.

        Returns
        -------
        json_data : dict
            Dictionary containing face data in JSON format.
        """
        json_data = None
        return json_data

    def send_image(self, image, face):
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
        response = requests.post(
            api_url,
            data={
                "merchant_id": int(self.config("MERCHANT_ID")),
                "location_id": int(self.config("LOCATION_ID")),
                "camera_id": int(self.config("CAMERA_ID")),
                "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
                "frame": str(base64.encodebytes(img_encoded), "utf-8"),
                "facedata": self.face2json(face)
            },
        )
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
        faces = self.app.detection(image)
        for face in faces:
            diagonal = self.get_diagonal(face)
            dioganal_min = int(self.config("DIOGANAL_MIN"))
            dioganal_max = int(self.config("DIOGANAL_MAX"))
            if dioganal_min < diagonal < dioganal_max:
                self.send_image(image, face)

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
                image = self.get_image()
                self.analyze_faces(image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
            except Exception as ex:
                print("xatolik ", ex)
        cv2.destroyAllWindows()


# ishlatilishi
processor = CameraProcessor(config)
while True:
    try:
        processor.process()
    except Exception as ex:
            print("xatolik ", ex)