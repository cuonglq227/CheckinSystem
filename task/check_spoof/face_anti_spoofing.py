import os
from ultralytics import YOLO

LOCALPATH = os.path.dirname(os.path.abspath(__file__))

class FaceAntiSpoofing:
    def __init__(self) -> None:
        self.model_path = os.path.join(LOCALPATH,'Model')+"/best.pt"
        self.model = YOLO(model = self.model_path)
        self.result = None
        self.real = None

    def check_spoof(self, path_img:str):
        self.result = self.model.predict(source=path_img, save=False, imgsz=640, conf=0.25)
        self.real = round(float(self.result[0].probs.data[0]), 4)
        return self.real