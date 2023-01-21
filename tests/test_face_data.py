import os
import cv2
from hr import HR
from utils import project_dir


PROJECT_DIR = project_dir()


def test_face_data():
    """
    Hamma data olinganini test qilish.
    Agar ham embedding ham age gender modellari
    ishlatilsa, list elementlari 7 ta bo'lishi kerak.
    """
    hr = HR(option_list=["emb", "ag"])

    root_emb_data = os.path.join(PROJECT_DIR, "tests", "embedding")
    img_path = os.path.join(root_emb_data, "1_1_1_2022-10-09-17-32-26.jpg")
    img = cv2.imread(img_path)
    face_data = hr.get_face_data(img)
    assert len(face_data) == 7, "List itemlarida muammo bor"
