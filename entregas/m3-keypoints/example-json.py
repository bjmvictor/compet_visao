import cv2, numpy as np, math          # cv2/np: desenho e cálculo; math: distância
import matplotlib.pyplot as plt
import json, random, math   # json: ler/escrever; random: simular; math: geometria
random.seed(0)                       # semente fixa -> resultado reproduzível

def gerar_keypoints(n_frames=60, fps=20, taxa_maos=0.92, taxa_pose=0.96):
    frames = []                      # lista de quadros
    com_maos = com_pose = 0          # contadores de deteccao
    for i in range(n_frames):        # para cada quadro do "video"
        hands = []                   # maos detectadas neste quadro
        if random.random() < taxa_maos:      # simula deteccao de mao
            com_maos += 1
            cx = 0.5 + 0.1 * math.sin(i / 5) # centro da mao oscila (simula movimento)
            lm = []                          # 21 landmarks da mao
            for k in range(21):              # MediaPipe: 21 pontos por mao
                dy = -0.15 if k == 8 else 0.0  # landmark 8 = ponta do indicador (mais acima)
                lm.append({"landmark": k,
                           "x": round(cx + 0.02 * math.cos(k), 4),  # x normalizado (0..1)
                           "y": round(0.5 + 0.02 * math.sin(k) + dy, 4),  # y normalizado
                           "z": 0.0,          # profundidade relativa (nao usada aqui)
                           "score": 0.99})    # confianca
            hands.append({"hand": "Right", "landmarks": lm})
        pose = []                    # 33 landmarks do corpo
        if random.random() < taxa_pose:
            com_pose += 1
            for k in range(33):      # MediaPipe: 33 pontos de pose
                pose.append({"landmark": k, "x": 0.5, "y": 0.5, "z": 0.0, "score": 0.9})
        frames.append({"frame": i, "timestamp_ms": int(i * 1000 / fps),
                       "hands": hands, "pose": pose})
    meta = {"video_id": "exemplo", "source_file": "exemplo.mp4", "fps": fps,
            "frames_declared": n_frames, "frames_processed": n_frames,
            "hand_detection_rate": round(com_maos / n_frames, 4),
            "pose_detection_rate": round(com_pose / n_frames, 4)}
    return {"metadata": meta, "frames": frames}

dados = gerar_keypoints(n_frames=60)     # cria dados de exemplo (60 quadros)
import json
with open("keypoints_exemplo.json", "w", encoding="utf-8") as f:
    json.dump(dados, f)                   # salva no formato do projeto
print("JSON de exemplo criado")