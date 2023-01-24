import os
from utils import project_dir

PROJEJECT_DIR = project_dir()


def fayl_ichidagi_elementlar_soni(asosiy_joy):
    """
    falylar ichidagi elementlarini sanaydi
    Parameters
    ----------
    asosiy_joy:list

    Returns
    -------
    fayllar ichidagi elementlar soni
    """
    s = 0
    folders = os.listdir(asosiy_joy)
    for folder in folders:
        camera = os.path.join(asosiy_joy, folder)
        print(folder)
        fayllar = os.listdir(camera)
        # harb bir kamera ichiga kirish
        for _joy_fayl in fayllar:
            if _joy_fayl[-5:] != "yomon":
                _joy2 = os.path.join(camera, _joy_fayl)
                _joy2_fayllar = os.listdir(_joy2)
                # har bir kamera ichidagi faylllarga kirish
                for _joy2_fayl in _joy2_fayllar:
                    _joy3 = os.path.join(_joy2, _joy2_fayl)
                    s = s + 1
                print(_joy_fayl, "da", s, "ta rasm bor")


asosiy_joy = os.path.join(
    PROJEJECT_DIR,
    "data",
    "s3",
    "merchant_1",
    "location_1",
)

fayl_ichidagi_elementlar_soni(asosiy_joy)
