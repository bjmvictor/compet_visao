import json                              # ler o JSON de keypoints
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

'''
# Simula um vídeo com detecção IMPERFEITA (algumas falhas), para praticar a análise
dados = gerar_keypoints(n_frames=80, taxa_maos=0.86)   # 86% -> abaixo da meta de propósito
with open("keypoints_qualidade.json", "w", encoding="utf-8") as f:
    json.dump(dados, f)
'''

with open("keypoints_qualidade.json", encoding="utf-8") as f:  # troque pelo seu JSON
    kp = json.load(f)
frames = kp["frames"]                       # lista de quadros
print("quadros:", len(frames))

#-------------------------------------------------------------------------------------------------------
## Taxa de detecção (mão e pose)
#-------------------------------------------------------------------------------------------------------
total = len(frames)                                   # total de quadros
com_mao = sum(1 for f in frames if f["hands"])        # quadros com mão
com_pose = sum(1 for f in frames if f["pose"])        # quadros com pose
taxa_mao = com_mao / total                            # fração 0..1
taxa_pose = com_pose / total
print(f"mãos: {com_mao}/{total} = {100*taxa_mao:.1f}%")
print(f"pose: {com_pose}/{total} = {100*taxa_pose:.1f}%")

#-------------------------------------------------------------------------------------------------------
## Mão encontrada por quadros 1 quando há mão no quadro, 0 quando não há
#-------------------------------------------------------------------------------------------------------
linha = [1 if f["hands"] else 0 for f in frames]      # lista de 0/1
plt.figure(figsize=(9, 1.6))                          # figura larga e baixa
plt.plot(linha, drawstyle="steps-post")               # degraus: mostra on/off
plt.yticks([0, 1], ["sem mão", "com mão"])            # rótulos do eixo y
plt.xlabel("quadro"); plt.title("Detecção de mão ao longo do vídeo"); plt.show()


#-------------------------------------------------------------------------------------------------------
## Veredito de qualidade (meta ≥ 90%)
#-------------------------------------------------------------------------------------------------------
META = 0.90                                # meta do projeto (M2)
if taxa_mao >= META:                        # atingiu a meta?
    print(f"✔ OK: detecção de mãos {100*taxa_mao:.1f}% (>= 90%). Dados prontos para modelar.")
else:
    print(f"✗ ABAIXO da meta: {100*taxa_mao:.1f}% (< 90%). Sugestões para regravar:")
    print("  - Melhore a iluminação (luz de frente, sem contraluz).")
    print("  - Mantenha as mãos totalmente no enquadramento.")
    print("  - Evite movimento muito rápido e fundo confuso.")
    print("  - Aumente a resolução/estabilidade (apoie o celular).")





