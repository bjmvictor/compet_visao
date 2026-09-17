import mediapipe as mp
import cv2
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision as mp_vision

base = mp_python.BaseOptions(
    model_asset_path=r"./models/hand_landmarker.task",   # arquivo do modelo (baixe conforme o README)
)
opts = mp_vision.HandLandmarkerOptions(
    base_options=base,                         # modelo a usar
    running_mode=mp_vision.RunningMode.IMAGE,  # IMAGE: processa uma imagem por vez
    num_hands=2,                               # nº máximo de mãos a detectar
    min_hand_detection_confidence=0.4,         # confiança mínima para aceitar a detecção
)
detector = mp_vision.HandLandmarker.create_from_options(opts)   # cria o detector

bgr = cv2.imread(r"./files/img/hands.png")                    # carrega uma foto de mão (BGR)
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)     # MediaPipe espera RGB
mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)  # embrulha para o MediaPipe
res = detector.detect(mp_img)                  # detecta (modo IMAGE)
print("mãos detectadas:", len(res.hand_landmarks))