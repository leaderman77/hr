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
from hr import HR


class CameraProcessor:
    def __init__(self, config, option_list=["det"]):
        self.config = config
        self.option_list = option_list
        self.app = FaceAnalysis(allowed_modules=["detection"], name="buffalo_sc")
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

    def det2json(self, face):
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

        bbox, kps, crop_face_img, img_shape = face

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
        b_kps["right_eye"] = [int(kps[0][0]), int(kps[0][1])]
        b_kps["left_eye"] = [int(kps[1][0]), int(kps[1][1])]
        b_kps["nose"] = [int(kps[2][0]), int(kps[2][1])]
        b_kps["right_lip"] = [int(kps[3][0]), int(kps[3][1])]
        b_kps["left_lip"] = [int(kps[4][0]), int(kps[4][1])]

        # crop img shape
        b_crop_shape = {}
        b_crop_shape["h"] = crop_face_img[0]
        b_crop_shape["w"] = crop_face_img[1]
        b_crop_shape["c"] = crop_face_img[2]

        # orginal img shape
        b_org_shape = {}
        b_org_shape["h"] = img_shape[0]
        b_org_shape["w"] = img_shape[1]
        b_org_shape["c"] = img_shape[2]

        # har bir topilgan yuz uchun
        obj = {}
        obj["bbox"] = b_box
        obj["kps"] = b_kps
        obj["crop_shape"] = b_crop_shape
        obj["img_shape"] = b_org_shape

        det_result = {}
        det_result["person"] = obj

        json_data = json.dumps(det_result)
        return json_data

    def ag2json(self, face):
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
        bbox, kps, crop_face_img, gender, age, img_shape = face

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
        b_kps["right_eye"] = [int(kps[0][0]), int(kps[0][1])]
        b_kps["left_eye"] = [int(kps[1][0]), int(kps[1][1])]
        b_kps["nose"] = [int(kps[2][0]), int(kps[2][1])]
        b_kps["right_lip"] = [int(kps[3][0]), int(kps[3][1])]
        b_kps["left_lip"] = [int(kps[4][0]), int(kps[4][1])]

        # crop img shape
        b_crop_shape = {}
        b_crop_shape["h"] = crop_face_img[0]
        b_crop_shape["w"] = crop_face_img[1]
        b_crop_shape["c"] = crop_face_img[2]

        # orginal img shape
        b_org_shape = {}
        b_org_shape["h"] = img_shape[0]
        b_org_shape["w"] = img_shape[1]
        b_org_shape["c"] = img_shape[2]

        # gender
        b_gender = {}
        b_gender["gender"] = gender

        # age
        b_age = {}
        b_age["age"] = age

        # har bir topilgan yuz uchun
        obj = {}
        obj["bbox"] = b_box
        obj["kps"] = b_kps
        obj["crop_shape"] = b_crop_shape
        obj["gender"] = b_gender
        obj["age"] = b_age
        obj["img_shape"] = b_org_shape

        det_result = {}
        det_result["person"] = obj

        json_data = json.dumps(det_result)
        return json_data

    def emb2json(self, face):
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
        bbox, kps, embedding, crop_face_img, img_shape = face

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
        b_kps["right_eye"] = [int(kps[0][0]), int(kps[0][1])]
        b_kps["left_eye"] = [int(kps[1][0]), int(kps[1][1])]
        b_kps["nose"] = [int(kps[2][0]), int(kps[2][1])]
        b_kps["right_lip"] = [int(kps[3][0]), int(kps[3][1])]
        b_kps["left_lip"] = [int(kps[4][0]), int(kps[4][1])]

        # embedding
        b_embedding = {}
        b_embedding["embedding_vek"] = embedding

        # crop img shape
        b_crop_shape = {}
        b_crop_shape["h"] = crop_face_img[0]
        b_crop_shape["w"] = crop_face_img[1]
        b_crop_shape["c"] = crop_face_img[2]

        # orginal img shape
        b_org_shape = {}
        b_org_shape["h"] = img_shape[0]
        b_org_shape["w"] = img_shape[1]
        b_org_shape["c"] = img_shape[2]

        # har bir topilgan yuz uchun
        obj = {}
        obj["bbox"] = b_box
        obj["kps"] = b_kps
        obj["crop_shape"] = b_crop_shape
        obj["embedding"] = b_embedding
        obj["org_shape"] = b_org_shape

        det_result = {}
        det_result["person"] = obj

        json_data = json.dumps(det_result)
        return json_data

    def all2json(self, face):
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
        bbox, kps, embedding, gender, age, crop_face_img, img_shape = face

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
        b_kps["right_eye"] = [int(kps[0][0]), int(kps[0][1])]
        b_kps["left_eye"] = [int(kps[1][0]), int(kps[1][1])]
        b_kps["nose"] = [int(kps[2][0]), int(kps[2][1])]
        b_kps["right_lip"] = [int(kps[3][0]), int(kps[3][1])]
        b_kps["left_lip"] = [int(kps[4][0]), int(kps[4][1])]

        # embedding
        b_embedding = {}
        b_embedding["embedding_vek"] = str(list(embedding))

        # gender
        b_gender = {}
        b_gender["gender_f"] = int(gender)

        # age
        b_age = {}
        b_age["age_f"] = age

        # crop img shape
        b_crop_shape = {}
        b_crop_shape["h"] = crop_face_img[0]
        b_crop_shape["w"] = crop_face_img[1]
        b_crop_shape["c"] = crop_face_img[2]

        # orginal img shape
        b_org_shape = {}
        b_org_shape["h"] = img_shape[0]
        b_org_shape["w"] = img_shape[1]
        b_org_shape["c"] = img_shape[2]

        # har bir topilgan yuz uchun
        obj = {}
        obj["bbox"] = b_box
        obj["kps"] = b_kps
        obj["embedding"] = b_embedding
        obj["gender"] = b_gender
        obj["age"] = b_age
        obj["crop_shape"] = b_crop_shape
        obj["org_shape"] = b_org_shape

        det_result = {}
        det_result["person"] = obj
        json_data = json.dumps(jsonpickle.encode(det_result))
        return json_data

    def get_obj(self, face):
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
        bbox, kps, embedding, gender, age, crop_face_img, img_shape = face

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
        b_kps["right_eye"] = [int(kps[0][0]), int(kps[0][1])]
        b_kps["left_eye"] = [int(kps[1][0]), int(kps[1][1])]
        b_kps["nose"] = [int(kps[2][0]), int(kps[2][1])]
        b_kps["right_lip"] = [int(kps[3][0]), int(kps[3][1])]
        b_kps["left_lip"] = [int(kps[4][0]), int(kps[4][1])]

        # embedding
        b_embedding = {}
        b_embedding["embedding_vek"] = jsonpickle.encode(embedding.tolist())

        # gender
        b_gender = {}
        b_gender["gender_f"] = int(gender)

        # age
        b_age = {}
        b_age["age_f"] = age

        # crop img shape
        b_crop_shape = {}
        b_crop_shape["h"] = crop_face_img[0]
        b_crop_shape["w"] = crop_face_img[1]
        b_crop_shape["c"] = crop_face_img[2]

        # har bir topilgan yuz uchun
        obj = {}
        obj["bbox"] = b_box
        obj["kps"] = b_kps
        obj["embedding"] = b_embedding
        obj["gender"] = b_gender
        obj["age"] = b_age
        obj["shape"] = b_crop_shape

        return obj

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
        headers = {"Content-Type": "multipart/form-data"}

        response = requests.post(
            api_url,
            data={
                "merchant_id": int(self.config("MERCHANT_ID")),
                "key": int(self.config("MERCHANT_KEY")),
                "location_id": int(self.config("LOCATION_ID")),
                "camera_id": int(self.config("CAMERA_ID")),
                "timestamp": f"{datetime.datetime.now():%Y-%m-%d-%H:%M:%S}",
                "img": open("../tests/embedding/2022-11-02 18_59_59.jpg", "rb"),
                # "frame": str(base64.encodebytes(img_encoded), "utf-8"),
            },
            verify=False,
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
        dioganal_min = int(self.config("DIOGANAL_MIN"))
        dioganal_max = int(self.config("DIOGANAL_MAX"))

        faces = self.app.get(image)

        for face in faces:
            print("face bor!")
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
