import os

location_1 = [
    [
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-10-09",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-10-10",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-02",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-03",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-04",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-05",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-07",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_1/2022-11-09",
    ],
    [
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-10-10",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-02",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-03",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-04",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-05",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-07",
        "/home/ubuntuuser/proyektlar/hr/data/s3/merchant_1/location_1/camera_2/2022-11-09",
    ],
]

s = 0
j = 0
for idx, value in enumerate(location_1):
    print("kamera_", idx + 1)
    for i, joyi in enumerate(value):
        print(i + 1, len(os.listdir(joyi)))
        s = s + len(os.listdir(joyi))
    print("camera_", idx + 1, "da", s, "ta rasm bor")
