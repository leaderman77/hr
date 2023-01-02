import json
from src.hr import HR
import cv2


# {
#     bbox:
#         {
#             x1
#             y1
#             x2
#             y2
#         }
#     kps:
#         {
#
#         }
#     size:
#         {
#
#         }
# }


def det():
    _path = "../data/drive/rasmlar_chiqish/1_1_1_2022-10-09-17-38-10.jpg"
    img = cv2.imread(_path)
    myHR = HR()
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
        b_kps["left_eye"] = (int(kps[4][0]), int(kps[4][1]))

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

    print(det_result)
    print(type(det_result))
    det_json = json.dumps(det_result)
    print(det_json)
    print(type(det_json))
    # det_json API orqali jo'natiladi


det()
