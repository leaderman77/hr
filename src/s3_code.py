import os

from utils import project_dir

PROJEJECT_DIR = project_dir()
print(PROJEJECT_DIR)

# location_1 = [
#     [
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-10-09",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-10-10",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-02",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-03",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-04",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-05",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-07",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-09",
#     ],
#     [
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-10-10",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-02",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-03",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-04",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-05",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-07",
#         "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-09",
#     ],
# ]
#
# # s = 0
# # for idx, value in enumerate(location_1):
# #     print("camera_", idx + 1)
# #     for joyi in value:
# #         print(joyi[-10:], "da", len(os.listdir(joyi)), "ta rasm")
# #         s = s + len(os.listdir(joyi))
# #     print("camera_", idx + 1, "da", s, "ta rasm bor")
#


asosiy_joy = os.path.join(PROJEJECT_DIR, "data", "s3", "merchant_1", "location_1")

folders = os.listdir(asosiy_joy)

# cmeralar ichiga kirish
for folder in folders:
    _joy = os.path.join(asosiy_joy, folder)
    print(_joy)
    _joy_fayllar = os.listdir(_joy)
    # harb bir kamera ichiga kirish
    for _joy_fayl in _joy_fayllar:
        _joy2 = os.path.join(_joy, _joy_fayl)
        print(_joy2)
        _joy2_fayllar = os.listdir(_joy2)
        for _joy2_fayl in _joy2_fayllar:
            _joy3 = os.path.join(_joy2, _joy2_fayl)
            print(_joy3)
