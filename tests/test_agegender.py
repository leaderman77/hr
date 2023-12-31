import cv2
import os.path

from hr import HR
from utils import project_dir

PROJECT_DIR = project_dir()


def test_agegender():
    """
    Age gender metodini test qilish
    Returns
    -------
    None
    """
    hr = HR(option_list=["ag"])
    img1_path = os.path.join(
        PROJECT_DIR, "tests", "embedding", "1_1_1_2022-10-09-17-32-26.jpg"
    )
    assert os.path.isfile(img1_path), "fayl yo'q"
    img1 = cv2.imread(img1_path)
    face_data = hr.agegender(img1)  # [[1, 26]]
    gender = face_data[0][3]  # [1, 26][0] --> 1
    age = face_data[0][4]  # [1, 26][1] --> 26

    assert gender == 1, "Genderda xatolik."
    assert age == 26, "Yoshda xatolik."
