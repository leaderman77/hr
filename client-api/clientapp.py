from src.hr import HR
import cv2


{
    bbox:
        {
            x1
            y1
            x2
            y2
        }
    kps:
        {

        }
    size:
        {

        }
}

def det():
    _path = "../data/drive/rasmlar_chiqish/1_1_1_2022-10-09-17-38-10.jpg"
    img = cv2.imread(_path)
    myHR = HR()
    faces = myHR.detection(img)

    return json.data([...])