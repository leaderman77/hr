from src.kamera import CameraProcessor
import os
from decouple import AutoConfig

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")
config = AutoConfig(search_path=CONFIG_DIR)
processor = CameraProcessor(config)

while True:
    try:
        processor.process()
    except Exception as ex:
        print("xatolik ", ex)
