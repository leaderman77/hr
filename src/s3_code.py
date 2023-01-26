import os
from utils import project_dir

PROJEJECT_DIR = project_dir()


def count_elements(asosiy_joy):
    """
    falylar ichidagi elementlarini sanaydi
    Parameters
    ----------
    asosiy_joy:list

    Returns
    -------
    elementlar soni
    """
    my_satr = ""
    folders = os.listdir(asosiy_joy)
    for folder in folders:
        k = 0
        camera = os.path.join(asosiy_joy, folder)
        fayllar = os.listdir(camera)
        # harb bir kamera ichiga kirish
        for _joy_fayl in fayllar:
            s = 0
            if _joy_fayl[-5:] != "yomon":
                _joy2 = os.path.join(camera, _joy_fayl)
                _joy2_fayllar = os.listdir(_joy2)
                # har bir kamera ichidagi faylllarga kirish
                for _joy2_fayl in _joy2_fayllar:
                    _joy3 = os.path.join(_joy2, _joy2_fayl)
                    s = s + 1
                    k = k + 1
                my_satr += _joy_fayl + " da " + str(s) + " ta rasm bor \n"
        my_satr += "\n" + folder + " da " + str(k) + " ta rasm bor \n \n"
    return my_satr


asosiy_joy = os.path.join(
    PROJEJECT_DIR,
    "data",
    "s3",
    "merchant_1",
    "location_1",
)
result = count_elements(asosiy_joy)
print(result)
