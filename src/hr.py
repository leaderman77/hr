# import cv2
from insightface.app import FaceAnalysis
from insightface.model_zoo import ArcFaceONNX
import os
from insightface.utils import face_align


class HR:
    def __init__(self, module="detection", det_size=(640, 640), det_thresh=0.3):
        self.app = FaceAnalysis(allowed_modules=[module])
        self.app.prepare(ctx_id=0, det_size=det_size, det_thresh=det_thresh)

        assets_dir = os.path.expanduser('~/.insightface/models/buffalo_l')
        model_path = os.path.join(assets_dir, 'w600k_r50.onnx')
        self.arcFace = ArcFaceONNX(model_path)
        self.arcFace.prepare(0)

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

    def embeding(self, img):
        """Class method on getting face embeddings

        Analyses the given image and converts each detected face
        in the image into 512-d numerical vectors. The insightface's
        ArcFaceONNX library is used in order to get faces and their key points.
        Each detected face is cropped in size w112, h112 and calculated embedding
        is applied for face.embedding list

        Parameters
        ----------
        img : :obj:`Unit8`
            The second parameter. Image

        Returns
        -------
        The method returns list of detected faces that are populated with embeddings and
        cropped face image's shape
        """

        faces = self.app.get(img)

        face_embeddings = []
        for face in faces:

            # Get the face embedding vector
            embedding = self.arcFace.get(img, face)

            # Crop face from img
            crop_face_img = face_align.norm_crop(
                img,
                landmark=face.kps,
                image_size=self.arcFace.input_size[0]
            )

            # collect bboxes, kpss, embeddings, crop shape, img shape
            face_embeddings.append([face.bbox, face.kps, embedding, crop_face_img.shape, img.shape])

        return face_embeddings


# myHR = HR()
# myHR.agegender()
# myHR.recognation()
