from src.hr import HR
import cv2

_path = "../data/drive/rasmlar_chiqish/1_1_1_2022-10-09-17-37-44.jpg"
img = cv2.imread(_path)
myHR = HR()
myHR.detection(img)
